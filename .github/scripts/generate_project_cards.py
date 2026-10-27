import os

projects = [
    {
        "id": "meliodas_manus",
        "title": "meliodas_manus",
        "domain": "AI Engineering",
        "domain_color": "#00EA64",
        "desc_line1": "Multimodal AI Agent using GPT-4 Vision to",
        "desc_line2": "analyze Excel files & generate PDF reports.",
        "tags": ["Python", "GPT-4V", "Vision AI"]
    },
    {
        "id": "portnet",
        "title": "PortNet-Predictive-Modeling",
        "domain": "Machine Learning",
        "domain_color": "#38BDF8",
        "desc_line1": "Predictive analytics & feature engineering for",
        "desc_line2": "maritime logistics and port operations.",
        "tags": ["Python", "NumPy", "Jupyter"]
    },
    {
        "id": "sofac",
        "title": "Sofac-commercial-agent",
        "domain": "AI Agent",
        "domain_color": "#F59E0B",
        "desc_line1": "Commercial intelligent agent for automated",
        "desc_line2": "customer interaction and process workflows.",
        "tags": ["Python", "LLMs", "Automation"]
    },
    {
        "id": "deep_learning",
        "title": "Deep-Learning",
        "domain": "Deep Learning",
        "domain_color": "#A855F7",
        "desc_line1": "Neural networks from scratch, backprop",
        "desc_line2": "implementations, and NLP experiments.",
        "tags": ["PyTorch", "Neural Nets", "NLP"]
    },
    {
        "id": "machine_learning",
        "title": "Machine-Learning",
        "domain": "ML Algorithms",
        "domain_color": "#00EA64",
        "desc_line1": "Core algorithms (Logistic Regression, K-Means)",
        "desc_line2": "implemented from ground zero in pure NumPy.",
        "tags": ["Python", "NumPy", "From Scratch"]
    },
    {
        "id": "python_100",
        "title": "100-Days-Of-Code-PYTHON",
        "domain": "Python Mastery",
        "domain_color": "#38BDF8",
        "desc_line1": "Comprehensive codebase covering Python OOP,",
        "desc_line2": "algorithms, and 40+ practical applications.",
        "tags": ["Python", "40+ Projects", "OOP"]
    }
]

def render_project_card(p):
    width = 295
    height = 136
    dom_color = p["domain_color"]
    title = p["title"]
    if len(title) > 20:
        display_title = title[:18] + ".."
    else:
        display_title = title

    # Render tags
    tag_x = 16
    tag_svgs = []
    for tag in p["tags"]:
        # approximate tag width
        tag_w = len(tag) * 6.5 + 14
        tag_svgs.append(f'''
        <g transform="translate({tag_x}, 104)">
            <rect x="0" y="0" width="{tag_w}" height="18" rx="9" fill="rgba(255, 255, 255, 0.04)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="0.8"/>
            <text x="{tag_w / 2}" y="12.5" text-anchor="middle" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
                {tag}
            </text>
        </g>
        ''')
        tag_x += tag_w + 6

    tags_content = "".join(tag_svgs)

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient matching HackerRank card -->
    <linearGradient id="bg-grad-{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="50%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>

    <!-- Border Gradient with Emerald/Cyan touch -->
    <linearGradient id="border-grad-{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{dom_color}" stop-opacity="0.4" />
      <stop offset="40%" stop-color="#00EA64" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.05" />
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-{p['id']}" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="{dom_color}" flood-opacity="0.35"/>
    </filter>
  </defs>

  <!-- Card Background -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="14" fill="url(#bg-grad-{p['id']})" stroke="url(#border-grad-{p['id']})" stroke-width="1.2" />

  <!-- Ambient Light Corner Glow -->
  <circle cx="25" cy="25" r="45" fill="{dom_color}" opacity="0.06" />

  <!-- Header: Icon + Title + Domain Badge -->
  <g transform="translate(16, 16)">
    <!-- Repo Book Icon -->
    <g transform="translate(0, 1)">
      <path d="M2 1.5C2 0.67 2.67 0 3.5 0H12.5C13.33 0 14 0.67 14 1.5V12C14 12.83 13.33 13.5 12.5 13.5H3.5C2.67 13.5 2 12.83 2 12V1.5Z" stroke="{dom_color}" stroke-width="1.5" fill="none"/>
      <path d="M5 4H11M5 7H9" stroke="{dom_color}" stroke-width="1.3" stroke-linecap="round"/>
    </g>

    <!-- Title -->
    <text x="22" y="12" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700" letter-spacing="-0.2px">
      {display_title}
    </text>

    <!-- External Link Arrow -->
    <g transform="translate({width - 32 - 14}, 2)">
      <path d="M1 9L9 1M9 1H3M9 1V7" stroke="#64748B" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </g>

  <!-- Domain Tag / Category Pill -->
  <g transform="translate(16, 38)">
    <rect x="0" y="0" width="{len(p['domain']) * 6.5 + 20}" height="17" rx="8.5" fill="{dom_color}" fill-opacity="0.1" stroke="{dom_color}" stroke-opacity="0.3" stroke-width="0.8"/>
    <circle cx="8" cy="8.5" r="2.5" fill="{dom_color}" filter="url(#glow-{p['id']})"/>
    <text x="16" y="12" fill="{dom_color}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="700" letter-spacing="0.3px">
      {p['domain'].upper()}
    </text>
  </g>

  <!-- Description (2 lines) -->
  <g transform="translate(16, 68)">
    <text x="0" y="0" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="400">
      {p['desc_line1']}
    </text>
    <text x="0" y="15" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="400">
      {p['desc_line2']}
    </text>
  </g>

  <!-- Footer Tags -->
  {tags_content}
</svg>
'''
    return svg

out_dir = "C:/Users/MELIODAS/.gemini/antigravity/scratch/BadrKandri/assets/projects"
os.makedirs(out_dir, exist_ok=True)

for p in projects:
    svg_code = render_project_card(p)
    file_path = os.path.join(out_dir, f"{p['id']}.svg")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_code)

print("Generated all 6 project cards successfully!")
