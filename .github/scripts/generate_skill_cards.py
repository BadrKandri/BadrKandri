import os

skill_categories = [
    {
        "id": "ai_engineering",
        "title": "AI Engineering &amp; Autonomous Agents",
        "domain": "AI Engineering",
        "domain_color": "#38BDF8",  # Blue
        "subtitle": "Agentic Workflows, Hybrid RAG &amp; LLM Fine-Tuning",
        "icon": '''
          <path d="M11 1L12.4 5.2L16.5 6.6L12.4 8L11 12.2L9.6 8L5.5 6.6L9.6 5.2L11 1Z" fill="{color}" fill-opacity="0.25" stroke="{color}" stroke-width="1.3" stroke-linejoin="round"/>
          <path d="M4.5 12.5L5.2 14.4L7.1 15.1L5.2 15.8L4.5 17.7L3.8 15.8L1.9 15.1L3.8 14.4L4.5 12.5Z" fill="{color}" stroke="{color}" stroke-width="0.9" stroke-linejoin="round"/>
          <path d="M16 11.5L16.6 13.1L18.2 13.7L16.6 14.3L16 15.9L15.4 14.3L13.8 13.7L15.4 13.1L16 11.5Z" fill="{color}" stroke="{color}" stroke-width="0.9" stroke-linejoin="round"/>
        ''',
        "rows": [
            ["LangGraph Workflows", "Agno Multi-Agents"],
            ["Hybrid RAG", "Qdrant Vector", "ChromaDB"],
            ["PEFT / LoRA", "LLaMA-Factory", "OpenAI &amp; Claude"]
        ]
    },
    {
        "id": "machine_learning",
        "title": "Machine Learning &amp; Data Science",
        "domain": "Machine Learning",
        "domain_color": "#F97316",  # Orange
        "subtitle": "Predictive Modeling, Statistical Learning &amp; EDA",
        "icon": '''
          <path d="M2 16L7 10L11 14L18 5" stroke="{color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="7" cy="10" r="2" fill="{color}"/>
          <circle cx="11" cy="14" r="2" fill="{color}"/>
          <circle cx="18" cy="5" r="2.2" fill="{color}"/>
          <path d="M2 19H19" stroke="{color}" stroke-width="1.2" stroke-linecap="round" opacity="0.4"/>
        ''',
        "rows": [
            ["Scikit-Learn", "NumPy &amp; Pandas", "XGBoost"],
            ["SVM &amp; PCA", "Random Forest", "GridSearchCV"],
            ["Power BI Dashboards", "CRISP-DM / EDA"]
        ]
    },
    {
        "id": "data_engineering",
        "title": "Data Engineering &amp; Big Data",
        "domain": "Data Engineering",
        "domain_color": "#A855F7",  # Violet
        "subtitle": "Distributed Computing, Streaming &amp; Data Pipelines",
        "icon": '''
          <ellipse cx="10" cy="4" rx="7" ry="2.6" stroke="{color}" stroke-width="1.3" fill="{color}" fill-opacity="0.2"/>
          <path d="M3 4V9.5C3 11 6.1 12.1 10 12.1C13.9 12.1 17 11 17 9.5V4" stroke="{color}" stroke-width="1.3"/>
          <path d="M3 9.5V15C3 16.5 6.1 17.6 10 17.6C13.9 17.6 17 16.5 17 15V9.5" stroke="{color}" stroke-width="1.3"/>
        ''',
        "rows": [
            ["Apache Spark", "PySpark", "Apache Kafka"],
            ["Hadoop Ecosystem", "ETL / ELT Pipelines"],
            ["SQL Relational", "MongoDB (NoSQL)"]
        ]
    },
    {
        "id": "mlops",
        "title": "MLOps &amp; Core Engineering",
        "domain": "Coding &amp; MLOps",
        "domain_color": "#00EA64",  # Emerald Green
        "subtitle": "Containerization, Microservices &amp; CI/CD Pipelines",
        "icon": '''
          <rect x="2" y="3" width="16" height="13" rx="2" stroke="{color}" stroke-width="1.4" fill="{color}" fill-opacity="0.1"/>
          <path d="M6 7.5L9 9.5L6 11.5" stroke="{color}" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M11 11.5H14" stroke="{color}" stroke-width="1.3" stroke-linecap="round"/>
        ''',
        "rows": [
            ["Python 3", "FastAPI (Async Microservices)"],
            ["Docker", "Kubernetes", "Linux (Bash)"],
            ["Git / GitHub", "CI/CD Automation"]
        ]
    }
]

def render_skill_card(c):
    width = 390
    height = 185
    dom_color = c["domain_color"]
    icon_svg = c["icon"].replace("{color}", dom_color)
    clean_domain = c["domain"].replace("&amp;", "&")
    domain_text = clean_domain.upper().replace("&", "&amp;")
    pill_badge_w = len(clean_domain) * 6.5 + 20

    # Render pill rows
    rows_svg = []
    y_start = 92
    row_height = 29

    for r_idx, row in enumerate(c["rows"]):
        y = y_start + r_idx * row_height
        x = 18
        row_items = []
        for item in row:
            clean_item = item.replace("&amp;", "&")
            item_w = len(clean_item) * 6.6 + 22
            row_items.append(f'''
            <g transform="translate({x}, {y})">
                <rect x="0" y="0" width="{item_w}" height="22" rx="11" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.07)" stroke-width="0.8"/>
                <circle cx="8" cy="11" r="2.2" fill="{dom_color}" opacity="0.85"/>
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

    <!-- Border Gradient -->
    <linearGradient id="border-grad-{c['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{dom_color}" stop-opacity="0.45" />
      <stop offset="40%" stop-color="{dom_color}" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-{c['id']}" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="{dom_color}" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Card Background -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="14" fill="url(#bg-grad-{c['id']})" stroke="url(#border-grad-{c['id']})" stroke-width="1.2" />

  <!-- Ambient Light Corner Glow -->
  <circle cx="28" cy="28" r="50" fill="{dom_color}" opacity="0.06" />

  <!-- Header: Category Icon + Title -->
  <g transform="translate(18, 16)">
    <!-- Category Icon -->
    <g transform="translate(0, 1)">
      {icon_svg}
    </g>

    <!-- Title -->
    <text x="26" y="14" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="700" letter-spacing="-0.2px">
      {c['title']}
    </text>
  </g>

  <!-- Domain Pill Badge -->
  <g transform="translate(18, 38)">
    <rect x="0" y="0" width="{pill_badge_w}" height="17" rx="8.5" fill="{dom_color}" fill-opacity="0.1" stroke="{dom_color}" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="8" cy="8.5" r="2.5" fill="{dom_color}" filter="url(#glow-{c['id']})"/>
    <text x="16" y="12" fill="{dom_color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="700" letter-spacing="0.3px">
      {domain_text}
    </text>
  </g>

  <!-- Subtitle / Focus Summary -->
  <text x="18" y="66" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="400">
    {c['subtitle']}
  </text>

  <!-- Divider Line -->
  <line x1="18" y1="78" x2="{width - 18}" y2="78" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1" />

  <!-- Skill Badges Grid -->
  {skills_content}
</svg>
'''
    return svg

def main():
    target_dirs = [
        "C:/Users/MELIODAS/.gemini/antigravity/scratch/BadrKandri/assets/skills"
    ]
    for out_dir in target_dirs:
        os.makedirs(out_dir, exist_ok=True)
        for c in skill_categories:
            svg_code = render_skill_card(c)
            for prefix in ["", "card_", "card_v1_"]:
                file_path = os.path.join(out_dir, f"{prefix}{c['id']}.svg")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(svg_code)

    print("Regenerated all skill cards successfully!")

if __name__ == "__main__":
    main()
