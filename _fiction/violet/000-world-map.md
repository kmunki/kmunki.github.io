---
layout: minimal
title: "World Map"
permalink: /fiction/violet/world-map/
collection: fiction
series: violet
order: 0
published: true
---

<article class="violet-page world-map-page">
    <header class="page-header">
        <div class="back-link-container">
            <a href="/fiction/violet/" class="back-link">← Violet</a>
        </div>
        <h1 class="page-title">World Map</h1>
    </header>

<div class="page-content">
    <div class="map-container">
        <a href="/assets/images/violet/world-map.jpg" target="_blank" class="map-link">
            <img src="/assets/images/violet/world-map.jpg" alt="Map of the World of Violet" class="world-map-image"/>
            <span class="zoom-hint">Click to view full size</span>
        </a>
    </div>

    <p class="map-caption">
        <em>An alternate history where Zheng He's westward expansion changed everything.</em>
    </p>
</div>

    <nav class="page-navigation">
        <div class="nav-links">
            <a href="/fiction/violet/prologue/" class="nav-skip">Skip to Prologue →</a>
            <a href="/fiction/violet/personages/" class="nav-next">Continue →</a>
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
        max-width: 1200px;
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
        max-width: 1200px;
        margin: 0 auto 4rem auto;
    }

    /* Map container */
    .map-container {
        margin: 2rem 0;
        position: relative;
    }

    .map-link {
        display: block;
        position: relative;
        border: 2px solid #2d1a3d;
        border-radius: 8px;
        overflow: hidden;
        transition: all 0.3s ease;
        cursor: pointer;
        background: #0f0a1a;
        border: none;
    }

    .map-link:hover {
        border-color: #b47cc7;
        box-shadow: 0 8px 24px rgba(180, 124, 199, 0.2);
        transform: translateY(-4px);
        opacity: 1;
    }

    .world-map-image {
        width: 100%;
        height: auto;
        display: block;
        transition: all 0.3s ease;
        filter: brightness(0.95) contrast(1.05);
    }

    .map-link:hover .world-map-image {
        filter: brightness(1) contrast(1.1);
    }

    .zoom-hint {
        position: absolute;
        bottom: 1.5rem;
        right: 1.5rem;
        background: rgba(180, 124, 199, 0.9);
        color: #0a0514;
        padding: 0.75rem 1.5rem;
        border-radius: 4px;
        font-size: 0.85rem;
        font-weight: 500;
        opacity: 0;
        transition: opacity 0.3s ease;
        pointer-events: none;
        letter-spacing: 0.02em;
    }

    .map-link:hover .zoom-hint {
        opacity: 1;
    }

    .map-caption {
        text-align: center;
        margin-top: 2rem;
        font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
        font-size: 1.1rem;
        color: #c49fd1;
    }

    .map-caption em {
        font-style: italic;
        color: #8566a0;
    }

    /* Navigation */
    .page-navigation {
        max-width: 1200px;
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
            padding: 2rem 1rem;
        }

        .page-header {
            margin-bottom: 3rem;
        }

        .page-title {
            font-size: 1.8rem;
            margin-top: 2rem;
        }

        .back-link-container {
            position: static;
            margin-bottom: 1.5rem;
        }

        .zoom-hint {
            opacity: 0.85;
            font-size: 0.75rem;
            padding: 0.5rem 1rem;
            bottom: 1rem;
            right: 1rem;
        }

        .map-caption {
            font-size: 1rem;
            margin-top: 1.5rem;
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
