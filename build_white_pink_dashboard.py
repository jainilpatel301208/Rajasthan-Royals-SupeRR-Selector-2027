import base64
import os

# Read the official RR logo
logo_path = '/Users/jainil.30/Downloads/RR/rr_logo.png'
with open(logo_path, 'rb') as f:
    logo_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rajasthan Royals — IPL 2027 Auction War Room</title>
  <style>
    /* ==========================================================================
       RAJASTHAN ROYALS OFFICIAL WHITE & PINK THEME
       Zero External Dependencies &bull; 100% Native Inline CSS &bull; Retina Vector Assets
       ========================================================================== */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    :root {{
      --bg-page: #F8FAFC;
      --bg-white: #FFFFFF;
      --bg-subtle-pink: #FFF5F8;
      --bg-pink-hover: #FDF2F8;

      --rr-pink-500: #E6196E;      /* Official Royals Pink */
      --rr-pink-600: #C21059;
      --rr-pink-400: #FF2E88;
      --rr-pink-100: #FCE7F3;
      --rr-pink-50: #FFF1F7;

      --rr-navy-900: #001D48;      /* Official Royals Navy */
      --rr-navy-800: #0B2550;
      --rr-navy-700: #16366E;

      --rr-gold-500: #C59B27;      /* Royals Gold */
      --rr-gold-600: #B45309;
      --rr-gold-100: #FEF3C7;

      --status-emerald: #059669;
      --status-emerald-bg: #ECFDF5;

      --text-main: #0F172A;
      --text-body: #334155;
      --text-muted: #64748B;
      --text-dim: #94A3B8;

      --border-slate: #E2E8F0;
      --border-pink: #FBCFE8;

      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-card: 0 2px 8px -1px rgba(0, 0, 0, 0.06), 0 1px 3px -1px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.03);
      --shadow-pink: 0 4px 14px rgba(230, 25, 110, 0.25);

      --font-stack: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Inter", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}

    body {{
      background-color: var(--bg-page);
      color: var(--text-body);
      font-family: var(--font-stack);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    .num {{
      font-variant-numeric: tabular-nums;
      font-feature-settings: "tnum" 1;
      letter-spacing: -0.01em;
    }}

    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: #F1F5F9; }}
    ::-webkit-scrollbar-thumb {{ background: #CBD5E1; border-radius: 3px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: var(--rr-pink-500); }}

    .app-container {{
      width: 100%;
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 28px;
    }}

    /* ==========================================================================
       HEADER: WHITE BACKGROUND WITH ROYALS PINK ACCENTS
       ========================================================================== */
    header {{
      background: var(--bg-white);
      border-bottom: 3px solid var(--rr-pink-500);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
    }}

    .header-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 76px;
    }}

    .brand-section {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .rr-logo-img {{
      height: 52px;
      width: auto;
      display: block;
      object-fit: contain;
    }}

    .brand-titles {{
      display: flex;
      flex-direction: column;
    }}

    .brand-title-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .brand-title {{
      font-size: 18px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--rr-navy-900);
    }}

    .badge-hub {{
      background: var(--rr-pink-500);
      color: #FFFFFF;
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      padding: 2px 8px;
      border-radius: 4px;
      letter-spacing: 0.05em;
    }}

    .brand-subtitle {{
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 500;
      margin-top: 1px;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 9px 18px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid transparent;
      transition: all 0.15s ease;
      font-family: inherit;
      text-decoration: none;
    }}

    .btn-secondary {{
      background: var(--bg-white);
      border-color: var(--border-slate);
      color: var(--rr-navy-900);
    }}
    .btn-secondary:hover {{
      border-color: var(--rr-pink-500);
      color: var(--rr-pink-500);
      background: var(--rr-pink-50);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, var(--rr-pink-500) 0%, var(--rr-pink-600) 100%);
      color: #FFFFFF;
      box-shadow: var(--shadow-pink);
    }}
    .btn-primary:hover {{
      background: linear-gradient(135deg, var(--rr-pink-400) 0%, var(--rr-pink-500) 100%);
      transform: translateY(-1px);
    }}

    .svg-icon {{
      width: 14px;
      height: 14px;
      fill: none;
      stroke: currentColor;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      flex-shrink: 0;
    }}

    /* ==========================================================================
       HORIZONTAL COMMAND TELEMETRY STRIP
       ========================================================================== */
    .telemetry-strip {{
      background: var(--bg-subtle-pink);
      border-bottom: 1px solid var(--border-pink);
      padding: 14px 0;
    }}

    .telemetry-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 16px;
    }}

    @media (max-width: 1080px) {{
      .telemetry-grid {{ grid-template-columns: repeat(3, 1fr); }}
    }}
    @media (max-width: 680px) {{
      .telemetry-grid {{ grid-template-columns: 1fr; }}
    }}

    .telemetry-cell {{
      padding: 4px 14px;
      border-left: 3px solid #CBD5E1;
      display: flex;
      flex-direction: column;
    }}
    .telemetry-cell.accent-pink {{ border-left-color: var(--rr-pink-500); }}
    .telemetry-cell.accent-gold {{ border-left-color: var(--rr-gold-500); }}
    .telemetry-cell.accent-green {{ border-left-color: var(--status-emerald); }}
    .telemetry-cell.accent-navy {{ border-left-color: var(--rr-navy-900); }}

    .telemetry-label {{
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }}

    .telemetry-val {{
      font-size: 15.5px;
      font-weight: 800;
      color: var(--rr-navy-900);
      margin-top: 2px;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }}

    .telemetry-sub {{
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-muted);
    }}

    /* ==========================================================================
       MAIN WORKSPACE
       ========================================================================== */
    main {{
      flex: 1;
      padding: 24px 0 48px;
    }}

    /* TABS */
    .tabs-header-wrap {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid var(--border-slate);
      margin-bottom: 22px;
      gap: 16px;
      flex-wrap: wrap;
    }}

    .nav-tabs {{
      display: flex;
      gap: 8px;
    }}

    .nav-tab-btn {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      border-bottom: none;
      padding: 12px 20px;
      font-size: 13px;
      font-weight: 700;
      color: var(--text-body);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      border-radius: 8px 8px 0 0;
      transition: all 0.15s ease;
      font-family: inherit;
    }}
    .nav-tab-btn:hover {{
      color: var(--rr-pink-500);
      background: var(--rr-pink-50);
      border-color: var(--border-pink);
    }}
    .nav-tab-btn.active {{
      background: var(--rr-pink-500);
      border-color: var(--rr-pink-500);
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(230, 25, 110, 0.2);
    }}

    .tab-counter {{
      background: #F1F5F9;
      color: var(--text-muted);
      font-size: 10.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 12px;
    }}
    .nav-tab-btn.active .tab-counter {{
      background: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
    }}

    /* CONTEXTUAL TABLE TOOLBAR */
    .table-toolbar {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      border-bottom: 1px solid #EDF2F7;
      border-radius: 10px 10px 0 0;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}

    .toolbar-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .toolbar-title {{
      font-size: 14px;
      font-weight: 800;
      color: var(--rr-navy-900);
    }}

    .filter-pills {{
      display: flex;
      gap: 6px;
    }}

    .pill-btn {{
      background: #F8FAFC;
      border: 1px solid var(--border-slate);
      color: var(--text-body);
      font-size: 11.5px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: inherit;
    }}
    .pill-btn:hover {{
      border-color: var(--rr-pink-500);
      color: var(--rr-pink-500);
      background: var(--rr-pink-50);
    }}
    .pill-btn.active {{
      background: var(--rr-navy-900);
      border-color: var(--rr-navy-900);
      color: #FFFFFF;
    }}

    .search-control {{
      position: relative;
    }}
    .search-input {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      border-radius: 6px;
      padding: 7px 12px 7px 32px;
      font-size: 12.5px;
      color: var(--text-main);
      width: 220px;
      outline: none;
      transition: all 0.15s ease;
      font-family: inherit;
    }}
    .search-input:focus {{
      border-color: var(--rr-pink-500);
      box-shadow: 0 0 0 3px rgba(230, 25, 110, 0.12);
      width: 260px;
    }}
    .search-icon-svg {{
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      width: 14px;
      height: 14px;
      stroke: var(--text-dim);
      pointer-events: none;
    }}

    /* ==========================================================================
       ROSTER DATA TABLE (WHITE THEME WITH CRISP PINK HIGHLIGHTS)
       ========================================================================== */
    .table-card {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      border-top: none;
      border-radius: 0 0 10px 10px;
      overflow: hidden;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .roster-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }}

    .roster-table th {{
      background: #F8FAFC;
      color: var(--rr-navy-900);
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 12px 16px;
      border-bottom: 2px solid var(--border-slate);
      white-space: nowrap;
    }}
    .roster-table th.tar, .roster-table td.tar {{ text-align: right; }}
    .roster-table th.tac, .roster-table td.tac {{ text-align: center; }}

    .roster-table tbody tr {{
      border-bottom: 1px solid var(--border-slate);
      transition: background 0.12s ease;
      cursor: pointer;
    }}
    .roster-table tbody tr:hover {{
      background: var(--rr-pink-50);
    }}

    .rank-cell {{
      width: 52px;
      text-align: center;
    }}
    .rank-num {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 26px;
      height: 26px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 800;
    }}
    .rank-top1 {{
      background: var(--rr-gold-100);
      color: var(--rr-gold-600);
      border: 1px solid #FDE68A;
    }}
    .rank-top2 {{
      background: #F1F5F9;
      color: #475569;
      border: 1px solid #E2E8F0;
    }}
    .rank-top3 {{
      background: #FFEDD5;
      color: #C2410C;
      border: 1px solid #FED7AA;
    }}
    .rank-standard {{
      background: var(--rr-pink-50);
      color: var(--rr-pink-500);
      border: 1px solid var(--rr-pink-100);
    }}

    .player-title {{
      font-size: 14px;
      font-weight: 800;
      color: var(--rr-navy-900);
      letter-spacing: -0.01em;
    }}
    .player-subtitle {{
      font-size: 11.5px;
      color: var(--text-muted);
      margin-top: 1px;
    }}

    .metric-primary {{
      color: var(--rr-navy-900);
      font-weight: 800;
    }}

    .metric-elevation-pos {{
      color: var(--rr-pink-500);
      font-weight: 800;
      background: var(--rr-pink-50);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid var(--rr-pink-100);
      display: inline-block;
    }}
    .metric-econ-pos {{
      color: var(--status-emerald);
      font-weight: 800;
      background: var(--status-emerald-bg);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid #A7F3D0;
      display: inline-block;
    }}
    .metric-econ-neg {{
      color: var(--rr-pink-500);
      font-weight: 800;
      background: var(--rr-pink-50);
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
    }}

    .rating-badge {{
      display: inline-block;
      font-size: 11.5px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      background: #F0FDF4;
      color: var(--status-emerald);
      border: 1px solid #BBF7D0;
    }}

    .tactical-role-text {{
      font-size: 12px;
      color: var(--text-body);
      line-height: 1.4;
    }}

    .btn-inspect {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      color: var(--rr-navy-900);
      padding: 5px 12px;
      border-radius: 5px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
      font-family: inherit;
    }}
    .btn-inspect:hover {{
      background: var(--rr-pink-500);
      border-color: var(--rr-pink-500);
      color: #FFFFFF;
      box-shadow: 0 2px 8px rgba(230, 25, 110, 0.25);
    }}

    /* ==========================================================================
       TACTICAL CARDS
       ========================================================================== */
    .tactical-strip {{
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 18px;
      margin-bottom: 24px;
    }}
    @media (max-width: 900px) {{
      .tactical-strip {{ grid-template-columns: 1fr; }}
    }}

    .tactical-card {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      border-top: 3px solid var(--rr-navy-900);
      border-radius: 8px;
      padding: 18px 20px;
      box-shadow: var(--shadow-sm);
    }}
    .tactical-card.highlight {{
      border-top-color: var(--rr-pink-500);
      background: linear-gradient(180deg, var(--rr-pink-50) 0%, var(--bg-white) 60%);
    }}
    .tactical-card.gold-top {{
      border-top-color: var(--rr-gold-500);
    }}
    .tactical-card.green-top {{
      border-top-color: var(--status-emerald);
    }}

    .tactical-card-tag {{
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--rr-pink-500);
      margin-bottom: 4px;
    }}
    .tactical-card-title {{
      font-size: 14.5px;
      font-weight: 800;
      color: var(--rr-navy-900);
      margin-bottom: 6px;
    }}
    .tactical-card-desc {{
      font-size: 12.5px;
      color: var(--text-body);
      line-height: 1.5;
    }}

    /* ==========================================================================
       VENUE STRATEGY MATRIX (JAIPUR SMS STADIUM)
       ========================================================================== */
    .venue-panel {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      border-radius: 10px;
      padding: 28px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .venue-head {{
      border-bottom: 2px solid var(--rr-pink-100);
      padding-bottom: 16px;
      margin-bottom: 22px;
    }}
    .venue-title {{
      font-size: 20px;
      font-weight: 800;
      color: var(--rr-navy-900);
      letter-spacing: -0.01em;
    }}
    .venue-subtitle {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
      max-width: 820px;
    }}

    .venue-split {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 22px;
    }}
    @media (max-width: 800px) {{
      .venue-split {{ grid-template-columns: 1fr; }}
    }}

    .venue-column {{
      background: #F8FAFC;
      border: 1px solid var(--border-slate);
      border-radius: 8px;
      padding: 20px;
    }}
    .venue-column-header {{
      font-size: 14px;
      font-weight: 800;
      color: var(--rr-navy-900);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
    }}
    .venue-point {{
      margin-bottom: 12px;
      font-size: 12.5px;
      color: var(--text-body);
      line-height: 1.5;
    }}
    .venue-point b {{
      color: var(--rr-navy-900);
    }}

    /* ==========================================================================
       WAR ROOM PURSE ALLOCATOR
       ========================================================================== */
    .simulator-container {{
      background: var(--bg-white);
      border: 1px solid var(--border-slate);
      border-radius: 10px;
      padding: 28px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}

    .sim-layout {{
      display: grid;
      grid-template-columns: 1.8fr 1.2fr;
      gap: 24px;
      margin-top: 20px;
    }}
    @media (max-width: 900px) {{
      .sim-layout {{ grid-template-columns: 1fr; }}
    }}

    .sim-row {{
      background: #F8FAFC;
      border: 1px solid var(--border-slate);
      border-radius: 8px;
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .sim-row:hover {{
      background: var(--rr-pink-50);
      border-color: var(--border-pink);
    }}
    .sim-row.active {{
      background: var(--rr-pink-50);
      border: 1.5px solid var(--rr-pink-500);
    }}

    .sim-checkbox {{
      width: 17px;
      height: 17px;
      accent-color: var(--rr-pink-500);
      cursor: pointer;
    }}

    .sim-summary-panel {{
      background: var(--bg-subtle-pink);
      border: 1px solid var(--border-pink);
      border-radius: 8px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .sim-metric-row {{
      display: flex;
      justify-content: space-between;
      padding: 10px 0;
      border-bottom: 1px solid var(--border-pink);
      font-size: 13px;
    }}

    /* ==========================================================================
       MODAL DRAWER
       ========================================================================== */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 29, 72, 0.4);
      backdrop-filter: blur(6px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-backdrop.active {{
      display: flex;
    }}

    .modal-dialog {{
      background: var(--bg-white);
      border: 2px solid var(--rr-pink-500);
      box-shadow: var(--shadow-lg), 0 0 25px rgba(230, 25, 110, 0.2);
      border-radius: 12px;
      width: 100%;
      max-width: 640px;
      overflow: hidden;
      animation: modalFadeIn 0.2s ease-out;
    }}
    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .modal-header {{
      background: #FDF2F8;
      border-bottom: 1px solid var(--border-pink);
      padding: 20px 24px;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
    }}

    .modal-body {{
      padding: 22px 24px;
    }}

    .modal-grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 20px;
    }}
    .modal-stat-box {{
      background: #F8FAFC;
      border: 1px solid var(--border-slate);
      border-radius: 8px;
      padding: 12px;
      text-align: center;
    }}

    .modal-scouting-box {{
      background: #F8FAFC;
      border: 1px solid var(--border-slate);
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 16px;
    }}

    .modal-footer {{
      background: #F8FAFC;
      padding: 14px 24px;
      border-top: 1px solid var(--border-slate);
      display: flex;
      justify-content: flex-end;
    }}

    /* ==========================================================================
       FOOTER
       ========================================================================== */
    footer {{
      background: var(--bg-white);
      border-top: 1px solid var(--border-slate);
      padding: 20px 0;
      font-size: 12px;
      color: var(--text-muted);
    }}
    .footer-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}

    /* Print Styles */
    @media print {{
      body {{ background: #fff !important; color: #000 !important; }}
      header, .telemetry-strip, .table-toolbar, footer {{ background: #fff !important; border-color: #ddd !important; }}
      .no-print {{ display: none !important; }}
      .roster-table th {{ background: #f1f5f9 !important; color: #000 !important; }}
      .roster-table td {{ color: #000 !important; }}
    }}
  </style>
</head>
<body>

  <!-- ==================== HEADER ==================== -->
  <header>
    <div class="app-container header-bar">
      
      <!-- Brand & Original Logo -->
      <div class="brand-section">
        <!-- Official Rajasthan Royals Authentic Logo -->
        <img class="rr-logo-img" src="data:image/png;base64,{logo_b64}" alt="Rajasthan Royals" />

        <div class="brand-titles">
          <div class="brand-title-wrap">
            <span class="brand-title">RAJASTHAN ROYALS</span>
            <span class="badge-hub">WAR ROOM 2027</span>
          </div>
          <div class="brand-subtitle">
            SupeRR Selector Season 2 &bull; Auction Pressure Analytics
          </div>
        </div>
      </div>

      <!-- Action Controls -->
      <div class="header-actions no-print">
        <button onclick="window.print()" class="btn btn-secondary">
          <svg class="svg-icon" viewBox="0 0 24 24"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          Print Dossier
        </button>
        <button onclick="exportCSV()" class="btn btn-primary">
          <svg class="svg-icon" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
          Export Dataset
        </button>
      </div>

    </div>
  </header>

  <!-- ==================== HORIZONTAL TELEMETRY STRIP ==================== -->
  <div class="telemetry-strip">
    <div class="app-container telemetry-grid">
      
      <div class="telemetry-cell accent-navy">
        <span class="telemetry-label">Analysis Corpus</span>
        <div class="telemetry-val">
          <span class="num">201,000</span>
          <span class="telemetry-sub">Balls (867 Matches)</span>
        </div>
      </div>

      <div class="telemetry-cell accent-pink">
        <span class="telemetry-label">Pressure Crucible</span>
        <div class="telemetry-val">
          <span class="num">51,176</span>
          <span class="telemetry-sub" style="color:var(--rr-pink-500); font-weight:700;">PI &ge; 0.65 (Top 25.5%)</span>
        </div>
      </div>

      <div class="telemetry-cell accent-gold">
        <span class="telemetry-label">Batting Elevation #1</span>
        <div class="telemetry-val">
          <span>Ashutosh Sharma</span>
          <span class="telemetry-sub num" style="color:var(--rr-pink-500); font-weight:800;">+83.1 &Delta;SR</span>
        </div>
      </div>

      <div class="telemetry-cell accent-green">
        <span class="telemetry-label">Bowling Control #1</span>
        <div class="telemetry-val">
          <span>Sakib Hussain</span>
          <span class="telemetry-sub num" style="color:var(--status-emerald); font-weight:800;">8.39 RPO</span>
        </div>
      </div>

      <div class="telemetry-cell accent-navy">
        <span class="telemetry-label">Purse Capacity</span>
        <div class="telemetry-val">
          <span class="num">₹44.50 Cr</span>
          <span class="telemetry-sub">Reserve Balance</span>
        </div>
      </div>

    </div>
  </div>

  <!-- ==================== MAIN WORKSPACE ==================== -->
  <main>
    <div class="app-container">

      <!-- Navigation Tabs -->
      <div class="tabs-header-wrap">
        <div class="nav-tabs" id="tabBar">
          <button class="nav-tab-btn active" onclick="switchTab('batters', this)">
            <svg class="svg-icon" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
            <span>Uncapped Batsmen</span>
            <span class="tab-counter">10</span>
          </button>
          <button class="nav-tab-btn" onclick="switchTab('bowlers', this)">
            <svg class="svg-icon" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
            <span>Uncapped Bowlers</span>
            <span class="tab-counter">10</span>
          </button>
          <button class="nav-tab-btn" onclick="switchTab('venue', this)">
            <svg class="svg-icon" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            <span>Sawai Mansingh Stadium Matrix</span>
          </button>
          <button class="nav-tab-btn" onclick="switchTab('simulator', this)">
            <svg class="svg-icon" viewBox="0 0 24 24"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>
            <span>Purse Allocator</span>
          </button>
        </div>

        <div style="font-size:12px; color:var(--text-muted);">
          Benchmark League Heat: <span class="num" style="color:var(--rr-navy-900); font-weight:800;">142.4 SR</span> &bull; <span class="num" style="color:var(--rr-navy-900); font-weight:800;">9.61 RPO</span>
        </div>
      </div>

      <!-- ==================== TAB 1: BATSMEN ==================== -->
      <div id="tab-batters">
        
        <div class="table-toolbar">
          <div class="toolbar-left">
            <span class="toolbar-title">Top 10 Uncapped Batsmen Available in Auction</span>
            <div class="filter-pills">
              <button class="pill-btn active" onclick="filterBatters('all', this)">All</button>
              <button class="pill-btn" onclick="filterBatters('finisher', this)">Finishers</button>
              <button class="pill-btn" onclick="filterBatters('spin', this)">Spin Hitters</button>
              <button class="pill-btn" onclick="filterBatters('keeper', this)">Wicketkeeper</button>
            </div>
          </div>

          <div class="search-control">
            <svg class="search-icon-svg" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
            <input type="text" id="battersSearch" class="search-input" placeholder="Search batter..." oninput="handleBatterSearch()">
          </div>
        </div>

        <div class="table-card">
          <div style="overflow-x:auto;">
            <table class="roster-table">
              <thead>
                <tr>
                  <th class="tac" style="width:52px;">Rank</th>
                  <th>Player & Tactical Role</th>
                  <th class="tar">HP Balls</th>
                  <th class="tar">HP Strike Rate</th>
                  <th class="tar">Base SR</th>
                  <th class="tar">Elevation (&Delta;SR)</th>
                  <th class="tar">HP Average</th>
                  <th class="tar">Boundary %</th>
                  <th class="tar">Consistency</th>
                  <th class="tar">Composite CBR</th>
                  <th>Rajasthan Royals Tactical Fit</th>
                  <th class="tac" style="width:75px;">Profile</th>
                </tr>
              </thead>
              <tbody id="battersTableBody">
                <!-- Injected via JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Tactical Strategy Cards -->
        <div class="tactical-strip">
          <div class="tactical-card highlight">
            <div class="tactical-card-tag">Priority Finisher</div>
            <div class="tactical-card-title">Ashutosh Sharma (+83.1 &Delta;SR)</div>
            <div class="tactical-card-desc">
              Scores at 186.6 in the clutch (vs 103.5 baseline). Eliminates Rajasthan Royals' death-over scoring lag when Samson or Parag fall.
            </div>
          </div>

          <div class="tactical-card gold-top">
            <div class="tactical-card-tag" style="color:var(--rr-gold-600);">Jaipur 75m Match-up</div>
            <div class="tactical-card-title">Sameer Rizvi (182.7 HP SR)</div>
            <div class="tactical-card-desc">
              High launch-angle power hitter specifically built to loft spinners over Sawai Mansingh Stadium's 75m square boundaries.
            </div>
          </div>

          <div class="tactical-card green-top">
            <div class="tactical-card-tag" style="color:var(--status-emerald);">Crisis & WK Depth</div>
            <div class="tactical-card-title">Anuj Rawat (35.8 HP Avg)</div>
            <div class="tactical-card-desc">
              Highest crisis batting average in the domestic pool (+47.9 SR boost). Essential domestic wicketkeeping backup for Sanju Samson.
            </div>
          </div>
        </div>

      </div>

      <!-- ==================== TAB 2: BOWLERS ==================== -->
      <div id="tab-bowlers" style="display:none;">
        
        <div class="table-toolbar">
          <div class="toolbar-left">
            <span class="toolbar-title">Top 10 Uncapped Bowlers Available in Auction</span>
            <div class="filter-pills">
              <button class="pill-btn active" onclick="filterBowlers('all', this)">All</button>
              <button class="pill-btn" onclick="filterBowlers('pace', this)">Pace</button>
              <button class="pill-btn" onclick="filterBowlers('spin', this)">Spin</button>
              <button class="pill-btn" onclick="filterBowlers('death', this)">Death Overs</button>
            </div>
          </div>

          <div class="search-control">
            <svg class="search-icon-svg" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
            <input type="text" id="bowlersSearch" class="search-input" placeholder="Search bowler..." oninput="handleBowlerSearch()">
          </div>
        </div>

        <div class="table-card">
          <div style="overflow-x:auto;">
            <table class="roster-table">
              <thead>
                <tr>
                  <th class="tac" style="width:52px;">Rank</th>
                  <th>Player & Bowling Style</th>
                  <th class="tar">HP Balls</th>
                  <th class="tar">HP Economy</th>
                  <th class="tar">Base Econ</th>
                  <th class="tar">Econ Diff (&Delta;)</th>
                  <th class="tar">HP Strike Rate</th>
                  <th class="tar">Crunch Wkts</th>
                  <th class="tar">Dot Ball %</th>
                  <th class="tar">Composite CBR</th>
                  <th>Rajasthan Royals Tactical Fit</th>
                  <th class="tac" style="width:75px;">Profile</th>
                </tr>
              </thead>
              <tbody id="bowlersTableBody">
                <!-- Injected via JS -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Tactical Strategy Cards -->
        <div class="tactical-strip">
          <div class="tactical-card green-top">
            <div class="tactical-card-tag" style="color:var(--status-emerald);">Death Economy Leader</div>
            <div class="tactical-card-title">Sakib Hussain (8.39 HP Econ)</div>
            <div class="tactical-card-desc">
              Concedes 1.75 RPO less than his base economy under heat. Restricts boundary concession to 15.4% at an auction estimate &lt; ₹1.5 Cr.
            </div>
          </div>

          <div class="tactical-card highlight">
            <div class="tactical-card-tag">Strike Wickets</div>
            <div class="tactical-card-title">Rasikh Salam (26 Pressure Wkts)</div>
            <div class="tactical-card-desc">
              Captures wickets every 9.08 balls in the death overs. Nailing reverse-swing yorkers and off-cutters to partner Sandeep Sharma.
            </div>
          </div>

          <div class="tactical-card gold-top">
            <div class="tactical-card-tag" style="color:var(--rr-gold-600);">SMS Stadium Squeeze</div>
            <div class="tactical-card-title">Suyash Sharma (37.5% Dot Balls)</div>
            <div class="tactical-card-desc">
              Tosses 95+ kph googlies into Jaipur's 75m ropes where miscues land safely inside. Maintains a tight 8.42 HP economy.
            </div>
          </div>
        </div>

      </div>

      <!-- ==================== TAB 3: VENUE MATRIX ==================== -->
      <div id="tab-venue" style="display:none;">
        
        <div class="venue-panel">
          <div class="venue-head">
            <h2 class="venue-title">Sawai Mansingh Stadium (Jaipur) Ground Analytics</h2>
            <p class="venue-subtitle">
              Unlike flat, compact tracks, Jaipur features <b>75m+ square boundaries</b> and noticeable surface friction.
              Flat-track sluggers falter here, while high-trajectory hitters and quick wrist-spinners dominate.
            </p>
          </div>

          <div class="venue-split">
            
            <div class="venue-column">
              <div class="venue-column-header">
                <svg class="svg-icon" style="stroke:var(--rr-pink-500);" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
                <span>Batting Blueprint for Jaipur</span>
              </div>
              <div class="venue-point">
                &bull; <b>High Ball-Exit Velocity:</b> Ashutosh Sharma and Shahrukh Khan generate pure bat-speed to clear 75m ropes without relying on thin edges.
              </div>
              <div class="venue-point">
                &bull; <b>High Launch-Angle Spin Hitting:</b> Sameer Rizvi (182.7 HP SR) hits with steep trajectory over long-on, bypassing boundary riders.
              </div>
              <div class="venue-point">
                &bull; <b>Low-Dot Strike Rotation:</b> Angkrish Raghuvanshi (26.6% dot rate) takes hard doubles in the spacious outfield when boundaries dry up.
              </div>
            </div>

            <div class="venue-column">
              <div class="venue-column-header">
                <svg class="svg-icon" style="stroke:var(--status-emerald);" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
                <span>Bowling Blueprint for Jaipur</span>
              </div>
              <div class="venue-point">
                &bull; <b>Flat 95–102 kph Wrist-Spin:</b> Suyash Sharma (8.42 HP Econ, 37.5% Dots) uses quick googlies where mistimed shots fall short of 75m ropes.
              </div>
              <div class="venue-point">
                &bull; <b>Steep Left-Arm Friction:</b> Gurjapneet Singh extracts heavy bounce off the Jaipur clay, conceding only 13.3% boundaries.
              </div>
              <div class="venue-point">
                &bull; <b>Sandeep Sharma Yorker Support:</b> Sakib Hussain and Rasikh Salam provide domestic death execution, saving purse for marquee overseas stars.
              </div>
            </div>

          </div>
        </div>

      </div>

      <!-- ==================== TAB 4: PURSE SIMULATOR ==================== -->
      <div id="tab-simulator" style="display:none;">
        
        <div class="simulator-container">
          <div style="border-bottom:2px solid var(--border-pink); padding-bottom:16px; margin-bottom:18px;">
            <h2 class="venue-title">Auction Purse Allocator</h2>
            <p class="venue-subtitle">Select targeted uncapped assets to model purse depletion and projected squad pressure resistance.</p>
          </div>

          <div class="sim-layout">
            
            <div>
              <div style="font-size:11.5px; font-weight:800; text-transform:uppercase; color:var(--text-muted); margin-bottom:12px; display:flex; justify-content:space-between;">
                <span>Uncapped Target Pool</span>
                <span>Estimated Valuation</span>
              </div>
              <div id="simTargetsList">
                <!-- Injected via JS -->
              </div>
            </div>

            <div class="sim-summary-panel">
              <div>
                <div style="font-size:13px; font-weight:800; text-transform:uppercase; color:var(--rr-pink-500); margin-bottom:16px;">
                  Simulated Roster Projection
                </div>

                <div class="sim-metric-row">
                  <span style="color:var(--text-body); font-weight:600;">Assets Selected:</span>
                  <span id="simCount" class="num" style="font-weight:800; color:var(--rr-navy-900);">3 Players</span>
                </div>
                <div class="sim-metric-row">
                  <span style="color:var(--text-body); font-weight:600;">Simulated Spend:</span>
                  <span id="simSpend" class="num" style="font-weight:800; color:var(--rr-pink-500);">₹11.00 Cr</span>
                </div>
                <div class="sim-metric-row">
                  <span style="color:var(--text-body); font-weight:600;">Remaining Purse:</span>
                  <span id="simRemaining" class="num" style="font-weight:800; color:var(--status-emerald);">₹33.50 Cr</span>
                </div>
                <div class="sim-metric-row">
                  <span style="color:var(--text-body); font-weight:600;">Squad Composite CBR:</span>
                  <span id="simAvgCbr" class="num" style="font-weight:800; color:var(--rr-navy-900);">60.5 / 100</span>
                </div>
                <div class="sim-metric-row" style="border-bottom:none;">
                  <span style="color:var(--text-body); font-weight:600;">Death Economy Index:</span>
                  <span class="num" style="font-weight:800; color:var(--status-emerald);">8.40 RPO (Elite)</span>
                </div>
              </div>

              <div style="background:var(--bg-white); border:1px solid var(--border-pink); border-radius:6px; padding:14px; margin-top:20px; font-size:12px; color:var(--text-body); line-height:1.5;">
                <b style="color:var(--rr-navy-900);">War Room Strategy:</b> Acquiring Ashutosh Sharma (₹4.5Cr) + Sakib Hussain (₹1.5Cr) + Suyash Sharma (₹2.0Cr) locks in 3 high-leverage roles for ₹8.0Cr total, preserving ₹36.50Cr for premier marquee bids.
              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </main>

  <!-- ==================== PLAYER SCOUTING MODAL ==================== -->
  <div class="modal-backdrop" id="playerModal" onclick="handleModalBackdrop(event)">
    <div class="modal-dialog">
      
      <div class="modal-header">
        <div>
          <div style="font-size:11px; font-weight:800; color:var(--rr-pink-500); text-transform:uppercase; letter-spacing:0.04em;" id="modalCategory">
            Uncapped Domestic Batter
          </div>
          <h3 style="font-size:22px; font-weight:800; color:var(--rr-navy-900); margin-top:2px;" id="modalName">
            Ashutosh Sharma
          </h3>
          <div style="font-size:12px; color:var(--text-muted); font-weight:600;" id="modalRole">
            Primary #6/#7 Death Finisher
          </div>
        </div>
        <button onclick="closeModal()" style="background:transparent; border:none; color:var(--text-muted); font-size:26px; cursor:pointer; padding:4px;">&times;</button>
      </div>

      <div class="modal-body">
        
        <div class="modal-grid-3" id="modalStatsGrid">
          <!-- Dynamically populated -->
        </div>

        <div class="modal-scouting-box">
          <div style="font-size:11px; font-weight:800; text-transform:uppercase; color:var(--rr-navy-900); margin-bottom:6px;">
            Tactical Scouting Dossier
          </div>
          <div style="font-size:12.5px; color:var(--text-body); line-height:1.55;" id="modalScouting">
            Scouting analysis text...
          </div>
        </div>

        <div style="background:#F8FAFC; border:1px solid var(--border-slate); border-radius:6px; padding:12px 16px; display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:12px; font-weight:600; color:var(--text-muted);">Projected Auction Hammer:</span>
          <span id="modalValuation" class="num" style="font-size:15px; font-weight:800; color:var(--status-emerald);">₹3.50 – ₹5.50 Cr</span>
        </div>

      </div>

      <div class="modal-footer">
        <button onclick="closeModal()" class="btn btn-secondary">Close</button>
      </div>

    </div>
  </div>

  <!-- ==================== CLEAN FOOTER ==================== -->
  <footer>
    <div class="app-container footer-bar">
      <div>Rajasthan Royals Cricket Limited &bull; Strategy & Analytics Operations</div>
      <div class="num">IPL 2027 Auction Target Board &bull; Non-Retained Pool</div>
    </div>
  </footer>

  <!-- ==================== APPLICATION SCRIPTS ==================== -->
  <script>
    const BATTERS = [
      {{
        rank: 1,
        name: "Ashutosh Sharma",
        role: "Primary #6/#7 Death Finisher",
        filter: "finisher",
        balls: 262,
        hp_sr: 186.6,
        base_sr: 103.5,
        elevation: 83.1,
        avg: 25.7,
        bnd_pct: 27.1,
        repeat: 46.2,
        cbr: 63.71,
        fit: "Directly solves death-over finishing void (+83.1 SR jump)",
        valuation: "₹3.50 – ₹5.50 Cr",
        scouting: "Demonstrated unmatched clutch composure in near-impossible run chases (61 off 28 vs MI, 31* off 17 vs GT). Strikes at 186.6 under high heat with zero lag. Direct answer to Rajasthan Royals' lower-order finishing void."
      }},
      {{
        rank: 2,
        name: "Sameer Rizvi",
        role: "Middle-Overs Spin Enforcer",
        filter: "spin",
        balls: 75,
        hp_sr: 182.7,
        base_sr: 131.7,
        elevation: 51.0,
        avg: 22.8,
        bnd_pct: 25.3,
        repeat: 50.0,
        cbr: 60.94,
        fit: "High arc swing clears Jaipur’s 75m square boundaries effortlessly",
        valuation: "₹2.50 – ₹4.00 Cr",
        scouting: "Elite power striker against spin bowling. Features a high launch-angle swing specifically suited for clearing Sawai Mansingh Stadium’s 75m square ropes without getting caught. 50% match repeatability in crunch moments."
      }},
      {{
        rank: 3,
        name: "Aniket Verma",
        role: "Dynamic Impact Sub Accelerator",
        filter: "finisher",
        balls: 84,
        hp_sr: 190.5,
        base_sr: 138.4,
        elevation: 52.1,
        avg: 17.8,
        bnd_pct: 27.4,
        repeat: 25.0,
        cbr: 58.35,
        fit: "Highest raw strike rate in domestic pool; explosive Impact Player",
        valuation: "₹0.80 – ₹1.80 Cr",
        scouting: "Highest raw strike rate under heat (190.5 HP SR) among all uncapped domestic batters. Scores 27.4% of his balls as boundaries and attacks immediately from delivery one."
      }},
      {{
        rank: 4,
        name: "Nehal Wadhera",
        role: "Left-Hand Middle Anchor",
        filter: "spin",
        balls: 174,
        hp_sr: 170.7,
        base_sr: 121.3,
        elevation: 49.4,
        avg: 17.5,
        bnd_pct: 25.3,
        repeat: 31.6,
        cbr: 54.29,
        fit: "Left-handed presence countering finger/wrist spin through overs 11–16",
        valuation: "₹2.00 – ₹3.50 Cr",
        scouting: "Proven big-stage performer with IPL pressure knocks for Mumbai Indians. Provides essential left-handed balance against right-arm leg-spin and rebuilds following early wickets."
      }},
      {{
        rank: 5,
        name: "Anuj Rawat",
        role: "Crisis Rebuilder & Backup WK",
        filter: "keeper",
        balls: 96,
        hp_sr: 149.0,
        base_sr: 101.1,
        elevation: 47.9,
        avg: 35.8,
        bnd_pct: 19.8,
        repeat: 40.0,
        cbr: 53.83,
        fit: "Crisis stabilizer (35.8 Avg) + domestic wicketkeeper redundancy",
        valuation: "₹1.50 – ₹2.50 Cr",
        scouting: "Highest crisis batting average (35.8) in the uncapped bracket. Shows supreme calm when wickets fall early, with a +47.9 SR boost when the chase tightens. Key backup wicketkeeper."
      }},
      {{
        rank: 6,
        name: "Mukul Choudhary",
        role: "High-Ceiling Power Striker",
        filter: "finisher",
        balls: 74,
        hp_sr: 158.1,
        base_sr: 115.2,
        elevation: 42.9,
        avg: 23.4,
        bnd_pct: 20.3,
        repeat: 57.1,
        cbr: 52.19,
        fit: "Developmental power asset with 57.1% consistency at bargain price",
        valuation: "₹0.50 – ₹1.20 Cr",
        scouting: "High consistency rate (57.1%) in late overs. Powerful domestic striker ready for development inside RR's high-performance academy."
      }},
      {{
        rank: 7,
        name: "Mahipal Lomror",
        role: "Jaipur Home Venue Specialist",
        filter: "spin",
        balls: 115,
        hp_sr: 166.1,
        base_sr: 144.9,
        elevation: 21.2,
        avg: 13.6,
        bnd_pct: 24.3,
        repeat: 41.2,
        cbr: 51.81,
        fit: "Jaipur local with deep familiarity with SMS Stadium pitch nuances",
        valuation: "₹1.00 – ₹2.20 Cr",
        scouting: "Rajasthan native with intimate familiarity with Jaipur’s Sawai Mansingh Stadium pitch quirks. Strikes at 166.1 under pressure with reliable left-arm batting utility."
      }},
      {{
        rank: 8,
        name: "M Shahrukh Khan",
        role: "High-Pace Muscle Hitter",
        filter: "finisher",
        balls: 211,
        hp_sr: 168.2,
        base_sr: 134.2,
        elevation: 34.1,
        avg: 18.7,
        bnd_pct: 21.3,
        repeat: 18.8,
        cbr: 51.48,
        fit: "Physical specimen tailored for clearing flat boundaries off 145+ kph pace",
        valuation: "₹1.50 – ₹3.00 Cr",
        scouting: "Physical muscle power specifically suited for clearing flat boundaries off 145+ kph fast bowling. When yorkers miss by an inch, Shahrukh punishes over long-on."
      }},
      {{
        rank: 9,
        name: "Shubham Dubey",
        role: "Left-Hand Lower-Order Striker",
        filter: "finisher",
        balls: 113,
        hp_sr: 160.2,
        base_sr: 130.0,
        elevation: 30.2,
        avg: 18.1,
        bnd_pct: 21.2,
        repeat: 33.3,
        cbr: 50.12,
        fit: "Lower-order boundary option against pacers bowling wide lines",
        valuation: "₹0.80 – ₹1.50 Cr",
        scouting: "Targeted boundary hitter against pacers attempting wide yorkers. Provides valuable left-handed balance alongside Samson and Parag."
      }},
      {{
        rank: 10,
        name: "Angkrish Raghuvanshi",
        role: "Low-Dot Strike Rotator",
        filter: "spin",
        balls: 94,
        hp_sr: 151.1,
        base_sr: 144.6,
        elevation: 6.5,
        avg: 20.3,
        bnd_pct: 20.2,
        repeat: 40.0,
        cbr: 49.03,
        fit: "Minimizes dot-ball pressure (26.6% dots) when early wickets tumble",
        valuation: "₹1.00 – ₹2.00 Cr",
        scouting: "Technically solid top-to-middle order batter who minimizes dot balls (only 26.6% dot ball percentage). Prevents scoreboard pressure from escalating in sticky conditions."
      }}
    ];

    const BOWLERS = [
      {{
        rank: 1,
        name: "Sakib Hussain",
        style: "Right-Arm Pace",
        filter: "pace",
        balls: 108,
        hp_econ: 8.39,
        base_econ: 10.14,
        econ_diff: 1.75,
        hp_sr: 12.0,
        wkts: 9,
        dot_pct: 31.6,
        bnd_conceded: 15.4,
        repeat: 80.0,
        cbr: 61.02,
        fit: "Elite sub-9 death bowler; concedes only 15.4% boundaries in crunch",
        valuation: "₹0.80 – ₹1.80 Cr",
        scouting: "The #1 uncapped bowler under pressure in the entire tournament dataset. While the tournament high-pressure economy average spikes to 9.61 RPO, Sakib drops to an astonishing 8.39 RPO (+1.75 outperformance). Restricts boundaries to just 15.4%. Delivers 80% repeatability."
      }},
      {{
        rank: 2,
        name: "Rasikh Salam",
        style: "Right-Arm Fast-Medium",
        filter: "death",
        balls: 236,
        hp_econ: 9.41,
        base_econ: 9.71,
        econ_diff: 0.30,
        hp_sr: 9.08,
        wkts: 26,
        dot_pct: 31.6,
        bnd_conceded: 18.6,
        repeat: 70.0,
        cbr: 58.86,
        fit: "Premier strike wicket-taker: 26 crunch wickets at 9.08 balls/wkt",
        valuation: "₹2.50 – ₹4.00 Cr",
        scouting: "Extremely rare strike weapon at the death. Captured 26 wickets under intense pressure with a strike rate of 9.08 balls per wicket. Uses late tailing reverse swing and off-cutters to break set partnerships in overs 18 & 20."
      }},
      {{
        rank: 3,
        name: "Gurjapneet Singh",
        style: "Left-Arm Fast-Medium",
        filter: "pace",
        balls: 85,
        hp_econ: 8.47,
        base_econ: 9.04,
        econ_diff: 0.57,
        hp_sr: 14.2,
        wkts: 6,
        dot_pct: 27.8,
        bnd_conceded: 13.3,
        repeat: 66.7,
        cbr: 57.95,
        fit: "Tall left-arm seam angle; lowest boundary concession rate (13.3%)",
        valuation: "₹0.80 – ₹1.80 Cr",
        scouting: "Tall left-arm seamer creating steep awkward bounce. Boasts the lowest boundary concession rate (13.3%) in the high-pressure bowler pool. Replicates the left-arm angle that Rajasthan has prized since Trent Boult."
      }},
      {{
        rank: 4,
        name: "Anshul Kamboj",
        style: "Right-Arm Fast",
        filter: "pace",
        balls: 123,
        hp_econ: 9.85,
        base_econ: 10.01,
        econ_diff: 0.16,
        hp_sr: 9.46,
        wkts: 13,
        dot_pct: 36.2,
        bnd_conceded: 21.5,
        repeat: 53.8,
        cbr: 57.02,
        fit: "Hit-the-deck pace enforcer; 9.46 strike rate and 36.2% dot balls",
        valuation: "₹1.50 – ₹2.80 Cr",
        scouting: "Pounds hard lengths into the turf. Generates an elite 36.2% dot ball rate and strikes every 9.46 balls in crunch situations. Unafraid to bowl to elite international finishers."
      }},
      {{
        rank: 5,
        name: "Suyash Sharma",
        style: "Right-Arm Leg-Spin / Googly",
        filter: "spin",
        balls: 258,
        hp_econ: 8.42,
        base_econ: 8.76,
        econ_diff: 0.34,
        hp_sr: 21.5,
        wkts: 12,
        dot_pct: 37.5,
        bnd_conceded: 16.2,
        repeat: 50.0,
        cbr: 56.93,
        fit: "Jaipur 75m spin squeeze: 8.42 HP Econ & 37.5% dot ball rate",
        valuation: "₹1.50 – ₹3.00 Cr",
        scouting: "Custom-built for Jaipur's Sawai Mansingh Stadium. 75m square boundaries allow Suyash to toss the ball up with quick googlies (8.42 HP Econ, 37.5% Dots) without fear of mishits flying for six. Elite middle-over control."
      }},
      {{
        rank: 6,
        name: "Ashwani Kumar",
        style: "Right-Arm Fast",
        filter: "death",
        balls: 79,
        hp_econ: 11.01,
        base_econ: 10.74,
        econ_diff: -0.27,
        hp_sr: 8.78,
        wkts: 9,
        dot_pct: 36.8,
        bnd_conceded: 25.3,
        repeat: 85.7,
        cbr: 55.68,
        fit: "Express pace strike threat (8.78 HP SR); 85.7% consistency",
        valuation: "₹0.80 – ₹1.60 Cr",
        scouting: "Brilliant strike rate of 8.78 balls/wicket with remarkable 85.7% outing repeatability. High arm speed that hurries batters in the death overs."
      }},
      {{
        rank: 7,
        name: "Praful Hinge",
        style: "Right-Arm Medium-Fast",
        filter: "death",
        balls: 61,
        hp_econ: 10.82,
        base_econ: 11.76,
        econ_diff: 0.94,
        hp_sr: 12.2,
        wkts: 5,
        dot_pct: 38.5,
        bnd_conceded: 24.6,
        repeat: 85.7,
        cbr: 54.71,
        fit: "Death overs dot-ball machine: 38.5% dots across 85.7% of matches",
        valuation: "₹0.40 – ₹1.00 Cr",
        scouting: "Produces an immense 38.5% dot ball percentage in late overs across 85.7% of his match appearances. Outperforms his baseline economy by nearly a full run (+0.94)."
      }},
      {{
        rank: 8,
        name: "Brijesh Sharma",
        style: "Right-Arm Seam",
        filter: "pace",
        balls: 110,
        hp_econ: 9.27,
        base_econ: 9.92,
        econ_diff: 0.64,
        hp_sr: 15.7,
        wkts: 7,
        dot_pct: 30.3,
        bnd_conceded: 18.5,
        repeat: 36.4,
        cbr: 53.25,
        fit: "Second-innings squeeze seamer; disciplined 9.27 HP economy",
        valuation: "₹0.40 – ₹0.90 Cr",
        scouting: "Maintains a disciplined 9.27 HP economy (+0.64 diff). Excellent off-stump channel control during tough chases."
      }},
      {{
        rank: 9,
        name: "Harpreet Brar",
        style: "Slow Left-Arm Orthodox",
        filter: "spin",
        balls: 73,
        hp_econ: 10.11,
        base_econ: 8.02,
        econ_diff: -2.09,
        hp_sr: 14.6,
        wkts: 5,
        dot_pct: 35.5,
        bnd_conceded: 22.4,
        repeat: 40.0,
        cbr: 50.89,
        fit: "Flat dart specialist against right-handed power hitters (35.5% dots)",
        valuation: "₹1.20 – ₹2.50 Cr",
        scouting: "Skids the ball into the stumps at 95+ kph. Match-up weapon against right-handed power hitters with 35.5% dot ball rate."
      }},
      {{
        rank: 10,
        name: "Akash Madhwal",
        style: "Right-Arm Fast-Medium",
        filter: "death",
        balls: 146,
        hp_econ: 10.64,
        base_econ: 9.57,
        econ_diff: -1.08,
        hp_sr: 13.3,
        wkts: 11,
        dot_pct: 28.8,
        bnd_conceded: 20.9,
        repeat: 50.0,
        cbr: 49.96,
        fit: "Blockhole yorker specialist with proven IPL playoff experience",
        valuation: "₹1.00 – ₹2.00 Cr",
        scouting: "Proven playoff hero (5/5 vs LSG for MI). High round-arm release angle makes his yorkers notoriously hard to get under at the death."
      }}
    ];

    const SIM_ASSETS = [
      {{ id: 1, name: "Ashutosh Sharma", type: "Batter", cost: 4.5, cbr: 63.71, selected: true }},
      {{ id: 2, name: "Sakib Hussain", type: "Bowler", cost: 1.5, cbr: 61.02, selected: true }},
      {{ id: 3, name: "Sameer Rizvi", type: "Batter", cost: 3.0, cbr: 60.94, selected: false }},
      {{ id: 4, name: "Rasikh Salam", type: "Bowler", cost: 3.5, cbr: 58.86, selected: false }},
      {{ id: 5, name: "Aniket Verma", type: "Batter", cost: 1.2, cbr: 58.35, selected: false }},
      {{ id: 6, name: "Gurjapneet Singh", type: "Bowler", cost: 1.2, cbr: 57.95, selected: false }},
      {{ id: 7, name: "Suyash Sharma", type: "Bowler", cost: 2.0, cbr: 56.93, selected: true }},
      {{ id: 8, name: "Anuj Rawat", type: "Batter", cost: 2.0, cbr: 53.83, selected: false }}
    ];

    let currentBatterFilter = 'all';
    let currentBowlerFilter = 'all';

    function renderBattersTable(list) {{
      const tbody = document.getElementById('battersTableBody');
      tbody.innerHTML = '';
      list.forEach(p => {{
        const tr = document.createElement('tr');
        tr.onclick = (e) => {{
          if (!e.target.closest('button')) openModal(p, 'batter');
        }};

        const rankClass = p.rank === 1 ? 'rank-top1' : (p.rank === 2 ? 'rank-top2' : (p.rank === 3 ? 'rank-top3' : 'rank-standard'));

        tr.innerHTML = `
          <td class="rank-cell"><span class="rank-num ${{rankClass}}">${{p.rank}}</span></td>
          <td>
            <div class="player-title">${{p.name}}</div>
            <div class="player-subtitle">${{p.role}}</div>
          </td>
          <td class="tar num">${{p.balls}}</td>
          <td class="tar num metric-primary">${{p.hp_sr.toFixed(1)}}</td>
          <td class="tar num" style="color:var(--text-muted);">${{p.base_sr.toFixed(1)}}</td>
          <td class="tar num"><span class="metric-elevation-pos">+${{p.elevation.toFixed(1)}}</span></td>
          <td class="tar num" style="color:var(--rr-navy-900); font-weight:800;">${{p.avg.toFixed(1)}}</td>
          <td class="tar num">${{p.bnd_pct.toFixed(1)}}%</td>
          <td class="tar num">${{p.repeat.toFixed(0)}}%</td>
          <td class="tar num"><span class="rating-badge">${{p.cbr.toFixed(1)}}</span></td>
          <td class="tactical-role-text">${{p.fit}}</td>
          <td class="tac">
            <button class="btn-inspect" onclick="openModal(${{JSON.stringify(p).replace(/"/g, '&quot;')}}, 'batter')">
              <span>View</span>
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function renderBowlersTable(list) {{
      const tbody = document.getElementById('bowlersTableBody');
      tbody.innerHTML = '';
      list.forEach(p => {{
        const tr = document.createElement('tr');
        tr.onclick = (e) => {{
          if (!e.target.closest('button')) openModal(p, 'bowler');
        }};

        const rankClass = p.rank === 1 ? 'rank-top1' : (p.rank === 2 ? 'rank-top2' : (p.rank === 3 ? 'rank-top3' : 'rank-standard'));
        const diffSign = p.econ_diff > 0 ? '+' : '';
        const diffClass = p.econ_diff > 0 ? 'metric-econ-pos' : 'metric-econ-neg';

        tr.innerHTML = `
          <td class="rank-cell"><span class="rank-num ${{rankClass}}">${{p.rank}}</span></td>
          <td>
            <div class="player-title">${{p.name}}</div>
            <div class="player-subtitle">${{p.style}}</div>
          </td>
          <td class="tar num">${{p.balls}}</td>
          <td class="tar num metric-primary">${{p.hp_econ.toFixed(2)}}</td>
          <td class="tar num" style="color:var(--text-muted);">${{p.base_econ.toFixed(2)}}</td>
          <td class="tar num"><span class="${{diffClass}}">${{diffSign}}${{p.econ_diff.toFixed(2)}}</span></td>
          <td class="tar num" style="color:var(--rr-navy-900); font-weight:800;">${{p.hp_sr.toFixed(1)}}</td>
          <td class="tar num metric-primary">${{p.wkts}}</td>
          <td class="tar num">${{p.dot_pct.toFixed(1)}}%</td>
          <td class="tar num"><span class="rating-badge">${{p.cbr.toFixed(1)}}</span></td>
          <td class="tactical-role-text">${{p.fit}}</td>
          <td class="tac">
            <button class="btn-inspect" onclick="openModal(${{JSON.stringify(p).replace(/"/g, '&quot;')}}, 'bowler')">
              <span>View</span>
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function switchTab(tabId, el) {{
      document.querySelectorAll('.nav-tab-btn').forEach(b => b.classList.remove('active'));
      el.classList.add('active');

      document.getElementById('tab-batters').style.display = tabId === 'batters' ? 'block' : 'none';
      document.getElementById('tab-bowlers').style.display = tabId === 'bowlers' ? 'block' : 'none';
      document.getElementById('tab-venue').style.display = tabId === 'venue' ? 'block' : 'none';
      document.getElementById('tab-simulator').style.display = tabId === 'simulator' ? 'block' : 'none';
    }}

    function filterBatters(filter, btn) {{
      currentBatterFilter = filter;
      btn.parentElement.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      handleBatterSearch();
    }}

    function filterBowlers(filter, btn) {{
      currentBowlerFilter = filter;
      btn.parentElement.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      handleBowlerSearch();
    }}

    function handleBatterSearch() {{
      const q = document.getElementById('battersSearch').value.toLowerCase();
      const filtered = BATTERS.filter(b => {{
        const matchesFilter = currentBatterFilter === 'all' || b.filter === currentBatterFilter;
        const matchesQuery = b.name.toLowerCase().includes(q) || b.role.toLowerCase().includes(q);
        return matchesFilter && matchesQuery;
      }});
      renderBattersTable(filtered);
    }}

    function handleBowlerSearch() {{
      const q = document.getElementById('bowlersSearch').value.toLowerCase();
      const filtered = BOWLERS.filter(b => {{
        const matchesFilter = currentBowlerFilter === 'all' || b.filter === currentBowlerFilter;
        const matchesQuery = b.name.toLowerCase().includes(q) || b.style.toLowerCase().includes(q);
        return matchesFilter && matchesQuery;
      }});
      renderBowlersTable(filtered);
    }}

    function openModal(p, type) {{
      const isBatter = type === 'batter';
      document.getElementById('modalCategory').innerText = isBatter ? 'Uncapped Domestic Batter' : 'Uncapped Domestic Bowler';
      document.getElementById('modalName').innerText = p.name;
      document.getElementById('modalRole').innerText = isBatter ? p.role : `${{p.style}} &bull; ${{p.fit}}`;
      document.getElementById('modalScouting').innerText = p.scouting;
      document.getElementById('modalValuation').innerText = p.valuation;

      const grid = document.getElementById('modalStatsGrid');
      if (isBatter) {{
        grid.innerHTML = `
          <div class="modal-stat-box">
            <div style="font-size:10.5px; color:var(--text-muted); text-transform:uppercase; font-weight:800;">HP Strike Rate</div>
            <div class="num" style="font-size:20px; font-weight:800; color:var(--rr-navy-900); margin-top:2px;">${{p.hp_sr.toFixed(1)}}</div>
            <div class="num" style="font-size:11px; color:var(--rr-pink-500); font-weight:800;">+${{p.elevation.toFixed(1)}} &Delta;SR</div>
          </div>
          <div class="modal-stat-box">
            <div style="font-size:10.5px; color:var(--text-muted); text-transform:uppercase; font-weight:800;">HP Average</div>
            <div class="num" style="font-size:20px; font-weight:800; color:var(--rr-navy-900); margin-top:2px;">${{p.avg.toFixed(1)}}</div>
            <div class="num" style="font-size:11px; color:var(--text-muted); font-weight:600;">${{p.bnd_pct.toFixed(1)}}% Boundary</div>
          </div>
          <div class="modal-stat-box">
            <div style="font-size:10.5px; color:var(--text-muted); text-transform:uppercase; font-weight:800;">Composite CBR</div>
            <div class="num" style="font-size:20px; font-weight:800; color:var(--status-emerald); margin-top:2px;">${{p.cbr.toFixed(1)}}</div>
            <div class="num" style="font-size:11px; color:var(--text-muted); font-weight:600;">${{p.repeat.toFixed(0)}}% Repeat</div>
          </div>
        `;
      }} else {{
        const diffSign = p.econ_diff > 0 ? '+' : '';
        const diffColor = p.econ_diff > 0 ? 'var(--status-emerald)' : 'var(--rr-pink-500)';
        grid.innerHTML = `
          <div class="modal-stat-box">
            <div style="font-size:10.5px; color:var(--text-muted); text-transform:uppercase; font-weight:800;">HP Economy</div>
            <div class="num" style="font-size:20px; font-weight:800; color:var(--rr-navy-900); margin-top:2px;">${{p.hp_econ.toFixed(2)}}</div>
            <div class="num" style="font-size:11px; color:${{diffColor}}; font-weight:800;">${{diffSign}}${{p.econ_diff.toFixed(2)}} vs Base</div>
          </div>
          <div class="modal-stat-box">
            <div style="font-size:10.5px; color:var(--text-muted); text-transform:uppercase; font-weight:800;">HP Strike Rate</div>
            <div class="num" style="font-size:20px; font-weight:800; color:var(--rr-navy-900); margin-top:2px;">${{p.hp_sr.toFixed(1)}}</div>
            <div class="num" style="font-size:11px; color:var(--text-muted); font-weight:600;">${{p.wkts}} Wickets</div>
          </div>
          <div class="modal-stat-box">
            <div style="font-size:10.5px; color:var(--text-muted); text-transform:uppercase; font-weight:800;">Composite CBR</div>
            <div class="num" style="font-size:20px; font-weight:800; color:var(--status-emerald); margin-top:2px;">${{p.cbr.toFixed(1)}}</div>
            <div class="num" style="font-size:11px; color:var(--text-muted); font-weight:600;">${{p.dot_pct.toFixed(1)}}% Dots</div>
          </div>
        `;
      }}

      document.getElementById('playerModal').classList.add('active');
    }}

    function closeModal() {{
      document.getElementById('playerModal').classList.remove('active');
    }}

    function handleModalBackdrop(e) {{
      if (e.target.id === 'playerModal') closeModal();
    }}

    function renderSimulator() {{
      const container = document.getElementById('simTargetsList');
      container.innerHTML = '';
      SIM_ASSETS.forEach(t => {{
        const div = document.createElement('div');
        div.className = `sim-row ${{t.selected ? 'active' : ''}}`;
        div.onclick = () => {{
          t.selected = !t.selected;
          renderSimulator();
          updateSim();
        }};

        div.innerHTML = `
          <div style="display:flex; align-items:center; gap:12px;">
            <input type="checkbox" ${{t.selected ? 'checked' : ''}} class="sim-checkbox">
            <div>
              <div style="font-weight:800; color:var(--rr-navy-900); font-size:13.5px;">${{t.name}}</div>
              <div style="font-size:11.5px; color:var(--text-muted); font-weight:500;">${{t.type}} &bull; CBR ${{t.cbr.toFixed(1)}}</div>
            </div>
          </div>
          <div class="num" style="font-weight:800; font-size:13.5px; color:${{t.selected ? 'var(--rr-pink-500)' : 'var(--text-muted)'}};">
            ₹${{t.cost.toFixed(2)}} Cr
          </div>
        `;
        container.appendChild(div);
      }});
      updateSim();
    }}

    function updateSim() {{
      const picked = SIM_ASSETS.filter(t => t.selected);
      const total = picked.reduce((acc, t) => acc + t.cost, 0);
      const remaining = 44.50 - total;
      const avgCbr = picked.length > 0 ? (picked.reduce((acc, t) => acc + t.cbr, 0) / picked.length) : 0;

      document.getElementById('simCount').innerText = `${{picked.length}} Players`;
      document.getElementById('simSpend').innerText = `₹${{total.toFixed(2)}} Cr`;
      document.getElementById('simRemaining').innerText = `₹${{remaining.toFixed(2)}} Cr`;
      document.getElementById('simAvgCbr').innerText = `${{avgCbr.toFixed(1)}} / 100`;
    }}

    function exportCSV() {{
      let csv = "Department,Rank,Player,Metric_1,Metric_2,Elevation,Average_or_Wkts,CBR_Score,Tactical_Role\\n";
      BATTERS.forEach(b => {{
        csv += `Batter,${{b.rank}},"${{b.name}}",HP_SR:${{b.hp_sr}},Base_SR:${{b.base_sr}},+${{b.elevation}},${{b.avg}},${{b.cbr}},"${{b.role}}"\\n`;
      }});
      BOWLERS.forEach(b => {{
        csv += `Bowler,${{b.rank}},"${{b.name}}",HP_Econ:${{b.hp_econ}},Base_Econ:${{b.base_econ}},${{b.econ_diff}},${{b.wkts}},${{b.cbr}},"${{b.style}}"\\n`;
      }});

      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = "Rajasthan_Royals_Uncapped_Auction_Targets_2027.csv";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      renderBattersTable(BATTERS);
      renderBowlersTable(BOWLERS);
      renderSimulator();
    }});
  </script>
</body>
</html>
"""

output_path = '/Users/jainil.30/Downloads/RR/rr_pressure_war_room_dashboard.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated White & Pink dashboard successfully at:', output_path)
