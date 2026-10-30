import os
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

# 6 Core Roadmap Nodes and their metadata
CORE_CATEGORIES = [
    {"name": "Arrays & Hashing", "total": 9, "easy": 3, "medium": 6, "hard": 0},
    {"name": "Two Pointers", "total": 5, "easy": 1, "medium": 3, "hard": 1},
    {"name": "Stack", "total": 7, "easy": 1, "medium": 5, "hard": 1},
    {"name": "Binary Search", "total": 7, "easy": 1, "medium": 5, "hard": 1},
    {"name": "Sliding Window", "total": 6, "easy": 1, "medium": 3, "hard": 2},
    {"name": "Linked List", "total": 11, "easy": 3, "medium": 6, "hard": 2},
]

# Slug to (category, difficulty, problem_name)
NEETCODE_150_MAP = {
    # Arrays & Hashing (9)
    "duplicate-integer": ("Arrays & Hashing", "Easy", "Contains Duplicate"),
    "is-anagram": ("Arrays & Hashing", "Easy", "Valid Anagram"),
    "two-integer-sum": ("Arrays & Hashing", "Easy", "Two Sum"),
    "anagram-groups": ("Arrays & Hashing", "Medium", "Group Anagrams"),
    "top-k-elements-in-list": ("Arrays & Hashing", "Medium", "Top K Frequent Elements"),
    "products-of-array-discluding-self": ("Arrays & Hashing", "Medium", "Product of Array Except Self"),
    "valid-sudoku": ("Arrays & Hashing", "Medium", "Valid Sudoku"),
    "string-encode-and-decode": ("Arrays & Hashing", "Medium", "Encode and Decode Strings"),
    "longest-consecutive-sequence": ("Arrays & Hashing", "Medium", "Longest Consecutive Sequence"),

    # Two Pointers (5)
    "is-palindrome": ("Two Pointers", "Easy", "Valid Palindrome"),
    "two-integer-sum-ii": ("Two Pointers", "Medium", "Two Sum II"),
    "three-integer-sum": ("Two Pointers", "Medium", "3Sum"),
    "max-water-container": ("Two Pointers", "Medium", "Container With Most Water"),
    "trapping-rain-water": ("Two Pointers", "Hard", "Trapping Rain Water"),

    # Sliding Window (6)
    "buy-and-sell-crypto": ("Sliding Window", "Easy", "Best Time to Buy And Sell Stock"),
    "longest-substring-without-duplicates": ("Sliding Window", "Medium", "Longest Substring Without Repeating Characters"),
    "longest-repeating-substring-with-replacement": ("Sliding Window", "Medium", "Longest Repeating Character Replacement"),
    "permutation-string": ("Sliding Window", "Medium", "Permutation In String"),
    "minimum-window-with-characters": ("Sliding Window", "Hard", "Minimum Window Substring"),
    "sliding-window-maximum": ("Sliding Window", "Hard", "Sliding Window Maximum"),

    # Stack (7)
    "validate-parentheses": ("Stack", "Easy", "Valid Parentheses"),
    "minimum-stack": ("Stack", "Medium", "Min Stack"),
    "evaluate-reverse-polish-notation": ("Stack", "Medium", "Evaluate Reverse Polish Notation"),
    "generate-parentheses": ("Stack", "Medium", "Generate Parentheses"),
    "daily-temperatures": ("Stack", "Medium", "Daily Temperatures"),
    "car-fleet": ("Stack", "Medium", "Car Fleet"),
    "largest-rectangle-in-histogram": ("Stack", "Hard", "Largest Rectangle In Histogram"),

    # Binary Search (7)
    "binary-search": ("Binary Search", "Easy", "Binary Search"),
    "search-2d-matrix": ("Binary Search", "Medium", "Search a 2D Matrix"),
    "eating-bananas": ("Binary Search", "Medium", "Koko Eating Bananas"),
    "find-minimum-in-rotated-sorted-array": ("Binary Search", "Medium", "Find Minimum In Rotated Sorted Array"),
    "find-target-in-rotated-sorted-array": ("Binary Search", "Medium", "Search In Rotated Sorted Array"),
    "time-based-key-value-store": ("Binary Search", "Medium", "Time Based Key-Value Store"),
    "median-of-two-sorted-arrays": ("Binary Search", "Hard", "Median of Two Sorted Arrays"),

    # Linked List (11)
    "reverse-a-linked-list": ("Linked List", "Easy", "Reverse Linked List"),
    "merge-two-sorted-linked-lists": ("Linked List", "Easy", "Merge Two Sorted Lists"),
    "reorder-linked-list": ("Linked List", "Medium", "Reorder List"),
    "remove-node-from-end-of-linked-list": ("Linked List", "Medium", "Remove Nth Node From End of List"),
    "copy-linked-list-with-random-pointer": ("Linked List", "Medium", "Copy List With Random Pointer"),
    "add-two-numbers": ("Linked List", "Medium", "Add Two Numbers"),
    "linked-list-cycle-detection": ("Linked List", "Easy", "Linked List Cycle"),
    "find-duplicate-integer": ("Linked List", "Medium", "Find The Duplicate Number"),
    "lru-cache": ("Linked List", "Medium", "LRU Cache"),
    "merge-k-sorted-linked-lists": ("Linked List", "Hard", "Merge K Sorted Lists"),
    "reverse-nodes-in-k-group": ("Linked List", "Hard", "Reverse Nodes In K Group"),
}

def fetch_solved_problems_from_repo(repo_owner="BadrKandri", repo_name="neetcode-submissions"):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/git/trees/main?recursive=1"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    solved_slugs = set()
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        for item in data.get("tree", []):
            path = item.get("path", "")
            if path.startswith("Data Structures & Algorithms/"):
                parts = path.split("/")
                if len(parts) >= 2 and parts[1]:
                    solved_slugs.add(parts[1])
        print(f"Fetched {len(solved_slugs)} solved problems from {repo_owner}/{repo_name}")
    except Exception as e:
        print(f"Warning: Could not fetch from GitHub API ({e}). Using known solved set.")
        solved_slugs = {
            "duplicate-integer",
            "is-anagram",
            "two-integer-sum",
            "anagram-groups",
            "top-k-elements-in-list",
            "products-of-array-discluding-self",
            "longest-consecutive-sequence",
            "validate-parentheses",
            "minimum-stack",
            "evaluate-reverse-polish-notation",
            "daily-temperatures",
        }
    return solved_slugs

def compute_roadmap_stats(solved_slugs):
    node_data = {c["name"]: {**c, "solved": 0} for c in CORE_CATEGORIES}
    diff_solved = {"Easy": 0, "Medium": 0, "Hard": 0}

    for slug in solved_slugs:
        if slug in NEETCODE_150_MAP:
            cat, diff, name = NEETCODE_150_MAP[slug]
            if cat in node_data:
                node_data[cat]["solved"] += 1
                if diff in diff_solved:
                    diff_solved[diff] += 1

    return node_data, diff_solved

def render_roadmap_tree_card(node_data, diff_solved):
    width = 780
    height = 310

    total_solved = sum(c["solved"] for c in node_data.values())
    grand_total = sum(c["total"] for c in node_data.values())
    pct = round((total_solved / grand_total) * 100, 1) if grand_total > 0 else 0
    master_fill_w = max(6, int((total_solved / grand_total) * 732)) if total_solved > 0 else 0

    tot_easy = sum(c["easy"] for c in node_data.values())
    tot_med = sum(c["medium"] for c in node_data.values())
    tot_hard = sum(c["hard"] for c in node_data.values())

    # Node positions (Exact hierarchy from NeetCode Roadmap)
    # L1: Arrays & Hashing (Center: 390)
    # L2: Two Pointers (Center: 240), Stack (Center: 540)
    # L3: Binary Search (Center: 145), Sliding Window (Center: 390), Linked List (Center: 635)
    nodes = {
        "Arrays & Hashing": {"x": 285, "y": 74, "w": 210, "h": 50},
        "Two Pointers": {"x": 140, "y": 148, "w": 200, "h": 50},
        "Stack": {"x": 440, "y": 148, "w": 200, "h": 50},
        "Binary Search": {"x": 40, "y": 222, "w": 210, "h": 50},
        "Sliding Window": {"x": 285, "y": 222, "w": 210, "h": 50},
        "Linked List": {"x": 530, "y": 222, "w": 210, "h": 50},
    }

    # Connector cables
    # Active solved path (Arrays -> Stack) glows emerald
    cables_svg = '''
    <!-- Connecting Cables -->
    <g stroke-linecap="round" fill="none">
      <!-- Arrays & Hashing -> Two Pointers -->
      <path d="M 390 124 C 390 138, 240 134, 240 148" stroke="#334155" stroke-width="2"/>
      
      <!-- Arrays & Hashing -> Stack (Active Solved Path) -->
      <path d="M 390 124 C 390 138, 540 134, 540 148" stroke="#00EA64" stroke-opacity="0.65" stroke-width="2">
        <animate attributeName="stroke-opacity" values="0.45;0.85;0.45" dur="3s" repeatCount="indefinite"/>
      </path>

      <!-- Two Pointers -> Binary Search -->
      <path d="M 240 198 C 240 212, 145 208, 145 222" stroke="#334155" stroke-width="1.8"/>

      <!-- Two Pointers -> Sliding Window -->
      <path d="M 240 198 C 240 212, 390 208, 390 222" stroke="#334155" stroke-width="1.8"/>

      <!-- Two Pointers -> Linked List -->
      <path d="M 240 198 C 240 212, 635 208, 635 222" stroke="#334155" stroke-width="1.8"/>

      <!-- Outgoing Cables to Future Categories (Subtle Dash) -->
      <path d="M 145 272 C 145 284, 200 290, 200 300" stroke="#334155" stroke-width="1.4" stroke-dasharray="3 3" opacity="0.35"/>
      <path d="M 390 272 C 390 284, 390 290, 390 300" stroke="#334155" stroke-width="1.4" stroke-dasharray="3 3" opacity="0.35"/>
      <path d="M 635 272 C 635 284, 580 290, 580 300" stroke="#334155" stroke-width="1.4" stroke-dasharray="3 3" opacity="0.35"/>
    </g>
    '''

    # Render Node boxes
    nodes_svg = []
    for name, pos in nodes.items():
        data = node_data[name]
        solved = data["solved"]
        tot = data["total"]
        w = pos["w"]
        h = pos["h"]
        x = pos["x"]
        y = pos["y"]
        bar_w = w - 32
        fill_w = int((solved / tot) * bar_w) if tot > 0 else 0
        clean_name = name.replace("&", "&amp;")

        if solved > 0:
            border_stroke = "#00EA64"
            border_opacity = "0.55"
            bar_svg = f'''
              <rect x="16" y="32" width="{bar_w}" height="5" rx="2.5" fill="rgba(255, 255, 255, 0.08)"/>
              <rect x="16" y="32" width="{max(6, fill_w)}" height="5" rx="2.5" fill="#00EA64">
                <animate attributeName="opacity" values="0.85;1;0.85" dur="2.5s" repeatCount="indefinite"/>
              </rect>
              <circle cx="{16 + max(6, fill_w)}" cy="34.5" r="2.2" fill="#FFFFFF"/>
            '''
            num_svg = f'<tspan fill="#00EA64" font-weight="700">{solved}</tspan><tspan fill="#64748B">/{tot}</tspan>'
            node_bg = "#1B2233"
        else:
            border_stroke = "rgba(255, 255, 255, 0.12)"
            border_opacity = "0.2"
            bar_svg = f'<rect x="16" y="32" width="{bar_w}" height="5" rx="2.5" fill="rgba(255, 255, 255, 0.08)"/>'
            num_svg = f'<tspan fill="#64748B">0/{tot}</tspan>'
            node_bg = "#161B28"

        nodes_svg.append(f'''
        <g transform="translate({x}, {y})">
          <!-- Node Background -->
          <rect x="0" y="0" width="{w}" height="{h}" rx="10" fill="{node_bg}" stroke="{border_stroke}" stroke-opacity="{border_opacity}" stroke-width="1.2"/>
          <!-- Title -->
          <text x="16" y="21" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700">
            {clean_name}
          </text>
          <!-- Solved Fraction -->
          <text x="{w - 16}" y="21" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11">
            {num_svg}
          </text>
          <!-- Progress Track -->
          {bar_svg}
        </g>
        ''')

    all_nodes = "".join(nodes_svg)

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="tree-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A0E17"/>
      <stop offset="50%" stop-color="#0E1422"/>
      <stop offset="100%" stop-color="#121826"/>
    </linearGradient>

    <!-- Border Gradient -->
    <linearGradient id="tree-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00EA64" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#38BDF8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0.45"/>
    </linearGradient>

    <!-- Master Progress Gradient -->
    <linearGradient id="tree-master-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00EA64"/>
      <stop offset="60%" stop-color="#38BDF8"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>

    <!-- Glow Filter -->
    <filter id="glow-tree" x="-50%" y="-50%" width="200%" height="200%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#00EA64" flood-opacity="0.5"/>
    </filter>
    <filter id="laser-glow" x="-100%" y="-100%" width="300%" height="300%">
      <feDropShadow dx="0" dy="0" stdDeviation="2.5" flood-color="#00EA64" flood-opacity="0.9"/>
    </filter>

    <!-- Dot Matrix Pattern -->
    <pattern id="dot-matrix" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#FFFFFF" opacity="0.04"/>
    </pattern>
  </defs>

  <!-- Card Background -->
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="16" fill="url(#tree-bg)" stroke="url(#tree-border)" stroke-width="1.2">
    <animate attributeName="stroke-opacity" values="0.35;0.7;0.35" dur="4s" repeatCount="indefinite"/>
  </rect>

  <!-- Dot Matrix Grid Canvas -->
  <rect x="2" y="2" width="{width - 4}" height="{height - 4}" rx="15" fill="url(#dot-matrix)"/>

  <!-- Ambient Light Corner Glows -->
  <circle cx="35" cy="35" r="75" fill="#00EA64" opacity="0.05">
    <animate attributeName="opacity" values="0.03;0.09;0.03" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{width - 35}" cy="35" r="75" fill="#A855F7" opacity="0.04">
    <animate attributeName="opacity" values="0.03;0.08;0.03" begin="2s" dur="4s" repeatCount="indefinite"/>
  </circle>

  <!-- Header Section -->
  <g transform="translate(24, 18)">
    <!-- Puzzle Piece Icon -->
    <g transform="translate(0, 1)">
      <path d="M7 2H10V4C11.1 4 12 4.9 12 6C12 7.1 11.1 8 10 8V10H8C8 8.9 7.1 8 6 8C4.9 8 4 8.9 4 10H2V7C3.1 7 4 6.1 4 5C4 3.9 3.1 3 2 3V2H5C5 3.1 5.9 4 7 4C8.1 4 9 3.1 9 2H7Z" stroke="#00EA64" stroke-width="1.4" fill="#00EA64" fill-opacity="0.15" stroke-linejoin="round"/>
    </g>

    <!-- Title -->
    <text x="20" y="12" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="700">
      NeetCode Roadmap Tracker
    </text>

    <!-- Domain Pill -->
    <g transform="translate(216, 0)">
      <rect x="0" y="0" width="168" height="17" rx="8.5" fill="#00EA64" fill-opacity="0.08" stroke="#00EA64" stroke-opacity="0.25" stroke-width="0.8"/>
      <!-- Radar Pulse -->
      <circle cx="8" cy="8.5" r="2.5" fill="none" stroke="#00EA64" stroke-width="0.8">
        <animate attributeName="r" values="2.5;6.5" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.75;0" dur="2s" repeatCount="indefinite"/>
      </circle>
      <circle cx="8" cy="8.5" r="2.5" fill="#00EA64" filter="url(#glow-tree)">
        <animate attributeName="r" values="2.5;3.1;2.5" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="16" y="12" fill="#00EA64" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="8.5" font-weight="700" letter-spacing="0.3px">
        CORE DATA STRUCTURES
      </text>
    </g>

    <!-- Total Counter -->
    <g transform="translate({width - 48 - 145}, 0)">
      <text x="0" y="12" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5">
        Solved: <tspan fill="#00EA64" font-weight="700" font-size="12">{total_solved} / {grand_total}</tspan> <tspan fill="#64748B">({pct}%)</tspan>
      </text>
    </g>

    <!-- Master Progress Track -->
    <rect x="0" y="27" width="732" height="5" rx="2.5" fill="rgba(255, 255, 255, 0.05)"/>
    <rect x="0" y="27" width="{master_fill_w}" height="5" rx="2.5" fill="url(#tree-master-grad)"/>

    <!-- Active Scanner Beam -->
    <circle cy="29.5" r="2.2" fill="#00EA64" filter="url(#laser-glow)">
      <animate attributeName="cx" values="0;{master_fill_w};0" dur="2.8s" repeatCount="indefinite" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1"/>
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2.8s" repeatCount="indefinite"/>
    </circle>

    <!-- Divider Line -->
    <line x1="0" y1="42" x2="732" y2="42" stroke="rgba(255, 255, 255, 0.05)" stroke-width="1" />
  </g>

  <!-- Connectors -->
  {cables_svg}

  <!-- Roadmap Nodes -->
  {all_nodes}

  <!-- Bottom Legend Bar -->
  <g transform="translate(24, 282)">
    <!-- Easy -->
    <circle cx="6" cy="5" r="2.5" fill="#00EA64"/>
    <text x="14" y="8" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Easy: <tspan fill="#00EA64" font-weight="700">{diff_solved['Easy']}</tspan><tspan fill="#64748B">/{tot_easy}</tspan>
    </text>

    <!-- Medium -->
    <circle cx="110" cy="5" r="2.5" fill="#F59E0B"/>
    <text x="118" y="8" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Medium: <tspan fill="#F59E0B" font-weight="700">{diff_solved['Medium']}</tspan><tspan fill="#64748B">/{tot_med}</tspan>
    </text>

    <!-- Hard -->
    <circle cx="230" cy="5" r="2.5" fill="#EF4444"/>
    <text x="238" y="8" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Hard: <tspan fill="#EF4444" font-weight="700">{diff_solved['Hard']}</tspan><tspan fill="#64748B">/{tot_hard}</tspan>
    </text>

    <!-- Right Tag -->
    <text x="732" y="8" text-anchor="end" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="600">
      PHASE 1: CORE DATA STRUCTURES &#183; {total_solved}/{grand_total} SOLVED
    </text>
  </g>
</svg>'''
    return svg

def main():
    target_dirs = [
        "assets/neetcode"
    ]
    solved_slugs = fetch_solved_problems_from_repo()
    node_data, diff_solved = compute_roadmap_stats(solved_slugs)
    svg_code = render_roadmap_tree_card(node_data, diff_solved)

    # Validate XML
    ET.fromstring(svg_code)

    for out_dir in target_dirs:
        os.makedirs(out_dir, exist_ok=True)
        for prefix in ["", "card_", "card_v1_", "card_v2_", "card_v3_"]:
            file_path = os.path.join(out_dir, f"{prefix}neetcode.svg")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_code)

    total_solved = sum(c["solved"] for c in node_data.values())
    print(f"Generated 6-node NeetCode Roadmap Tree with {total_solved} solved problems ({diff_solved})!")

if __name__ == "__main__":
    main()
