import os
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

# Full mapping of NeetCode 150 problem slugs to category & difficulty
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

    # Trees (15)
    "invert-a-binary-tree": ("Trees", "Easy", "Invert Binary Tree"),
    "depth-of-binary-tree": ("Trees", "Easy", "Maximum Depth of Binary Tree"),
    "binary-tree-diameter": ("Trees", "Easy", "Diameter of Binary Tree"),
    "balanced-binary-tree": ("Trees", "Easy", "Balanced Binary Tree"),
    "same-binary-tree": ("Trees", "Easy", "Same Tree"),
    "subtree-of-a-binary-tree": ("Trees", "Easy", "Subtree of Another Tree"),
    "lowest-common-ancestor-in-binary-search-tree": ("Trees", "Medium", "Lowest Common Ancestor of a BST"),
    "level-order-traversal-of-binary-tree": ("Trees", "Medium", "Binary Tree Level Order Traversal"),
    "binary-tree-right-side-view": ("Trees", "Medium", "Binary Tree Right Side View"),
    "count-good-nodes-in-binary-tree": ("Trees", "Medium", "Count Good Nodes In Binary Tree"),
    "valid-binary-search-tree": ("Trees", "Medium", "Validate Binary Search Tree"),
    "kth-smallest-integer-in-bst": ("Trees", "Medium", "Kth Smallest Element In a BST"),
    "construct-binary-tree-from-preorder-and-inorder-traversal": ("Trees", "Medium", "Construct Binary Tree From Preorder & Inorder"),
    "binary-tree-maximum-path-sum": ("Trees", "Hard", "Binary Tree Maximum Path Sum"),
    "serialize-and-deserialize-binary-tree": ("Trees", "Hard", "Serialize And Deserialize Binary Tree"),

    # Heap / Priority Queue (7)
    "kth-largest-integer-in-a-stream": ("Heap / Priority Queue", "Easy", "Kth Largest Element In a Stream"),
    "last-stone-weight": ("Heap / Priority Queue", "Easy", "Last Stone Weight"),
    "k-closest-points-to-origin": ("Heap / Priority Queue", "Medium", "K Closest Points to Origin"),
    "kth-largest-element-in-an-array": ("Heap / Priority Queue", "Medium", "Kth Largest Element In An Array"),
    "task-scheduler": ("Heap / Priority Queue", "Medium", "Task Scheduler"),
    "design-twitter-feed": ("Heap / Priority Queue", "Medium", "Design Twitter"),
    "find-median-in-a-data-stream": ("Heap / Priority Queue", "Hard", "Find Median From Data Stream"),

    # Backtracking (9)
    "subsets": ("Backtracking", "Medium", "Subsets"),
    "combination-target-sum": ("Backtracking", "Medium", "Combination Sum"),
    "combination-target-sum-ii": ("Backtracking", "Medium", "Combination Sum II"),
    "permutations": ("Backtracking", "Medium", "Permutations"),
    "subsets-ii": ("Backtracking", "Medium", "Subsets II"),
    "search-for-word": ("Backtracking", "Medium", "Word Search"),
    "palindrome-partitioning": ("Backtracking", "Medium", "Palindrome Partitioning"),
    "combinations-of-a-phone-number": ("Backtracking", "Medium", "Letter Combinations of a Phone Number"),
    "n-queens": ("Backtracking", "Hard", "N-Queens"),

    # Tries (3)
    "implement-prefix-tree": ("Tries", "Medium", "Implement Trie Prefix Tree"),
    "design-add-and-search-words-data-structure": ("Tries", "Medium", "Design Add And Search Words"),
    "word-search-ii": ("Tries", "Hard", "Word Search II"),

    # Graphs (13)
    "count-number-of-islands": ("Graphs", "Medium", "Number of Islands"),
    "max-area-of-island": ("Graphs", "Medium", "Max Area of Island"),
    "clone-graph": ("Graphs", "Medium", "Clone Graph"),
    "islands-and-treasure": ("Graphs", "Medium", "Walls and Gates"),
    "rotting-fruit": ("Graphs", "Medium", "Rotting Oranges"),
    "pacific-atlantic-water-flow": ("Graphs", "Medium", "Pacific Atlantic Water Flow"),
    "surrounded-regions": ("Graphs", "Medium", "Surrounded Regions"),
    "course-schedule": ("Graphs", "Medium", "Course Schedule"),
    "course-schedule-ii": ("Graphs", "Medium", "Course Schedule II"),
    "graph-valid-tree": ("Graphs", "Medium", "Graph Valid Tree"),
    "number-of-connected-components-in-an-undirected-graph": ("Graphs", "Medium", "Connected Components in Graph"),
    "redundant-connection": ("Graphs", "Medium", "Redundant Connection"),
    "word-ladder": ("Graphs", "Hard", "Word Ladder"),

    # Advanced Graphs (6)
    "reconstruct-flight-path": ("Advanced Graphs", "Hard", "Reconstruct Itinerary"),
    "min-cost-to-connect-points": ("Advanced Graphs", "Medium", "Min Cost to Connect All Points"),
    "network-delay-time": ("Advanced Graphs", "Medium", "Network Delay Time"),
    "swim-in-rising-water": ("Advanced Graphs", "Hard", "Swim In Rising Water"),
    "alien-dictionary": ("Advanced Graphs", "Hard", "Alien Dictionary"),
    "cheapest-flights-within-k-stops": ("Advanced Graphs", "Medium", "Cheapest Flights Within K Stops"),

    # 1-D Dynamic Prog (12)
    "climbing-stairs": ("1-D Dynamic Prog", "Easy", "Climbing Stairs"),
    "min-cost-climbing-stairs": ("1-D Dynamic Prog", "Easy", "Min Cost Climbing Stairs"),
    "house-robber": ("1-D Dynamic Prog", "Medium", "House Robber"),
    "house-robber-ii": ("1-D Dynamic Prog", "Medium", "House Robber II"),
    "longest-palindromic-substring": ("1-D Dynamic Prog", "Medium", "Longest Palindromic Substring"),
    "palindromic-substrings": ("1-D Dynamic Prog", "Medium", "Palindromic Substrings"),
    "decode-ways": ("1-D Dynamic Prog", "Medium", "Decode Ways"),
    "coin-change": ("1-D Dynamic Prog", "Medium", "Coin Change"),
    "maximum-product-subarray": ("1-D Dynamic Prog", "Medium", "Maximum Product Subarray"),
    "word-break": ("1-D Dynamic Prog", "Medium", "Word Break"),
    "longest-increasing-subsequence": ("1-D Dynamic Prog", "Medium", "Longest Increasing Subsequence"),
    "partition-equal-subset-sum": ("1-D Dynamic Prog", "Medium", "Partition Equal Subset Sum"),

    # 2-D Dynamic Prog (11)
    "unique-paths": ("2-D Dynamic Prog", "Medium", "Unique Paths"),
    "longest-common-subsequence": ("2-D Dynamic Prog", "Medium", "Longest Common Subsequence"),
    "best-time-to-buy-and-sell-stock-with-cooldown": ("2-D Dynamic Prog", "Medium", "Best Time to Buy/Sell Stock with Cooldown"),
    "coin-change-ii": ("2-D Dynamic Prog", "Medium", "Coin Change II"),
    "target-sum": ("2-D Dynamic Prog", "Medium", "Target Sum"),
    "interleaving-string": ("2-D Dynamic Prog", "Medium", "Interleaving String"),
    "longest-increasing-path-in-a-matrix": ("2-D Dynamic Prog", "Hard", "Longest Increasing Path in a Matrix"),
    "distinct-subsequences": ("2-D Dynamic Prog", "Hard", "Distinct Subsequences"),
    "edit-distance": ("2-D Dynamic Prog", "Medium", "Edit Distance"),
    "burst-balloons": ("2-D Dynamic Prog", "Hard", "Burst Balloons"),
    "regular-expression-matching": ("2-D Dynamic Prog", "Hard", "Regular Expression Matching"),

    # Greedy (8)
    "maximum-subarray": ("Greedy", "Medium", "Maximum Subarray"),
    "jump-game": ("Greedy", "Medium", "Jump Game"),
    "jump-game-ii": ("Greedy", "Medium", "Jump Game II"),
    "gas-station": ("Greedy", "Medium", "Gas Station"),
    "hand-of-straights": ("Greedy", "Medium", "Hand of Straights"),
    "merge-triplets-to-form-target": ("Greedy", "Medium", "Merge Triplets to Form Target Triplet"),
    "partition-labels": ("Greedy", "Medium", "Partition Labels"),
    "valid-parenthesis-string": ("Greedy", "Medium", "Valid Parenthesis String"),

    # Intervals (6)
    "insert-new-interval": ("Intervals", "Medium", "Insert Interval"),
    "merge-intervals": ("Intervals", "Medium", "Merge Intervals"),
    "non-overlapping-intervals": ("Intervals", "Medium", "Non-overlapping Intervals"),
    "meeting-schedule": ("Intervals", "Easy", "Meeting Rooms"),
    "meeting-schedule-ii": ("Intervals", "Medium", "Meeting Rooms II"),
    "minimum-interval-including-query": ("Intervals", "Hard", "Minimum Interval to Include Each Query"),

    # Math & Geometry (8)
    "rotate-matrix": ("Math & Geometry", "Medium", "Rotate Image"),
    "spiral-matrix": ("Math & Geometry", "Medium", "Spiral Matrix"),
    "set-matrix-zeroes": ("Math & Geometry", "Medium", "Set Matrix Zeroes"),
    "happy-number": ("Math & Geometry", "Easy", "Happy Number"),
    "plus-one": ("Math & Geometry", "Easy", "Plus One"),
    "pow-x-n": ("Math & Geometry", "Medium", "Pow(x, n)"),
    "multiply-strings": ("Math & Geometry", "Medium", "Multiply Strings"),
    "detect-squares": ("Math & Geometry", "Medium", "Detect Squares"),

    # Bit Manipulation (7)
    "single-number": ("Bit Manipulation", "Easy", "Single Number"),
    "number-of-one-bits": ("Bit Manipulation", "Easy", "Number of 1 Bits"),
    "counting-bits": ("Bit Manipulation", "Easy", "Counting Bits"),
    "reverse-bits": ("Bit Manipulation", "Easy", "Reverse Bits"),
    "missing-number": ("Bit Manipulation", "Easy", "Missing Number"),
    "sum-of-two-integers": ("Bit Manipulation", "Medium", "Sum of Two Integers"),
    "reverse-integer": ("Bit Manipulation", "Medium", "Reverse Integer"),
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
        print(f"Warning: Could not fetch from GitHub API ({e}). Using fallback solved set.")
        # Fallback to known solved problems
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

def compute_neetcode_stats(solved_slugs):
    # Initialize categories
    categories = [
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

    cat_index = {c["name"]: idx for idx, c in enumerate(categories)}
    diff_counts = {"Easy": 0, "Medium": 0, "Hard": 0}

    for slug in solved_slugs:
        if slug in NEETCODE_150_MAP:
            cat, diff, name = NEETCODE_150_MAP[slug]
            if cat in cat_index:
                categories[cat_index[cat]]["solved"] += 1
            if diff in diff_counts:
                diff_counts[diff] += 1

    return categories, diff_counts

def render_neetcode_card(categories, diff_counts):
    width = 780
    height = 295

    total_solved = sum(c["solved"] for c in categories)
    grand_total = sum(c["total"] for c in categories)
    pct = round((total_solved / grand_total) * 100, 1) if grand_total > 0 else 0
    master_fill_w = max(4, int((total_solved / grand_total) * 732)) if total_solved > 0 else 0

    col_headers = [
        {"title": "CORE DATA STRUCTURES", "color": "#00EA64"},
        {"title": "TREES &amp; GRAPHS", "color": "#38BDF8"},
        {"title": "DYNAMIC PROG &amp; MATH", "color": "#A855F7"}
    ]

    col_x = [24, 276, 528]
    items_by_col = [[], [], []]
    for c in categories:
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

            # If solved > 0, highlight number and add neon glow
            if item_solved > 0:
                fraction_text = f'''<text x="175" y="10" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="700">
                <tspan fill="{item['color']}">{item_solved}</tspan><tspan fill="#64748B">/{item_total}</tspan>
              </text>'''
                fill_bar = f'''<rect x="182" y="3" width="{max(4, fill_w)}" height="5" rx="2.5" fill="{item['color']}">
                <animate attributeName="opacity" values="0.85;1;0.85" dur="3s" repeatCount="indefinite"/>
              </rect>
              <circle cx="{182 + max(4, fill_w)}" cy="5.5" r="2" fill="#FFFFFF" opacity="0.9"/>'''
            else:
                fraction_text = f'''<text x="175" y="10" text-anchor="end" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="500">
                0/{item_total}
              </text>'''
                fill_bar = ""

            items_svg.append(f'''
            <g transform="translate({x}, {y})">
              <!-- Category Name -->
              <text x="0" y="10" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10.5" font-weight="500">
                {clean_name}
              </text>
              <!-- Fraction -->
              {fraction_text}
              <!-- Mini Bar Track -->
              <rect x="182" y="3" width="{bar_w}" height="5" rx="2.5" fill="rgba(255, 255, 255, 0.05)"/>
              {fill_bar}
            </g>
            ''')
        columns_svg.append(header_svg + "".join(items_svg))

    columns_content = "".join(columns_svg)

    # Active scanner beam end
    laser_end = master_fill_w if master_fill_w > 0 else 732

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
  <circle cx="35" cy="35" r="75" fill="#00EA64" opacity="0.05">
    <animate attributeName="opacity" values="0.03;0.09;0.03" dur="4s" repeatCount="indefinite"/>
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
    <circle cy="29.5" r="2.2" fill="#00EA64" filter="url(#glow-laser)">
      <animate attributeName="cx" values="0;{master_fill_w};0" dur="2.8s" repeatCount="indefinite" keyTimes="0;0.5;1" calcMode="spline" keySplines="0.4 0 0.2 1; 0.4 0 0.2 1"/>
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2.8s" repeatCount="indefinite"/>
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
      Easy: <tspan font-weight="700" fill="#00EA64">{diff_counts['Easy']}</tspan><tspan fill="#64748B"> / 44</tspan>
    </text>

    <!-- Medium -->
    <circle cx="140" cy="12" r="3" fill="#F59E0B">
      <animate attributeName="opacity" values="0.6;1;0.6" begin="0.8s" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="149" y="15" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Medium: <tspan font-weight="700" fill="#F59E0B">{diff_counts['Medium']}</tspan><tspan fill="#64748B"> / 88</tspan>
    </text>

    <!-- Hard -->
    <circle cx="280" cy="12" r="3" fill="#EF4444">
      <animate attributeName="opacity" values="0.6;1;0.6" begin="1.6s" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="289" y="15" fill="#CBD5E1" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9.5" font-weight="500">
      Hard: <tspan font-weight="700" fill="#EF4444">{diff_counts['Hard']}</tspan><tspan fill="#64748B"> / 18</tspan>
    </text>

    <!-- Roadmap Total Tag -->
    <text x="720" y="15" text-anchor="end" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="9" font-weight="600">
      ACTIVE ROADMAP &#183; {total_solved} / {grand_total} SOLVED
    </text>
  </g>
</svg>
'''
    return svg

def main():
    target_dirs = [
        "assets/neetcode"
    ]
    solved_slugs = fetch_solved_problems_from_repo()
    categories, diff_counts = compute_neetcode_stats(solved_slugs)
    svg_code = render_neetcode_card(categories, diff_counts)

    # Validate XML
    ET.fromstring(svg_code)

    for out_dir in target_dirs:
        os.makedirs(out_dir, exist_ok=True)
        for prefix in ["", "card_", "card_v1_", "card_v2_"]:
            file_path = os.path.join(out_dir, f"{prefix}neetcode.svg")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_code)

    total_solved = sum(c["solved"] for c in categories)
    print(f"Successfully generated NeetCode card with {total_solved} solved problems ({diff_counts})!")

if __name__ == "__main__":
    main()
