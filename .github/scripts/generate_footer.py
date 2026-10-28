import os
import xml.etree.ElementTree as ET

def render_animated_footer():
    width = 780
    height = 46
    pill_w = 320
    pill_x = int((width - pill_w) / 2)  # 230

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Left Accent Line Gradient -->
    <linearGradient id="fade-left-ft" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00EA64" stop-opacity="0"/>
      <stop offset="60%" stop-color="#38BDF8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0.45"/>
    </linearGradient>

    <!-- Right Accent Line Gradient -->
    <linearGradient id="fade-right-ft" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.45"/>
      <stop offset="40%" stop-color="#38BDF8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#00EA64" stop-opacity="0"/>
    </linearGradient>

    <!-- Capsule Background Gradient -->
    <linearGradient id="pill-bg-ft" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>

    <!-- Animated Border Gradient -->
    <linearGradient id="pill-border-ft" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00EA64" stop-opacity="0.5">
        <animate attributeName="stop-color" values="#00EA64;#38BDF8;#A855F7;#00EA64" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#38BDF8" stop-opacity="0.35">
        <animate attributeName="stop-color" values="#38BDF8;#A855F7;#00EA64;#38BDF8" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0.5">
        <animate attributeName="stop-color" values="#A855F7;#00EA64;#38BDF8;#A855F7" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Animated Brand Name Gradient -->
    <linearGradient id="brand-grad-ft" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00EA64">
        <animate attributeName="stop-color" values="#00EA64;#38BDF8;#A855F7;#00EA64" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#38BDF8">
        <animate attributeName="stop-color" values="#38BDF8;#A855F7;#00EA64;#38BDF8" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#A855F7">
        <animate attributeName="stop-color" values="#A855F7;#00EA64;#38BDF8;#A855F7" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Ruby Glow Filter for Heart -->
    <filter id="heart-glow-ft" x="-60%" y="-60%" width="220%" height="220%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#EF4444" flood-opacity="0.8"/>
    </filter>

    <!-- Comet Glow Filter for Traveling Energy Pulses -->
    <filter id="comet-glow-cyan" x="-100%" y="-100%" width="300%" height="300%">
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="#38BDF8" flood-opacity="0.9"/>
    </filter>
    <filter id="comet-glow-purple" x="-100%" y="-100%" width="300%" height="300%">
      <feDropShadow dx="0" dy="0" stdDeviation="2" flood-color="#A855F7" flood-opacity="0.9"/>
    </filter>

    <style>
      @keyframes heartbeat {{
        0% {{ transform: scale(1); }}
        14% {{ transform: scale(1.24); }}
        28% {{ transform: scale(1); }}
        42% {{ transform: scale(1.18); }}
        70% {{ transform: scale(1); }}
        100% {{ transform: scale(1); }}
      }}
      .heart-pulse {{
        animation: heartbeat 1.6s cubic-bezier(0.215, 0.61, 0.355, 1) infinite;
        transform-origin: 0px 0px;
      }}
      @keyframes subtleBreath {{
        0%, 100% {{ stroke-opacity: 0.35; }}
        50% {{ stroke-opacity: 0.7; }}
      }}
      .capsule-rect {{
        animation: subtleBreath 3s ease-in-out infinite;
      }}
    </style>
  </defs>

  <!-- Base Accent Fading Lines -->
  <line x1="24" y1="23" x2="216" y2="23" stroke="url(#fade-left-ft)" stroke-width="1.2" stroke-linecap="round"/>
  <line x1="564" y1="23" x2="756" y2="23" stroke="url(#fade-right-ft)" stroke-width="1.2" stroke-linecap="round"/>

  <!-- Traveling Energy Light Pulses (Left Stream -> Towards Capsule) -->
  <circle cy="23" r="2" fill="#38BDF8" filter="url(#comet-glow-cyan)">
    <animate attributeName="cx" values="24;216" dur="2.4s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.4s" repeatCount="indefinite" keyTimes="0;0.2;0.8;1"/>
  </circle>
  <circle cy="23" r="1.6" fill="#00EA64" filter="url(#comet-glow-cyan)">
    <animate attributeName="cx" values="24;216" begin="1.2s" dur="2.4s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;0.75;0.75;0" begin="1.2s" dur="2.4s" repeatCount="indefinite" keyTimes="0;0.2;0.8;1"/>
  </circle>

  <!-- Traveling Energy Light Pulses (Right Stream -> Towards Capsule) -->
  <circle cy="23" r="2" fill="#A855F7" filter="url(#comet-glow-purple)">
    <animate attributeName="cx" values="756;564" dur="2.4s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.4s" repeatCount="indefinite" keyTimes="0;0.2;0.8;1"/>
  </circle>
  <circle cy="23" r="1.6" fill="#38BDF8" filter="url(#comet-glow-purple)">
    <animate attributeName="cx" values="756;564" begin="1.2s" dur="2.4s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines="0.4 0 0.2 1"/>
    <animate attributeName="opacity" values="0;0.75;0.75;0" begin="1.2s" dur="2.4s" repeatCount="indefinite" keyTimes="0;0.2;0.8;1"/>
  </circle>

  <!-- Center Capsule -->
  <rect class="capsule-rect" x="{pill_x}" y="6" width="{pill_w}" height="34" rx="17" fill="url(#pill-bg-ft)" stroke="url(#pill-border-ft)" stroke-width="1.2"/>

  <!-- Center Content -->
  <g transform="translate(256, 23)">
    <!-- Designed & maintained with -->
    <text x="0" y="4" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500">
      Designed &amp; maintained with
    </text>
    
    <!-- Centered Heart Icon with Pure Dual-Engine (CSS + SMIL) Pulse Animation -->
    <g transform="translate(160, -2)">
      <g class="heart-pulse">
        <animateTransform
          attributeName="transform"
          type="scale"
          values="1; 1.25; 1; 1.18; 1; 1"
          keyTimes="0; 0.14; 0.28; 0.42; 0.7; 1"
          dur="1.6s"
          repeatCount="indefinite"
        />
        <path transform="translate(-6, -5)" d="M6 10.5L5.13 9.71C2.06 6.93 0.03 5.09 0.03 2.82C0.03 0.98 1.48 -0.47 3.32 -0.47C4.36 -0.47 5.36 0.01 6 0.77C6.64 0.01 7.64 -0.47 8.68 -0.47C10.52 -0.47 11.97 0.98 11.97 2.82C11.97 5.09 9.94 6.93 6.87 9.71L6 10.5Z" fill="#EF4444" filter="url(#heart-glow-ft)"/>
      </g>
    </g>

    <!-- by Badr Kandri -->
    <text x="174" y="4" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">
      <tspan fill="#94A3B8" font-weight="500">by </tspan>
      <tspan fill="url(#brand-grad-ft)" font-weight="700">Badr Kandri</tspan>
    </text>
  </g>
</svg>'''
    return svg

def main():
    out_dir = "assets/footer"
    os.makedirs(out_dir, exist_ok=True)
    svg_code = render_animated_footer()
    ET.fromstring(svg_code)
    for name in ["footer_capsule.svg", "card_footer.svg", "card_v1_footer.svg", "card_v2_footer.svg"]:
        with open(os.path.join(out_dir, name), "w", encoding="utf-8") as f:
            f.write(svg_code)
    print("All animated footer SVGs generated successfully!")

if __name__ == "__main__":
    main()
