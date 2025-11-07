---
layout: minimal
title: "Prologue"
permalink: /fiction/violet/prologue/
date: November 02, 2025
---

<article class="violet-page prologue-page">
    <header class="page-header">
        <div class="back-link-container">
            <a href="/fiction/violet/" class="back-link">← Violet</a>
        </div>
        <h1 class="page-title">Prologue</h1>
    </header>

    <div class="prologue-content">
        <p class="prologue-epigraph">
            <em>About a thousand years ago, something else happened; not in addition to – instead of. As a result, many things happened that never did and more than few happened that haven't yet. Quite a lot that happened still did. Or looks like it when you squint.</em>
        </p>
    </div>

    <nav class="page-navigation">
        <div class="nav-links">
            <a href="/fiction/violet/act-1-ātmanic-exaptations/" class="nav-next">Begin the Story →</a>
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
        display: flex;
        flex-direction: column;
    }

    /* Header */
    .page-header {
        max-width: 900px;
        margin: 0 auto 4rem auto;
        text-align: center;
        position: relative;
        width: 100%;
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

    /* Prologue content */
    .prologue-content {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        max-width: 900px;
        margin: 0 auto;
        width: 100%;
        min-height: 50vh;
    }

    .prologue-epigraph {
        font-size: 1.3rem;
        line-height: 1.9;
        text-align: center;
        color: #c49fd1;
        max-width: 700px;
        margin: 0 auto;
        padding: 3rem 2rem;
        font-family: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
        border: 1px solid #2d1a3d;
        border-radius: 8px;
        background: #0f0a1a;
        box-shadow: 0 4px 16px rgba(180, 124, 199, 0.1);
    }

    .prologue-epigraph em {
        font-style: italic;
        color: #d5b8e0;
    }

    /* Navigation */
    .page-navigation {
        max-width: 900px;
        margin: 0 auto;
        padding-top: 3rem;
        border-top: 1px solid #2d1a3d;
        width: 100%;
    }

    .nav-links {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .nav-next {
        font-size: 1.1rem;
        font-weight: 500;
        padding: 1rem 2.5rem;
        border: 2px solid #b47cc7;
        border-radius: 4px;
        transition: all 0.3s ease;
        text-decoration: none;
        color: #d5b8e0;
        background: transparent;
        position: relative;
        animation: subtle-pulse 3s ease-in-out infinite;
        border: none;
    }

    @keyframes subtle-pulse {
        0%, 100% {
            box-shadow: 0 0 0 0 rgba(180, 124, 199, 0);
        }
        50% {
            box-shadow: 0 0 0 4px rgba(180, 124, 199, 0.2);
        }
    }

    .nav-next:hover {
        background: #b47cc7;
        color: #0a0514;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(180, 124, 199, 0.3);
        animation: none;
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

        .prologue-epigraph {
            font-size: 1.1rem;
            padding: 2rem 1.5rem;
        }

        .nav-next {
            width: 100%;
            text-align: center;
            padding: 1rem 2rem;
        }
    }
</style>