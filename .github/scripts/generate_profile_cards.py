import os

def render_header_card():
    width = 780
    height = 142
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="header-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="50%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>

    <!-- Border Gradient -->
    <linearGradient id="header-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00EA64" stop-opacity="0.5" />
      <stop offset="40%" stop-color="#38BDF8" stop-opacity="0.3" />
      <stop offset="80%" stop-color="#A855F7" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>

    <!-- Name Title Gradient -->
    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00EA64" />
      <stop offset="60%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-header" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="3" flood-color="#00EA64" flood-opacity="0.45"/>
    </filter>
  </defs>

  <!-- Card Background -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#header-bg)" stroke="url(#header-border)" stroke-width="1.2" />

  <!-- Ambient Light Corner Glows -->
  <circle cx="40" cy="40" r="90" fill="#00EA64" opacity="0.04" />
  <circle cx="{width - 40}" cy="40" r="90" fill="#38BDF8" opacity="0.04" />

  <!-- Status Pill Badge -->
  <g transform="translate(32, 22)">
    <rect x="0" y="0" width="350" height="20" rx="10" fill="#00EA64" fill-opacity="0.08" stroke="#00EA64" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="10" cy="10" r="3" fill="#00EA64" filter="url(#glow-header)"/>
    <text x="19" y="13.5" fill="#00EA64" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="700" letter-spacing="0.4px">
      OPEN FOR PFE / DATA SCIENCE &amp; AI INTERNSHIPS
    </text>
  </g>

  <!-- Location Badge (Top Right) -->
  <g transform="translate({width - 32 - 140}, 22)">
    <rect x="0" y="0" width="140" height="20" rx="10" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="0.8"/>
    <circle cx="12" cy="10" r="2.5" fill="#38BDF8"/>
    <text x="22" y="13.5" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Casablanca, Morocco
    </text>
  </g>

  <!-- Headline: Hi, I'm Badreddine Idrissi Kandri 👋 -->
  <g transform="translate(32, 70)">
    <text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="25" font-weight="800" letter-spacing="-0.5px">
      <tspan fill="#F8FAFC">Hi, I'm </tspan>
      <tspan fill="url(#name-grad)">Badreddine Idrissi Kandri</tspan>
      <tspan fill="#F8FAFC"> 👋</tspan>
    </text>
  </g>

  <!-- Subtitle: Role & School -->
  <g transform="translate(32, 98)">
    <text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600">
      <tspan fill="#E2E8F0">Data Scientist &amp; Ingénieur Data/IA</tspan>
      <tspan fill="#475569"> • </tspan>
      <tspan fill="#94A3B8">ENSA Berrechid (Big Data &amp; Systèmes d'Information)</tspan>
    </text>
  </g>

  <!-- Mission Statement -->
  <g transform="translate(32, 120)">
    <text fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11.5" font-weight="400">
      Engineering autonomous AI agents, scalable industrial ML pipelines, and production data workflows.
    </text>
  </g>
</svg>
'''
    return svg

def render_badge_hackerrank():
    width = 190
    height = 34
    color = "#00EA64"
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-hr" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>
    <filter id="glow-hr" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="{color}" flood-opacity="0.35"/>
    </filter>
  </defs>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#bg-hr)" stroke="{color}" stroke-opacity="0.4" stroke-width="1.2"/>
  <!-- HackerRank Icon -->
  <g transform="translate(14, 9)">
    <path d="M0 2.5L7 0L14 2.5V13.5L7 16L0 13.5V2.5Z" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.2"/>
    <path d="M4.5 5.5V10.5M9.5 5.5V10.5M4.5 8H9.5" stroke="{color}" stroke-width="1.2" stroke-linecap="round"/>
  </g>
  <!-- Text -->
  <g transform="translate(36, 13)">
    <text x="0" y="0" fill="{color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="8.5" font-weight="700" letter-spacing="0.4px">HACKERRANK</text>
    <text x="0" y="12" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="600">badr_kandri_10</text>
  </g>
  <!-- Link Arrow -->
  <g transform="translate({width - 22}, 11)">
    <path d="M1 9L9 1M9 1H3M9 1V7" stroke="#64748B" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>'''
    return svg

def render_badge_linkedin():
    width = 220
    height = 34
    color = "#38BDF8"
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-li" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>
    <filter id="glow-li" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="{color}" flood-opacity="0.35"/>
    </filter>
  </defs>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#bg-li)" stroke="{color}" stroke-opacity="0.4" stroke-width="1.2"/>
  <!-- LinkedIn Icon -->
  <g transform="translate(14, 9)">
    <rect x="0" y="0" width="16" height="16" rx="3.5" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.2"/>
    <text x="8" y="12" text-anchor="middle" fill="{color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="800">in</text>
  </g>
  <!-- Text -->
  <g transform="translate(38, 13)">
    <text x="0" y="0" fill="{color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="8.5" font-weight="700" letter-spacing="0.4px">LINKEDIN</text>
    <text x="0" y="12" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="600">Badreddine Idrissi</text>
  </g>
  <!-- Link Arrow -->
  <g transform="translate({width - 22}, 11)">
    <path d="M1 9L9 1M9 1H3M9 1V7" stroke="#64748B" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>'''
    return svg

def render_badge_gmail():
    width = 215
    height = 34
    color = "#EA4335"
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg-gm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>
    <filter id="glow-gm" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="{color}" flood-opacity="0.35"/>
    </filter>
  </defs>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#bg-gm)" stroke="{color}" stroke-opacity="0.4" stroke-width="1.2"/>
  <!-- Gmail / Mail Icon -->
  <g transform="translate(14, 9)">
    <rect x="0" y="1" width="16" height="14" rx="2.5" fill="{color}" fill-opacity="0.15" stroke="{color}" stroke-width="1.2"/>
    <path d="M1 2L8 8L15 2" stroke="{color}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <!-- Text -->
  <g transform="translate(38, 13)">
    <text x="0" y="0" fill="{color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="8.5" font-weight="700" letter-spacing="0.4px">DIRECT GMAIL</text>
    <text x="0" y="12" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="600">Send Email Now</text>
  </g>
  <!-- Link Arrow -->
  <g transform="translate({width - 22}, 11)">
    <path d="M1 9L9 1M9 1H3M9 1V7" stroke="#64748B" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>'''
    return svg

def render_about_profile_card():
    width = 390
    height = 205
    dom_color = "#38BDF8"  # Blue
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="about-prof-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="50%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>
    <linearGradient id="about-prof-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{dom_color}" stop-opacity="0.45" />
      <stop offset="40%" stop-color="{dom_color}" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>
    <filter id="glow-prof" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="{dom_color}" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="14" fill="url(#about-prof-bg)" stroke="url(#about-prof-border)" stroke-width="1.2" />
  <circle cx="28" cy="28" r="50" fill="{dom_color}" opacity="0.06" />

  <!-- Header -->
  <g transform="translate(18, 16)">
    <!-- Academic Cap Icon -->
    <path d="M2 7L11 2L20 7L11 12L2 7Z" stroke="{dom_color}" stroke-width="1.4" stroke-linejoin="round" fill="{dom_color}" fill-opacity="0.2"/>
    <path d="M5.5 9V14C5.5 16.5 8 18 11 18C14 18 16.5 16.5 16.5 14V9" stroke="{dom_color}" stroke-width="1.3"/>
    <path d="M20 7V13" stroke="{dom_color}" stroke-width="1.2" stroke-linecap="round"/>

    <text x="28" y="14" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="700">
      Academic &amp; Research Focus
    </text>
  </g>

  <!-- Domain Pill -->
  <g transform="translate(18, 40)">
    <rect x="0" y="0" width="132" height="17" rx="8.5" fill="{dom_color}" fill-opacity="0.1" stroke="{dom_color}" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="8" cy="8.5" r="2.5" fill="{dom_color}" filter="url(#glow-prof)"/>
    <text x="16" y="12" fill="{dom_color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="700" letter-spacing="0.3px">
      DATA &amp; AI ENGINEERING
    </text>
  </g>

  <!-- Divider -->
  <line x1="18" y1="67" x2="{width - 18}" y2="67" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1" />

  <!-- Point 1 -->
  <g transform="translate(18, 77)">
    <circle cx="4" cy="9" r="2.5" fill="{dom_color}"/>
    <text x="14" y="9" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">
      5th Year State Engineer
    </text>
    <text x="14" y="23" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="400">
      ENSA Berrechid (Information Systems &amp; Big Data)
    </text>
  </g>

  <!-- Point 2 -->
  <g transform="translate(18, 117)">
    <circle cx="4" cy="9" r="2.5" fill="{dom_color}"/>
    <text x="14" y="9" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">
      Autonomous Agents &amp; RAG
    </text>
    <text x="14" y="23" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="400">
      Multi-agent workflows (LangGraph, Agno) &amp; Qdrant RAG
    </text>
  </g>

  <!-- Point 3 -->
  <g transform="translate(18, 157)">
    <circle cx="4" cy="9" r="2.5" fill="{dom_color}"/>
    <text x="14" y="9" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">
      First-Principles Machine Learning
    </text>
    <text x="14" y="23" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="400">
      Algorithms recreated from scratch using pure vector math
    </text>
  </g>
</svg>
'''
    return svg

def render_about_experience_card():
    width = 390
    height = 205
    dom_color = "#F97316"  # Orange
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="about-exp-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="50%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>
    <linearGradient id="about-exp-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{dom_color}" stop-opacity="0.45" />
      <stop offset="40%" stop-color="{dom_color}" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>
    <filter id="glow-exp" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="{dom_color}" flood-opacity="0.4"/>
    </filter>
  </defs>

  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="14" fill="url(#about-exp-bg)" stroke="url(#about-exp-border)" stroke-width="1.2" />
  <circle cx="28" cy="28" r="50" fill="{dom_color}" opacity="0.06" />

  <!-- Header -->
  <g transform="translate(18, 16)">
    <!-- Briefcase / Industry Icon -->
    <rect x="2" y="5" width="18" height="13" rx="2" stroke="{dom_color}" stroke-width="1.4" fill="{dom_color}" fill-opacity="0.15"/>
    <path d="M7 5V3.5C7 2.67 7.67 2 8.5 2H13.5C14.33 2 15 2.67 15 3.5V5" stroke="{dom_color}" stroke-width="1.3"/>
    <circle cx="11" cy="11.5" r="1.5" fill="{dom_color}"/>

    <text x="28" y="14" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="700">
      Experience &amp; Leadership
    </text>
  </g>

  <!-- Domain Pill -->
  <g transform="translate(18, 40)">
    <rect x="0" y="0" width="138" height="17" rx="8.5" fill="{dom_color}" fill-opacity="0.1" stroke="{dom_color}" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="8" cy="8.5" r="2.5" fill="{dom_color}" filter="url(#glow-exp)"/>
    <text x="16" y="12" fill="{dom_color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="700" letter-spacing="0.3px">
      IMPACT &amp; LEADERSHIP
    </text>
  </g>

  <!-- Divider -->
  <line x1="18" y1="67" x2="{width - 18}" y2="67" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1" />

  <!-- Point 1 -->
  <g transform="translate(18, 77)">
    <circle cx="4" cy="9" r="2.5" fill="{dom_color}"/>
    <text x="14" y="9" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">
      Industrial Predictive Pipelines
    </text>
    <text x="14" y="23" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="400">
      PortNet: +5M national transactions analyzed (R² = 0.93)
    </text>
  </g>

  <!-- Point 2 -->
  <g transform="translate(18, 117)">
    <circle cx="4" cy="9" r="2.5" fill="{dom_color}"/>
    <text x="14" y="9" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">
      Enterprise Internships (SOFAC &amp; Peaqock)
    </text>
    <text x="14" y="23" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="400">
      Fine-tuning Qwen2.5 (PEFT/LoRA) &amp; streaming FastAPI
    </text>
  </g>

  <!-- Point 3 -->
  <g transform="translate(18, 157)">
    <circle cx="4" cy="9" r="2.5" fill="{dom_color}"/>
    <text x="14" y="9" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700">
      Leadership &amp; Competitive Practice
    </text>
    <text x="14" y="23" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="400">
      President Club R-41, VP Lions Club &amp; HackerRank L5
    </text>
  </g>
</svg>
'''
    return svg

def main():
    base_dir = "C:/Users/MELIODAS/.gemini/antigravity/scratch/BadrKandri/assets"
    header_dir = os.path.join(base_dir, "header")
    about_dir = os.path.join(base_dir, "about")
    os.makedirs(header_dir, exist_ok=True)
    os.makedirs(about_dir, exist_ok=True)

    # 1. Header Card (Updated without bottom pills)
    header_svg = render_header_card()
    for prefix in ["", "card_", "card_v1_", "card_v2_"]:
        with open(os.path.join(header_dir, f"{prefix}header.svg"), "w", encoding="utf-8") as f:
            f.write(header_svg)

    # 2. Contact Badges (HackerRank, LinkedIn, Direct Gmail)
    badge_hr = render_badge_hackerrank()
    badge_li = render_badge_linkedin()
    badge_gm = render_badge_gmail()

    with open(os.path.join(header_dir, "badge_hackerrank.svg"), "w", encoding="utf-8") as f:
        f.write(badge_hr)
    with open(os.path.join(header_dir, "badge_linkedin.svg"), "w", encoding="utf-8") as f:
        f.write(badge_li)
    with open(os.path.join(header_dir, "badge_gmail.svg"), "w", encoding="utf-8") as f:
        f.write(badge_gm)

    # 3. About Cards
    prof_svg = render_about_profile_card()
    for prefix in ["", "card_", "card_v1_"]:
        with open(os.path.join(about_dir, f"{prefix}profile.svg"), "w", encoding="utf-8") as f:
            f.write(prof_svg)

    exp_svg = render_about_experience_card()
    for prefix in ["", "card_", "card_v1_"]:
        with open(os.path.join(about_dir, f"{prefix}experience.svg"), "w", encoding="utf-8") as f:
            f.write(exp_svg)

    print("Profile cards & custom contact badges generated successfully!")

if __name__ == "__main__":
    main()
