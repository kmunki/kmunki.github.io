#!/usr/bin/env python3
"""
Convert Violet novel from Scrivener RTF files to Jekyll format with formatting preserved
"""

import re
import os
import subprocess
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timedelta
from html.parser import HTMLParser

# Configuration
SCRIVENER_PROJECT = Path("/Users/kylem/Library/CloudStorage/Dropbox/Apps/Scrivener/Violet.scriv")
SCRIVX_FILE = SCRIVENER_PROJECT / "Violet.scrivx"
RTF_DATA_DIR = SCRIVENER_PROJECT / "Files" / "Data"
OUTPUT_DIR = Path("/Users/kylem/Documents/Writing/kmunki.github.io/_fiction/violet")
START_DATE = datetime(2025, 11, 2)  # Sunday, November 2, 2025 - first chapter publication
WEEKLY_INTERVAL = timedelta(days=7)

# Chapter manifest from Project Outline
# Format: (order, filename_prefix, chapter_num, title, sync_num, act)
CHAPTERS = [
    # Prologue & Front Matter
    (1, "001-prologue", 0, "Prologue", 0, 0),

    # Act 1: Ātmanic Exaptations
    (10, "010-act-1", None, "Act 1: Ātmanic Exaptations", 9, 1),
    (11, "011-chapter-01", 1, "The Ward, the Princess, and the Sifu", 11, 1),
    (12, "012-chapter-02", 2, "Jack Brand, International Man of Mystery", 14, 1),
    (13, "013-chapter-03", 3, "The Ogre; The Viceroy", 16, 1),
    (14, "014-chapter-04", 4, "Hiding in Plain Sight", 18, 1),
    (15, "015-chapter-05", 5, "Arcology", 20, 1),
    (16, "016-chapter-06", 6, "Tree Top Espionage", 21, 1),
    (17, "017-chapter-07", 7, "The Organs of the Olgoi", 22, 1),
    (18, "018-chapter-08", 8, "Brave New World", 23, 1),
    (19, "019-chapter-09", 9, "The Eye of the Swarm", 25, 1),

    # Act 2: Stochastic Kaihō
    (27, "027-act-2", None, "Act 2: Stochastic Kaihō", 27, 2),
    (28, "028-chapter-10", 10, "Fallout at the European Security Agency", 29, 2),
    (29, "029-chapter-11", 11, "War Weaving", 30, 2),
    (30, "030-chapter-12", 12, "Owl in Daylight", 31, 2),
    (31, "031-chapter-13", 13, "Narobi", 32, 2),
    (32, "032-chapter-14", 14, "Coin Flip", 33, 2),
    (33, "033-chapter-15", 15, "Hexagrams", 34, 2),
    (34, "034-chapter-16", 16, "Uplift", 35, 2),
    (35, "035-chapter-17", 17, "A Brewing Storm", 36, 2),
    (36, "036-chapter-18", 18, "The Persian", 37, 2),
    (37, "037-chapter-19", 19, "Storm the Palace", 39, 2),
    (38, "038-chapter-20", 20, "The Asura", 40, 2),
    (39, "039-chapter-21", 21, "Join Us", 41, 2),
    (40, "040-chapter-22", 22, "Graduation and Matriculation", 42, 2),

    # Act 3: Ecotone Arcana
    (43, "043-act-3", None, "Act 3: Ecotone Arcana", 43, 3),
    (44, "044-chapter-23", 23, "To the Floating City", 45, 3),
    (45, "045-chapter-24", 24, "Bank, Hotel, Tickets", 47, 3),
    (46, "046-chapter-25", 25, "Undercurrent", 50, 3),
    (47, "047-chapter-26", 26, "The Railroad of Bones", 51, 3),
    (48, "048-chapter-27", 27, "Investigating the Aftermath", 53, 3),
    (49, "049-chapter-28", 28, "Where the War Never Ended", 55, 3),
    (50, "050-chapter-29", 29, "Treasures of the Sifu", 56, 3),
    (51, "051-chapter-30", 30, "Free Beasts", 57, 3),
    (52, "052-chapter-31", 31, "Legendary Weapons", 61, 3),
    (53, "053-chapter-32", 32, "The High Priestess", 62, 3),
    (54, "054-chapter-33", 33, "The Blade of Kahina", 63, 3),
    (55, "055-chapter-34", 34, "The Hermit", 64, 3),
    (56, "056-chapter-35", 35, "Mercenaries' Mecca", 65, 3),
    (57, "057-chapter-36", 36, "The Coin", 66, 3),

    # Act 4: Revenants' Maya
    (67, "067-act-4", None, "Act 4: Revenants' Maya", 67, 4),
    (68, "068-chapter-37", 37, "The Magicians", 69, 4),
    (69, "069-chapter-38", 38, "The Quartermaster; The Coffin", 71, 4),
    (70, "070-chapter-39", 39, "The Chariot", 73, 4),
    (71, "071-chapter-40", 40, "The Gift of Betrayal", 75, 4),
    (72, "072-chapter-41", 41, "Old Friends", 76, 4),
    (73, "073-chapter-42", 42, "The Reliquery and the Vial", 78, 4),
    (74, "074-chapter-43", 43, "The Chamber of Harmonic Discord", 79, 4),
    (75, "075-chapter-44", 44, "The Residential Pavillion of Global Serenity", 80, 4),
    (76, "076-chapter-45", 45, "Yōkai", 81, 4),
    (77, "077-chapter-46", 46, "Saṃsāra", 82, 4),
    (78, "078-chapter-47", 47, "The Thing on the Doorstep", 84, 4),
    (79, "079-chapter-48", 48, "Naraka", 87, 4),

    # Act 5: Aleatory Syzygy
    (88, "088-act-5", None, "Act 5: Aleatory Syzygy", 88, 5),
    (89, "089-chapter-49", 49, "The Asura", 90, 5),
    (90, "090-chapter-50", 50, "Ghul", 92, 5),
    (91, "091-chapter-51", 51, "Busaw", 93, 5),
    (92, "092-chapter-52", 52, "Appulse", 96, 5),
    (93, "093-chapter-53", 53, "Transit; Occultation", 101, 5),
    (94, "094-chapter-54", 54, "The Cuckoo", 103, 5),
    (95, "095-chapter-55", 55, "Conjunction", 104, 5),
    (96, "096-chapter-56", 56, "Revenants; Segaki", 105, 5),
    (97, "097-chapter-57", 57, "Bardo", 114, 5),
    (98, "098-chapter-58", 58, "Crane-Dragon Duel", 115, 5),
    (99, "099-chapter-59", 59, "Grave Robbers", 116, 5),
    (100, "100-chapter-60", 60, "Enthronement", 117, 5),
]

# Act epigraph sync numbers
ACT_EPIGRAPHS = {
    1: 10,  # Chance & Destiny Epigraph
    2: 28,  # Hybrids Epigraph
    3: 44,  # Uplift Epigraph
    4: 68,  # Unearth Epigraph
    5: 89,  # Agar Epigraph
}


class RTFToMarkdownConverter(HTMLParser):
    """Convert HTML (from RTF) to Markdown, preserving formatting"""

    def __init__(self):
        super().__init__()
        self.markdown = []
        self.current_text = ""
        self.in_italic = False
        self.in_bold = False
        self.in_paragraph = False
        self.in_style = False  # Skip content inside <style> tags

    def handle_starttag(self, tag, attrs):
        if tag == 'style':
            self.in_style = True
        elif tag == 'i' or tag == 'em':
            self.in_italic = True
        elif tag == 'b' or tag == 'strong':
            self.in_bold = True
        elif tag == 'p' or tag == 'div':
            self.in_paragraph = True

    def handle_endtag(self, tag):
        if tag == 'style':
            self.in_style = False
        elif tag == 'i' or tag == 'em':
            self.in_italic = False
        elif tag == 'b' or tag == 'strong':
            self.in_bold = False
        elif tag == 'p' or tag == 'div':
            if self.current_text.strip():
                self.markdown.append(self.current_text)
                self.markdown.append("")  # Paragraph break
            self.current_text = ""
            self.in_paragraph = False

    def handle_data(self, data):
        # Skip content inside <style> tags
        if self.in_style:
            return

        # Clean up the text
        text = data

        # Apply formatting
        if self.in_italic and self.in_bold:
            text = f"***{text}***"
        elif self.in_italic:
            text = f"*{text}*"
        elif self.in_bold:
            text = f"**{text}**"

        self.current_text += text

    def get_markdown(self):
        # Handle any remaining text
        if self.current_text.strip():
            self.markdown.append(self.current_text)

        # Clean up excessive newlines
        result = "\n".join(self.markdown)
        result = re.sub(r'\n{3,}', '\n\n', result)
        return result.strip()


def parse_scrivx_for_sync_mapping():
    """Parse the scrivx file to build sync number -> UUID mapping"""
    print("Parsing Scrivener project file for sync mappings...")

    tree = ET.parse(SCRIVX_FILE)
    root = tree.getroot()

    # Find all SyncItem elements
    sync_mapping = {}
    for sync_item in root.findall('.//SyncItem'):
        uuid = sync_item.get('ID')
        sync_num = int(sync_item.text)
        sync_mapping[sync_num] = uuid

    print(f"  ✓ Found {len(sync_mapping)} sync mappings")
    return sync_mapping


def load_scrivener_structure():
    """Load the full Scrivener JSON export to access document hierarchy"""
    json_path = Path("/Users/kylem/Documents/Writing/Scrivener-Vault/Scrivener-Exports/Violet/Violet.json")
    print("Loading Scrivener document structure...")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    documents = data.get('documents', {})
    print(f"  ✓ Loaded {len(documents)} documents")
    return documents


def find_rtf_file(sync_num, sync_mapping):
    """Find the RTF file for a given sync number"""
    uuid = sync_mapping.get(sync_num)
    if not uuid:
        return None

    rtf_path = RTF_DATA_DIR / uuid / "content.rtf"
    if rtf_path.exists():
        return rtf_path
    return None


def convert_rtf_to_markdown(rtf_path):
    """Convert RTF file to markdown using textutil + HTML parsing"""

    # Step 1: Convert RTF to HTML using textutil
    try:
        result = subprocess.run(
            ['textutil', '-convert', 'html', '-stdout', str(rtf_path)],
            capture_output=True,
            text=True,
            check=True
        )
        html_content = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"  ERROR running textutil: {e}")
        return None

    # Step 2: Parse HTML and convert to markdown
    parser = RTFToMarkdownConverter()
    parser.feed(html_content)
    markdown = parser.get_markdown()

    return markdown


def collect_child_content(uuid, documents, sync_mapping, depth=0):
    """
    Recursively collect content from a document and all its children.
    Returns concatenated markdown content.
    """
    content_parts = []

    # Get the document
    doc = documents.get(uuid)
    if not doc:
        return ""

    # Skip if not included in compile
    if not doc.get('include_in_compile', True):
        print(f"  {'  ' * depth}⊗ Skipping {doc.get('title', 'untitled')} (not in compile)")
        return ""

    # Get sync number for this document
    # Reverse-lookup: find sync_num where sync_mapping[sync_num] == uuid
    doc_sync_num = None
    for sync_num, mapped_uuid in sync_mapping.items():
        if mapped_uuid == uuid:
            doc_sync_num = sync_num
            break

    # Get content for this document if it has a sync number
    if doc_sync_num is not None:
        rtf_file = find_rtf_file(doc_sync_num, sync_mapping)
        if rtf_file:
            try:
                doc_content = convert_rtf_to_markdown(rtf_file)
                if doc_content:
                    content_parts.append(doc_content)
                    print(f"  {'  ' * depth}✓ Added content from {doc.get('title', 'untitled')} (sync {doc_sync_num})")
            except Exception as e:
                print(f"  {'  ' * depth}ERROR converting {doc.get('title', 'untitled')}: {e}")

    # Process children
    children = doc.get('children', [])
    if children:
        print(f"  {'  ' * depth}→ Processing {len(children)} children of {doc.get('title', 'untitled')}")
        for child_uuid in children:
            child_content = collect_child_content(child_uuid, documents, sync_mapping, depth + 1)
            if child_content:
                # Add scene break divider between scenes
                content_parts.append("\n\n---\n\n")
                content_parts.append(child_content)

    return "".join(content_parts)


def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def clean_content(content):
    """Clean up content for Jekyll"""
    # Remove any leading/trailing whitespace
    content = content.strip()
    return content


def generate_front_matter(order, filename_prefix, chapter_num, title, act, is_act_page=False):
    """Generate Jekyll front matter"""
    lines = ["---"]

    # Use 'chapter' layout for actual chapters, 'post' for other pages
    if chapter_num is not None and chapter_num > 0:
        lines.append("layout: chapter")
        lines.append("novel: Violet")
        lines.append(f"chapter: {chapter_num}")
        lines.append(f'title: "{title}"')
        # Chapters need explicit permalinks too
        lines.append(f'permalink: /fiction/violet/chapter-{chapter_num:02d}/')
    else:
        lines.append("layout: post")
        lines.append(f'title: "{title}"')

        # Generate permalink for non-chapter pages
        if is_act_page:
            slug = slugify(title)
            lines.append(f'permalink: /fiction/violet/{slug}/')
        elif chapter_num == 0:
            lines.append(f'permalink: /fiction/violet/prologue/')
        else:
            slug = slugify(title)
            lines.append(f'permalink: /fiction/violet/{slug}/')

    # Don't add 'collection' - files in _fiction/ are automatically in the collection
    # Don't add 'published' - use filename or other method to control publishing

    if act and not is_act_page:
        lines.append(f"act: {act}")

    # Calculate theoretical publish date for reference
    if chapter_num is not None and chapter_num >= 0:
        weeks = chapter_num
        pub_date = START_DATE + (weeks * WEEKLY_INTERVAL)
        lines.append(f"date: {pub_date.strftime('%B %d, %Y')}")

    lines.append("---")
    lines.append("")

    return "\n".join(lines)


def process_chapter(order, filename_prefix, chapter_num, title, sync_num, act, sync_mapping, documents):
    """Process a single chapter and all its nested scenes"""
    print(f"Processing: {title} (sync {sync_num})")

    # Check if it's an act page
    is_act_page = chapter_num is None and "Act" in title

    if is_act_page:
        # Handle act page with epigraph
        return process_act_page(order, filename_prefix, title, sync_num, act, sync_mapping)

    # Find the UUID for this sync number
    uuid = sync_mapping.get(sync_num)
    if not uuid:
        print(f"  WARNING: Could not find UUID for sync {sync_num}")
        return False

    # Collect content from this chapter and ALL its children recursively
    try:
        content = collect_child_content(uuid, documents, sync_mapping)
        if not content:
            print(f"  ERROR: No content collected")
            return False
    except Exception as e:
        print(f"  ERROR collecting content: {e}")
        return False

    # Clean content
    content = clean_content(content)

    # Generate front matter
    front_matter = generate_front_matter(order, filename_prefix, chapter_num, title, act, is_act_page)

    # Combine and write
    output_file = OUTPUT_DIR / f"{filename_prefix}.md"
    full_content = front_matter + content

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"  ✓ Written to {output_file.name} ({len(content)} chars)")
        return True
    except Exception as e:
        print(f"  ERROR writing {output_file}: {e}")
        return False


def process_act_page(order, filename_prefix, title, sync_num, act, sync_mapping):
    """Process an act divider page with epigraph"""
    print(f"Processing ACT PAGE: {title}")

    # Get the epigraph sync number
    epigraph_sync = ACT_EPIGRAPHS.get(act)
    if not epigraph_sync:
        print(f"  WARNING: No epigraph defined for act {act}")
        epigraph_content = ""
    else:
        epigraph_file = find_rtf_file(epigraph_sync, sync_mapping)
        if epigraph_file:
            try:
                epigraph_content = convert_rtf_to_markdown(epigraph_file)
                if not epigraph_content:
                    epigraph_content = ""
            except Exception as e:
                print(f"  ERROR reading epigraph: {e}")
                epigraph_content = ""
        else:
            print(f"  WARNING: Could not find epigraph file")
            epigraph_content = ""

    # Generate front matter
    front_matter = generate_front_matter(order, filename_prefix, None, title, act, is_act_page=True)

    # Create act page content
    content_lines = [
        f"# {title}",
        "",
    ]

    if epigraph_content:
        content_lines.append(epigraph_content)
        content_lines.append("")

    content = "\n".join(content_lines)

    # Combine and write
    output_file = OUTPUT_DIR / f"{filename_prefix}.md"
    full_content = front_matter + content

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"  ✓ Written to {output_file.name}")
        return True
    except Exception as e:
        print(f"  ERROR writing {output_file}: {e}")
        return False


def main():
    """Main conversion process"""
    print("=" * 60)
    print("VIOLET NOVEL CONVERSION SCRIPT - WITH FORMATTING")
    print("=" * 60)
    print()

    # Parse scrivx for sync mappings
    sync_mapping = parse_scrivx_for_sync_mapping()
    print()

    # Load full document structure
    documents = load_scrivener_structure()
    print()

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Process all chapters
    success_count = 0
    fail_count = 0

    for chapter_data in CHAPTERS:
        try:
            if process_chapter(*chapter_data, sync_mapping, documents):
                success_count += 1
            else:
                fail_count += 1
        except Exception as e:
            print(f"  EXCEPTION: {e}")
            import traceback
            traceback.print_exc()
            fail_count += 1
        print()

    print("=" * 60)
    print(f"COMPLETE: {success_count} succeeded, {fail_count} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
