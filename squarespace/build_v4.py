import html as htmlmod
import json
import os

# --- Real logo / badge images -----------------------------------------
# Hosted on Squarespace's own Media Library. Re-run this script any time
# these change -- every page regenerates with the real images automatically.
LOGO_IMG_URL = "https://images.squarespace-cdn.com/content/67be24bed792a2372316aadf/ab150a06-6b43-4f83-9884-46128c4aeafe/TRAZO+TRUST+CODE.png?content-type=image%2Fpng"          # "trustcode mx" wordmark -- header/footer brand mark
MONDAY_BADGE_IMG_URL = "https://images.squarespace-cdn.com/content/67be24bed792a2372316aadf/05b7e34f-8f9d-49aa-b1f8-eb40e5717b77/badge+for+your+website+only.png?content-type=image%2Fpng"  # hexagon badge -- hero pill + final CTA badge (compact spots)
MONDAY_WORDMARK_IMG_URL = "https://images.squarespace-cdn.com/content/67be24bed792a2372316aadf/62db7255-405d-4544-920e-1a5c025a6e74/monday.com+certified+partner+%281%29.png?content-type=image%2Fpng"  # wordmark -- footer, alongside the Trust Code logo
MONDAY_LOGO_IMG_URL = "https://images.squarespace-cdn.com/content/67be24bed792a2372316aadf/9217fbfa-f063-4b18-9f2f-f76ae567aadb/logo_black.png?content-type=image%2Fpng"  # plain monday.com logo (no partner text) -- not wired to a page yet, pending a placement decision
GABRIEL_PHOTO_URL = "https://images.squarespace-cdn.com/content/67be24bed792a2372316aadf/5a457d5f-7752-4740-b7d8-8d9a084dd42b/IMG_4979+%281%29.PNG?content-type=image%2Fjpeg"  # founder photo -- About Us page
# ------------------------------------------------------------------------

BASE_URL = "https://www.trustcodemx.com"
OUT = os.path.dirname(os.path.abspath(__file__))
PREVIEW_DIR = os.path.join(OUT, "preview")
SLIM_DIR = os.path.join(OUT, "squarespace-slim")
PAGEHEAD_DIR = os.path.join(OUT, "squarespace-page-head")
SITEWIDE_DIR = os.path.join(OUT, "squarespace-sitewide")
for d in (PREVIEW_DIR, SLIM_DIR, PAGEHEAD_DIR, SITEWIDE_DIR):
    os.makedirs(d, exist_ok=True)

# ---------------------------------------------------------------
# ICONS (feather-style line icons, 24x24, stroke=currentColor)
# ---------------------------------------------------------------
def icon(paths, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="ic" {extra}>{paths}</svg>'

ICONS = {
    "link":        icon('<path d="M10 14a5 5 0 0 1 0-7l2-2a5 5 0 0 1 7 7l-1 1"/><path d="M14 10a5 5 0 0 1 0 7l-2 2a5 5 0 0 1-7-7l1-1"/>'),
    "eye":         icon('<path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7S1 12 1 12z"/><circle cx="12" cy="12" r="3"/>'),
    "repeat":      icon('<path d="M17 2l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>'),
    "layers":      icon('<rect x="3" y="3" width="9" height="9" rx="1"/><rect x="12" y="12" width="9" height="9" rx="1"/>'),
    "shield":      icon('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6l8-4z"/><path d="M9 12l2 2 4-4"/>'),
    "briefcase":   icon('<rect x="2" y="7" width="20" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M2 13h20"/>'),
    "bars":        icon('<path d="M4 20V10"/><path d="M12 20V4"/><path d="M20 20v-7"/><path d="M2 20h20"/>'),
    "venn":        icon('<circle cx="9" cy="12" r="6"/><circle cx="15" cy="12" r="6"/>'),
    "grid":        icon('<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/>'),
    "cap":         icon('<path d="M2 9l10-5 10 5-10 5-10-5z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/>'),
    "megaphone":   icon('<path d="M3 11v2a2 2 0 0 0 2 2h1l3 5V4l-3 5H5a2 2 0 0 0-2 2z"/><path d="M14 8a4 4 0 0 1 0 8"/><path d="M17 5a8 8 0 0 1 0 14"/>'),
    "sliders":     icon('<path d="M4 6h10"/><circle cx="17" cy="6" r="2"/><path d="M20 12H10"/><circle cx="7" cy="12" r="2"/><path d="M4 18h10"/><circle cx="17" cy="18" r="2"/>'),
    "trending":    icon('<path d="M3 17l6-6 4 4 7-8"/><path d="M15 6h5v5"/>'),
    "alert":       icon('<circle cx="12" cy="12" r="9"/><path d="M12 8v5"/><path d="M12 16h.01"/>'),
    "check":       icon('<circle cx="12" cy="12" r="9"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>'),
    "browser":     icon('<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 8h20"/><circle cx="5.5" cy="6" r=".6" fill="currentColor" stroke="none"/>'),
    "share":       icon('<circle cx="6" cy="12" r="2.6"/><circle cx="17" cy="6" r="2.6"/><circle cx="17" cy="18" r="2.6"/><path d="M8.3 10.8l6.4-3.2M8.3 13.2l6.4 3.2"/>'),
    "image":       icon('<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.6"/><path d="M21 15l-5-5-9 9"/>'),
    "calendar":    icon('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
}

ANIMATED_BARS = '<svg viewBox="0 0 24 24" fill="none" class="ic"><rect class="roi-bar b1" x="3" y="12" width="4.5" height="8" rx="1" fill="currentColor"/><rect class="roi-bar b2" x="9.75" y="7" width="4.5" height="13" rx="1" fill="currentColor"/><rect class="roi-bar b3" x="16.5" y="2" width="4.5" height="18" rx="1" fill="currentColor"/></svg>'

# BUILD_MODE["lang"] is one of "toggle-en" / "toggle-es" for every generated page.
# Every page is a genuinely separate, static, crawlable page in its own language
# (correct for SEO / hreflang), but each also carries data-en/data-es pairs so the
# client-side EN/ES button can still flip text in place without navigating.
BUILD_MODE = {"lang": "toggle-en"}

def is_es():
    return BUILD_MODE["lang"] == "toggle-es"

def prefix():
    return "/es" if is_es() else ""

def T(en, es, tag="span", cls=""):
    visible = es if is_es() else en
    esc_es = htmlmod.escape(es, quote=True)
    esc_en = htmlmod.escape(en, quote=True)
    c = f' {cls}' if cls else ''
    return f'<{tag} class="i18n{c}" data-es="{esc_es}" data-en="{esc_en}">{visible}</{tag}>'

# ---------------------------------------------------------------
# STYLE (dark base -> derives the light theme actually shipped)
# ---------------------------------------------------------------
STYLE = """
<style>
  :root {
    --bg: #0B0D12;
    --surface: #14171D;
    --surface-2: #1B1F27;
    --line: rgba(255,255,255,0.09);
    --ink: #E7E9EE;
    --muted: #8A8F9C;
    --purple: #6161FF;
    --purple-bright: #8A8AFF;
    --emerald: #00CA72;
    --font-display: 'Manrope', sans-serif;
    --font-mono: 'IBM Plex Mono', monospace;
    /* motion language: 3 curves used consistently, not invented per-component */
    --ease-entrance: cubic-bezier(.16,1,.3,1);      /* one-time reveals */
    --ease-interactive: cubic-bezier(.4,0,.2,1);    /* hover / interactive feedback */
    --ease-emphasis: cubic-bezier(.34,1.56,.64,1);  /* pulses, pops, gentle overshoot */
    /* monday.com product status colors -- scoped to the 5 illustrative diagram
       components ONLY (workflow/funnel/chart/ring/board). Brand-fixed, not
       swapped between themes. Do not use these on site chrome/buttons/cards. */
    --status-stuck: #FB275D;
    --status-working: #FFCC00;
    --status-done: #00CA72;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.001ms !important; transition-duration: 0.001ms !important; }
  }
  html { scroll-behavior: smooth; }
  body { font-family: var(--font-display); color: var(--ink); background: var(--bg); line-height: 1.55; overflow-x: hidden; }
  h1, h2, h3, h4 { font-family: var(--font-display); color: var(--ink); line-height: 1.15; font-weight: 700; letter-spacing: -0.01em; }
  a { text-decoration: none; color: inherit; }
  .tc-wrap { max-width: 1160px; margin: 0 auto; padding: 0 32px; }
  .ic { width: 22px; height: 22px; flex-shrink: 0; }
  .eyebrow {
    font-family: var(--font-mono); font-size: 12px; font-weight: 500; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--purple-bright); display: inline-flex; align-items: center; gap: 10px;
  }
  .eyebrow::before { content: ''; width: 16px; height: 1px; background: var(--purple-bright); }

  header { position: sticky; top: 0; z-index: 100; background: rgba(11,13,18,0.82); backdrop-filter: blur(10px); border-bottom: 1px solid var(--line); }
  nav.tc-wrap { display: flex; align-items: center; justify-content: space-between; height: 78px; gap: 18px; }
  .brand-lockup { display: inline-flex; align-items: baseline; gap: 1px; flex-shrink: 0; }
  .bl-trust { font-family: var(--font-display); font-weight: 400; font-size: 18px; color: var(--muted); }
  .bl-code { font-family: var(--font-display); font-weight: 800; font-size: 18px; color: var(--ink); }
  .bl-mx { font-family: var(--font-mono); font-size: 10.5px; font-weight: 600; color: var(--purple-bright); margin-left: 3px; letter-spacing: 0.02em; }
  .footer-col .brand-lockup .bl-trust, .footer-col .brand-lockup .bl-code { font-size: 20px; }
  .nav-links { display: flex; align-items: center; gap: 28px; font-size: 14px; font-weight: 500; color: var(--muted); }
  .nav-links a { transition: color 0.2s ease; }
  .nav-links a:hover { color: var(--ink); }
  .nav-right { display: flex; align-items: center; gap: 14px; }
  .lang-toggle {
    font-family: var(--font-mono); font-size: 12px; font-weight: 600; color: var(--muted);
    border: 1px solid var(--line); padding: 7px 12px; border-radius: 20px; cursor: pointer; background: transparent;
    transition: color 0.2s ease, border-color 0.2s ease;
  }
  .lang-toggle:hover { color: var(--ink); border-color: var(--purple-bright); }
  .nav-cta {
    border: 1px solid var(--purple); color: var(--purple-bright) !important; padding: 10px 20px; border-radius: 3px;
    font-size: 13.5px; font-weight: 600; letter-spacing: 0.02em; transition: background 0.2s ease, color 0.2s ease;
  }
  .nav-cta:hover { background: var(--purple); color: #fff !important; }

  .nav-burger {
    display: none; flex-direction: column; justify-content: center; gap: 5px;
    width: 32px; height: 32px; background: transparent; border: none; cursor: pointer; padding: 0; flex-shrink: 0;
  }
  .nav-burger span {
    display: block; width: 100%; height: 2px; background: var(--ink); border-radius: 2px;
    transition: transform 0.25s var(--ease-interactive), opacity 0.2s ease;
  }
  .nav-burger[aria-expanded="true"] span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
  .nav-burger[aria-expanded="true"] span:nth-child(2) { opacity: 0; }
  .nav-burger[aria-expanded="true"] span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

  .mobile-menu {
    display: flex; flex-direction: column; position: fixed; top: 78px; left: 0; right: 0; bottom: 0;
    background: var(--surface); border-top: 1px solid var(--line); overflow-y: auto;
    -webkit-overflow-scrolling: touch; z-index: 150;
    opacity: 0; transform: translateY(-6px); pointer-events: none;
    transition: opacity 0.25s var(--ease-interactive), transform 0.25s var(--ease-interactive);
  }
  .mobile-menu.open { opacity: 1; transform: translateY(0); pointer-events: auto; }
  .mobile-menu a {
    display: block; padding: 15px 32px; font-size: 15.5px; font-weight: 500; color: var(--ink) !important;
    border-bottom: 1px solid var(--line); transition: background 0.15s ease; flex-shrink: 0;
  }
  .mobile-menu a:active, .mobile-menu a:hover { background: var(--surface-2); }
  .mobile-accordion { border-bottom: 1px solid var(--line); flex-shrink: 0; }
  .mobile-accordion-trigger {
    width: 100%; display: flex; align-items: center; justify-content: space-between;
    padding: 15px 32px; font-size: 15.5px; font-weight: 500; color: var(--ink); font-family: var(--font-display);
    background: transparent; border: none; cursor: pointer; text-align: left;
  }
  .mobile-accordion-trigger svg { width: 11px; height: 11px; flex-shrink: 0; transition: transform 0.2s ease; }
  .mobile-accordion.open .mobile-accordion-trigger svg { transform: rotate(180deg); }
  .mobile-accordion-panel { max-height: 0; overflow: hidden; background: var(--surface-2); transition: max-height 0.3s var(--ease-interactive); }
  .mobile-accordion.open .mobile-accordion-panel { max-height: 500px; }
  .mobile-accordion-panel a { padding-left: 46px; border-bottom: 1px solid var(--line); }
  .mobile-accordion-panel a:last-child { border-bottom: none; }
  .mobile-cta {
    display: block; margin: 20px 32px; text-align: center; background: var(--purple);
    color: #fff !important; padding: 14px; border-radius: 3px; font-weight: 700; font-size: 14.5px;
    border-bottom: none !important; flex-shrink: 0;
  }

  .hero { position: relative; padding: 90px 0 100px; border-bottom: 1px solid var(--line); }
  .hero::before {
    content: ''; position: absolute; inset: 0; pointer-events: none;
    background: radial-gradient(600px 380px at 88% 8%, rgba(97,97,255,0.14), transparent 70%);
  }
  .hero .tc-wrap { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 60px; align-items: center; position: relative; }
  .hero-split { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 50px; align-items: center; }
  .hero h1 { font-size: clamp(34px, 4.4vw, 50px); margin: 18px 0 18px; }
  .hero h1 .purple { color: var(--purple-bright); }
  .hero p.lead { font-size: 16.5px; color: var(--muted); max-width: 440px; margin-bottom: 28px; }

  .btn-primary {
    display: inline-flex; align-items: center; gap: 10px; background: var(--purple); color: #fff;
    padding: 15px 26px; border-radius: 3px; font-weight: 700; font-size: 14.5px; letter-spacing: 0.01em;
    transition: transform 0.18s ease, background 0.18s ease, box-shadow 0.18s ease;
  }
  .btn-primary:hover { background: var(--purple-bright); transform: translateY(-2px); box-shadow: 0 10px 24px rgba(97,97,255,0.28); }
  .btn-primary svg { transition: transform 0.18s ease; }
  .btn-primary:hover svg { transform: translateX(3px); }
  .btn-ghost {
    display: inline-flex; align-items: center; gap: 8px; color: var(--muted) !important; font-size: 14px; font-weight: 500;
    margin-left: 18px; border-bottom: 1px solid transparent; transition: color 0.2s ease, border-color 0.2s ease;
  }
  .btn-ghost:hover { color: var(--ink) !important; border-color: var(--ink); }

  .diagram-card { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 26px 24px 20px; }
  .diagram-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
  .diagram-head span { font-family: var(--font-mono); font-size: 10.5px; color: var(--muted); letter-spacing: 0.06em; }
  .node-label { font-family: var(--font-mono); font-size: 10px; fill: var(--muted); letter-spacing: 0.04em; }
  .node-label.active { fill: var(--status-done); }
  .node-circle { fill: var(--surface-2); stroke: var(--line); stroke-width: 1.4; }
  .node-circle.lit { stroke: var(--status-done); }
  .path-line { fill: none; stroke: var(--line); stroke-width: 1.4; }
  .board-row { stroke: var(--line); stroke-width: 1; }
  .pulse-working { fill: var(--status-working); filter: drop-shadow(0 0 5px rgba(255,204,0,0.7)); }
  .pulse-done { fill: var(--status-done); filter: drop-shadow(0 0 6px rgba(0,202,114,0.9)); }

  section { padding: 90px 0; border-bottom: 1px solid var(--line); }
  section:last-of-type { border-bottom: none; }
  .section-head { max-width: 600px; margin: 0 auto 46px; text-align: center; }
  .section-head h2 { font-size: clamp(24px, 3vw, 34px); margin-top: 14px; }

  .reveal { opacity: 0; transform: translateY(18px); transition: opacity 0.6s var(--ease-entrance), transform 0.6s var(--ease-entrance); }
  .reveal.visible { opacity: 1; transform: translateY(0); }
  .icon-pop { transform: scale(0.5); opacity: 0; transition: transform 0.45s var(--ease-emphasis), opacity 0.3s ease; }
  .reveal.visible .icon-pop { transform: scale(1); opacity: 1; }
  .icon-pop.reveal { transform: translateY(14px) scale(0.94); }
  .icon-pop.reveal.visible { transform: translateY(0) scale(1); }

  .hero-in { opacity: 0; transform: translateY(16px); animation: heroFadeUp 0.7s var(--ease-entrance) forwards; }
  @keyframes heroFadeUp { to { opacity: 1; transform: translateY(0); } }

  .ambient-blob {
    position: absolute; border-radius: 50%; filter: blur(60px); pointer-events: none; z-index: 0;
    animation: driftBlob 14s ease-in-out infinite;
  }
  @keyframes driftBlob {
    0%, 100% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(24px, -18px) scale(1.08); }
  }

  .has-dropdown { position: relative; }
  .dropdown-trigger { display: flex; align-items: center; gap: 5px; cursor: pointer; }
  .dropdown-trigger svg { width: 11px; height: 11px; transition: transform 0.2s ease; }
  .has-dropdown.open .dropdown-trigger svg, .has-dropdown:hover .dropdown-trigger svg { transform: rotate(180deg); }
  .dropdown-menu {
    position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
    padding-top: 14px; opacity: 0; pointer-events: none; transition: opacity 0.18s ease; z-index: 200;
  }
  .has-dropdown.open .dropdown-menu, .has-dropdown:hover .dropdown-menu { opacity: 1; pointer-events: auto; }
  .dropdown-inner {
    background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 8px;
    min-width: 220px; box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    transform: translateY(6px); transition: transform 0.2s var(--ease-interactive);
  }
  .has-dropdown.open .dropdown-inner, .has-dropdown:hover .dropdown-inner { transform: translateY(0); }
  .dropdown-menu a { display: block; padding: 9px 12px; border-radius: 5px; font-size: 13.5px; color: var(--ink) !important; transition: background 0.15s ease; }
  .dropdown-menu a:hover { background: var(--surface-2); color: var(--purple-bright) !important; }

  .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); }
  .problem-card { background: var(--bg); padding: 26px 22px; transition: background 0.25s ease; }
  .problem-card:hover { background: var(--surface); }
  .problem-card .ic { color: var(--purple-bright); margin-bottom: 14px; }
  .problem-card h4 { font-size: 15.5px; margin-bottom: 6px; font-weight: 600; }
  .problem-card p { font-size: 13.5px; color: var(--muted); }

  .timeline { position: relative; max-width: 720px; margin: 0 auto; }
  .timeline::before { content: ''; position: absolute; left: 25px; top: 6px; bottom: 6px; width: 1px; background: var(--line); z-index: 0; }
  .timeline::after {
    content: ''; position: absolute; left: 25px; top: 6px; width: 1px; background: var(--purple); z-index: 0;
    transform-origin: top; transform: scaleY(0); height: calc(100% - 12px);
  }
  .timeline.visible::after { animation: lineGrowPause 2.6s var(--ease-entrance) forwards; }
  @keyframes lineGrowPause {
    0%   { transform: scaleY(0); }
    8%   { transform: scaleY(0.2); }
    20%  { transform: scaleY(0.2); }
    28%  { transform: scaleY(0.4); }
    40%  { transform: scaleY(0.4); }
    48%  { transform: scaleY(0.6); }
    60%  { transform: scaleY(0.6); }
    68%  { transform: scaleY(0.8); }
    80%  { transform: scaleY(0.8); }
    88%  { transform: scaleY(1); }
    100% { transform: scaleY(1); }
  }
  .step { display: flex; gap: 22px; padding-bottom: 38px; position: relative; z-index: 1; }
  .step:last-child { padding-bottom: 0; }
  .step-num {
    flex-shrink: 0; width: 50px; height: 50px; border-radius: 50%; position: relative;
    display: flex; align-items: center; justify-content: center; font-family: var(--font-display); font-weight: 700;
    color: var(--purple-bright); font-size: 15px; letter-spacing: 0; z-index: 2;
  }
  .step-num-ring { position: absolute; inset: 0; border-radius: 50%; background: var(--surface); border: 1px solid var(--line); }
  .step-num-txt { position: relative; }
  @keyframes stepRingPulse {
    0% { transform: scale(1); border-color: var(--line); box-shadow: none; }
    45% { transform: scale(1.14); border-color: var(--purple); box-shadow: 0 0 0 6px rgba(97,97,255,0.14); }
    100% { transform: scale(1); border-color: var(--line); box-shadow: none; }
  }
  .timeline.visible .step:nth-child(1) .step-num-ring { animation: stepRingPulse 0.65s var(--ease-emphasis) .18s; }
  .timeline.visible .step:nth-child(2) .step-num-ring { animation: stepRingPulse 0.65s var(--ease-emphasis) .68s; }
  .timeline.visible .step:nth-child(3) .step-num-ring { animation: stepRingPulse 0.65s var(--ease-emphasis) 1.18s; }
  .timeline.visible .step:nth-child(4) .step-num-ring { animation: stepRingPulse 0.65s var(--ease-emphasis) 1.68s; }
  .timeline.visible .step:nth-child(5) .step-num-ring { animation: stepRingPulse 0.65s var(--ease-emphasis) 2.18s; }
  .step h4 { font-size: 16px; margin-bottom: 4px; font-weight: 600; }
  .step p { color: var(--muted); font-size: 13.5px; max-width: 500px; }

  .grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); }
  .adv-card { background: var(--bg); display: flex; gap: 16px; padding: 24px; transition: background 0.25s ease; align-items: flex-start; }
  .adv-card:hover { background: var(--surface); }
  .adv-card .ic { color: var(--emerald); }
  .adv-card h4 { font-size: 15px; margin-bottom: 4px; font-weight: 600; }
  .adv-card p { font-size: 13px; color: var(--muted); }
  .roi-bar { transform: scaleY(0); transform-origin: bottom; transform-box: fill-box; transition: transform 0.6s var(--ease-emphasis); }
  .adv-card.visible .roi-bar.b1, .roi-target.visible .roi-bar.b1 { transition-delay: .05s; }
  .adv-card.visible .roi-bar.b2, .roi-target.visible .roi-bar.b2 { transition-delay: .15s; }
  .adv-card.visible .roi-bar.b3, .roi-target.visible .roi-bar.b3 { transition-delay: .25s; }
  .adv-card.visible .roi-bar, .roi-target.visible .roi-bar { transform: scaleY(1); }

  .ring-num { font-family: var(--font-display); font-weight: 800; font-size: 32px; color: var(--ink); }
  .ring-caption { font-family: var(--font-mono); font-size: 10.5px; color: var(--muted); letter-spacing: .04em; text-transform: uppercase; margin-top: 4px; text-align: center; max-width: 120px; }

  /* --- training checklist (modules checking off one by one) --- */
  .tchk-wrap { display: flex; flex-direction: column; gap: 11px; padding: 6px 4px 2px; }
  .tchk-row { display: flex; align-items: center; gap: 11px; }
  .tchk-box {
    width: 21px; height: 21px; border-radius: 6px; border: 1.5px solid var(--line); flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    transition: background 0.3s var(--ease-emphasis), border-color 0.3s var(--ease-emphasis);
  }
  .tchk-box svg { width: 13px; height: 13px; color: #fff; opacity: 0; transform: scale(0.4);
    transition: opacity 0.3s var(--ease-emphasis), transform 0.3s var(--ease-emphasis); }
  .tchk-wrap.visible .tchk-box { background: var(--status-done); border-color: var(--status-done); }
  .tchk-wrap.visible .tchk-box svg { opacity: 1; transform: scale(1); }
  .tchk-label { font-size: 13px; color: var(--muted); transition: color 0.3s ease; }
  .tchk-wrap.visible .tchk-label { color: var(--ink); }
  .tchk-result {
    display: flex; align-items: baseline; gap: 10px; margin-top: 8px; padding-top: 14px;
    border-top: 1px solid var(--line); opacity: 0; transform: translateY(6px);
    transition: opacity 0.5s var(--ease-entrance), transform 0.5s var(--ease-entrance);
  }
  .tchk-wrap.visible .tchk-result { opacity: 1; transform: translateY(0); }
  .tchk-result .ring-caption { text-transform: none; font-family: var(--font-display); font-size: 12.5px; font-weight: 600; max-width: none; }

  .funnel-wrap { position: relative; padding: 10px 30px 4px; }
  .funnel-seg { height: 34px; margin: 0 auto 6px; border-radius: 4px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px;
    font-size: 11.5px; color: #fff; font-weight: 600;
    transform: scaleX(0); transform-origin: center; transition: transform 0.5s var(--ease-entrance); }
  .funnel-seg span:last-child { font-family: var(--font-mono); font-weight: 600; }
  .ring-box.visible .funnel-seg, .funnel-wrap.visible .funnel-seg { transform: scaleX(1); }
  .funnel-wrap.visible .funnel-seg:nth-child(1) { transition-delay: .05s; }
  .funnel-wrap.visible .funnel-seg:nth-child(2) { transition-delay: .18s; }
  .funnel-wrap.visible .funnel-seg:nth-child(3) { transition-delay: .31s; }
  .funnel-wrap.visible .funnel-seg:nth-child(4) { transition-delay: .44s; }
  .funnel-dot { position: absolute; left: 50%; width: 5px; height: 5px; border-radius: 50%; background: var(--status-done);
    filter: drop-shadow(0 0 4px rgba(0,202,114,0.9)); animation: funnelFall 3.6s linear infinite; }
  @keyframes funnelFall { 0% { top: 6%; opacity: 0; transform: translateX(-50%) scale(1); } 8% { opacity: 1; } 92% { opacity: 1; } 100% { top: 92%; opacity: 0; transform: translateX(-50%) scale(0.4); } }

  /* --- chaos -> order: home hero --- */
  .chaos-stage { position: relative; height: 250px; }
  .chaos-caption {
    font-family: var(--font-mono); font-size: 11px; color: rgba(255,255,255,0.5);
    letter-spacing: .05em; margin-bottom: 14px; transition: color .4s ease;
  }
  .chaos-stage.organized .chaos-caption { color: var(--purple-bright); }
  .chaos-card {
    position: absolute; left: var(--l); top: var(--t); width: 42%; height: 32px; border-radius: 6px;
    background: var(--cc); opacity: .85; transform: rotate(var(--r));
    animation: chaosJitter 2.4s ease-in-out infinite;
    transition: top 1s var(--ease-emphasis), left 1s var(--ease-emphasis), width 1s var(--ease-emphasis),
                height 1s var(--ease-emphasis), background .6s ease, transform 1s var(--ease-emphasis);
  }
  @keyframes chaosJitter {
    0%, 100% { transform: rotate(var(--r)) scale(1); }
    50% { transform: rotate(calc(var(--r) * 1.3)) scale(1.04); }
  }
  .chaos-check {
    position: absolute; right: 10px; top: 50%; transform: translateY(-50%) scale(0);
    width: 18px; height: 18px; border-radius: 50%; background: #14171D; color: var(--status-done);
    font-size: 11px; display: flex; align-items: center; justify-content: center;
    transition: transform .4s var(--ease-emphasis);
  }
  .chaos-stage.organized .chaos-card {
    animation: none; left: 0; top: var(--ot); width: 100%; height: 36px;
    background: #1B1F27; border-left: 3px solid var(--cc); transform: none;
  }
  .chaos-stage.organized .chaos-card.landed .chaos-check { transform: translateY(-50%) scale(1); }

  /* --- results counter: work management hero --- */
  .results-line { stroke-dasharray: 500; stroke-dashoffset: 500; transition: stroke-dashoffset 1.8s var(--ease-entrance); }
  .results-wrap.visible .results-line { stroke-dashoffset: 0; }

  /* --- scaling grid: operations hero --- */
  .scaling-label {
    font-family: var(--font-mono); font-size: 11px; color: var(--status-done);
    letter-spacing: .04em; margin-bottom: 14px; text-align: right;
  }
  .scaling-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; height: 180px; }
  .grid-cell {
    background: var(--surface-2); border-radius: 5px; opacity: 0; transform: scale(0.5);
    display: flex; align-items: center; justify-content: center;
    transition: opacity .5s var(--ease-emphasis), transform .5s var(--ease-emphasis);
  }
  .grid-cell.on { opacity: 1; transform: scale(1); }
  .grid-cell .dot { width: 7px; height: 7px; border-radius: 50%; background: var(--status-done); }

  .chart-wrap { padding: 4px 6px; }
  .chart-num-row { display: flex; align-items: baseline; gap: 10px; margin-bottom: 14px; }
  .chart-num { font-family: var(--font-display); font-weight: 800; font-size: 30px; color: var(--ink); }
  .chart-bars-row { display: flex; align-items: flex-end; gap: 10px; height: 100px; }
  .chart-bars-row .roi-bar { flex: 1; border-radius: 4px 4px 0 0; }

  /* --- website builder: empty browser frame assembling itself --- */
  .wsite-wrap { display: flex; flex-direction: column; gap: 10px; padding: 6px 2px 2px; }
  .wsite-bar { display: flex; gap: 6px; }
  .wsite-bar span { width: 9px; height: 9px; border-radius: 50%; }
  .wsite-bar span:nth-child(1) { background: var(--status-stuck); }
  .wsite-bar span:nth-child(2) { background: var(--status-working); }
  .wsite-bar span:nth-child(3) { background: var(--status-done); }
  .wsite-block {
    background: var(--surface-2); border: 1px solid var(--line); border-radius: 6px;
    opacity: 0; transform: translateY(10px);
    transition: opacity 0.5s var(--ease-entrance), transform 0.5s var(--ease-entrance);
  }
  .wsite-hero { height: 68px; }
  .wsite-row { display: flex; gap: 10px; }
  .wsite-col { flex: 1; height: 54px; }
  .wsite-footer { height: 20px; }
  .wsite-wrap.visible .wsite-block { opacity: 1; transform: translateY(0); }
  .wsite-wrap.visible .wsite-hero { transition-delay: .1s; }
  .wsite-wrap.visible .wsite-col:nth-child(1) { transition-delay: .32s; }
  .wsite-wrap.visible .wsite-col:nth-child(2) { transition-delay: .44s; }
  .wsite-wrap.visible .wsite-footer { transition-delay: .58s; }

  .count-num { font-variant-numeric: tabular-nums; }

  /* flex, not grid: the service count doesn't divide evenly, and flex-wrap
     avoids leaving an empty trailing cell the way a fixed grid column count would */
  .grid-5 { display: flex; flex-wrap: wrap; gap: 1px; background: var(--line); border: 1px solid var(--line); }
  .service-card { flex: 1 1 240px; background: var(--bg); padding: 24px 18px; min-height: 165px; display: flex; flex-direction: column; gap: 10px; transition: background 0.28s ease; }
  .service-card:hover { background: var(--surface); }
  .service-card .ic { color: var(--sc-accent, var(--purple-bright)); }
  .service-card h4 { font-size: 14.5px; font-weight: 600; }
  .service-card p { font-size: 12px; color: var(--muted); }

  .marquee-wrap { overflow: hidden; position: relative; padding: 44px 0; background: var(--surface); border-bottom: 1px solid var(--line); }
  .marquee-wrap::before, .marquee-wrap::after { content: ''; position: absolute; top: 0; bottom: 0; width: 100px; z-index: 2; }
  .marquee-wrap::before { left: 0; background: linear-gradient(to right, var(--surface), transparent); }
  .marquee-wrap::after { right: 0; background: linear-gradient(to left, var(--surface), transparent); }
  .marquee-track { display: flex; gap: 18px; width: max-content; animation: scroll-left 36s linear infinite; }
  .quote-chip { font-size: 13.5px; color: var(--ink); background: var(--bg); border: 1px solid var(--line); border-radius: 4px; padding: 15px 20px; white-space: nowrap; }
  .quote-chip b { color: var(--purple-bright); font-weight: 600; }
  .quote-chip span { color: var(--muted); font-size: 11.5px; display: block; margin-top: 4px; }
  @keyframes scroll-left { from { transform: translateX(0); } to { transform: translateX(-50%); } }

  .final-cta { text-align: center; }
  .final-cta h2 { font-size: clamp(24px, 3.2vw, 36px); }
  .final-cta p { color: var(--muted); max-width: 460px; margin: 14px auto 26px; }
  .badge { display: inline-flex; align-items: center; gap: 10px; margin-top: 24px; font-family: var(--font-mono); font-size: 11px; color: var(--muted); border: 1px solid var(--line); padding: 8px 16px; border-radius: 20px; background: #000; }
  .eyebrow-logo { display: inline-flex; align-items: center; gap: 9px; background: #000; border: 1px solid var(--line); padding: 6px 12px 6px 10px; border-radius: 20px; margin-bottom: 4px; }
  .eyebrow-logo span, .badge span { font-family: var(--font-mono); font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }

  footer { padding: 54px 0 36px; }
  .footer-grid { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 30px; margin-bottom: 36px; }
  .footer-col h5 { font-family: var(--font-mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin-bottom: 14px; }
  .footer-col a { display: block; font-size: 13.5px; color: var(--ink); margin-bottom: 9px; opacity: 0.8; transition: opacity 0.2s ease, color 0.2s ease; }
  .footer-col a:hover { opacity: 1; color: var(--purple-bright); }
  .footer-bottom { border-top: 1px solid var(--line); padding-top: 22px; font-size: 12.5px; color: var(--muted); display: flex; justify-content: space-between; }
  .footer-bottom a:hover { color: var(--purple-bright); }

  .subhero { padding: 64px 0 54px; border-bottom: 1px solid var(--line); }
  .crumb { font-family: var(--font-mono); font-size: 12px; color: var(--muted); margin-bottom: 16px; display:block; }
  .crumb a { color: var(--muted); } .crumb a:hover { color: var(--ink); }
  .crumb .accent { color: var(--purple-bright); }
  .subhero h1 { font-size: clamp(28px, 3.8vw, 42px); max-width: 720px; margin-bottom: 14px; }
  .subhero .lead { font-size: 16px; color: var(--muted); max-width: 560px; margin-bottom: 26px; }
  .row-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: start; }
  .col-block h3 { font-size: 12.5px; font-family: var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 20px; }
  .item-list { display: flex; flex-direction: column; gap: 18px; }
  .item-list .it { display: flex; gap: 14px; align-items: flex-start; }
  .item-list .it .ic { margin-top: 2px; }
  .item-list .it.challenge .ic { color: var(--muted); }
  .item-list .it.solution .ic { color: var(--purple-bright); }
  .item-list .it b { display: block; font-size: 14.5px; color: var(--ink); font-weight: 600; }
  .item-list .it p { font-size: 13px; color: var(--muted); margin-top: 2px; }
  .getgrid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); }
  .getcard { background: var(--bg); padding: 22px; display: flex; gap: 12px; align-items: flex-start; }
  .getcard .ic { color: var(--emerald); }
  .getcard b { display: block; font-size: 14px; margin-bottom: 2px; }
  .getcard p { font-size: 13px; color: var(--muted); }

  /* --- founder / leadership card (About Us) --- */
  .founder-card { display: flex; gap: 36px; align-items: flex-start; max-width: 760px; margin: 0 auto; }
  .founder-photo { width: 140px; height: 140px; border-radius: 50%; object-fit: cover; flex-shrink: 0; border: 1px solid var(--line); }
  .founder-text h3 { font-size: 21px; margin-bottom: 8px; }
  .founder-text .eyebrow { display: inline-flex; margin-bottom: 14px; }
  .founder-text p { font-size: 14.5px; color: var(--muted); line-height: 1.7; }
  @media (max-width: 560px) {
    .founder-card { flex-direction: column; align-items: center; text-align: center; }
    .founder-text .eyebrow { justify-content: center; }
  }

  /* --- tool integration marquee --- */
  .tool-marquee { overflow: hidden; position: relative; padding: 6px 0; }
  .tool-marquee::before, .tool-marquee::after { content: ''; position: absolute; top: 0; bottom: 0; width: 90px; z-index: 2; }
  .tool-marquee::before { left: 0; background: linear-gradient(to right, var(--bg), transparent); }
  .tool-marquee::after { right: 0; background: linear-gradient(to left, var(--bg), transparent); }
  .tool-track { display: flex; gap: 14px; width: max-content; animation: scroll-left 30s linear infinite; }
  .tool-chip {
    display: inline-flex; align-items: center; gap: 9px; white-space: nowrap;
    background: var(--surface); border: 1px solid var(--line); border-radius: 8px;
    padding: 11px 18px; font-size: 13.5px; font-weight: 600; color: var(--ink);
    transition: border-color 0.2s var(--ease-interactive), transform 0.2s var(--ease-interactive);
  }
  .tool-chip:hover { border-color: var(--purple-bright); transform: translateY(-2px); }
  .tool-chip .dot {
    width: 9px; height: 9px; border-radius: 3px; flex-shrink: 0;
    filter: grayscale(1) opacity(0.55); transition: filter 0.2s var(--ease-interactive);
  }
  .tool-chip:hover .dot { filter: grayscale(0) opacity(1); }

  /* --- proof stat row --- */
  .stat-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
  .stat-cell { background: var(--bg); padding: 28px 20px; text-align: center; transition: background 0.25s ease; }
  .stat-cell:hover { background: var(--surface); }
  .stat-num { font-family: var(--font-display); font-weight: 800; font-size: 32px; color: var(--ink); font-variant-numeric: tabular-nums; }
  .stat-label { font-size: 12.5px; color: var(--muted); margin-top: 6px; }
  .stat-source-note { font-family: var(--font-mono); font-size: 11px; color: var(--muted); text-align: center; margin-top: 18px; opacity: .8; }

  /* --- magnetic primary buttons (site-wide) --- */
  .btn-primary { transform: translate(var(--mx, 0px), var(--my, 0px)); }
  .btn-primary:hover { transform: translate(var(--mx, 0px), calc(var(--my, 0px) - 2px)); }

  @media (max-width: 900px) {
    .hero .tc-wrap, .hero-split { grid-template-columns: 1fr; }
    .diagram-card { order: -1; }
    .nav-links { display: none; }
    .nav-burger { display: flex; }
    .nav-cta { display: none; }
    .grid-4, .grid-2, .row-2, .getgrid, .grid-3 { grid-template-columns: 1fr 1fr; }
    .service-card { flex-basis: 45%; }
    .stat-row { grid-template-columns: 1fr 1fr; }
  }
  @media (max-width: 560px) {
    .grid-4, .grid-2, .row-2, .getgrid, .grid-3 { grid-template-columns: 1fr; }
    .service-card { flex-basis: 100%; }
    .tc-wrap { padding: 0 20px; }
    .stat-row { grid-template-columns: 1fr; }
  }
</style>
"""

LIGHT_ROOT = """
  :root {
    --bg: #FAFAFC;
    --surface: #FFFFFF;
    --surface-2: #F0F1F5;
    --line: rgba(15,17,25,0.09);
    --ink: #14171D;
    --muted: #6B7080;
    --purple: #6161FF;
    --purple-bright: #4A46E0;
    --emerald: #00A05C;
    --font-display: 'Manrope', sans-serif;
    --font-mono: 'IBM Plex Mono', monospace;
    --ease-entrance: cubic-bezier(.16,1,.3,1);
    --ease-interactive: cubic-bezier(.4,0,.2,1);
    --ease-emphasis: cubic-bezier(.34,1.56,.64,1);
    --status-stuck: #FB275D;
    --status-working: #FFCC00;
    --status-done: #00CA72;
  }
"""

LIGHT_OVERRIDES = """
<style>
  /* --- light theme overrides --- */
  header { background: rgba(250,250,252,0.85); }
  .nav-cta:hover { color: #fff !important; }
  .problem-card:hover, .adv-card:hover, .service-card:hover { background: var(--surface-2); }
  .quote-chip { background: var(--surface); }
  .marquee-wrap { background: var(--surface-2); }
  .marquee-wrap::before { background: linear-gradient(to right, var(--surface-2), transparent); }
  .marquee-wrap::after { background: linear-gradient(to left, var(--surface-2), transparent); }
  .step-num-ring { background: var(--surface); }
  /* diagram card stays dark deliberately, as a product-UI accent panel */
  .diagram-card { background: #14171D; border-color: rgba(255,255,255,0.09); }
  .diagram-head span { color: rgba(255,255,255,0.5); }
  .node-circle { fill: #1B1F27; stroke: rgba(255,255,255,0.09); }
  .node-label { fill: rgba(255,255,255,0.45); }
  .path-line { stroke: rgba(255,255,255,0.12); }
  .board-row { stroke: rgba(255,255,255,0.12); }
  /* these headline numbers sit inside the always-dark diagram-card even in
     light theme -- var(--ink) resolves dark-on-dark there without this fix */
  .ring-num, .chart-num { color: #fff; }
  .tchk-wrap.visible .tchk-label { color: rgba(255,255,255,0.85); }
  .badge, .eyebrow-logo { background: #0B0D12; }
  .badge span, .eyebrow-logo span { color: rgba(255,255,255,0.6); }
  section { border-bottom-color: var(--line); }
  .final-cta { background: #14171D; border-radius: 20px; padding: 50px 30px; }
  .final-cta h2, .final-cta .eyebrow { color: #fff; }
  .final-cta .eyebrow::before { background: var(--purple-bright); }
  .final-cta p { color: rgba(255,255,255,0.6); }
  /* blog cards */
  .blog-card { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; transition: transform 0.3s cubic-bezier(0.16,1,0.3,1), box-shadow 0.3s ease; }
  .blog-card:hover { transform: translateY(-6px); box-shadow: 0 20px 34px rgba(15,17,25,0.09); }
  .blog-thumb { height: 150px; position: relative; overflow: hidden; }
  .blog-thumb::after { content:''; position:absolute; inset:0; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.25), transparent 60%); }
  .blog-body { padding: 20px 20px 22px; }
  .blog-tag { font-family: var(--font-mono); font-size: 10.5px; letter-spacing: 0.05em; text-transform: uppercase; color: var(--purple-bright); margin-bottom: 10px; display: inline-block; }
  .blog-card h4 { font-size: 16px; margin-bottom: 8px; }
  .blog-card p { font-size: 13.5px; color: var(--muted); margin-bottom: 12px; }
  .blog-meta { font-family: var(--font-mono); font-size: 11px; color: var(--muted); }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }

  /* --- brand lockup / monday.com placeholder badge (swap for real assets in Squarespace media library) --- */
  .mb-ic { display: inline-flex; }
  .mb-ic svg { width: 14px; height: 14px; color: var(--emerald); }
  .mb-txt { display: inline-flex; align-items: center; }
  .brand-logo-img { display: block; width: auto; }
  .footer-col .brand-logo-img { height: 30px; }
  .mb-badge-img { display: block; width: auto; }
  .eyebrow-logo.has-badge-img, .badge.has-badge-img {
    background: transparent; border: none; padding: 0;
  }
  .footer-monday-wordmark { display: block; width: auto; }
</style>
"""

LIGHT_STYLE = STYLE.replace(
    STYLE[STYLE.index(":root {"):STYLE.index("}", STYLE.index(":root {"))+1],
    LIGHT_ROOT.strip()
) + LIGHT_OVERRIDES

# Loaded non-render-blocking: a slow/blocked font CDN (corporate proxy, ad-blocker,
# regional restriction) must never stall the page's first paint -- which, since CSS
# animations only start once rendering begins, was also silently delaying every
# hero-in / count-up animation on this build until the font request resolved.
_FONT_HREF = "https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=IBM+Plex+Mono:wght@500;600&display=swap"
FONT_LINKS = f"""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="{_FONT_HREF}" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link href="{_FONT_HREF}" rel="stylesheet"></noscript>"""

# Styles the native Squarespace Blog Collection. Selectors below are taken
# directly from the client's real rendered markup for both the list view
# (blog-side-by-side list item) and the single-post view (blog-side-by-side
# detail template), not guessed.
BLOG_STYLE = """
<style>
  /* --- list view --- */
  .blog-item { border-bottom: 1px solid var(--line); padding: 44px 0; }
  article.blog-item:first-of-type { padding-top: 0; }
  .blog-image-wrapper .image-wrapper { border-radius: 8px; overflow: hidden; }
  .blog-meta-section {
    font-family: var(--font-mono) !important; font-size: 11px !important; letter-spacing: 0.06em;
    text-transform: uppercase; color: var(--muted) !important;
    display: flex; align-items: center; gap: 8px; margin-bottom: 12px;
  }
  .blog-meta-delimiter { width: 3px; height: 3px; border-radius: 50%; background: var(--muted); display: inline-block; }
  .blog-title {
    font-family: var(--font-display) !important; font-weight: 800 !important;
    font-size: clamp(22px, 3vw, 32px) !important; margin-bottom: 14px !important;
  }
  .blog-title a { color: var(--ink) !important; transition: color 0.2s ease; }
  .blog-title a:hover { color: var(--purple-bright) !important; }
  .blog-excerpt p, .blog-excerpt-wrapper p {
    font-family: var(--font-display) !important; font-size: 15.5px !important;
    color: var(--muted) !important; line-height: 1.6 !important;
  }
  .blog-more-link {
    font-family: var(--font-mono) !important; font-size: 12px !important; font-weight: 600 !important;
    letter-spacing: 0.05em; text-transform: uppercase; color: var(--purple-bright) !important;
    border-bottom: 1px solid var(--purple-bright); padding-bottom: 2px; transition: opacity 0.2s ease;
  }
  .blog-more-link:hover { opacity: 0.7; }

  /* --- single post view --- */
  .entry-title.entry-title--large {
    font-family: var(--font-display) !important; font-weight: 800 !important;
    font-size: clamp(28px, 4vw, 42px) !important; margin-bottom: 8px !important;
  }
  .blog-item-meta-wrapper, .blog-item-author-date-wrapper {
    font-family: var(--font-mono) !important; font-size: 12px !important; letter-spacing: 0.05em;
    text-transform: uppercase; color: var(--muted) !important;
    display: flex; align-items: center; gap: 10px;
  }
  .blog-meta-item--date, .blog-meta-item--author { color: var(--muted) !important; }
  .blog-author-name, .author-name { color: var(--purple-bright) !important; transition: opacity 0.2s ease; }
  .blog-author-name:hover, .author-name:hover { opacity: 0.75; }
  .blog-item-content-wrapper, .blog-item-content-wrapper .sqs-html-content {
    font-family: var(--font-display) !important; color: var(--ink) !important;
  }
  .blog-item-content-wrapper .sqs-html-content p {
    font-size: 16.5px !important; line-height: 1.75 !important; margin-bottom: 20px !important;
  }
  .blog-item-author-profile-wrapper { border-top: 1px solid var(--line); margin-top: 32px; padding-top: 20px; }
</style>
"""

EARLY_SCRIPT = """
<script>
  function animateCounters(root) {
    root.querySelectorAll('.count-num[data-target]').forEach(el => {
      const target = parseFloat(el.dataset.target);
      const suffix = el.dataset.suffix || '';
      const prefix = el.dataset.prefix || '';
      const decimals = (el.dataset.target.split('.')[1] || '').length;
      const duration = 1300;
      const start = performance.now();
      function step(now) {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        const val = (target * eased).toFixed(decimals);
        el.textContent = prefix + Number(val).toLocaleString('en-US', {minimumFractionDigits: decimals}) + suffix;
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }
</script>
"""
with open(os.path.join(SITEWIDE_DIR, "head-injection.txt"), "w") as f:
    f.write(FONT_LINKS + "\n" + LIGHT_STYLE + "\n" + BLOG_STYLE + "\n" + EARLY_SCRIPT)

# Shared script: scroll-reveal, dropdown, and the client-side EN/ES toggle.
# currentLang is read from <html lang> so each page starts in ITS OWN language,
# not hardcoded 'en' -- that was a real bug in the previous build.
LANG_SCRIPT = """
<script>
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        animateCounters(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  let currentLang = (document.documentElement.lang || 'en').toLowerCase().startsWith('es') ? 'es' : 'en';
  function toggleLang() {
    currentLang = currentLang === 'en' ? 'es' : 'en';
    document.querySelectorAll('.i18n').forEach(el => {
      el.innerHTML = currentLang === 'en' ? el.dataset.en : el.dataset.es;
    });
    document.querySelectorAll('.lang-toggle').forEach(b => b.textContent = currentLang === 'en' ? 'ES' : 'EN');
  }

  function toggleDropdown(el) {
    const wasOpen = el.classList.contains('open');
    document.querySelectorAll('.has-dropdown.open').forEach(d => d.classList.remove('open'));
    if (!wasOpen) el.classList.add('open');
  }
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.has-dropdown')) {
      document.querySelectorAll('.has-dropdown.open').forEach(d => d.classList.remove('open'));
    }
  });

  function closeMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    const burger = document.getElementById('navBurger');
    if (menu) menu.classList.remove('open');
    if (burger) burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    const burger = document.getElementById('navBurger');
    if (!menu || !burger) return;
    const opening = !menu.classList.contains('open');
    menu.classList.toggle('open', opening);
    burger.setAttribute('aria-expanded', opening ? 'true' : 'false');
    document.body.style.overflow = opening ? 'hidden' : '';
  }
  function toggleMobileAccordion(trigger) {
    trigger.closest('.mobile-accordion').classList.toggle('open');
  }
  const mobileMenuEl = document.getElementById('mobileMenu');
  if (mobileMenuEl) {
    mobileMenuEl.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMobileMenu));
  }

  // Magnetic primary buttons (site-wide) -- skipped entirely under reduced-motion.
  // rAF-throttled and rects cached on scroll/resize only, so it doesn't force a
  // synchronous layout read on every raw mousemove event (that was causing
  // visible stutter on pages with a prominent hero CTA).
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduceMotion) {
    const magnetPad = 24; // extra px around each button that still pulls it
    const magnetBtns = Array.from(document.querySelectorAll('.btn-primary'));
    let magnetRects = [];
    function refreshMagnetRects() {
      magnetRects = magnetBtns.map((btn) => btn.getBoundingClientRect());
    }
    refreshMagnetRects();
    window.addEventListener('resize', refreshMagnetRects);
    window.addEventListener('scroll', refreshMagnetRects, { passive: true });

    let pendingX = null, pendingY = null, ticking = false;
    function applyMagnet() {
      ticking = false;
      magnetBtns.forEach((btn, i) => {
        const r = magnetRects[i];
        const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
        const withinX = pendingX > r.left - magnetPad && pendingX < r.right + magnetPad;
        const withinY = pendingY > r.top - magnetPad && pendingY < r.bottom + magnetPad;
        if (withinX && withinY) {
          const dx = (pendingX - cx) / (r.width / 2 + magnetPad);
          const dy = (pendingY - cy) / (r.height / 2 + magnetPad);
          btn.style.setProperty('--mx', (dx * 8) + 'px');
          btn.style.setProperty('--my', (dy * 6) + 'px');
        } else {
          btn.style.setProperty('--mx', '0px');
          btn.style.setProperty('--my', '0px');
        }
      });
    }
    document.addEventListener('mousemove', (e) => {
      pendingX = e.clientX; pendingY = e.clientY;
      if (!ticking) { ticking = true; requestAnimationFrame(applyMagnet); }
    }, { passive: true });
  }

</script>
"""

print("style/scripts ready")

# ---------------------------------------------------------------
# Brand marks -- placeholders until the real logo / monday.com
# partner badge are supplied as actual image files.
# ---------------------------------------------------------------
def brand_lockup():
    if LOGO_IMG_URL:
        return f'<img class="brand-logo-img" src="{LOGO_IMG_URL}" alt="Trust Code MX" height="26">'
    return '<span class="brand-lockup"><span class="bl-trust">trust</span><span class="bl-code">code</span><span class="bl-mx">mx</span></span>'

def monday_badge(label_en, label_es, cls="eyebrow-logo"):
    if MONDAY_BADGE_IMG_URL:
        return (f'<span class="{cls} has-badge-img"><img class="mb-badge-img" src="{MONDAY_BADGE_IMG_URL}" '
                f'alt="monday.com Certified Partner" height="18"></span>')
    return (f'<span class="{cls}"><span class="mb-ic">{ICONS["shield"]}</span>'
            f'<span class="mb-txt">monday.com &middot; {T(label_en, label_es)}</span></span>')

def monday_wordmark():
    if MONDAY_WORDMARK_IMG_URL:
        return f'<img class="footer-monday-wordmark" src="{MONDAY_WORDMARK_IMG_URL}" alt="monday.com Certified Partner" height="34">'
    return ""

# ---------------------------------------------------------------
# SEO head block: canonical, hreflang, OpenGraph, Twitter, JSON-LD.
# Every page gets this now -- previously only the homepage did.
# ---------------------------------------------------------------
def page_urls(slug):
    en_path = "/" if slug == "" else f"/{slug}/"
    es_path = "/es/" if slug == "" else f"/es/{slug}/"
    return BASE_URL + en_path, BASE_URL + es_path

def seo_head(slug, title_en, title_es, desc_en, desc_es, json_ld_objects=None):
    _is_es = is_es()
    en_url, es_url = page_urls(slug)
    canonical = es_url if _is_es else en_url
    title = title_es if _is_es else title_en
    desc = desc_es if _is_es else desc_en
    og_locale = "es_MX" if _is_es else "en_US"
    html_lang = "es" if _is_es else "en"
    jsonld_scripts = ""
    for obj in (json_ld_objects or []):
        jsonld_scripts += f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>\n'
    head = f"""<title>{htmlmod.escape(title)}</title>
<meta name="description" content="{htmlmod.escape(desc, quote=True)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{htmlmod.escape(title, quote=True)}">
<meta property="og:description" content="{htmlmod.escape(desc, quote=True)}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{og_locale}">
<meta property="og:site_name" content="Trust Code">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{htmlmod.escape(title, quote=True)}">
<meta name="twitter:description" content="{htmlmod.escape(desc, quote=True)}">
{jsonld_scripts}"""
    return html_lang, head

def breadcrumb_jsonld(slug, crumb_en, crumb_es):
    _is_es = is_es()
    en_url, es_url = page_urls(slug)
    home_en, home_es = page_urls("")
    name = htmlmod.unescape(crumb_es if _is_es else crumb_en)
    items = [
        {"@type": "ListItem", "position": 1, "name": "Inicio" if _is_es else "Home", "item": home_es if _is_es else home_en},
        {"@type": "ListItem", "position": 2, "name": name, "item": es_url if _is_es else en_url},
    ]
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def service_jsonld(name_en, name_es, desc_en, desc_es):
    _is_es = is_es()
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": htmlmod.unescape(name_es if _is_es else name_en),
        "name": htmlmod.unescape(name_es if _is_es else name_en),
        "description": htmlmod.unescape(desc_es if _is_es else desc_en),
        "inLanguage": "es-MX" if _is_es else "en",
        "provider": {"@type": "ProfessionalService", "name": "Trust Code", "url": BASE_URL},
    }

print("seo helpers ready")

# ---------------------------------------------------------------
# HEADER / FOOTER (language-aware: internal links point at /es/... on Spanish pages)
# ---------------------------------------------------------------
def header():
    p = prefix()
    def navlink(href, en, es):
        return f'<a href="{p}{href}">{T(en, es)}</a>'
    chevron = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 9l6 6 6-6"/></svg>'
    dropdown_items = "\n".join([
        f'<a href="{p}/work-management/">{T("Work Management","Gesti&oacute;n del Trabajo")}</a>',
        f'<a href="{p}/team-training/">{T("Training","Capacitaci&oacute;n")}</a>',
        f'<a href="{p}/marketing-crm-solutions/">{T("Marketing &amp; CRM","Marketing y CRM")}</a>',
        f'<a href="{p}/monday-operations/">{T("Operations","Operaciones")}</a>',
        f'<a href="{p}/monday-sales-crm/">{T("Sales &amp; CRM","Ventas y CRM")}</a>',
        f'<a href="{p}/web-design-development/">{T("Web Design &amp; Development","Dise&ntilde;o y Desarrollo Web")}</a>',
        f'<a href="{p}/social-media-management/">{T("Social Media Management","Gesti&oacute;n de Redes Sociales")}</a>',
    ])
    home_href = f"{p}/" if p else "/"
    next_lang_label = "EN" if is_es() else "ES"
    lang_button = f'<button class="lang-toggle" onclick="toggleLang()">{next_lang_label}</button>'
    mobile_solutions_links = "\n".join([
        f'<a href="{p}/work-management/">{T("Work Management","Gesti&oacute;n del Trabajo")}</a>',
        f'<a href="{p}/team-training/">{T("Training","Capacitaci&oacute;n")}</a>',
        f'<a href="{p}/marketing-crm-solutions/">{T("Marketing &amp; CRM","Marketing y CRM")}</a>',
        f'<a href="{p}/monday-operations/">{T("Operations","Operaciones")}</a>',
        f'<a href="{p}/monday-sales-crm/">{T("Sales &amp; CRM","Ventas y CRM")}</a>',
        f'<a href="{p}/web-design-development/">{T("Web Design &amp; Development","Dise&ntilde;o y Desarrollo Web")}</a>',
        f'<a href="{p}/social-media-management/">{T("Social Media Management","Gesti&oacute;n de Redes Sociales")}</a>',
    ])
    mobile_top_links = "\n".join([
        f'<a href="{p}/monday-partner/">{T("Certified Partner","Socio Certificado")}</a>',
        f'<a href="{p}/blog/">{T("Blog","Blog")}</a>',
        f'<a href="{p}/#advantage">{T("Why Us","Por Qu&eacute; Nosotros")}</a>',
        f'<a href="{p}/about-us/">{T("About","Nosotros")}</a>',
    ])
    return f"""<header id="tc-header">
  <nav class="tc-wrap">
    <a href="{home_href}">{brand_lockup()}</a>
    <div class="nav-links">
      <div class="has-dropdown" onclick="toggleDropdown(this)">
        <span class="dropdown-trigger">{T('Solutions','Soluciones')} {chevron}</span>
        <div class="dropdown-menu"><div class="dropdown-inner">{dropdown_items}</div></div>
      </div>
      {navlink('/monday-partner/','Certified Partner','Socio Certificado')}
      {navlink('/blog/','Blog','Blog')}
      {navlink('/#advantage','Why Us','Por Qu&eacute; Nosotros')}
      {navlink('/about-us/','About','Nosotros')}
    </div>
    <div class="nav-right">
      {lang_button}
      <a class="nav-cta" href="https://wkf.ms/49age3d">{T('Free Strategy Session','Sesi&oacute;n Estrat&eacute;gica Gratuita')}</a>
      <button class="nav-burger" id="navBurger" onclick="toggleMobileMenu()" aria-label="Menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</header>
<div class="mobile-menu" id="mobileMenu">
  <div class="mobile-accordion" id="mobileSolutions">
    <button class="mobile-accordion-trigger" onclick="toggleMobileAccordion(this)">
      {T('Solutions','Soluciones')} {chevron}
    </button>
    <div class="mobile-accordion-panel">{mobile_solutions_links}</div>
  </div>
  {mobile_top_links}
  <a class="mobile-cta" href="https://wkf.ms/49age3d">{T('Free Strategy Session','Sesi&oacute;n Estrat&eacute;gica Gratuita')}</a>
</div>
"""

def footer():
    p = prefix()
    return f"""<footer id="tc-footer">
  <div class="tc-wrap">
    <div class="footer-grid">
      <div class="footer-col" style="display:flex; flex-direction:column; gap:14px;">
        {brand_lockup()}
        {monday_wordmark()}
      </div>
      <div class="footer-col">
        <h5>{T('Services','Servicios')}</h5>
        <a href="{p}/work-management/">{T('Work Management','Gesti&oacute;n del Trabajo')}</a>
        <a href="{p}/team-training/">{T('Training','Capacitaci&oacute;n')}</a>
        <a href="{p}/marketing-crm-solutions/">{T('Marketing &amp; CRM','Marketing y CRM')}</a>
        <a href="{p}/monday-operations/">{T('Operations','Operaciones')}</a>
        <a href="{p}/monday-sales-crm/">{T('Sales &amp; CRM','Ventas y CRM')}</a>
        <a href="{p}/web-design-development/">{T('Web Design &amp; Development','Dise&ntilde;o y Desarrollo Web')}</a>
        <a href="{p}/social-media-management/">{T('Social Media Management','Gesti&oacute;n de Redes Sociales')}</a>
      </div>
      <div class="footer-col">
        <h5>{T('Company','Compa&ntilde;&iacute;a')}</h5>
        <a href="{p}/monday-partner/">{T('Solution Partner','Socio de Soluci&oacute;n')}</a>
        <a href="{p}/blog/">{T('Blog','Blog')}</a>
        <a href="{p}/about-us/">{T('About Us','Nosotros')}</a>
        <a href="https://wkf.ms/49age3d">{T('Contact Us','Cont&aacute;ctanos')}</a>
      </div>
    </div>
    <div class="footer-bottom"><span>&copy; Trust Code Mx</span><a href="https://www.trustcodemx.com/privacypolicy" style="color:inherit;">{T('Privacy Policy','Aviso de Privacidad')}</a></div>
  </div>
</footer>
"""

print("header/footer ready")

# ---------------------------------------------------------------
# ANIMATED DIAGRAMS (unchanged behaviourally; still driven by T())
# ---------------------------------------------------------------
def workflow_diagram(labels, id_prefix="h", tag_text="WORKFLOW_ENGINE // trustcodemx", delay="0.2s"):
    left, top, center, bottom, right = labels
    p = id_prefix
    return f"""<div class="diagram-card hero-in" style="animation-delay:{delay}">
      <div class="diagram-head">
        <span>{tag_text}</span>
        <span style="color:var(--status-done)">&#9679; live</span>
      </div>
      <svg viewBox="0 0 400 220" width="100%" style="height:auto; display:block;">
        <line class="board-row" x1="24" y1="50" x2="376" y2="50"/>
        <line class="board-row" x1="24" y1="110" x2="376" y2="110"/>
        <line class="board-row" x1="24" y1="170" x2="376" y2="170"/>
        <path id="{p}1" class="path-line" d="M50,110 C120,110 120,50 200,50"/>
        <path id="{p}2" class="path-line" d="M50,110 C120,110 120,110 200,110"/>
        <path id="{p}3" class="path-line" d="M50,110 C120,110 120,170 200,170"/>
        <path id="{p}4" class="path-line" d="M200,50 C260,50 260,110 320,110"/>
        <path id="{p}5" class="path-line" d="M200,110 C260,110 260,110 320,110"/>
        <path id="{p}6" class="path-line" d="M200,170 C260,170 260,110 320,110"/>
        <circle class="node-circle" cx="50" cy="110" r="20"/>
        <circle class="node-circle" cx="200" cy="50" r="14"/>
        <circle class="node-circle" cx="200" cy="110" r="14"/>
        <circle class="node-circle" cx="200" cy="170" r="14"/>
        <circle class="node-circle lit" cx="320" cy="110" r="20"/>
        <text class="node-label" x="50" y="145" text-anchor="middle">{left}</text>
        <text class="node-label" x="200" y="30" text-anchor="middle">{top}</text>
        <text class="node-label" x="200" y="132" text-anchor="middle">{center}</text>
        <text class="node-label" x="200" y="192" text-anchor="middle">{bottom}</text>
        <text class="node-label active" x="320" y="145" text-anchor="middle">{right}</text>
        <circle class="pulse-working" r="3.5"><animateMotion dur="3.2s" repeatCount="indefinite" begin="0s"><mpath href="#{p}1"/></animateMotion></circle>
        <circle class="pulse-done" r="3.5"><animateMotion dur="3.2s" repeatCount="indefinite" begin="0.5s"><mpath href="#{p}4"/></animateMotion></circle>
        <circle class="pulse-working" r="3.5"><animateMotion dur="2.6s" repeatCount="indefinite" begin="1.1s"><mpath href="#{p}2"/></animateMotion></circle>
        <circle class="pulse-done" r="3.5"><animateMotion dur="2.6s" repeatCount="indefinite" begin="1.7s"><mpath href="#{p}5"/></animateMotion></circle>
        <circle class="pulse-working" r="3.5"><animateMotion dur="3.4s" repeatCount="indefinite" begin="0.9s"><mpath href="#{p}3"/></animateMotion></circle>
        <circle class="pulse-done" r="3.5"><animateMotion dur="3.4s" repeatCount="indefinite" begin="1.5s"><mpath href="#{p}6"/></animateMotion></circle>
      </svg>
    </div>"""

def _self_trigger_script(id_prefix):
    # Waits for the diagram-card's own hero-in fade-in to finish before adding
    # 'visible' / running the counters. Triggering immediately (at parse time)
    # meant the "before" state (scattered cards, empty progress, zero bars) was
    # invisible -- it played out and finished while the card was still fading
    # in, so users only ever saw the final settled state with no visible motion.
    return f"""<script>
      (function(){{
        var el = document.getElementById('{id_prefix}');
        var card = el.closest('.hero-in');
        function trigger(){{ el.classList.add('visible'); animateCounters(el); }}
        if (card) {{ card.addEventListener('animationend', trigger, {{once:true}}); }} else {{ trigger(); }}
      }})();
    </script>"""

def _card_shell(inner, tag_text, id_attr, delay=".2s", extra_class=""):
    return f"""<div class="diagram-card hero-in {extra_class}" id="{id_attr}" style="animation-delay:{delay}">
      <div class="diagram-head">
        <span>{tag_text}</span>
        <span style="color:var(--emerald)">&#9679; live</span>
      </div>
      {inner}
    </div>"""

def training_checklist(id_prefix, tag_text, percent, items, cap_en, cap_es):
    # A literal training curriculum checking itself off, module by module --
    # replaces an abstract progress ring that read as "generic KPI," not
    # obviously about training. Reuses the same 4 real modules described on
    # the Training page itself, so the diagram is directly tied to that
    # content instead of an unrelated illustration.
    rows = "".join(
        f"""<div class="tchk-row" style="transition-delay:{i*0.22:.2f}s;">
              <span class="tchk-box">{ICONS['check']}</span>
              <span class="tchk-label">{T(en_l, es_l)}</span>
            </div>"""
        for i, (en_l, es_l) in enumerate(items)
    )
    result_delay = len(items) * 0.22 + 0.15
    inner = f"""<div class="tchk-wrap" id="{id_prefix}">
        {rows}
        <div class="tchk-result" style="transition-delay:{result_delay:.2f}s;">
          <span class="ring-num count-num" data-target="{percent}" data-suffix="%">0%</span>
          <span class="ring-caption" style="text-align:left; margin-top:0;">{T(cap_en, cap_es)}</span>
        </div>
      </div>
      {_self_trigger_script(id_prefix)}"""
    return _card_shell(inner, tag_text, f"{id_prefix}-card")

def marketing_funnel(id_prefix, tag_text, stages):
    widths = [100, 76, 52, 30]
    # Visitors haven't entered the pipeline yet (neutral); Leads/MQLs/Customers
    # follow monday.com's real Stuck -> Working on it -> Done status progression
    # as they move down the funnel toward becoming a customer.
    colors = ["var(--muted)", "var(--status-stuck)", "var(--status-working)", "var(--status-done)"]
    rows = ""
    for (en_l, es_l, count), w, c in zip(stages, widths, colors):
        rows += f'<div class="funnel-seg" style="width:{w}%; background:{c};"><span>{T(en_l, es_l)}</span><span class="count-num" data-target="{count}">0</span></div>\n'
    dots = "".join(f'<div class="funnel-dot" style="animation-delay:{i*0.7:.1f}s; left:{48+i*2}%;"></div>' for i in range(5))
    inner = f"""<div class="funnel-wrap" id="{id_prefix}" style="position:relative;">
        {dots}
        {rows}
      </div>
      {_self_trigger_script(id_prefix)}"""
    return _card_shell(inner, tag_text, f"{id_prefix}-card")

def sales_chart(id_prefix, tag_text, target_value, label_en, label_es):
    bars_h = [38, 55, 46, 72, 64, 95]
    # Deal stages mature left-to-right: earlier bars = Stuck (red), mid = Working
    # on it (yellow), most recent/tallest = Done (green) -- ties the growth
    # metaphor to monday.com's real status progression, not a generic gradient.
    bar_colors = [
        "var(--status-stuck)", "var(--status-stuck)",
        "var(--status-working)", "var(--status-working)",
        "var(--status-done)", "var(--status-done)",
    ]
    bars = "".join(
        f'<div class="roi-bar" style="height:{h}%; background:{bar_colors[i % len(bar_colors)]}; transition-delay:{i*0.08:.2f}s;"></div>'
        for i, h in enumerate(bars_h)
    )
    inner = f"""<div class="chart-wrap roi-target" id="{id_prefix}" style="padding:4px 6px;">
        <div class="chart-num-row">
          <span class="chart-num count-num" data-target="{target_value}" data-prefix="$">$0</span>
          <span style="color:var(--status-done); font-size:13px;">&#9650; +18%</span>
        </div>
        <div class="chart-bars-row">{bars}</div>
        <div class="ring-caption" style="margin-top:10px;">{T(label_en, label_es)}</div>
      </div>
      {_self_trigger_script(id_prefix)}"""
    return _card_shell(inner, tag_text, f"{id_prefix}-card")

def website_builder(id_prefix, tag_text):
    # An empty browser frame assembling itself block by block -- a literal,
    # legible metaphor for "we build your site" rather than a repurposed
    # illustration. The three chrome dots double as monday.com status colors.
    inner = f"""<div class="wsite-wrap" id="{id_prefix}">
        <div class="wsite-bar"><span></span><span></span><span></span></div>
        <div class="wsite-block wsite-hero"></div>
        <div class="wsite-row">
          <div class="wsite-block wsite-col"></div>
          <div class="wsite-block wsite-col"></div>
        </div>
        <div class="wsite-block wsite-footer"></div>
      </div>
      {_self_trigger_script(id_prefix)}"""
    return _card_shell(inner, tag_text, f"{id_prefix}-card")

def chaos_to_order(id_prefix, tag_text, caption_chaos_en="CHAOS", caption_chaos_es="CAOS",
                    caption_organized_en="ORGANIZED", caption_organized_es="ORGANIZADO"):
    # 5 cards start scattered + jittering, then periodically snap into an ordered,
    # checked-off stack -- runs on its own loop (not scroll/reveal-triggered),
    # since it's meant to read as ambient "before/after" motion in the hero.
    p = id_prefix
    cap_chaos = caption_chaos_es if is_es() else caption_chaos_en
    cap_organized = caption_organized_es if is_es() else caption_organized_en
    colors = ["var(--status-stuck)", "var(--status-working)", "var(--status-done)",
              "var(--purple-bright)", "var(--status-working)"]
    # left%, top-px, rotate-deg, jitter-delay-s -- rough scattered layout within the stage.
    # Top values start below the caption row (~26px) so settled rows never underlap it.
    chaos_pos = [(6, 26, -12, 0.0), (52, 34, 10, 0.3), (16, 112, -8, 0.6), (58, 120, 12, 0.9), (30, 170, -6, 1.2)]
    org_top = [26, 68, 110, 152, 194]
    cards = ""
    for i, (c, (l, t, r, jd)) in enumerate(zip(colors, chaos_pos)):
        cards += (f'<div class="chaos-card" style="--cc:{c}; --l:{l}%; --t:{t}px; --r:{r}deg; '
                   f'--ot:{org_top[i]}px; animation-delay:{jd}s;"><span class="chaos-check">&#10003;</span></div>')
    return f"""<div class="diagram-card hero-in" style="animation-delay:.2s;">
      <div class="diagram-head">
        <span>{tag_text}</span>
        <span style="color:var(--status-done)">&#9679; live</span>
      </div>
      <div class="chaos-stage" id="{p}">
        <div class="chaos-caption" id="{p}-cap">{cap_chaos}</div>
        {cards}
      </div>
      <script>
        (function(){{
          var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
          var stage = document.getElementById('{p}');
          var cap = document.getElementById('{p}-cap');
          var cards = Array.from(stage.querySelectorAll('.chaos-card'));
          if (reduceMotion) return;
          function organize(){{
            stage.classList.add('organized');
            cap.textContent = '{cap_organized}';
            cards.forEach(function(c, i){{ setTimeout(function(){{ c.classList.add('landed'); }}, i * 180); }});
          }}
          function scatter(){{
            stage.classList.remove('organized');
            cap.textContent = '{cap_chaos}';
            cards.forEach(function(c){{ c.classList.remove('landed'); }});
          }}
          (function loopCycle(){{
            setTimeout(function(){{
              organize();
              setTimeout(function(){{ scatter(); setTimeout(loopCycle, 2600); }}, 3600);
            }}, 2400);
          }})();
        }})();
      </script>
    </div>"""

def results_counter(id_prefix, tag_text, target_value, label_en, label_es, suffix=""):
    # A count-up headline number with a self-drawing line graph beneath it --
    # a "results dashboard" moment rather than a repeated flow diagram.
    p = id_prefix
    inner = f"""<div class="results-wrap" id="{p}">
        <div class="chart-num-row" style="margin-bottom:2px;">
          <span class="chart-num count-num" data-target="{target_value}" data-suffix="{suffix}">0</span>
        </div>
        <div class="ring-caption" style="text-align:left; margin-top:0;">{T(label_en, label_es)}</div>
        <svg viewBox="0 0 300 70" width="100%" height="70" style="margin-top:10px; display:block;">
          <polyline points="0,55 40,50 80,52 120,38 160,40 200,22 240,18 300,6" fill="none" stroke="var(--line)" stroke-width="1"/>
          <polyline class="results-line" points="0,55 40,50 80,52 120,38 160,40 200,22 240,18 300,6" fill="none" stroke="var(--purple-bright)" stroke-width="2" stroke-linecap="round"/>
          <circle cx="300" cy="6" r="4" fill="var(--status-done)"/>
        </svg>
      </div>
      {_self_trigger_script(id_prefix)}"""
    return _card_shell(inner, tag_text, f"{id_prefix}-card")

def scaling_grid(id_prefix, tag_text, label_suffix_en="processes", label_suffix_es="procesos"):
    # A 4x4 grid of cells lighting up in non-sequential order (not a left-to-right
    # scan) while a live count climbs 4/8/12/16 -- a literal illustration of
    # "scale without scaling the chaos": growth that stays perfectly ordered.
    p = id_prefix
    suffix = label_suffix_es if is_es() else label_suffix_en
    cells = "".join(f'<div class="grid-cell" id="{p}-c{i}"><span class="dot"></span></div>' for i in range(16))
    inner = f"""<div class="scaling-wrap" id="{p}">
        <div class="scaling-label" id="{p}-lbl">4 {suffix}</div>
        <div class="scaling-grid">{cells}</div>
      </div>
      <script>
        (function(){{
          var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
          var order = [5,6,9,10,1,2,13,14,0,3,12,15,4,7,8,11];
          var lbl = document.getElementById('{p}-lbl');
          var cells = order.map(function(i){{ return document.getElementById('{p}-c' + i); }});
          if (reduceMotion) {{
            cells.forEach(function(c){{ c.classList.add('on'); }});
            lbl.textContent = '16 {suffix}';
            return;
          }}
          function run(){{
            cells.forEach(function(c){{ c.classList.remove('on'); }});
            lbl.textContent = '4 {suffix}';
            cells.forEach(function(c, i){{
              setTimeout(function(){{
                c.classList.add('on');
                var n = i + 1;
                if (n === 4 || n === 8 || n === 12 || n === 16) lbl.textContent = n + ' {suffix}';
              }}, i * 220);
            }});
            setTimeout(run, cells.length * 220 + 2600);
          }}
          run();
        }})();
      </script>"""
    return _card_shell(inner, tag_text, f"{id_prefix}-card")

print("diagram builders ready")

# ---------------------------------------------------------------
# PAGE ASSEMBLY + OUTPUT (preview / slim / page-head / sitemap)
# ---------------------------------------------------------------
SITEMAP_ENTRIES = []
CAPTURED = {}  # captured EN/ES header+footer HTML, for the sitewide footer-injection templates

def emit_page(slug, lang, title_en, title_es, desc_en, desc_es, body_html, json_ld_objects=None):
    """Builds + writes the full preview page, the Squarespace slim body fragment,
    and the Squarespace page-head fragment, for one language of one page."""
    BUILD_MODE["lang"] = lang
    html_lang, seo_html = seo_head(slug, title_en, title_es, desc_en, desc_es, json_ld_objects)
    hdr = header()
    ftr = footer()

    name = slug if slug else "home"
    lang_tag = "es" if lang == "toggle-es" else "en"
    CAPTURED[f"header-{lang_tag}"] = hdr
    CAPTURED[f"footer-{lang_tag}"] = ftr

    full_html = f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{FONT_LINKS}
{LIGHT_STYLE}
{EARLY_SCRIPT}
{seo_html}
</head>
<body>
{hdr}
{body_html}
{ftr}
{LANG_SCRIPT}
</body>
</html>
"""
    with open(os.path.join(PREVIEW_DIR, f"tc-{name}-{lang_tag}.html"), "w") as f:
        f.write(full_html)
    with open(os.path.join(SLIM_DIR, f"{name}-{lang_tag}.txt"), "w") as f:
        f.write(body_html)
    with open(os.path.join(PAGEHEAD_DIR, f"{name}-{lang_tag}.txt"), "w") as f:
        f.write(f"<!-- Also set these natively in Squarespace's own Page Settings -> SEO fields:\n"
                 f"Title: {title_es if lang_tag=='es' else title_en}\n"
                 f"Description: {desc_es if lang_tag=='es' else desc_en}\n"
                 f"(Squarespace already renders its own <title>/<meta description> from those fields --\n"
                 f"do NOT also paste the <title>/<meta description> lines below, only everything else.) -->\n\n"
                 + seo_html)

    en_url, es_url = page_urls(slug)
    SITEMAP_ENTRIES.append({"url": es_url if lang_tag == "es" else en_url, "alt_en": en_url, "alt_es": es_url})
    return full_html

def build_both_langs(slug, title_en, title_es, desc_en, desc_es, build_body_fn, json_ld_fn=None):
    for lang in ("toggle-en", "toggle-es"):
        BUILD_MODE["lang"] = lang
        jsonld = json_ld_fn() if json_ld_fn else None
        body = build_body_fn()
        emit_page(slug, lang, title_en, title_es, desc_en, desc_es, body, jsonld)
    BUILD_MODE["lang"] = "toggle-en"

print("page assembly helpers ready")

# ---------------------------------------------------------------
# HOME PAGE CONTENT
# ---------------------------------------------------------------
def home_hero():
    return f"""<section class="hero">
  <div class="ambient-blob" style="width:340px; height:340px; top:-80px; right:8%; background:rgba(97,97,255,0.16); animation-delay:0s;"></div>
  <div class="ambient-blob" style="width:220px; height:220px; bottom:-60px; left:4%; background:rgba(0,202,114,0.12); animation-delay:-6s;"></div>
  <div class="tc-wrap">
    <div>
      {monday_badge('Certified Partner','Socio Certificado', cls="eyebrow-logo hero-in")}
      <h1 class="hero-in" style="animation-delay:.15s">{T('Unlock Peak','Libera el M&aacute;ximo')} <span class="purple">{T('Performance','Rendimiento')}</span></h1>
      <p class="lead hero-in" style="animation-delay:.25s">{T('We turn operational friction into a custom-built engine for growth &mdash; on monday.com.','Convertimos la fricci&oacute;n operativa en un motor de crecimiento a la medida &mdash; en monday.com.')}</p>
      <div class="hero-in" style="display:flex; align-items:center; animation-delay:.35s">
        <a class="btn-primary" href="https://wkf.ms/49age3d">
          {T('Schedule a Strategy Session','Agenda una Sesi&oacute;n Estrat&eacute;gica')}
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a class="btn-ghost" href="#process">{T('See the process &darr;','Ver el proceso &darr;')}</a>
      </div>
    </div>
    {chaos_to_order("h", "WORKFLOW_ENGINE // trustcodemx")}
  </div>
</section>
"""

PROBLEMS = [
    ("link", "Disconnected Teams", "Equipos Desconectados", "Missed deadlines from siloed work.", "Plazos perdidos por trabajo aislado."),
    ("eye", "Low Visibility", "Poca Visibilidad", "No real-time view of progress.", "Sin vista en tiempo real del avance."),
    ("repeat", "Manual Busywork", "Trabajo Manual", "Hours lost to repetitive tasks.", "Horas perdidas en tareas repetitivas."),
    ("layers", "Generic Tools", "Herramientas Gen&eacute;ricas", "Software that doesn't fit your process.", "Software que no se adapta a tu proceso."),
]

def home_problems():
    cards = ""
    for i, (ic, en_t, es_t, en_d, es_d) in enumerate(PROBLEMS):
        cards += f"""<div class="problem-card icon-pop reveal" style="transition-delay:{i*0.08:.2f}s">
          <div class="ic">{ICONS[ic]}</div>
          <h4>{T(en_t, es_t)}</h4><p>{T(en_d, es_d)}</p>
        </div>"""
    return f"""<section id="process">
  <div class="tc-wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{T('the problem','el problema')}</span>
      <h2>{T('Is your workflow holding you back?','&iquest;Tu flujo de trabajo te frena?')}</h2>
    </div>
    <div class="grid-4">{cards}</div>
  </div>
</section>
"""

PROCESS = [
    ("Workflow Analysis", "An&aacute;lisis de Flujo", "Map bottlenecks into a clear blueprint.", "Mapeamos cuellos de botella en un plan claro."),
    ("Custom Automation", "Automatizaci&oacute;n a Medida", "Boards and automations built for you.", "Tableros y automatizaciones hechos para ti."),
    ("Integrations", "Integraciones", "monday.com connected to your tools.", "monday.com conectado a tus herramientas."),
    ("Reporting &amp; KPIs", "Reportes y KPIs", "Real-time dashboards that matter.", "Dashboards en tiempo real que importan."),
    ("Training", "Capacitaci&oacute;n", "Fast adoption, real productivity.", "Adopci&oacute;n r&aacute;pida, productividad real."),
]

def home_process():
    steps = ""
    arrival = [0.18, 0.74, 1.30, 1.86, 2.42]
    for i, (en_t, es_t, en_d, es_d) in enumerate(PROCESS, 1):
        steps += f"""<div class="step reveal" style="transition-delay:{arrival[i-1]:.2f}s"><div class="step-num"><span class="step-num-ring"></span><span class="step-num-txt">{i:02d}</span></div>
          <div><h4>{T(en_t, es_t)}</h4><p>{T(en_d, es_d)}</p></div></div>"""
    return f"""<section>
  <div class="tc-wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{T('our process','nuestro proceso')}</span>
      <h2>{T('Your custom engine for efficiency','Tu motor de eficiencia a la medida')}</h2>
    </div>
    <div class="timeline reveal">{steps}</div>
  </div>
</section>
"""

# Client-verified stat row. Only the first figure is TrustCode's own; the other
# three cite published third-party research -- flagged with * and the footnote
# below, never presented as TrustCode's own client results.
STATS = [
    (4, "+", "Years implementing monday.com", "A&ntilde;os implementando monday.com"),
    (288, "%", "Average ROI reported by monday.com clients*", "ROI promedio reportado por clientes de monday.com*"),
    (85, "K+", "Hours saved per year (real client case)*", "Horas ahorradas al a&ntilde;o (caso real de cliente)*"),
    (50, "%", "Less time in meetings with centralized workflows*", "Menos tiempo en juntas con flujos centralizados*"),
]

def home_stats():
    cells = ""
    for target, suffix, en_l, es_l in STATS:
        cells += f"""<div class="stat-cell">
          <div class="stat-num count-num" data-target="{target}" data-suffix="{suffix}">0</div>
          <div class="stat-label">{T(en_l, es_l)}</div>
        </div>"""
    return f"""<section style="padding-top:60px; padding-bottom:52px;">
  <div class="tc-wrap">
    <div class="stat-row reveal">{cells}</div>
    <p class="stat-source-note">{T('*Data from independent Forrester studies and customer cases published by monday.com. Individual results vary.','*Datos de estudios independientes de Forrester y casos de clientes publicados por monday.com. Resultados individuales var&iacute;an.')}</p>
  </div>
</section>
"""

# Client-verified integration list -- do not add tools beyond this list without
# asking first.
TOOLS = [
    ("Slack", "#4A154B"),
    ("Microsoft Teams", "#6264A7"),
    ("Gmail / Outlook", "#EA4335"),
    ("Google Drive / Calendar", "#0F9D58"),
    ("QuickBooks", "#2CA01C"),
    ("WhatsApp", "#25D366"),
    ("Zoom", "#2D8CFF"),
    ("Zapier", "#FF4A00"),
    ("Make", "#6D00CC"),
]

def home_tools():
    chips = "".join(
        f'<span class="tool-chip"><span class="dot" style="background:{color}"></span>{name}</span>'
        for name, color in (TOOLS * 2)
    )
    return f"""<section style="padding-top:56px; padding-bottom:56px;">
  <div class="tc-wrap">
    <div class="section-head reveal" style="margin-bottom:26px;">
      <span class="eyebrow">{T('integrations','integraciones')}</span>
      <h2>{T('Connected to the tools your team already uses','Conectado a las herramientas que tu equipo ya usa')}</h2>
    </div>
  </div>
  <div class="tool-marquee"><div class="tool-track">{chips}</div></div>
</section>
"""

ADVANTAGE = [
    ("shield", "Certified Experts", "Expertos Certificados", "Deep, certified monday.com knowledge.", "Conocimiento certificado y profundo de monday.com."),
    ("briefcase", "Business-First", "Enfoque en Negocio", "Consultants first, tech second.", "Consultores primero, tecnolog&iacute;a despu&eacute;s."),
    ("bars", "Measurable ROI", "ROI Medible", "Clear metrics from day one.", "M&eacute;tricas claras desde el d&iacute;a uno."),
    ("venn", "Long-Term Partnership", "Socios a Largo Plazo", "Support that grows with you.", "Soporte que crece contigo."),
]

def home_advantage():
    cards = ""
    for i, (ic, en_t, es_t, en_d, es_d) in enumerate(ADVANTAGE):
        ic_html = ANIMATED_BARS if ic == "bars" else ICONS[ic]
        cards += f"""<div class="adv-card icon-pop reveal" style="transition-delay:{i*0.08:.2f}s">
          <div class="ic">{ic_html}</div>
          <div><h4>{T(en_t, es_t)}</h4><p>{T(en_d, es_d)}</p></div>
        </div>"""
    return f"""<section id="advantage">
  <div class="tc-wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{T('why trust code','por qu&eacute; trust code')}</span>
      <h2>{T('Your partner in digital transformation','Tu socio en transformaci&oacute;n digital')}</h2>
    </div>
    <div class="grid-2">{cards}</div>
  </div>
</section>
"""

SERVICES = [
    ("grid", "purple-bright", "/work-management/", "Work Management", "Gesti&oacute;n del Trabajo", "One command center for your business.", "Un centro de mando para tu negocio."),
    ("cap", "emerald", "/team-training/", "Training", "Capacitaci&oacute;n", "Turn your team into power users.", "Convierte a tu equipo en expertos."),
    ("megaphone", "purple-bright", "/marketing-crm-solutions/", "Marketing", "Marketing", "Predictable leads, measurable ROI.", "Leads predecibles, ROI medible."),
    ("sliders", "emerald", "/monday-operations/", "Operations", "Operaciones", "Scale without scaling the chaos.", "Escala sin escalar el caos."),
    ("trending", "purple-bright", "/monday-sales-crm/", "Sales &amp; CRM", "Ventas y CRM", "Shorter cycles, more closed deals.", "Ciclos m&aacute;s cortos, m&aacute;s cierres."),
    ("browser", "emerald", "/web-design-development/", "Web Design &amp; Development", "Dise&ntilde;o y Desarrollo Web", "A site as sharp as your operation.", "Un sitio a la altura de tu operaci&oacute;n."),
    ("share", "purple-bright", "/social-media-management/", "Social Media", "Redes Sociales", "A content engine, not just posts.", "Un motor de contenido, no solo posts."),
]

def home_services():
    p = prefix()
    cards = ""
    for i, (ic, accent, href, en_t, es_t, en_d, es_d) in enumerate(SERVICES):
        cards += f"""<a class="service-card icon-pop reveal" href="{p}{href}" style="--sc-accent:var(--{accent}); transition-delay:{i*0.07:.2f}s">
          <div class="ic">{ICONS[ic]}</div>
          <h4>{T(en_t, es_t)}</h4><p>{T(en_d, es_d)}</p>
        </a>"""
    return f"""<section id="services">
  <div class="tc-wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{T('our services','nuestros servicios')}</span>
      <h2>{T('Seven ways we help your business run and grow','Siete formas en que ayudamos a tu negocio a operar y crecer')}</h2>
    </div>
    <div class="grid-5">{cards}</div>
  </div>
</section>
"""

QUOTES = [
    ("Innovation distinguishes a leader from a follower.", "La innovaci&oacute;n distingue a un l&iacute;der de un seguidor.", "Steve Jobs"),
    ("The best way to predict the future is to create it.", "La mejor manera de predecir el futuro es crearlo.", "Peter Drucker"),
    ("Every company is a software company.", "Toda empresa es, hoy, una empresa de software.", "Satya Nadella"),
    ("Digital transformation begins with the customer.", "La transformaci&oacute;n digital comienza con el cliente.", "Marc Benioff"),
]

def home_quotes():
    chips = ""
    for q_en, q_es, author in QUOTES * 2:
        chips += f'<div class="quote-chip"><b>&ldquo;</b>{T(q_en, q_es)}<span>{author}</span></div>'
    return f'<div id="quotes" class="marquee-wrap"><div class="marquee-track">{chips}</div></div>'

def home_final():
    return f"""<section id="partner">
  <div class="tc-wrap final-cta reveal">
    <span class="eyebrow" style="justify-content:center">{T('ready when you are','listos cuando t&uacute; lo est&eacute;s')}</span>
    <h2>{T('Ready to revolutionize your operations?','&iquest;Listo para revolucionar tus operaciones?')}</h2>
    <p>{T('Schedule your free consultation today.','Agenda tu consulta gratuita hoy.')}</p>
    <a class="btn-primary" href="https://wkf.ms/49age3d">{T('Claim My Free Consultation','Reclama mi Consulta Gratuita')}</a>
    <div>{monday_badge('Certified Partner','Socio Certificado', cls="badge")}</div>
  </div>
</section>
"""

def home_body():
    return (home_hero() + home_stats() + home_problems() + home_process() + home_advantage()
            + home_services() + home_tools() + home_quotes() + home_final())

def home_jsonld():
    _is_es = is_es()
    return [
        {
            "@context": "https://schema.org",
            "@type": "ProfessionalService",
            "name": "Trust Code",
            "url": page_urls("")[1 if _is_es else 0],
            "description": ("Socio certificado de monday.com. Diseñamos flujos de trabajo, "
                             "automatizaciones y sistemas CRM a la medida.") if _is_es else
                            ("Certified monday.com consulting partner building custom workflows, "
                             "automations, and CRM systems."),
            "inLanguage": "es-MX" if _is_es else "en",
            "sameAs": [],
        }
    ]

HOME_TITLE_EN = "Trust Code | monday.com Consulting & Custom Workflow Automation"
HOME_DESC_EN = ("Certified monday.com partner. We design custom workflows, automations, "
                "dashboards, and CRM systems that turn operational chaos into measurable growth. "
                "Book a free strategy session.")
HOME_TITLE_ES = "Trust Code | Consultoría y Automatización monday.com"
HOME_DESC_ES = ("Socio certificado de monday.com. Diseñamos flujos de trabajo, "
                "automatizaciones, dashboards y sistemas CRM a la medida que convierten el caos "
                "operativo en crecimiento medible. Agenda tu sesión estratégica gratuita.")

build_both_langs("", HOME_TITLE_EN, HOME_TITLE_ES, HOME_DESC_EN, HOME_DESC_ES, home_body, home_jsonld)
print("home (en + es) written")

# ---------------------------------------------------------------
# SUBPAGE TEMPLATE
# ---------------------------------------------------------------
def sub_item(cls, icon_key, en_t, es_t, en_d, es_d, delay=0.0):
    return f"""<div class="it {cls} icon-pop reveal" style="transition-delay:{delay:.2f}s"><div class="ic">{ICONS[icon_key]}</div>
      <div><b>{T(en_t, es_t)}</b><p>{T(en_d, es_d)}</p></div></div>"""

def get_item(icon_key, en_t, es_t, en_d, es_d, delay=0.0):
    return f"""<div class="getcard icon-pop reveal" style="transition-delay:{delay:.2f}s"><div class="ic">{ICONS[icon_key]}</div>
      <div><b>{T(en_t, es_t)}</b><p>{T(en_d, es_d)}</p></div></div>"""

def founder_section():
    bio_en = ("Gabriel Villegas is the founder and CEO of Trust Code. A marketing professional "
              "with 5+ years of hands-on experience in monday.com, he's built custom workflows, "
              "configured CRM systems, and managed digital platforms &mdash; including full-scale "
              "events &mdash; that streamline operations and drive real business growth. Gabriel "
              "trains teams, coordinates cross-functional projects, and is always looking for the "
              "next challenge to solve with a smarter system.")
    bio_es = ("Gabriel Villegas es el fundador y CEO de Trust Code. Profesional de marketing con "
              "m&aacute;s de 5 a&ntilde;os de experiencia pr&aacute;ctica en monday.com, ha construido "
              "flujos de trabajo a la medida, configurado sistemas CRM y gestionado plataformas "
              "digitales &mdash; incluyendo eventos a gran escala &mdash; que agilizan operaciones y "
              "generan crecimiento real. Gabriel capacita equipos, coordina proyectos "
              "multidisciplinarios y siempre busca el siguiente reto que resolver con un sistema "
              "m&aacute;s inteligente.")
    return f"""<section>
  <div class="tc-wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{T('the person behind it','la persona detr&aacute;s')}</span>
      <h2>{T('Meet the Founder','Conoce al Fundador')}</h2>
    </div>
    <div class="founder-card reveal">
      <img class="founder-photo" src="{GABRIEL_PHOTO_URL}" alt="Gabriel Villegas">
      <div class="founder-text">
        <h3>Gabriel Villegas</h3>
        <span class="eyebrow">{T('Founder &amp; CEO','Fundador y CEO')}</span>
        <p>{T(bio_en, bio_es)}</p>
      </div>
    </div>
  </div>
</section>"""

def subpage_body(crumb_en, crumb_es, h1_en, h1_es, lead_en, lead_es,
                  cta_en, cta_es, challenge, solution, getgrid_title_en, getgrid_title_es,
                  getcards, final_h2_en, final_h2_es, final_lead_en, final_lead_es,
                  final_cta_en, final_cta_es, diagram_html,
                  col1_header_en="The Challenge", col1_header_es="El Reto",
                  col2_header_en="Our Solution", col2_header_es="Nuestra Soluci&oacute;n",
                  crumb_root_en="Solutions", crumb_root_es="Soluciones",
                  extra_section_html=None):
    p = prefix()
    challenge_html = "\n".join(sub_item("challenge", ic, en_t, es_t, en_d, es_d, delay=i*0.08) for i, (ic, en_t, es_t, en_d, es_d) in enumerate(challenge))
    solution_html = "\n".join(sub_item("solution", ic, en_t, es_t, en_d, es_d, delay=i*0.08) for i, (ic, en_t, es_t, en_d, es_d) in enumerate(solution))
    get_html = "\n".join(get_item(ic, en_t, es_t, en_d, es_d, delay=i*0.07) for i, (ic, en_t, es_t, en_d, es_d) in enumerate(getcards))

    return f"""<section class="subhero" style="position:relative;">
  <div class="ambient-blob" style="width:260px; height:260px; top:-70px; right:6%; background:rgba(97,97,255,0.14); animation-delay:-3s;"></div>
  <div class="tc-wrap hero-split" style="position:relative;">
    <div>
      <span class="crumb hero-in" style="animation-delay:.05s"><a href="{p}/">{T(crumb_root_en, crumb_root_es)}</a> / <span class="accent">{T(crumb_en, crumb_es)}</span></span>
      <h1 class="hero-in" style="animation-delay:.15s">{T(h1_en, h1_es)}</h1>
      <p class="lead hero-in" style="animation-delay:.25s">{T(lead_en, lead_es)}</p>
      <a class="btn-primary hero-in" style="animation-delay:.35s" href="https://wkf.ms/49age3d">{T(cta_en, cta_es)}
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M13 6l6 6-6 6" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
    </div>
    {diagram_html()}
  </div>
</section>

<section>
  <div class="tc-wrap row-2">
    <div class="col-block reveal">
      <h3>{T(col1_header_en, col1_header_es)}</h3>
      <div class="item-list">{challenge_html}</div>
    </div>
    <div class="col-block reveal">
      <h3>{T(col2_header_en, col2_header_es)}</h3>
      <div class="item-list">{solution_html}</div>
    </div>
  </div>
</section>
{extra_section_html() if extra_section_html else ''}
<section style="background:var(--surface);">
  <div class="tc-wrap">
    <div class="section-head reveal">
      <span class="eyebrow">{T('what you get','lo que obtienes')}</span>
      <h2>{T(getgrid_title_en, getgrid_title_es)}</h2>
    </div>
    <div class="getgrid reveal">{get_html}</div>
  </div>
</section>

<section>
  <div class="tc-wrap final-cta reveal">
    <span class="eyebrow" style="justify-content:center">{T('ready when you are','listos cuando t&uacute; lo est&eacute;s')}</span>
    <h2>{T(final_h2_en, final_h2_es)}</h2>
    <p>{T(final_lead_en, final_lead_es)}</p>
    <a class="btn-primary" href="https://wkf.ms/49age3d">{T(final_cta_en, final_cta_es)}</a>
  </div>
</section>
"""

def build_subpage(slug, title_en, title_es, desc_en, desc_es, crumb_en, crumb_es, **kw):
    def body_fn():
        return subpage_body(crumb_en, crumb_es, **kw)
    def jsonld_fn():
        return [
            breadcrumb_jsonld(slug, crumb_en, crumb_es),
            service_jsonld(kw["h1_en"], kw["h1_es"], desc_en, desc_es),
        ]
    build_both_langs(slug, title_en, title_es, desc_en, desc_es, body_fn, jsonld_fn)

# ---------------- 1. Work Management ----------------
build_subpage(
    slug="work-management",
    title_en="monday.com Work Management Consulting | Trust Code",
    title_es="Gestión del Trabajo con monday.com | Consultoría Trust Code",
    desc_en="Custom monday.com work management systems built by a certified partner. Real-time dashboards, one source of truth, and full visibility across every team.",
    desc_es="Sistemas de gestión del trabajo a la medida en monday.com, diseñados por un socio certificado. Dashboards en tiempo real y visibilidad total para tu equipo.",
    crumb_en="Work Management", crumb_es="Gesti&oacute;n del Trabajo",
    h1_en="One Command Center for Your Whole Business", h1_es="Un Centro de Mando para Todo tu Negocio",
    lead_en="Siloed data leads to reactive decisions and burnout. We build your single source of truth on monday.com.",
    lead_es="Los datos aislados llevan a decisiones reactivas y desgaste. Construimos tu &uacute;nica fuente de verdad en monday.com.",
    cta_en="Request a Demo", cta_es="Solicita una Demo",
    challenge=[
        ("alert","Reactive Decisions","Decisiones Reactivas","Acting on outdated info, not real-time data.","Actuar con informaci&oacute;n desactualizada."),
        ("alert","Admin Overload","Sobrecarga Administrativa","Hours lost chasing updates and reports.","Horas perdidas persiguiendo reportes."),
        ("alert","Unclear Ownership","Propiedad Poco Clara","Missed deadlines from unclear task owners.","Plazos perdidos por due&ntilde;os poco claros."),
        ("alert","Poor Allocation","Mala Asignaci&oacute;n","No visibility into who's working on what.","Sin visibilidad de qui&eacute;n hace qu&eacute;."),
    ],
    solution=[
        ("check","Map Core Processes","Mapeo de Procesos","Analyze how projects and budgets are run.","Analizamos c&oacute;mo corren tus proyectos."),
        ("check","Custom Dashboards","Dashboards a Medida","Executive KPIs, visible in real time.","KPIs ejecutivos, visibles en tiempo real."),
        ("check","Automated Reporting","Reportes Autom&aacute;ticos","No more manual report generation.","Sin generaci&oacute;n manual de reportes."),
        ("check","Tool Integration","Integraci&oacute;n de Herramientas","One seamless flow of information.","Un flujo de informaci&oacute;n sin fricci&oacute;n."),
    ],
    getgrid_title_en="A unified management ecosystem", getgrid_title_es="Un ecosistema de gesti&oacute;n unificado",
    getcards=[
        ("eye","360&deg; Visibility","Visibilidad 360&deg;","Real-time view of every project.","Vista en tiempo real de cada proyecto."),
        ("bars","Data-Driven Leadership","Liderazgo con Datos","Strategic decisions, backed by data.","Decisiones estrat&eacute;gicas basadas en datos."),
        ("grid","Team Efficiency","Eficiencia de Equipo","One system everyone understands.","Un sistema que todos entienden."),
        ("venn","Strategic Freedom","Libertad Estrat&eacute;gica","More time to grow, less to manage.","M&aacute;s tiempo para crecer, menos para gestionar."),
    ],
    final_h2_en="Ready for one command center?", final_h2_es="&iquest;Listo para un centro de mando?",
    final_lead_en="Let's build the dashboards your leadership actually needs.", final_lead_es="Construyamos los dashboards que tu liderazgo necesita.",
    final_cta_en="Request a Demo", final_cta_es="Solicita una Demo",
    diagram_html=lambda: results_counter("wm", "WORK_MANAGEMENT // trustcodemx", 247, "Hours Saved This Month", "Horas Ahorradas Este Mes"),
)

# ---------------- 2. Training ----------------
build_subpage(
    slug="team-training",
    title_en="monday.com Training & Team Adoption Programs | Trust Code",
    title_es="Capacitación en monday.com para Equipos | Trust Code",
    desc_en="Hands-on monday.com training and workshops that drive real adoption. Role-based curriculum, train-the-trainer programs, and ongoing support from a certified partner.",
    desc_es="Talleres y capacitación práctica en monday.com que garantizan adopción real. Programas por rol, formación de formadores y soporte continuo, con un socio certificado.",
    crumb_en="Training", crumb_es="Capacitaci&oacute;n",
    h1_en="Maximize Your Technology ROI", h1_es="Maximiza el ROI de tu Tecnolog&iacute;a",
    lead_en="Powerful software is useless without adoption. We train your team to actually use it.",
    lead_es="El software potente no sirve sin adopci&oacute;n. Capacitamos a tu equipo para usarlo de verdad.",
    cta_en="Contact Us", cta_es="Cont&aacute;ctanos",
    challenge=[
        ("alert","Low Engagement","Poco Compromiso","Employees reverting to email and spreadsheets.","Empleados regresan a correo y hojas de c&aacute;lculo."),
        ("alert","Inconsistent Usage","Uso Inconsistente","Different teams, different silos.","Distintos equipos, distintos silos."),
        ("alert","Wasted Features","Funciones Desperdiciadas","Only 10% of the platform gets used.","Solo se usa el 10% de la plataforma."),
        ("alert","Team Resistance","Resistencia del Equipo","New tech feels like a burden.","La nueva tecnolog&iacute;a se siente como carga."),
    ],
    solution=[
        ("check","Role-Based Curriculum","Curr&iacute;culo por Rol","Training specific to each role.","Capacitaci&oacute;n espec&iacute;fica para cada rol."),
        ("check","Hands-On Workshops","Talleres Pr&aacute;cticos","Using your real projects and data.","Con tus proyectos y datos reales."),
        ("check","Train-the-Trainer","Formaci&oacute;n de Formadores","Internal champions, built in-house.","Expertos internos, formados por nosotros."),
        ("check","Ongoing Support","Soporte Continuo","Cheat sheets, videos, live Q&amp;A.","Gu&iacute;as, videos y sesiones de preguntas."),
    ],
    getgrid_title_en="Custom-tailored empowerment programs", getgrid_title_es="Programas a la medida de tu equipo",
    getcards=[
        ("shield","A Proficient Team","Un Equipo Capaz","Confident, efficient platform users.","Usuarios seguros y eficientes."),
        ("trending","Immediate Gains","Ganancias Inmediatas","A real boost in output, fast.","Un aumento real en resultados, r&aacute;pido."),
        ("repeat","Culture of Efficiency","Cultura de Eficiencia","A team that seeks smarter workflows.","Un equipo que busca mejores flujos."),
        ("check","Guaranteed ROI","ROI Garantizado","Your investment finally pays off.","Tu inversi&oacute;n por fin rinde frutos."),
    ],
    final_h2_en="Ready to close the adoption gap?", final_h2_es="&iquest;Listo para cerrar la brecha de adopci&oacute;n?",
    final_lead_en="Let's build training around your workflows, not a generic deck.", final_lead_es="Construyamos capacitaci&oacute;n para tu flujo de trabajo real.",
    final_cta_en="Contact Us", final_cta_es="Cont&aacute;ctanos",
    diagram_html=lambda: training_checklist("tr", "TRAINING_ENGINE // trustcodemx", 94, [
        ("Role-Based Curriculum", "Curr&iacute;culo por Rol"),
        ("Hands-On Workshops", "Talleres Pr&aacute;cticos"),
        ("Train-the-Trainer", "Formaci&oacute;n de Formadores"),
        ("Ongoing Support", "Soporte Continuo"),
    ], "Team Proficiency", "Dominio del Equipo"),
)

# ---------------- 3. Marketing & CRM ----------------
build_subpage(
    slug="marketing-crm-solutions",
    title_en="monday.com Marketing & CRM Solutions | Trust Code",
    title_es="Marketing y CRM con monday.com | Trust Code",
    desc_en="Full-funnel monday.com marketing systems with measurable ROI. Campaign hubs, lead routing automation, and integrated reporting built by a certified partner.",
    desc_es="Sistemas de marketing en monday.com con visibilidad total del embudo y ROI medible. Automatización de leads, reportes integrados y más, con un socio certificado.",
    crumb_en="Marketing &amp; CRM", crumb_es="Marketing y CRM",
    h1_en="From Ad Spend to Predictable Revenue", h1_es="De Inversi&oacute;n Publicitaria a Ingresos Predecibles",
    lead_en="Stop guessing at marketing ROI. We build transparent, full-funnel systems on monday.com.",
    lead_es="Deja de adivinar tu ROI. Construimos sistemas transparentes de principio a fin en monday.com.",
    cta_en="Let's Improve My Business", cta_es="Mejora Mi Negocio",
    challenge=[
        ("alert","Disconnected Data","Datos Desconectados","Ads, analytics, and CRM don't talk.","Anuncios, anal&iacute;tica y CRM no se comunican."),
        ("alert","Manual Reporting","Reportes Manuales","More spreadsheets than strategy.","M&aacute;s hojas de c&aacute;lculo que estrategia."),
        ("alert","Unclear Attribution","Atribuci&oacute;n Confusa","Can't tell what's driving revenue.","No se sabe qu&eacute; genera ingresos."),
        ("alert","Leaky Handoffs","Fugas en la Entrega","Leads lost between marketing and sales.","Leads perdidos entre marketing y ventas."),
    ],
    solution=[
        ("check","Funnel Mapping","Mapeo de Embudo","A data-driven customer journey.","Un recorrido del cliente basado en datos."),
        ("check","Campaign Hub","Centro de Campa&ntilde;as","Calendars, budgets, approvals in one place.","Calendarios, presupuestos y aprobaciones juntos."),
        ("check","Full Integration","Integraci&oacute;n Total","Ads, Analytics, Mailchimp, connected.","Anuncios, Analytics y Mailchimp conectados."),
        ("check","Auto Lead Routing","Ruteo Autom&aacute;tico","Leads nurtured and routed instantly.","Leads nutridos y enviados al instante."),
    ],
    getgrid_title_en="An integrated marketing operations hub", getgrid_title_es="Un centro de operaciones de marketing integrado",
    getcards=[
        ("eye","Full Funnel Visibility","Visibilidad Total","See spend-to-close in one place.","Ve todo desde el gasto hasta el cierre."),
        ("bars","Measurable ROI","ROI Medible","Know exactly what drives revenue.","Sabe exactamente qu&eacute; genera ingresos."),
        ("trending","Scalable Growth","Crecimiento Escalable","A repeatable system for quality leads.","Un sistema repetible de leads de calidad."),
        ("venn","Sales Alignment","Alineaci&oacute;n con Ventas","Seamless handoff, every time.","Entrega perfecta, cada vez."),
    ],
    final_h2_en="Ready for predictable revenue?", final_h2_es="&iquest;Listo para ingresos predecibles?",
    final_lead_en="Let's build a growth engine that reports on itself.", final_lead_es="Construyamos un motor de crecimiento que se reporta solo.",
    final_cta_en="Book an Appointment", final_cta_es="Agenda una Cita",
    diagram_html=lambda: marketing_funnel("mk", "GROWTH_ENGINE // trustcodemx", [
        ("Visitors","Visitantes",2400),("Leads","Leads",640),("MQLs","MQLs",180),("Customers","Clientes",42),
    ]),
)

# ---------------- 4. Operations ----------------
build_subpage(
    slug="monday-operations",
    title_en="monday.com Operations & Process Automation | Trust Code",
    title_es="Operaciones y Automatización de Procesos con monday.com | Trust Code",
    desc_en="Scale your operations without scaling the chaos. Custom monday.com process automation, accountability tracking, and real-time health dashboards from a certified partner.",
    desc_es="Escala tu operación sin escalar el caos. Automatización de procesos, responsabilidad y visibilidad en tiempo real en monday.com, con un socio certificado.",
    crumb_en="Operations", crumb_es="Operaciones",
    h1_en="Scale Without Scaling the Chaos", h1_es="Escala Sin Escalar el Caos",
    lead_en="Scaling a broken process only magnifies the cracks. We rewire how your company works.",
    lead_es="Escalar un proceso roto solo agranda las grietas. Redise&ntilde;amos c&oacute;mo trabaja tu empresa.",
    cta_en="Map My Processes", cta_es="Mapea Mis Procesos",
    challenge=[
        ("alert","Slower at Scale","M&aacute;s Lento al Escalar","More hires, yet execution slows down.","M&aacute;s gente, pero la ejecuci&oacute;n se frena."),
        ("alert","Buried Workflows","Flujos Enterrados","Work lost in chat apps and sheets.","Trabajo perdido en chats y hojas de c&aacute;lculo."),
        ("alert","Constant Firefighting","Apagar Incendios","Leaders managing crises, not strategy.","L&iacute;deres gestionando crisis, no estrategia."),
        ("alert","Not a Tool Problem","No Es de Herramientas","You need an overhaul, not another app.","Necesitas un redise&ntilde;o, no otra app."),
    ],
    solution=[
        ("check","Frictionless Execution","Ejecuci&oacute;n Sin Fricci&oacute;n","Core processes migrated into monday.com.","Procesos clave migrados a monday.com."),
        ("check","Automated Accountability","Responsabilidad Autom&aacute;tica","Deadlines and approvals trigger themselves.","Plazos y aprobaciones se activan solos."),
        ("check","Executive Visibility","Visibilidad Ejecutiva","Real-time pulse on capacity and health.","Pulso en tiempo real de capacidad y salud."),
        ("check","Early Risk Detection","Detecci&oacute;n Temprana","Spot risks before they're roadblocks.","Detecta riesgos antes de que frenen todo."),
    ],
    getgrid_title_en="Your operations, rewired", getgrid_title_es="Tus operaciones, redise&ntilde;adas",
    getcards=[
        ("link","Frictionless Execution","Ejecuci&oacute;n Sin Fricci&oacute;n","No more guessing who owns what.","Se acab&oacute; adivinar qui&eacute;n hace qu&eacute;."),
        ("check","Automated Accountability","Responsabilidad Autom&aacute;tica","Status updates trigger by themselves.","Actualizaciones que se activan solas."),
        ("bars","Real-Time Health","Salud en Tiempo Real","Capacity visible at a glance.","Capacidad visible de un vistazo."),
        ("trending","A Growth Catalyst","Un Catalizador","Operations that scale with you.","Operaciones que crecen contigo."),
    ],
    final_h2_en="Ready to make ops your catalyst?", final_h2_es="&iquest;Listo para que operaciones sea tu motor?",
    final_lead_en="Let's map what's actually broken and rebuild it.", final_lead_es="Mapeemos lo que realmente est&aacute; roto y reconstruy&aacute;moslo.",
    final_cta_en="Map My Processes", final_cta_es="Mapea Mis Procesos",
    diagram_html=lambda: scaling_grid("op", "OPS_ENGINE // trustcodemx"),
)

# ---------------- 5. Sales & CRM ----------------
build_subpage(
    slug="monday-sales-crm",
    title_en="monday.com Sales CRM & Pipeline Management | Trust Code",
    title_es="CRM de Ventas y Pipeline con monday.com | Trust Code",
    desc_en="Custom monday.com CRM builds for faster sales cycles. Automated lead routing, live forecasting, and a pipeline engineered for velocity — by a certified partner.",
    desc_es="CRM a la medida en monday.com para vender más rápido. Ruteo automático de leads, pronósticos en vivo y un pipeline diseñado para la velocidad, con un socio certificado.",
    crumb_en="Sales &amp; CRM", crumb_es="Ventas y CRM",
    h1_en="Turn Your Pipeline Into a Revenue Engine", h1_es="Convierte tu Pipeline en un Motor de Ingresos",
    lead_en="Growth stalls when sales infrastructure can't keep up. We design a seamless sales journey.",
    lead_es="El crecimiento se detiene sin la infraestructura correcta. Dise&ntilde;amos un proceso de ventas sin fricci&oacute;n.",
    cta_en="Accelerate My Pipeline", cta_es="Acelera Mi Pipeline",
    challenge=[
        ("alert","Reps Buried in Admin","Vendedores en lo Administrativo","More spreadsheet time than selling time.","M&aacute;s tiempo en hojas de c&aacute;lculo que vendiendo."),
        ("alert","Leads Slipping Away","Leads que se Pierden","High-value leads lost to forgotten follow-ups.","Leads valiosos perdidos por falta de seguimiento."),
        ("alert","Gut-Feel Forecasting","Pron&oacute;sticos a Ojo","Forecasts based on outdated reports.","Pron&oacute;sticos basados en reportes viejos."),
        ("alert","Zero Visibility","Cero Visibilidad","No insight into stalled deals.","Sin visibilidad de por qu&eacute; se frenan tratos."),
    ],
    solution=[
        ("check","Zero-Friction Capture","Captura Sin Fricci&oacute;n","Leads routed to the right rep instantly.","Leads asignados al instante al vendedor correcto."),
        ("check","Automated Follow-ups","Seguimiento Autom&aacute;tico","Smart triggers, no prospect goes cold.","Alertas inteligentes, ning&uacute;n prospecto se enfr&iacute;a."),
        ("check","Clear Forecasting","Pron&oacute;sticos Claros","Win rates and pipeline value, live.","Tasas de cierre y valor de pipeline en vivo."),
        ("check","One Tool Ecosystem","Un Solo Ecosistema","Email and calendar, all in one place.","Correo y calendario, todo en un solo lugar."),
    ],
    getgrid_title_en="A CRM engineered for high-velocity sales", getgrid_title_es="Un CRM dise&ntilde;ado para vender m&aacute;s r&aacute;pido",
    getcards=[
        ("trending","Speed to Lead","Velocidad de Respuesta","New leads assigned instantly.","Leads nuevos asignados al instante."),
        ("check","No Cold Prospects","Cero Prospectos Fr&iacute;os","Automated reminders keep it warm.","Recordatorios autom&aacute;ticos mantienen el inter&eacute;s."),
        ("bars","Live Forecasting","Pron&oacute;sticos en Vivo","Decisions based on real data.","Decisiones basadas en datos reales."),
        ("briefcase","Less Admin","Menos Administraci&oacute;n","A system reps actually want to use.","Un sistema que tu equipo s&iacute; quiere usar."),
    ],
    final_h2_en="Ready to stop the revenue leaks?", final_h2_es="&iquest;Listo para detener la fuga de ingresos?",
    final_lead_en="Let's engineer a pipeline built for velocity.", final_lead_es="Dise&ntilde;emos un pipeline hecho para vender r&aacute;pido.",
    final_cta_en="Accelerate My Pipeline", final_cta_es="Acelera Mi Pipeline",
    diagram_html=lambda: sales_chart("sc", "SALES_ENGINE // trustcodemx", 284500, "Pipeline Value (MXN)", "Valor del Pipeline (MXN)"),
)

# ---------------- 6. Certified Partner ----------------
build_subpage(
    slug="monday-partner",
    title_en="Certified monday.com Partner | Trust Code",
    title_es="Socio Certificado de monday.com | Trust Code",
    desc_en="Trust Code is an officially certified monday.com implementation partner — verified expertise, ongoing training, and direct access to monday.com's own resources.",
    desc_es="Trust Code es socio certificado de monday.com — experiencia verificada, capacitación continua y acceso directo a los recursos oficiales de la plataforma.",
    crumb_en="Certified Partner", crumb_es="Socio Certificado",
    crumb_root_en="Company", crumb_root_es="Compa&ntilde;&iacute;a",
    h1_en="A Certified Partner, Not Just a Freelancer", h1_es="Un Socio Certificado, No Solo un Freelancer",
    lead_en="Certification isn't a logo &mdash; it's proof of tested expertise, ongoing training, and direct access to monday.com's own playbook.",
    lead_es="La certificaci&oacute;n no es solo un logo &mdash; es prueba de experiencia comprobada, capacitaci&oacute;n continua y acceso directo a los recursos de monday.com.",
    cta_en="Talk to a Certified Expert", cta_es="Habla con un Experto Certificado",
    col1_header_en="What Certification Means", col1_header_es="Qu&eacute; Significa la Certificaci&oacute;n",
    col2_header_en="Why It Matters to You", col2_header_es="Por Qu&eacute; te Conviene",
    challenge=[
        ("shield","Verified Product Mastery","Dominio Verificado del Producto","Tested and certified directly by monday.com on the platform's core capabilities.","Evaluado y certificado directamente por monday.com."),
        ("cap","Continuous Training","Capacitaci&oacute;n Continua","Certifications require ongoing education as the platform evolves.","Las certificaciones exigen formaci&oacute;n continua conforme evoluciona la plataforma."),
        ("link","Direct Resource Access","Acceso Directo a Recursos","A direct line to monday.com's own partner resources and best practices.","L&iacute;nea directa a los recursos y mejores pr&aacute;cticas de monday.com."),
        ("check","Accountability","Rendici&oacute;n de Cuentas","Certified partners are held to a standard &mdash; this isn't self-proclaimed.","Los socios certificados responden a un est&aacute;ndar real, no autoproclamado."),
    ],
    solution=[
        ("check","Fewer Costly Mistakes","Menos Errores Costosos","Avoid the common implementation pitfalls that come from learning on the job.","Evita los errores comunes de aprender sobre la marcha."),
        ("trending","Faster Time to Value","Resultados M&aacute;s R&aacute;pido","Certified expertise means less trial-and-error, more results, faster.","Menos prueba y error, m&aacute;s resultados, m&aacute;s r&aacute;pido."),
        ("shield","A Real Support Channel","Un Canal de Soporte Real","When something needs monday.com's own team, we have the access to get it resolved.","Cuando algo requiere al equipo de monday.com, tenemos el acceso para resolverlo."),
        ("venn","A Long-Term Ally","Un Aliado a Largo Plazo","Certification isn't a one-time badge &mdash; it's an ongoing relationship with the platform.","No es una insignia &uacute;nica &mdash; es una relaci&oacute;n continua con la plataforma."),
    ],
    getgrid_title_en="What working with a certified partner gets you", getgrid_title_es="Lo que obtienes al trabajar con un socio certificado",
    getcards=[
        ("shield","A Vetted Partner","Un Socio Verificado","Confidence that comes from third-party verification, not just a sales pitch.","Confianza respaldada por verificaci&oacute;n externa, no solo un discurso de ventas."),
        ("check","Fewer Surprises","Menos Sorpresas","Implementation done right the first time.","Implementaci&oacute;n bien hecha desde la primera vez."),
        ("bars","Platform-Level Support","Soporte a Nivel de Plataforma","Escalation paths a non-certified freelancer simply doesn't have.","Canales de escalaci&oacute;n que un freelancer no certificado simplemente no tiene."),
        ("venn","A Partner Who Stays Current","Un Socio Siempre Actualizado","monday.com evolves constantly &mdash; certification means we do too.","monday.com evoluciona constantemente &mdash; la certificaci&oacute;n significa que nosotros tambi&eacute;n."),
    ],
    final_h2_en="Ready to work with a certified partner?", final_h2_es="&iquest;Listo para trabajar con un socio certificado?",
    final_lead_en="Schedule a free strategy session and see the difference certification makes.", final_lead_es="Agenda una sesi&oacute;n estrat&eacute;gica gratuita y comprueba la diferencia.",
    final_cta_en="Schedule a Strategy Session", final_cta_es="Agenda una Sesi&oacute;n Estrat&eacute;gica",
    diagram_html=lambda: workflow_diagram(("CERTIFIED","TRAINED","VERIFIED","SUPPORTED","TRUSTED"), id_prefix="cp", tag_text="PARTNER_STATUS // trustcodemx"),
)

# ---------------- 7. About Us ----------------
build_subpage(
    slug="about-us",
    title_en="About Trust Code | monday.com Consulting Partner",
    title_es="Nosotros | Trust Code, Socio de Consultoría monday.com",
    desc_en="Trust Code is a certified monday.com partner on a mission to end operational friction — consultants first, technologists second.",
    desc_es="Trust Code es socio certificado de monday.com, con la misión de acabar con la fricción operativa — consultores primero, tecnólogos después.",
    crumb_en="About Us", crumb_es="Nosotros",
    crumb_root_en="Company", crumb_root_es="Compa&ntilde;&iacute;a",
    h1_en="We Exist to End Operational Friction", h1_es="Existimos para Acabar con la Fricci&oacute;n Operativa",
    lead_en="Trust Code was built on a simple belief: the right workflow shouldn't feel like a fight. We're consultants first, technologists second.",
    lead_es="Trust Code nace de una idea simple: el flujo de trabajo correcto no deber&iacute;a sentirse como una pelea. Somos consultores primero, tecn&oacute;logos despu&eacute;s.",
    cta_en="Work With Us", cta_es="Trabaja con Nosotros",
    col1_header_en="What We Believe", col1_header_es="En Qu&eacute; Creemos",
    col2_header_en="How We Work", col2_header_es="C&oacute;mo Trabajamos",
    challenge=[
        ("briefcase","Business First","Negocio Primero","We're consultants before we're technologists &mdash; every decision starts with your bottom line.","Somos consultores antes que tecn&oacute;logos &mdash; toda decisi&oacute;n empieza por tu rentabilidad."),
        ("bars","Results Over Reports","Resultados, No Solo Reportes","Measurable ROI, not just dashboards nobody reads.","ROI medible, no solo dashboards que nadie lee."),
        ("venn","Partnership, Not a Handoff","Sociedad, No una Entrega","We stay involved after launch &mdash; support that grows with you.","Seguimos involucrados despu&eacute;s del lanzamiento."),
        ("shield","Rigor Over Guesswork","Rigor, No Adivinanza","Certified expertise, not on-the-job learning at your expense.","Experiencia certificada, no aprendizaje a tu costa."),
    ],
    solution=[
        ("eye","We Listen First","Escuchamos Primero","Every engagement starts with understanding your actual operation, not a template.","Cada proyecto empieza entendiendo tu operaci&oacute;n real, no una plantilla."),
        ("grid","We Build for Your Team","Construimos para tu Equipo","Custom boards and automations designed around how you actually work.","Tableros y automatizaciones dise&ntilde;ados para c&oacute;mo trabajas de verdad."),
        ("repeat","We Stay Accountable","Somos Responsables","Clear metrics from day one, so success isn't a matter of opinion.","M&eacute;tricas claras desde el d&iacute;a uno."),
        ("trending","We Grow With You","Crecemos Contigo","Ongoing support as your business &mdash; and your platform &mdash; evolves.","Soporte continuo conforme tu negocio evoluciona."),
    ],
    getgrid_title_en="Why businesses choose Trust Code", getgrid_title_es="Por qu&eacute; las empresas eligen Trust Code",
    getcards=[
        ("shield","A Certified monday.com Partner","Un Socio Certificado de monday.com","Verified expertise, not a self-proclaimed title.","Experiencia verificada, no un t&iacute;tulo autoproclamado."),
        ("briefcase","A Business-First Mindset","Una Mentalidad de Negocio Primero","We think like operators, not just implementers.","Pensamos como operadores, no solo implementadores."),
        ("bars","Transparent, Measurable Results","Resultados Transparentes y Medibles","You'll always know what success looks like.","Siempre sabr&aacute;s c&oacute;mo se ve el &eacute;xito."),
        ("venn","A Relationship, Not a Project","Una Relaci&oacute;n, No un Proyecto","We're here after launch, not just during it.","Seguimos aqu&iacute; despu&eacute;s del lanzamiento."),
    ],
    final_h2_en="Ready to build something that actually works?", final_h2_es="&iquest;Listo para construir algo que realmente funcione?",
    final_lead_en="Let's talk about what's slowing your team down &mdash; and fix it.", final_lead_es="Hablemos de qu&eacute; est&aacute; frenando a tu equipo &mdash; y arregl&eacute;moslo.",
    final_cta_en="Schedule a Free Strategy Session", final_cta_es="Agenda una Sesi&oacute;n Estrat&eacute;gica Gratuita",
    diagram_html=lambda: workflow_diagram(("PEOPLE","PROCESS","PLATFORM","CULTURE","GROWTH"), id_prefix="au", tag_text="OUR_APPROACH // trustcodemx"),
    extra_section_html=founder_section,
)

# ---------------- 8. Web Design & Development ----------------
build_subpage(
    slug="web-design-development",
    title_en="Web Design & Development Services | Trust Code",
    title_es="Diseño y Desarrollo Web | Trust Code",
    desc_en="Custom, fast-loading websites built by a certified monday.com partner — designed to work as the front door to the systems we already build for you.",
    desc_es="Sitios web rápidos y a la medida, construidos por un socio certificado de monday.com — diseñados como la puerta de entrada a los sistemas que ya construimos para ti.",
    crumb_en="Web Design &amp; Development", crumb_es="Dise&ntilde;o y Desarrollo Web",
    h1_en="A Website That Works as Hard as Your Operation", h1_es="Un Sitio Web que Trabaja Tan Duro Como tu Operaci&oacute;n",
    lead_en="Your website shouldn't be disconnected from the systems running your business. We design and build sites that plug directly into the workflows we set up on monday.com.",
    lead_es="Tu sitio web no deber&iacute;a estar desconectado de los sistemas que dirigen tu negocio. Dise&ntilde;amos y construimos sitios que se conectan directamente a los flujos que configuramos en monday.com.",
    cta_en="Start My Website", cta_es="Inicia mi Sitio Web",
    challenge=[
        ("alert","Outdated or DIY Sites","Sitios Desactualizados o Caseros","A site that doesn't reflect the business you've become.","Un sitio que ya no refleja el negocio en que te has convertido."),
        ("alert","Disconnected From Your Systems","Desconectado de tus Sistemas","Leads from the site never make it into your CRM.","Los leads del sitio nunca llegan a tu CRM."),
        ("alert","Slow, Hard to Update","Lento y Dif&iacute;cil de Actualizar","Every small change means waiting on a developer.","Cada cambio peque&ntilde;o implica esperar a un desarrollador."),
        ("alert","No Clear Path to Contact","Sin un Camino Claro a Contacto","Visitors can't tell what to do next.","Los visitantes no saben qu&eacute; hacer despu&eacute;s."),
    ],
    solution=[
        ("check","Design Tied to Your Brand","Dise&ntilde;o Fiel a tu Marca","A site that actually looks like your business.","Un sitio que realmente se ve como tu negocio."),
        ("check","Connected to monday.com","Conectado a monday.com","Forms and leads flow straight into your boards.","Formularios y leads fluyen directo a tus tableros."),
        ("check","Built to Be Maintained","Construido para Mantenerse","Easy updates, without waiting on a developer.","Actualizaciones f&aacute;ciles, sin esperar a un desarrollador."),
        ("check","A Clear Path to Action","Un Camino Claro a la Acci&oacute;n","Every page points toward a next step.","Cada p&aacute;gina apunta hacia un siguiente paso."),
    ],
    getgrid_title_en="A site built to convert, not just exist", getgrid_title_es="Un sitio hecho para convertir, no solo para existir",
    getcards=[
        ("browser","A Modern, Fast Site","Un Sitio Moderno y R&aacute;pido","Built for speed, not just looks.","Construido para velocidad, no solo apariencia."),
        ("link","Full Integration","Integraci&oacute;n Total","Your site and your systems, working together.","Tu sitio y tus sistemas, trabajando juntos."),
        ("repeat","Easy to Maintain","F&aacute;cil de Mantener","Update content without touching code.","Actualiza contenido sin tocar c&oacute;digo."),
        ("trending","More Qualified Leads","M&aacute;s Leads Calificados","A site designed to turn visits into conversations.","Un sitio dise&ntilde;ado para convertir visitas en conversaciones."),
    ],
    final_h2_en="Ready for a site that pulls its weight?", final_h2_es="&iquest;Listo para un sitio que s&iacute; aporte?",
    final_lead_en="Let's design something that actually supports how you sell and operate.", final_lead_es="Dise&ntilde;emos algo que realmente apoye c&oacute;mo vendes y operas.",
    final_cta_en="Start My Website", final_cta_es="Inicia mi Sitio Web",
    diagram_html=lambda: website_builder("wd", "SITE_BUILDER // trustcodemx"),
)

# ---------------- 9. Social Media Management ----------------
build_subpage(
    slug="social-media-management",
    title_en="Social Media Management Services | Trust Code",
    title_es="Gestión de Redes Sociales | Trust Code",
    desc_en="Social media content planned, scheduled, and tracked the same way we run everything else — on monday.com, with a real content calendar and clear results.",
    desc_es="Contenido de redes sociales planeado, programado y medido igual que todo lo demás — en monday.com, con un calendario de contenido real y resultados claros.",
    crumb_en="Social Media Management", crumb_es="Gesti&oacute;n de Redes Sociales",
    h1_en="A Content Engine, Not Just a Posting Calendar", h1_es="Un Motor de Contenido, No Solo un Calendario de Publicaciones",
    lead_en="Random posting doesn't build a brand. We plan, produce, and publish content on a real system — the same one running the rest of your business.",
    lead_es="Publicar al azar no construye una marca. Planeamos, producimos y publicamos contenido sobre un sistema real — el mismo que dirige el resto de tu negocio.",
    cta_en="Plan My Content", cta_es="Planea mi Contenido",
    challenge=[
        ("alert","Inconsistent Posting","Publicaci&oacute;n Inconsistente","Weeks go by with no content, then a rush.","Pasan semanas sin contenido, luego una corrida."),
        ("alert","No Real Strategy","Sin Estrategia Real","Posting without a plan behind it.","Publicar sin un plan detr&aacute;s."),
        ("alert","Unclear Results","Resultados Poco Claros","No idea what's actually driving engagement.","Sin idea de qu&eacute; genera el compromiso real."),
        ("alert","Disconnected From Sales","Desconectado de Ventas","Social lives apart from the rest of the business.","Las redes viven aparte del resto del negocio."),
    ],
    solution=[
        ("check","Real Content Calendar","Calendario de Contenido Real","Planned weeks ahead, not day-of.","Planeado con semanas de anticipaci&oacute;n."),
        ("check","Strategy Before Posting","Estrategia Antes de Publicar","Every post ties back to a goal.","Cada publicaci&oacute;n conecta con un objetivo."),
        ("check","Clear Performance Tracking","Seguimiento Claro de Resultados","Real metrics, not just likes.","M&eacute;tricas reales, no solo likes."),
        ("check","Tied to the Rest of the Business","Conectado al Resto del Negocio","Leads from social routed like any other.","Leads de redes sociales ruteados como cualquier otro."),
    ],
    getgrid_title_en="Content that shows up, on purpose", getgrid_title_es="Contenido que aparece, a prop&oacute;sito",
    getcards=[
        ("calendar","A Real Calendar","Un Calendario Real","Content planned, not improvised.","Contenido planeado, no improvisado."),
        ("image","On-Brand Content","Contenido Fiel a tu Marca","Consistent look, consistent voice.","Imagen y voz consistentes."),
        ("bars","Clear Reporting","Reportes Claros","Know what's actually working.","Sabe qu&eacute; est&aacute; funcionando de verdad."),
        ("share","One Connected System","Un Sistema Conectado","Social tied into the rest of your operation.","Redes conectadas al resto de tu operaci&oacute;n."),
    ],
    final_h2_en="Ready for social media that works like the rest of your business?", final_h2_es="&iquest;Listo para redes sociales que funcionen como el resto de tu negocio?",
    final_lead_en="Let's build a content system, not just a posting habit.", final_lead_es="Construyamos un sistema de contenido, no solo un h&aacute;bito de publicar.",
    final_cta_en="Plan My Content", final_cta_es="Planea mi Contenido",
    diagram_html=lambda: marketing_funnel("sm", "CONTENT_ENGINE // trustcodemx", [
        ("Ideas","Ideas",86),("In Production","En Producci&oacute;n",34),("Scheduled","Programado",21),("Published","Publicado",18),
    ]),
)

print("all 9 subpages written (en + es)")

# ---------------------------------------------------------------
# BLOG LISTING (static design reference -- see deployment guide re:
# setting up a real Squarespace Blog Collection for actual publishing)
# ---------------------------------------------------------------
BLOG_POSTS = [
    ("purple", "Strategy", "Estrategia", "5 Signs Your Team Needs a Work OS", "5 Señales de que tu Equipo Necesita un Work OS",
     "How to tell when spreadsheets have stopped being enough for your team.", "Cómo saber cuándo las hojas de cálculo ya no alcanzan para tu equipo.", "Jun 12, 2026", "4 min read", "4 min de lectura"),
    ("emerald", "Case Study", "Caso de Éxito", "How We Cut Reporting Time by 80%", "Cómo Redujimos el Tiempo de Reportes en 80%",
     "A real client walkthrough: from manual spreadsheets to live dashboards.", "Un caso real: de hojas de cálculo manuales a dashboards en vivo.", "Jun 2, 2026", "6 min read", "6 min de lectura"),
    ("purple", "Comparison", "Comparativa", "monday.com vs. Asana: Which Fits You", "monday.com vs. Asana: ¿Cuál te Conviene?",
     "A practical, no-nonsense comparison for growing teams.", "Una comparación práctica y directa para equipos en crecimiento.", "May 20, 2026", "5 min read", "5 min de lectura"),
    ("emerald", "Automation", "Automatización", "Automate Your Sales Pipeline in 3 Steps", "Automatiza tu Pipeline de Ventas en 3 Pasos",
     "Zero-friction lead routing, without touching a single spreadsheet.", "Ruteo de leads sin fricción, sin tocar una sola hoja de cálculo.", "May 8, 2026", "3 min read", "3 min de lectura"),
    ("purple", "Training", "Capacitación", "The Real ROI of Proper Onboarding", "El Verdadero ROI de una Buena Capacitación",
     "Why the first two weeks decide whether your tool sticks or dies.", "Por qué las primeras dos semanas deciden si tu herramienta sobrevive.", "Apr 28, 2026", "4 min read", "4 min de lectura"),
    ("emerald", "News", "Noticias", "TrustCode Is Now Certified in monday CRM", "TrustCode Ya Está Certificado en monday CRM",
     "One more certification, one more reason to trust the process.", "Una certificación más, una razón más para confiar en el proceso.", "Apr 15, 2026", "2 min read", "2 min de lectura"),
]

def blog_card(i, accent, tag_en, tag_es, title_en, title_es, ex_en, ex_es, date, rt_en, rt_es):
    grad = "135deg, var(--purple) 0%, #8A8AFF 100%" if accent == "purple" else "135deg, var(--emerald) 0%, #4FD69C 100%"
    return f"""<a class="blog-card icon-pop reveal" href="https://wkf.ms/49age3d" style="transition-delay:{i*0.06:.2f}s; text-decoration:none;">
      <div class="blog-thumb" style="background:linear-gradient({grad});"></div>
      <div class="blog-body">
        <span class="blog-tag">{T(tag_en, tag_es)}</span>
        <h4>{T(title_en, title_es)}</h4>
        <p>{T(ex_en, ex_es)}</p>
        <span class="blog-meta">{date} &middot; {T(rt_en, rt_es)}</span>
      </div>
    </a>"""

def blog_body():
    cards = "\n".join(blog_card(i, *p) for i, p in enumerate(BLOG_POSTS))
    return f"""<section class="subhero" style="position:relative;">
  <div class="ambient-blob" style="width:260px; height:260px; top:-70px; right:6%; background:rgba(97,97,255,0.14); animation-delay:-3s;"></div>
  <div class="tc-wrap" style="position:relative;">
    <span class="crumb hero-in" style="animation-delay:.05s">{T('Resources','Recursos')} / <span class="accent">{T('Blog','Blog')}</span></span>
    <h1 class="hero-in" style="animation-delay:.15s">{T('Insights, Guides &amp; Case Studies','Ideas, Gu&iacute;as y Casos de &Eacute;xito')}</h1>
    <p class="lead hero-in" style="animation-delay:.25s">{T('Practical monday.com knowledge from real client work.','Conocimiento pr&aacute;ctico de monday.com basado en trabajo real con clientes.')}</p>
  </div>
</section>

<section>
  <div class="tc-wrap">
    <div class="grid-3">
      {cards}
    </div>
  </div>
</section>

<section>
  <div class="tc-wrap final-cta reveal">
    <span class="eyebrow" style="justify-content:center">{T('stay updated','mant&eacute;nte al d&iacute;a')}</span>
    <h2>{T('New posts, straight to your inbox','Nuevos art&iacute;culos directo a tu correo')}</h2>
    <p>{T('No spam. Just monday.com tips that actually help.','Sin spam. Solo tips de monday.com que realmente ayudan.')}</p>
    <a class="btn-primary" href="https://wkf.ms/49age3d">{T('Subscribe','Suscr&iacute;bete')}</a>
  </div>
</section>
"""

def blog_jsonld():
    return [breadcrumb_jsonld("blog", "Blog", "Blog")]

build_both_langs(
    "blog",
    title_en="Blog | monday.com Insights & Case Studies | Trust Code",
    title_es="Blog | Ideas y Casos de Éxito sobre monday.com | Trust Code",
    desc_en="Practical monday.com tips, automation guides, and real client case studies from the Trust Code team.",
    desc_es="Consejos prácticos de monday.com, guías de automatización y casos de éxito reales del equipo de Trust Code.",
    build_body_fn=blog_body,
    json_ld_fn=blog_jsonld,
)
print("blog (en + es) written")

# ---------------------------------------------------------------
# SITE-WIDE FOOTER INJECTION: 4 header/footer templates (raw HTML,
# not JS-string-escaped) + a script that clones the right pair based
# on whether the path starts with /es/, then runs the shared reveal /
# dropdown / lang-toggle script.
# ---------------------------------------------------------------
footer_injection = f"""<template id="tc-tpl-header-en">{CAPTURED['header-en']}</template>
<template id="tc-tpl-footer-en">{CAPTURED['footer-en']}</template>
<template id="tc-tpl-header-es">{CAPTURED['header-es']}</template>
<template id="tc-tpl-footer-es">{CAPTURED['footer-es']}</template>
<script>
  (function () {{
    var isEs = /^\\/es(\\/|$)/.test(location.pathname);
    document.documentElement.lang = isEs ? 'es' : 'en';
    var hTpl = document.getElementById(isEs ? 'tc-tpl-header-es' : 'tc-tpl-header-en');
    var fTpl = document.getElementById(isEs ? 'tc-tpl-footer-es' : 'tc-tpl-footer-en');
    document.body.insertBefore(hTpl.content.cloneNode(true), document.body.firstChild);
    document.body.appendChild(fTpl.content.cloneNode(true));
  }})();
</script>
{LANG_SCRIPT}
"""
with open(os.path.join(SITEWIDE_DIR, "footer-injection.txt"), "w") as f:
    f.write(footer_injection)
print("squarespace-sitewide/footer-injection.txt written")

# ---------------------------------------------------------------
# SITEMAP + ROBOTS
# ---------------------------------------------------------------
sitemap_items = ""
seen_urls = set()
for entry in SITEMAP_ENTRIES:
    if entry["url"] in seen_urls:
        continue
    seen_urls.add(entry["url"])
    sitemap_items += f"""  <url>
    <loc>{entry['url']}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{entry['alt_en']}"/>
    <xhtml:link rel="alternate" hreflang="es" href="{entry['alt_es']}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{entry['alt_en']}"/>
    <changefreq>monthly</changefreq>
  </url>
"""
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{sitemap_items}</urlset>
"""
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write(sitemap_xml)

robots_txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(robots_txt)

print(f"sitemap.xml written with {len(seen_urls)} URLs, robots.txt written")
print("BUILD COMPLETE")
