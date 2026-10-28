import os
import xml.etree.ElementTree as ET

def render_header_card():
    width = 780
    height = 128
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="header-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="50%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>

    <!-- Animated Border Gradient -->
    <linearGradient id="header-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00EA64" stop-opacity="0.5">
        <animate attributeName="stop-color" values="#00EA64;#38BDF8;#A855F7;#00EA64" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="40%" stop-color="#38BDF8" stop-opacity="0.3">
        <animate attributeName="stop-color" values="#38BDF8;#A855F7;#00EA64;#38BDF8" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="80%" stop-color="#A855F7" stop-opacity="0.25">
        <animate attributeName="stop-color" values="#A855F7;#00EA64;#38BDF8;#A855F7" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>

    <!-- Animated Name Title Gradient -->
    <linearGradient id="name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00EA64">
        <animate attributeName="stop-color" values="#00EA64;#38BDF8;#A855F7;#00EA64" dur="7s" repeatCount="indefinite"/>
      </stop>
      <stop offset="60%" stop-color="#38BDF8">
        <animate attributeName="stop-color" values="#38BDF8;#A855F7;#00EA64;#38BDF8" dur="7s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#A855F7">
        <animate attributeName="stop-color" values="#A855F7;#00EA64;#38BDF8;#A855F7" dur="7s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-header" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="3" flood-color="#00EA64" flood-opacity="0.5"/>
    </filter>
    <filter id="glow-cyan-hd" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#38BDF8" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Card Background -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#header-bg)" stroke="url(#header-border)" stroke-width="1.2" />

  <!-- Ambient Light Corner Glows with Breathing Animation -->
  <circle cx="40" cy="40" r="90" fill="#00EA64" opacity="0.04">
    <animate attributeName="opacity" values="0.03;0.08;0.03" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{width - 40}" cy="40" r="90" fill="#38BDF8" opacity="0.04">
    <animate attributeName="opacity" values="0.03;0.08;0.03" begin="2.5s" dur="5s" repeatCount="indefinite"/>
  </circle>

  <!-- Status Pill Badge with Radar Beacon Animation -->
  <g transform="translate(32, 22)">
    <rect x="0" y="0" width="350" height="20" rx="10" fill="#00EA64" fill-opacity="0.08" stroke="#00EA64" stroke-opacity="0.3" stroke-width="0.8"/>
    <!-- Outer Radar Pulse -->
    <circle cx="10" cy="10" r="3" fill="none" stroke="#00EA64" stroke-width="0.8">
      <animate attributeName="r" values="3;9" dur="2.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <!-- Core Dot -->
    <circle cx="10" cy="10" r="3" fill="#00EA64" filter="url(#glow-header)">
      <animate attributeName="r" values="3;3.6;3" dur="2.2s" repeatCount="indefinite"/>
    </circle>
    <text x="19" y="13.5" fill="#00EA64" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="700" letter-spacing="0.4px">
      OPEN FOR PFE / DATA SCIENCE &amp; AI INTERNSHIPS
    </text>
  </g>

  <!-- Location Badge (Top Right) -->
  <g transform="translate({width - 32 - 140}, 22)">
    <rect x="0" y="0" width="140" height="20" rx="10" fill="rgba(255, 255, 255, 0.03)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="0.8"/>
    <circle cx="12" cy="10" r="2.5" fill="#38BDF8" filter="url(#glow-cyan-hd)">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/>
    </circle>
    <text x="22" y="13.5" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Casablanca, Morocco
    </text>
  </g>

  <!-- Headline: Hi, I'm Badreddine Idrissi Kandri 👋 -->
  <g transform="translate(32, 68)">
    <text font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="25" font-weight="800" letter-spacing="-0.5px">
      <tspan fill="#F8FAFC">Hi, I'm </tspan>
      <tspan fill="url(#name-grad)">Badreddine Idrissi Kandri</tspan>
      <tspan fill="#F8FAFC"> 👋</tspan>
    </text>
  </g>

  <!-- Title: Junior Data Scientist/AI Engineer -->
  <g transform="translate(32, 98)">
    <text fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" letter-spacing="0.2px">
      Junior Data Scientist/AI Engineer
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
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="{color}" flood-opacity="0.4"/>
    </filter>
  </defs>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#bg-hr)" stroke="{color}" stroke-opacity="0.4" stroke-width="1.2">
    <animate attributeName="stroke-opacity" values="0.35;0.75;0.35" dur="3s" repeatCount="indefinite"/>
  </rect>
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
  <!-- Animated Link Arrow -->
  <g transform="translate({width - 22}, 11)">
    <animateTransform attributeName="transform" type="translate" values="{width - 22} 11; {width - 19} 11; {width - 22} 11" dur="2s" repeatCount="indefinite"/>
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
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="{color}" flood-opacity="0.4"/>
    </filter>
  </defs>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#bg-li)" stroke="{color}" stroke-opacity="0.4" stroke-width="1.2">
    <animate attributeName="stroke-opacity" values="0.35;0.75;0.35" dur="3s" repeatCount="indefinite"/>
  </rect>
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
  <!-- Animated Link Arrow -->
  <g transform="translate({width - 22}, 11)">
    <animateTransform attributeName="transform" type="translate" values="{width - 22} 11; {width - 19} 11; {width - 22} 11" dur="2s" repeatCount="indefinite"/>
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
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="{color}" flood-opacity="0.4"/>
    </filter>
  </defs>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#bg-gm)" stroke="{color}" stroke-opacity="0.4" stroke-width="1.2">
    <animate attributeName="stroke-opacity" values="0.35;0.75;0.35" dur="3s" repeatCount="indefinite"/>
  </rect>
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
  <!-- Animated Link Arrow -->
  <g transform="translate({width - 22}, 11)">
    <animateTransform attributeName="transform" type="translate" values="{width - 22} 11; {width - 19} 11; {width - 22} 11" dur="2s" repeatCount="indefinite"/>
    <path d="M1 9L9 1M9 1H3M9 1V7" stroke="#64748B" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>'''
    return svg

def main():
    base_dir = "assets"
    header_dir = os.path.join(base_dir, "header")
    os.makedirs(header_dir, exist_ok=True)

    header_svg = render_header_card()
    ET.fromstring(header_svg)
    for prefix in ["", "card_", "card_v1_", "card_v2_", "card_v3_"]:
        with open(os.path.join(header_dir, f"{prefix}header.svg"), "w", encoding="utf-8") as f:
            f.write(header_svg)

    badge_hr = render_badge_hackerrank()
    badge_li = render_badge_linkedin()
    badge_gm = render_badge_gmail()
    ET.fromstring(badge_hr)
    ET.fromstring(badge_li)
    ET.fromstring(badge_gm)

    with open(os.path.join(header_dir, "badge_hackerrank.svg"), "w", encoding="utf-8") as f:
        f.write(badge_hr)
    with open(os.path.join(header_dir, "badge_linkedin.svg"), "w", encoding="utf-8") as f:
        f.write(badge_li)
    with open(os.path.join(header_dir, "badge_gmail.svg"), "w", encoding="utf-8") as f:
        f.write(badge_gm)

    print("Profile header & badges updated with animations successfully!")

if __name__ == "__main__":
    main()
