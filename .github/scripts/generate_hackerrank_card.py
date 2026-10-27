import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone

def render_star_svg(filled=True):
    points = "7,0.5 9,5 13.8,5.4 10.1,8.6 11.2,13.4 7,10.8 2.8,13.4 3.9,8.6 0.2,5.4 5,5"
    if filled:
        return f'<polygon points="{points}" fill="url(#gold-star-grad)" filter="url(#star-glow)"/>'
    else:
        return f'<polygon points="{points}" fill="#1E2633" stroke="#2D3748" stroke-width="0.8"/>'

def get_track_color(title):
    title_lower = title.lower()
    if "python" in title_lower:
        return "#38BDF8"
    elif "problem" in title_lower or "algorithm" in title_lower:
        return "#00EA64"
    elif "sql" in title_lower or "database" in title_lower:
        return "#F59E0B"
    elif "30 days" in title_lower:
        return "#EC4899"
    elif "data structure" in title_lower:
        return "#A855F7"
    elif "java" in title_lower:
        return "#F97316"
    elif "c++" in title_lower:
        return "#06B6D4"
    elif "javascript" in title_lower or "js" in title_lower:
        return "#EAB308"
    elif "c" == title_lower or "c language" in title_lower:
        return "#64748B"
    return "#00EA64"

def generate_svg(data):
    username = data.get("username", "badr_kandri_10")
    country = data.get("country", "Morocco")
    level = data.get("level", 5)
    challenges_solved = data.get("challenges_solved", 0)
    stars_earned = data.get("stars_earned", 0)
    badges = data.get("badges", [])
    badges_count = len([b for b in badges if b.get("stars", 0) > 0 or b.get("solved", 0) > 0]) or len(badges)
    updated_date = data.get("updated_date", datetime.now(timezone.utc).strftime("%Y-%m-%d"))

    card_width = 600
    base_top = 188
    badge_row_height = 40
    
    if len(badges) == 0:
        badges_section_height = 70
    else:
        badges_section_height = 36 + len(badges) * badge_row_height + 12
        
    card_height = base_top + badges_section_height + 46

    display_username = f"@{username}"
    if len(display_username) > 28:
        display_username = display_username[:25] + "..."

    badges_svg = []
    if len(badges) == 0:
        badges_svg.append(f'''
        <g transform="translate(24, {base_top + 36})">
            <rect x="0" y="0" width="{card_width - 48}" height="46" rx="10" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1"/>
            <text x="{(card_width - 48) / 2}" y="28" text-anchor="middle" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif" font-size="12" font-weight="500">
                🌱 No badges yet. Solve challenges on HackerRank to unlock skill badges!
            </text>
        </g>
        ''')
    else:
        start_y = base_top + 34
        for idx, badge in enumerate(badges):
            row_y = start_y + idx * badge_row_height
            title = badge.get("title") or badge.get("badge_name", "Skill")
            solved = badge.get("solved", 0)
            stars = badge.get("stars", 0)
            max_stars = 6 if (title.lower() in ["30 days of code", "problem solving"] or stars > 5) else 5

            track_color = get_track_color(title)
            
            stars_svg = []
            star_spacing = 18
            for s in range(max_stars):
                is_filled = s < stars
                sx = s * star_spacing
                star_poly = render_star_svg(is_filled)
                stars_svg.append(f'<g transform="translate({sx}, 0)">{star_poly}</g>')

            stars_group = "".join(stars_svg)
            
            row = f'''
            <g transform="translate(24, {row_y})">
                <!-- Row background -->
                <rect x="0" y="0" width="{card_width - 48}" height="34" rx="8" fill="rgba(255, 255, 255, 0.02)" stroke="rgba(255, 255, 255, 0.04)" stroke-width="1"/>
                
                <!-- Track indicator pill / dot -->
                <circle cx="16" cy="17" r="4.5" fill="{track_color}" filter="url(#glow-{track_color.replace('#', '')})"/>
                
                <!-- Title -->
                <text x="30" y="22" fill="#F1F5F9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif" font-size="13" font-weight="600">
                    {title}
                </text>
                
                <!-- Solved count pill -->
                <rect x="284" y="8" width="82" height="18" rx="9" fill="rgba(255, 255, 255, 0.05)"/>
                <text x="325" y="21" text-anchor="middle" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif" font-size="11" font-weight="500">
                    {solved} solved
                </text>
                
                <!-- Star Rating -->
                <g transform="translate({card_width - 48 - (max_stars * star_spacing) - 12}, 10)">
                    {stars_group}
                </g>
            </g>
            '''
            badges_svg.append(row)

    badges_content = "\n".join(badges_svg)

    svg = f'''<svg width="{card_width}" height="{card_height}" viewBox="0 0 {card_width} {card_height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17" />
      <stop offset="45%" stop-color="#0E1422" />
      <stop offset="100%" stop-color="#121826" />
    </linearGradient>

    <!-- Outer Border Gradient -->
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00EA64" stop-opacity="0.45" />
      <stop offset="30%" stop-color="#22C55E" stop-opacity="0.2" />
      <stop offset="70%" stop-color="#38BDF8" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.06" />
    </linearGradient>

    <!-- Stat Box Background -->
    <linearGradient id="stat-box-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#161F2E" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#0F1622" stop-opacity="0.95" />
    </linearGradient>

    <!-- Gold Star Gradient -->
    <linearGradient id="gold-star-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE047" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>

    <!-- Star Glow Filter -->
    <filter id="star-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="1.5" flood-color="#F59E0B" flood-opacity="0.45"/>
    </filter>

    <!-- Dynamic Color Filters -->
    <filter id="glow-00EA64" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#00EA64" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-38BDF8" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#38BDF8" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-F59E0B" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#F59E0B" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-EC4899" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#EC4899" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-A855F7" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#A855F7" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-F97316" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#F97316" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-06B6D4" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#06B6D4" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-EAB308" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#EAB308" flood-opacity="0.45"/>
    </filter>
    <filter id="glow-64748B" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#64748B" flood-opacity="0.45"/>
    </filter>
  </defs>

  <style>
    .font-title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif; font-size: 17px; font-weight: 700; fill: #FFFFFF; letter-spacing: -0.2px; }}
    .font-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif; font-size: 12px; font-weight: 400; fill: #94A3B8; }}
    .font-stat-num {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif; font-size: 25px; font-weight: 800; fill: #FFFFFF; letter-spacing: -0.5px; }}
    .font-stat-lbl {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif; font-size: 11px; font-weight: 500; fill: #94A3B8; letter-spacing: 0.2px; }}
    .font-sec-hdr {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif; font-size: 10px; font-weight: 700; fill: #64748B; letter-spacing: 1.2px; }}
  </style>

  <!-- Main Card Container -->
  <rect x="1" y="1" width="{card_width - 2}" height="{card_height - 2}" rx="16" fill="url(#bg-grad)" stroke="url(#card-border)" stroke-width="1.5" />

  <!-- Ambient Glow top left -->
  <ellipse cx="65" cy="55" rx="100" ry="75" fill="#00EA64" opacity="0.07" />

  <!-- HEADER -->
  <g transform="translate(24, 22)">
    <!-- HackerRank Official Logo Mark -->
    <g transform="translate(0, 2)">
      <rect x="0" y="0" width="34" height="34" rx="9" fill="#00EA64" />
      <path d="M10 8.5H13.2V14.3H20.8V8.5H24V25.5H20.8V17.5H13.2V25.5H10V8.5Z" fill="#09141E" />
    </g>

    <!-- Platform Name & User Info -->
    <text x="44" y="18" class="font-title">HackerRank</text>
    <text x="44" y="34" class="font-sub">
      <tspan fill="#38BDF8" font-weight="600">{display_username}</tspan>
      <tspan fill="#475569"> • </tspan>
      <tspan fill="#94A3B8">{country}</tspan>
    </text>

    <!-- Level Pill (Top Right) -->
    <g transform="translate({card_width - 48 - 88}, 5)">
      <rect x="0" y="0" width="88" height="27" rx="13.5" fill="rgba(0, 234, 100, 0.12)" stroke="rgba(0, 234, 100, 0.35)" stroke-width="1"/>
      <circle cx="15" cy="13.5" r="3.5" fill="#00EA64" filter="url(#glow-00EA64)"/>
      <text x="25" y="17.5" fill="#00EA64" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="700" letter-spacing="0.5px">
        LEVEL {level}
      </text>
    </g>
  </g>

  <!-- 3 HERO STAT BOXES -->
  <g transform="translate(24, 76)">
    <!-- Box 1: Challenges Solved -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="176" height="74" rx="12" fill="url(#stat-box-bg)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>
      <circle cx="28" cy="27" r="13" fill="rgba(0, 234, 100, 0.12)"/>
      <!-- Checkmark / target icon -->
      <path d="M23 27L26.5 30.5L33 24" stroke="#00EA64" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="49" y="34" class="font-stat-num">{challenges_solved}</text>
      <text x="16" y="58" class="font-stat-lbl">Challenges solved</text>
    </g>

    <!-- Box 2: Stars Earned -->
    <g transform="translate(188, 0)">
      <rect x="0" y="0" width="176" height="74" rx="12" fill="url(#stat-box-bg)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>
      <circle cx="28" cy="27" r="13" fill="rgba(245, 158, 11, 0.14)"/>
      <!-- Star icon -->
      <polygon points="28,20 29.8,24 34.2,24.4 30.8,27.3 31.8,31.6 28,29.3 24.2,31.6 25.2,27.3 21.8,24.4 26.2,24" fill="#F59E0B"/>
      <text x="49" y="34" class="font-stat-num">{stars_earned}</text>
      <text x="16" y="58" class="font-stat-lbl">Stars earned</text>
    </g>

    <!-- Box 3: Badges -->
    <g transform="translate(376, 0)">
      <rect x="0" y="0" width="176" height="74" rx="12" fill="url(#stat-box-bg)" stroke="rgba(255, 255, 255, 0.06)" stroke-width="1"/>
      <circle cx="28" cy="27" r="13" fill="rgba(56, 189, 248, 0.14)"/>
      <!-- Trophy icon -->
      <path d="M24 21.5H32V25.5C32 27.7 30.2 29.5 28 29.5C25.8 29.5 24 27.7 24 25.5V21.5Z" stroke="#38BDF8" stroke-width="1.8" fill="none"/>
      <path d="M28 29.5V32.5M25 32.5H31" stroke="#38BDF8" stroke-width="1.8" stroke-linecap="round"/>
      <text x="49" y="34" class="font-stat-num">{badges_count}</text>
      <text x="16" y="58" class="font-stat-lbl">Badges unlocked</text>
    </g>
  </g>

  <!-- BADGES SECTION HEADER -->
  <g transform="translate(24, 168)">
    <line x1="0" y1="0" x2="{card_width - 48}" y2="0" stroke="rgba(255, 255, 255, 0.07)" stroke-width="1" />
    <text x="0" y="18" class="font-sec-hdr">BADGES &amp; SKILLS</text>
  </g>

  <!-- BADGES LIST -->
  {badges_content}

  <!-- FOOTER -->
  <g transform="translate(24, {card_height - 18})">
    <line x1="0" y1="-8" x2="{card_width - 48}" y2="-8" stroke="rgba(255, 255, 255, 0.04)" stroke-width="1" />
    <text x="0" y="4" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="500">
      ⚡ Live HackerRank Telemetry
    </text>
    <text x="{card_width - 48}" y="4" text-anchor="end" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="500">
      Updated {updated_date} (UTC)
    </text>
  </g>
</svg>
'''
    return svg

def fetch_json(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Warning: Failed to fetch {url}: {e}", file=sys.stderr)
    return None

def fetch_hackerrank_data(username="badr_kandri_10"):
    profile_url = f"https://www.hackerrank.com/rest/contests/master/hackers/{username}/profile"
    badges_url = f"https://www.hackerrank.com/rest/hackers/{username}/badges"

    profile_data = fetch_json(profile_url)
    badges_data = fetch_json(badges_url)

    # Defaults matching current known profile in case of API hiccups
    country = "Morocco"
    level = 5
    if profile_data and isinstance(profile_data, dict):
        model = profile_data.get("model", {})
        if isinstance(model, dict):
            country = model.get("country") or country
            level = model.get("level") or level

    # Parse badges
    raw_badges = []
    if badges_data and isinstance(badges_data, dict):
        if "models" in badges_data and isinstance(badges_data["models"], list):
            raw_badges = badges_data["models"]
        elif "model" in badges_data:
            if isinstance(badges_data["model"], list):
                raw_badges = badges_data["model"]
            elif isinstance(badges_data["model"], dict):
                raw_badges = badges_data["model"].get("badges", [])

    badges = []
    for item in raw_badges:
        if not isinstance(item, dict):
            continue
        hacker_badge = item.get("hacker_badge") if isinstance(item.get("hacker_badge"), dict) else {}
        title = (
            item.get("badge_name") 
            or item.get("title") 
            or hacker_badge.get("title")
            or hacker_badge.get("badge_name")
            or item.get("badge_type", "")
        )
        if not title:
            continue
            
        stars = (
            item.get("stars") 
            or item.get("current_star") 
            or hacker_badge.get("stars") 
            or hacker_badge.get("current_star") 
            or 0
        )
        solved = (
            item.get("solved") 
            or item.get("challenges_solved") 
            or hacker_badge.get("solved") 
            or hacker_badge.get("challenges_solved") 
            or 0
        )
        
        badges.append({
            "title": title.strip(),
            "stars": int(stars),
            "solved": int(solved)
        })

    # If API returned no badges or failed, preserve current known stats
    if not badges:
        badges = [{"title": "Python", "solved": 1, "stars": 1}]

    challenges_solved = sum(b["solved"] for b in badges)
    stars_earned = sum(b["stars"] for b in badges)

    return {
        "username": username,
        "country": country,
        "level": level,
        "challenges_solved": challenges_solved,
        "stars_earned": stars_earned,
        "badges": badges,
        "updated_date": datetime.now(timezone.utc).strftime("%Y-%m-%d")
    }

def main():
    username = os.environ.get("HACKERRANK_USERNAME", "badr_kandri_10")
    output_path = os.environ.get("OUTPUT_PATH", "assets/hackerrank-card.svg")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"Fetching HackerRank statistics for @{username}...")
    data = fetch_hackerrank_data(username)
    print(f"Data retrieved: {data['challenges_solved']} solved, {data['stars_earned']} stars, {len(data['badges'])} badges")

    svg_content = generate_svg(data)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated card at: {output_path}")

if __name__ == "__main__":
    main()
