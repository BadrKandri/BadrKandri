import os
import xml.etree.ElementTree as ET

skill_categories = [
    {
        "id": "data_science",
        "title": "Data Science &amp; AI Engineering",
        "domain_color": "#38BDF8",  # Cyan Blue
        "icon": '''
          <path d="M11 1L12.4 5.2L16.5 6.6L12.4 8L11 12.2L9.6 8L5.5 6.6L9.6 5.2L11 1Z" fill="{color}" fill-opacity="0.25" stroke="{color}" stroke-width="1.3" stroke-linejoin="round"/>
          <path d="M4.5 12.5L5.2 14.4L7.1 15.1L5.2 15.8L4.5 17.7L3.8 15.8L1.9 15.1L3.8 14.4L4.5 12.5Z" fill="{color}" stroke="{color}" stroke-width="0.9" stroke-linejoin="round"/>
          <path d="M16 11.5L16.6 13.1L18.2 13.7L16.6 14.3L16 15.9L15.4 14.3L13.8 13.7L15.4 13.1L16 11.5Z" fill="{color}" stroke="{color}" stroke-width="0.9" stroke-linejoin="round"/>
        ''',
        "rows": [
            ["Scikit-Learn", "NumPy &amp; Pandas", "XGBoost"],
            ["LangGraph", "Agentic AI &amp; RAG", "Qdrant"],
            ["PEFT / LoRA", "LLaMA-Factory", "SVM &amp; PCA"],
            ["Power BI Dashboards", "CRISP-DM / EDA"]
        ]
    },
    {
        "id": "mlops_bigdata",
        "title": "MLOps &amp; Big Data",
        "domain_color": "#00EA64",  # Emerald Green
        "icon": '''
          <rect x="2" y="3" width="16" height="13" rx="2" stroke="{color}" stroke-width="1.4" fill="{color}" fill-opacity="0.1"/>
          <path d="M6 7.5L9 9.5L6 11.5" stroke="{color}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M11 11.5H14" stroke="{color}" stroke-width="1.3" stroke-linecap="round"/>
        ''',
        "rows": [
            ["Apache Spark", "PySpark", "Apache Kafka"],
            ["Docker", "Kubernetes", "Linux (Bash)"],
            ["FastAPI (Async)", "SQL", "MongoDB (NoSQL)"],
            ["Hadoop Ecosystem", "CI/CD Pipelines"]
        ]
    }
]

def render_skill_card(c):
    width = 390
    height = 182
    dom_color = c["domain_color"]
    icon_svg = c["icon"].replace("{color}", dom_color)

    # Render pill rows (4 rows) with staggered dot twinkling
    rows_svg = []
    y_start = 58
    row_height = 28

    for r_idx, row in enumerate(c["rows"]):
        y = y_start + r_idx * row_height
        x = 18
        row_items = []
        for i_idx, item in enumerate(row):
            clean_item = item.replace("&amp;", "&")
            item_w = len(clean_item) * 6.6 + 22
            # Staggered twinkle timing
            delay = round((r_idx * 0.4 + i_idx * 0.3) % 2.4, 2)
            row_items.append(f'''
            <g transform="translate({x}, {y})">
                <rect x="0" y="0" width="{item_w}" height="22" rx="11" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="0.8"/>
                <circle cx="8" cy="11" r="2.2" fill="{dom_color}">
                    <animate attributeName="opacity" values="0.45;1;0.45" begin="{delay}s" dur="2.4s" repeatCount="indefinite"/>
                </circle>
                <text x="16" y="14.8" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="500">
                    {item}
                </text>
            </g>
            ''')
            x += item_w + 8
        rows_svg.append("".join(row_items))

    skills_content = "".join(rows_svg)

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad-{c['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="50%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>

    <!-- Animated Border Gradient -->
    <linearGradient id="border-grad-{c['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{dom_color}" stop-opacity="0.5">
        <animate attributeName="stop-opacity" values="0.35;0.65;0.35" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="40%" stop-color="{dom_color}" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-{c['id']}" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="{dom_color}" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Card Background -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="14" fill="url(#bg-grad-{c['id']})" stroke="url(#border-grad-{c['id']})" stroke-width="1.2" />

  <!-- Ambient Light Corner Glow with Breathing -->
  <circle cx="28" cy="28" r="50" fill="{dom_color}" opacity="0.06">
    <animate attributeName="opacity" values="0.04;0.10;0.04" dur="4s" repeatCount="indefinite"/>
  </circle>

  <!-- Header: Category Icon + Title -->
  <g transform="translate(18, 16)">
    <!-- Category Icon -->
    <g transform="translate(0, 1)">
      {icon_svg}
    </g>

    <!-- Title -->
    <text x="26" y="14" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700" letter-spacing="-0.2px">
      {c['title']}
    </text>
  </g>

  <!-- Divider Line -->
  <line x1="18" y1="45" x2="{width - 18}" y2="45" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1" />

  <!-- Skill Badges Grid (4 Rows) -->
  {skills_content}
</svg>
'''
    return svg

def main():
    target_dirs = [
        "assets/skills"
    ]
    for out_dir in target_dirs:
        os.makedirs(out_dir, exist_ok=True)
        for c in skill_categories:
            svg_code = render_skill_card(c)
            ET.fromstring(svg_code)
            for prefix in ["", "card_", "card_v1_", "card_v2_", "card_v3_"]:
                file_path = os.path.join(out_dir, f"{prefix}{c['id']}.svg")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(svg_code)

    print("Regenerated 2-card Tech Stack with twinkling constellations successfully!")

if __name__ == "__main__":
    main()
