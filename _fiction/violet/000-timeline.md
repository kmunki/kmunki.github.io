---
layout: minimal
title: "Historic Events: A Select Timeline"
permalink: /fiction/violet/timeline/
collection: fiction
series: violet
order: 0
published: true
---

<article class="violet-page timeline-page">
    <header class="page-header">
        <div class="back-link-container">
            <a href="/fiction/violet/" class="back-link">← Violet</a>
        </div>
        <h1 class="page-title">Historic Events:<br/>A Select Timeline</h1>
    </header>

<div class="page-content" markdown="1">

| Zhongguo | Gregorian | Hijri | Mayan | Event |
|----------|-----------|-------|-------|-------|
| 3698 | 1000 | 421 | 10.8.12 | _Centuries pass_ |
| 4138 | 1440 | 861 | 11.10.18 | Zheng He's 8th Voyage lands on the Gold Coast, establishes trade treaties with Mexica and Inka |
|  |  |  |  | _Centuries pass_ |
| 4480 | 1782 | 1203 | 12.8.5 | Agar synthesized for the first time |
|  |  |  |  | _Decades pass_ |
| 4573 | 1875 | 1296 | 12.13.0 | Zenith of the Biological Revolution |
|  |  |  |  | _Decades pass_ |
| 4601 | 1903 | 1324 | 12.14.8 | First emergence of Ananda's plagues |
|  |  |  |  | **The Long War** |
| 4640 | 1942 | 1363 | 12.16.8 | The Accords |
|  |  |  |  | Uplift Rebellions, Abandonment of the Wilds |
|  |  |  |  | Revolutionary Periods, first Corporate Wars, War-Relic Rush begins |
|  |  |  |  | **The Shadow** |
| 4695 | 1997 | 1418 | 12.19.3 | Hyeon Bong-Cha Chosen as Ward |
| 4712 | 2014 | 1435 | 13.0.1 | Violet Corporation declares itself a sovereignty |

</div>

    <nav class="page-navigation">
        <div class="nav-links">
            <a href="/fiction/violet/" class="nav-skip">Skip to Prologue →</a>
            <a href="/fiction/violet/world-map/" class="nav-next">Continue →</a>
        </div>
    </nav>
</article>

<style>
    /* Override minimal layout constraints */
    body {
        max-width: none !important;
        padding: 0 !important;
        margin: 0 !important;
        background: #0a0514 !important;
    }

    main {
        margin: 0 !important;
    }

    html, body {
        overflow-x: hidden;
    }

    /* Base page styling */
    .violet-page {
        min-height: 100vh;
        font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', 'Roboto Mono', 'Courier New', monospace;
        background: #0a0514;
        color: #e8d5f0;
        padding: 3rem 2rem;
    }

    /* Header */
    .page-header {
        max-width: 900px;
        margin: 0 auto 4rem auto;
        text-align: center;
        position: relative;
    }

    .back-link-container {
        position: absolute;
        left: 0;
        top: 0;
    }

    .back-link {
        color: #8566a0;
        text-decoration: none;
        font-size: 0.9rem;
        border: none;
        transition: all 0.3s ease;
    }

    .back-link:hover {
        color: #b47cc7;
        opacity: 1;
    }

    .page-title {
        font-size: 2.5rem;
        font-weight: 600;
        color: #b47cc7;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin: 0;
        line-height: 1.3;
    }

    /* Content area */
    .page-content {
        max-width: 900px;
        margin: 0 auto 4rem auto;
    }

    /* Timeline table styling */
    .page-content table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 2rem 0;
        font-size: 0.95rem;
        border: 1px solid #2d1a3d;
        border-radius: 8px;
        overflow: hidden;
        background: #0f0a1a;
    }

    .page-content table th {
        background: #1a0f24;
        padding: 1rem 0.75rem;
        text-align: left;
        font-weight: 600;
        color: #b47cc7;
        border-bottom: 2px solid #2d1a3d;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .page-content table td {
        padding: 0.75rem;
        border-bottom: 1px solid #1a0f24;
        vertical-align: top;
        color: #d5b8e0;
    }

    .page-content table tr:last-child td {
        border-bottom: none;
    }

    .page-content table tr {
        transition: all 0.3s ease;
    }

    .page-content table tbody tr:hover {
        background: #140c1d;
    }

    .page-content table td:last-child {
        font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
        font-style: normal;
        line-height: 1.6;
    }

    .page-content table td em {
        color: #8566a0;
        font-style: italic;
    }

    .page-content table td strong {
        color: #b47cc7;
        font-weight: 600;
    }

    /* Navigation */
    .page-navigation {
        max-width: 900px;
        margin: 0 auto;
        padding-top: 3rem;
        border-top: 1px solid #2d1a3d;
    }

    .nav-links {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
    }

    .nav-skip {
        font-size: 0.85rem;
        color: #6b4d7a;
        text-decoration: none;
        border: none;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
        border-radius: 4px;
    }

    .nav-skip:hover {
        color: #8566a0;
        background: #140c1d;
        opacity: 1;
    }

    .nav-next {
        font-size: 1rem;
        font-weight: 500;
        padding: 0.75rem 2rem;
        border: 2px solid #b47cc7;
        border-radius: 4px;
        transition: all 0.3s ease;
        text-decoration: none;
        color: #d5b8e0;
        background: transparent;
        position: relative;
        border: none;
    }

    .nav-next:hover {
        background: #b47cc7;
        color: #0a0514;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(180, 124, 199, 0.3);
        opacity: 1;
    }

    /* Mobile styles */
    @media (max-width: 768px) {
        .violet-page {
            padding: 2rem 0.5rem;
        }

        .page-header {
            margin-bottom: 3rem;
            padding: 0 1rem;
        }

        .page-title {
            font-size: 1.8rem;
            margin-top: 2rem;
        }

        .back-link-container {
            position: static;
            margin-bottom: 1.5rem;
        }

        .page-content {
            padding: 0;
        }

        .page-content table {
            font-size: 0.8rem;
            display: block;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }

        .page-content table tbody {
            display: table;
            width: 100%;
        }

        .page-content table th,
        .page-content table td {
            padding: 0.5rem 0.6rem;
        }

        .page-content table th {
            font-size: 0.75rem;
        }

        .page-content table td:last-child {
            padding-right: 1rem;
        }

        .page-navigation {
            padding: 3rem 1rem 0 1rem;
        }

        .nav-links {
            flex-direction: column-reverse;
            gap: 0.5rem;
        }

        .nav-skip,
        .nav-next {
            width: 100%;
            text-align: center;
        }
    }
</style>
