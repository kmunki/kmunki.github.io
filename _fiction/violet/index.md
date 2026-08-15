---
layout: violet
title: "Violet"
permalink: /fiction/violet/
collection: fiction
landing: true
published: true
---

<div class="hero">
    <img
        src="/assets/images/violet/violet_cover_1800.jpg"
        srcset="/assets/images/violet/violet_cover_900.jpg 900w, /assets/images/violet/violet_cover_1800.jpg 1800w"
        sizes="100vw"
        alt="Violet — a novel by Kyle Munkittrick"
        class="hero-image">
    <div class="hero-wordmark">
        <img src="/assets/images/violet/violet_wordmark.svg" alt="Violet">
    </div>
</div>

<div class="landing-body">

<div class="jacket">
<p>Nearly six centuries ago, Zheng He’s treasure fleet kept sailing east instead of turning for home. Everything since has happened differently — and, if you squint, exactly the same.</p>

<p>Hye is a royal Ward of Koryo: chosen from a fishing village at four, raised beside a princess, trained by an old woman who is more than she claims. Sun, her sister in everything but blood, wants the throne. Hye wants to see an arcology before the world ends again. Their tutor wants only to keep a promise.</p>

<p>Across the ocean, Violet — the largest corporation on earth — has just declared itself a nation. Its founder believes that progress is humanity’s gift to the universe, and that a certain kind of luck can be bred. She has a list of names. One of them belongs to a girl who was chosen, at four, in the rain.</p>

<p>When the palace burns, Hye escapes into the Wilds: the weaponized wilderness the Long War left behind, where the monsters are old, the cities are secret, and nothing is quite what its makers intended. To get her sister back she will have to learn what her tutor really was, what she herself was made to be — and whether the luck everyone keeps attributing to her is real, or only the story survivors tell.</p>
</div>

<div class="cta-block">
    <a class="btn-primary" href="/fiction/violet/prologue/">Begin reading →</a>
    <p class="continue-line" id="continue-line" hidden>or pick up where you left off — <a id="continue-link" href="#"></a></p>
</div>

<p class="meta-line">Complete draft · about 120,000 words · Book One of a planned trilogy</p>

</div>

<section id="contents">
<p class="section-eyebrow">Contents</p>

{%- assign seq = site.fiction | where_exp: "item", "item.series == 'violet'" | sort: "path" -%}
{%- assign act_romans = "|I|II|III|IV|V" | split: "|" -%}
{%- assign prologue = seq | where_exp: "item", "item.chapter == nil" | where_exp: "item", "item.act == nil" | first -%}
{%- if prologue %}
<div class="act-block prologue-block">
<div class="act-heading">
<h3><a href="{{ prologue.url }}">Prologue</a></h3>
</div>
</div>
{%- endif %}

{%- assign act_pages = seq | where_exp: "item", "item.act != nil" | where_exp: "item", "item.chapter == nil" -%}
{%- for act in act_pages %}
{%- assign parts = act.title | split: ": " -%}
{%- assign act_name = parts | slice: 1, parts.size | join: ": " -%}
{%- assign act_chapters = seq | where_exp: "item", "item.chapter != nil" | where: "act", act.act -%}
<div class="act-block">
<div class="act-heading">
<h3><span class="act-num">Act {{ act_romans[act.act] }}</span> {{ act_name }}</h3>
<a class="act-epigraph-link" href="{{ act.url }}">Epigraph →</a>
</div>
<ol class="chapter-list" start="{{ act_chapters.first.chapter }}">
{%- for ch in act_chapters %}
<li><a href="{{ ch.url }}">{{ ch.title }}</a></li>
{%- endfor %}
</ol>
</div>
{%- endfor %}

</section>

<div class="reference-row">
<a href="/fiction/violet/personages/">Personages</a>
<a href="/fiction/violet/timeline/">Timeline</a>
<a href="/fiction/violet/world-map/">World Map</a>
<a href="/fiction/violet/glossary/">Glossary</a>
</div>

<script>
(function () {
    if (typeof window === "undefined" || !window.localStorage) return;
    try {
        var raw = localStorage.getItem("violet:last");
        if (!raw) return;
        var last = JSON.parse(raw);
        if (!last || !last.url || !last.title) return;
        var line = document.getElementById("continue-line");
        var link = document.getElementById("continue-link");
        link.href = last.url;
        link.textContent = last.title;
        line.hidden = false;
    } catch (e) { /* storage unavailable or malformed; ignore */ }
})();
</script>
