import os
import xml.etree.ElementTree as ET

neetcode_categories = [
    # Column 1: Core Data Structures
    {"name": "Arrays & Hashing", "solved": 0, "total": 9, "color": "#00EA64", "col": 0},
    {"name": "Two Pointers", "solved": 0, "total": 5, "color": "#00EA64", "col": 0},
    {"name": "Sliding Window", "solved": 0, "total": 6, "color": "#00EA64", "col": 0},
    {"name": "Stack", "solved": 0, "total": 7, "color": "#00EA64", "col": 0},
    {"name": "Binary Search", "solved": 0, "total": 7, "color": "#00EA64", "col": 0},
    {"name": "Linked List", "solved": 0, "total": 11, "color": "#00EA64", "col": 0},

    # Column 2: Trees, Heaps & Graphs
    {"name": "Trees", "solved": 0, "total": 15, "color": "#38BDF8", "col": 1},
    {"name": "Heap / Priority Queue", "solved": 0, "total": 7, "color": "#38BDF8", "col": 1},
    {"name": "Backtracking", "solved": 0, "total": 9, "color": "#38BDF8", "col": 1},
    {"name": "Tries", "solved": 0, "total": 3, "color": "#38BDF8", "col": 1},
    {"name": "Graphs", "solved": 0, "total": 13, "color": "#38BDF8", "col": 1},
    {"name": "Advanced Graphs", "solved": 0, "total": 6, "color": "#38BDF8", "col": 1},

    # Column 3: DP, Greedy & Math
    {"name": "1-D Dynamic Prog", "solved": 0, "total": 12, "color": "#A855F7", "col": 2},
    {"name": "2-D Dynamic Prog", "solved": 0, "total": 11, "color": "#A855F7", "col": 2},
    {"name": "Greedy", "solved": 0, "total": 8, "color": "#F97316", "col": 2},
    {"name": "Intervals", "solved": 0, "total": 6, "color": "#F97316", "col": 2},
    {"name": "Math & Geometry", "solved": 0, "total": 8, "color": "#F97316", "col": 2},
    {"name": "Bit Manipulation", "solved": 0, "total": 7, "color": "#F97316", "col": 2},
]

def render_neetcode_card():
    width = 780
    height = 295

    total_solved = sum(c["solved"] for c in neetcode_categories)
    grand_total = sum(c["total"] for c in neetcode_categories)
    pct = round((total_solved / grand_total) * 100, 1) if grand_total > 0 else 0
    master_fill_w = max(4, int((total_solved / grand_total) * 732)) if total_solved > 0 else 0

    col_headers = [
        {"title": "CORE DATA STRUCTURES", "color": "#00EA64"},
        {"title": "TREES &amp; GRAPHS", "color": "#38BDF8"},
        {"title": "DYNAMIC PROG &amp; MATH", "color": "#A855F7"}
    ]

    col_x = [24, 276, 528]
    items_by_col = [[], [], []]
    for c in neetcode_categories:
        items_by_col[c["col"]].append(c)

    columns_svg = []
    for col_idx in range(3):
        x = col_x[col_idx]
        col_meta = col_headers[col_idx]
        header_svg = f'''
        <g transform="translate({x}, 76)">
          <circle cx="4" cy="5" r="2.5" fill="{col_meta['color']}">
            <animate attributeName="opacity" values="0.5;1;0.5" dur="2.5s" repeatCount="indefinite"/>
          </circle>
          <text x="12" y="8" fill="{col_meta['color']}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="700" letter-spacing="0.5px">
            {col_meta['title']}
          </text>
        </g>
        '''
        items_svg = []
        y_item_start = 98
        for i_idx, item in enumerate(items_by_col[col_idx]):
            y = y_item_start + i_idx * 24
            item_solved = item["solved"]
            item_total = item["total"]
            bar_w = 48
            fill_w = int((item_solved / item_total) * bar_w) if item_total > 0 else 0
            clean_name = item['name'].replace("&", "&amp;")
            items_svg.append(f'''
            <g transform="translate({x}, {y})">
              <!-- Category Name -->
              <text x="0" y="10" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500">
                {clean_name}
              </text>
              <!-- Fraction -->
              <text x="175" y="10" text-anchor="end" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="600">
                {item_solved}/{item_total}
              </text>
              <!-- Mini Bar Track -->
              <rect x="182" y="3" width="{bar_w}" height="5" rx="2.5" fill="rgba(255, 255, 255, 0.05)"/>
              {f'<rect x="182" y="3" width="{max(3, fill_w)}" height="5" rx="2.5" fill="{item["color"]}"/>' if fill_w > 0 else ''}
            </g>
            ''')
        columns_svg.append(header_svg + "".join(items_svg))

    columns_content = "".join(columns_svg)

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="nc-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="50%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>

    <!-- Border Gradient -->
    <linearGradient id="nc-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#A855F7" stop-opacity="0.45" />
      <stop offset="40%" stop-color="#38BDF8" stop-opacity="0.25" />
      <stop offset="80%" stop-color="#00EA64" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>

    <!-- Master Progress Gradient -->
    <linearGradient id="nc-master-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00EA64" />
      <stop offset="50%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-nc" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#00EA64" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-laser" x="-100%" y="-100%" width="300%" height="300%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#00EA64" flood-opacity="0.9"/>
    </filter>
  </defs>

  <!-- Card Background with Breathing Border -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#nc-bg)" stroke="url(#nc-border)" stroke-width="1.2">
    <animate attributeName="stroke-opacity" values="0.35;0.7;0.35" dur="4s" repeatCount="indefinite"/>
  </rect>

  <!-- Corner Ambient Light with Breathing -->
  <circle cx="35" cy="35" r="75" fill="#00EA64" opacity="0.04">
    <animate attributeName="opacity" values="0.03;0.08;0.03" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{width - 35}" cy="35" r="75" fill="#A855F7" opacity="0.04">
    <animate attributeName="opacity" values="0.03;0.08;0.03" begin="2s" dur="4s" repeatCount="indefinite"/>
  </circle>

  <!-- Top Header -->
  <g transform="translate(24, 18)">
    <!-- Puzzle Piece Icon -->
    <g transform="translate(0, 1)">
      <path d="M7 2H10V4C11.1 4 12 4.9 12 6C12 7.1 11.1 8 10 8V10H8C8 8.9 7.1 8 6 8C4.9 8 4 8.9 4 10H2V7C3.1 7 4 6.1 4 5C4 3.9 3.1 3 2 3V2H5C5 3.1 5.9 4 7 4C8.1 4 9 3.1 9 2H7Z" stroke="#00EA64" stroke-width="1.4" fill="#00EA64" fill-opacity="0.15" stroke-linejoin="round"/>
    </g>

    <!-- Title -->
    <text x="20" y="12" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="700">
      NeetCode 150 Roadmap Tracker
    </text>

    <!-- Domain Pill with Beacon Radar Animation -->
    <g transform="translate(242, 0)">
      <rect x="0" y="0" width="168" height="17" rx="8.5" fill="#00EA64" fill-opacity="0.08" stroke="#00EA64" stroke-opacity="0.25" stroke-width="0.8"/>
      <!-- Radar Pulse -->
      <circle cx="8" cy="8.5" r="2.5" fill="none" stroke="#00EA64" stroke-width="0.8">
        <animate attributeName="r" values="2.5;6.5" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.75;0" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="8" cy="8.5" r="2.5" fill="#00EA64" filter="url(#glow-nc)">
        <animate attributeName="r" values="2.5;3.1;2.5" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="16" y="12" fill="#00EA64" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="8.5" font-weight="700" letter-spacing="0.3px">
        DATA STRUCTURES &amp; ALGORITHMS
      </text>
    </g>

    <!-- Total Counter (Right) -->
    <g transform="translate({width - 48 - 145}, 0)">
      <text x="0" y="12" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5">
        Solved: <tspan fill="#00EA64" font-weight="700" font-size="12">{total_solved} / {grand_total}</tspan> <tspan fill="#64748B">({pct}%)</tspan>
      </text>
    </g>

    <!-- Master Progress Track -->
    <rect x="0" y="27" width="732" height="5" rx="2.5" fill="rgba(255, 255, 255, 0.05)"/>
    {f'<rect x="0" y="27" width="{master_fill_w}" height="5" rx="2.5" fill="url(#nc-master-grad)"/>' if master_fill_w > 0 else ''}

    <!-- Active Scanner Beam along the Track -->
    <circle cy="29.5" r="2" fill="#00EA64" filter="url(#glow-laser)">
      <animate attributeName="cx" values="0;732" dur="3.5s" repeatCount="indefinite" keyTimes="0;1" calcMode="spline" keySplines="0.4 0 0.2 1"/>
      <animate attributeName="opacity" values="0;0.9;0.9;0" dur="3.5s" repeatCount="indefinite" keyTimes="0;0.1;0.9;1"/>
    </circle>

    <!-- Divider Line -->
    <line x1="0" y1="42" x2="732" y2="42" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1" />
  </g>

  <!-- 3 Columns Content -->
  {columns_content}

  <!-- Footer Bar -->
  <g transform="translate(24, 254)">
    <rect x="0" y="0" width="732" height="24" rx="6" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.04)" stroke-width="0.8"/>
    <!-- Easy -->
    <circle cx="16" cy="12" r="3" fill="#00EA64">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="25" y="15" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Easy: <tspan font-weight="700" fill="#00EA64">44</tspan> Problems
    </text>

    <!-- Medium -->
    <circle cx="140" cy="12" r="3" fill="#F59E0B">
      <animate attributeName="opacity" values="0.6;1;0.6" begin="0.8s" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="149" y="15" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Medium: <tspan font-weight="700" fill="#F59E0B">88</tspan> Problems
    </text>

    <!-- Hard -->
    <circle cx="275" cy="12" r="3" fill="#EF4444">
      <animate attributeName="opacity" values="0.6;1;0.6" begin="1.6s" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="284" y="15" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Hard: <tspan font-weight="700" fill="#EF4444">18</tspan> Problems
    </text>

    <!-- Roadmap Total Tag -->
    <text x="720" y="15" text-anchor="end" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="600">
      ACTIVE ROADMAP · 150 CORE CHALLENGES
    </text>
  </g>
</svg>
'''
    return svg

def main():
    target_dirs = [
        "assets/neetcode"
    ]
    for out_dir in target_dirs:
        os.makedirs(out_dir, exist_ok=True)
        svg_code = render_neetcode_card()
        ET.fromstring(svg_code)
        for prefix in ["", "card_", "card_v1_"]:
            file_path = os.path.join(out_dir, f"{prefix}neetcode.svg")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_code)

    print("Regenerated NeetCode 150 card with animations successfully!")

if __name__ == "__main__":
    main()
