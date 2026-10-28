import os
import xml.etree.ElementTree as ET

titles = [
    {
        "id": "about",
        "title": "ABOUT ME",
        "color": "#38BDF8",  # Cyan Blue
        "pill_w": 180,
        "icon": '''<path d="M7 1C8.66 1 10 2.34 10 4C10 5.66 8.66 7 7 7C5.34 7 4 5.66 4 4C4 2.34 5.34 1 7 1ZM7 9C10.33 9 14 10.67 14 13V15H0V13C0 10.67 3.67 9 7 9Z" fill="{color}" transform="translate(0, -8)"/>'''
    },
    {
        "id": "tech_stack",
        "title": "TECH STACK &amp; COMPETENCIES",
        "color": "#00EA64",  # Emerald Green
        "pill_w": 288,
        "icon": '''<path d="M7 0L0 3.5L7 7L14 3.5L7 0ZM0 7.5L7 11L14 7.5M0 11.5L7 15L14 11.5" stroke="{color}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(0, -8)"/>'''
    },
    {
        "id": "projects",
        "title": "PROJECTS",
        "color": "#F97316",  # Orange
        "pill_w": 144,
        "icon": '''<path d="M4 11L0 7L4 3M10 3L14 7L10 11" stroke="{color}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate(0, -7)"/>'''
    },
    {
        "id": "hackerrank",
        "title": "HACKERRANK PROGRESS",
        "color": "#00EA64",  # Emerald
        "pill_w": 248,
        "icon": '''<path d="M0 2.5L7 0L14 2.5V12.5L7 15L0 12.5V2.5Z" stroke="{color}" stroke-width="1.2" fill="{color}" fill-opacity="0.2" transform="translate(0, -8)"/><path d="M4.5 5V10M9.5 5V10M4.5 7.5H9.5" stroke="{color}" stroke-width="1.1" stroke-linecap="round" transform="translate(0, -8)"/>'''
    },
    {
        "id": "neetcode",
        "title": "NEETCODE 150 ROADMAP",
        "color": "#A855F7",  # Violet
        "pill_w": 252,
        "icon": '''<path d="M6 1H9V3C10 3 11 4 11 5C11 6 10 7 9 7V9H7C7 8 6 7 5 7C4 7 3 8 3 9H1V6C2 6 3 5 3 4C3 3 2 2 1 2V1H4C4 2 5 3 6 3C7 3 8 2 8 1H6Z" stroke="{color}" stroke-width="1.2" fill="{color}" fill-opacity="0.2" stroke-linejoin="round" transform="translate(0, -6)"/>'''
    }
]

def render_title_svg(t):
    width = 780
    height = 46
    color = t["color"]
    pill_w = t["pill_w"]
    pill_x = int((width - pill_w) / 2)
    icon_svg = t["icon"].replace("{color}", color)
    left_end = pill_x - 14
    right_start = pill_x + pill_w + 14

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="fade-left-{t['id']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{color}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0.38"/>
    </linearGradient>
    <linearGradient id="fade-right-{t['id']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.38"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="pill-bg-{t['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>
    <filter id="glow-{t['id']}" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="{color}" flood-opacity="0.55"/>
    </filter>
    <filter id="comet-{t['id']}" x="-100%" y="-100%" width="300%" height="300%">
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="{color}" flood-opacity="0.85"/>
    </filter>
  </defs>

  <!-- Accent Fading Lines -->
  <line x1="24" y1="23" x2="{left_end}" y2="23" stroke="url(#fade-left-{t['id']})" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="{right_start}" y1="23" x2="756" y2="23" stroke="url(#fade-right-{t['id']})" stroke-width="1.2" stroke-linecap="round"/>

  <!-- Inward Traveling Energy Stream (Left -> Capsule) -->
  <circle cy="23" r="2" fill="{color}" filter="url(#comet-{t['id']})">
    <animate attributeName="cx" values="24;{left_end}" dur="2.5s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" keyTimes="0;0.2;0.8;1"/>
  </circle>

  <!-- Inward Traveling Energy Stream (Right -> Capsule) -->
  <circle cy="23" r="2" fill="{color}" filter="url(#comet-{t['id']})">
    <animate attributeName="cx" values="756;{right_start}" dur="2.5s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite" keyTimes="0;0.2;0.8;1"/>
  </circle>

  <!-- Center Capsule with Breathing Border -->
  <rect x="{pill_x}" y="6" width="{pill_w}" height="34" rx="17" fill="url(#pill-bg-{t['id']})" stroke="{color}" stroke-opacity="0.38" stroke-width="1.2">
    <animate attributeName="stroke-opacity" values="0.3;0.65;0.3" dur="3.5s" repeatCount="indefinite"/>
  </rect>

  <!-- Glowing Radar Beacon Dot -->
  <circle cx="{pill_x + 18}" cy="23" r="3" fill="none" stroke="{color}" stroke-width="0.8">
    <animate attributeName="r" values="3;8" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.75;0" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{pill_x + 18}" cy="23" r="3" fill="{color}" filter="url(#glow-{t['id']})">
    <animate attributeName="r" values="3;3.6;3" dur="2s" repeatCount="indefinite"/>
  </circle>

  <!-- Icon & Text Group -->
  <g transform="translate({pill_x + 30}, 23)">
    {icon_svg}
    <text x="22" y="4" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" letter-spacing="1px">
      {t['title']}
    </text>
  </g>
</svg>'''
    return svg

def main():
    out_dir = "assets/titles"
    os.makedirs(out_dir, exist_ok=True)
    for t in titles:
        svg_code = render_title_svg(t)
        ET.fromstring(svg_code)
        for prefix in ["", "title_", "title_v1_", "title_v2_"]:
            file_path = os.path.join(out_dir, f"{prefix}{t['id']}.svg")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_code)

    print("All section title SVGs regenerated with animations successfully!")

if __name__ == "__main__":
    main()
