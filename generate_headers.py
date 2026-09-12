import os
import html

os.makedirs('d:/githubreadme/wazed-md-abdul/assets/headers', exist_ok=True)

def create_h2_svg(text, prefix="## ", line_width=200):
    full_text = f"{prefix}{text}"
    escaped_text = html.escape(text)
    escaped_prefix = html.escape(prefix)
    width = max(380, len(full_text) * 15 + 40)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 42" width="{width}" height="42" fill="none">
  <defs>
    <linearGradient id="shimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#618F7F">
        <animate attributeName="stop-color" values="#618F7F;#A3D9C9;#618F7F" dur="3.5s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#88C2AF">
        <animate attributeName="stop-color" values="#88C2AF;#E3F8F2;#88C2AF" dur="3.5s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#618F7F">
        <animate attributeName="stop-color" values="#618F7F;#A3D9C9;#618F7F" dur="3.5s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
    <linearGradient id="line-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#618F7F" stop-opacity="0.9">
        <animate attributeName="stop-opacity" values="0.9;0.35;0.9" dur="3s" repeatCount="indefinite" />
      </stop>
      <stop offset="65%" stop-color="#618F7F" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#618F7F" stop-opacity="0" />
    </linearGradient>
    <filter id="subtle-glow" x="-10%" y="-20%" width="120%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="1.5" flood-color="#618F7F" flood-opacity="0.35" />
    </filter>
  </defs>
  <text x="0" y="24" font-family="'Fira Code', 'JetBrains Mono', Consolas, -apple-system, sans-serif" font-size="22" font-weight="700" fill="url(#shimmer)" filter="url(#subtle-glow)" letter-spacing="0.2px"><tspan fill="#618F7F" fill-opacity="0.85">{escaped_prefix}</tspan><tspan fill="url(#shimmer)">{escaped_text}</tspan></text>
  <rect x="0" y="34" width="{line_width}" height="2.5" rx="1.25" fill="url(#line-glow)">
    <animate attributeName="width" values="{int(line_width * 0.8)};{int(line_width * 1.15)};{int(line_width * 0.8)}" dur="3.5s" repeatCount="indefinite" />
  </rect>
</svg>'''
    return svg

def create_h3_svg(text, prefix="❯ "):
    full_text = f"{prefix}{text}"
    escaped_text = html.escape(text)
    escaped_prefix = html.escape(prefix)
    width = max(340, len(full_text) * 11 + 40)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 30" width="{width}" height="30" fill="none">
  <defs>
    <linearGradient id="h3-shimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#618F7F">
        <animate attributeName="stop-color" values="#618F7F;#9DD4C4;#618F7F" dur="3s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#7DB5A3">
        <animate attributeName="stop-color" values="#7DB5A3;#E0F6F0;#7DB5A3" dur="3s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#618F7F">
        <animate attributeName="stop-color" values="#618F7F;#9DD4C4;#618F7F" dur="3s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
  </defs>
  <text x="0" y="20" font-family="'Fira Code', 'JetBrains Mono', Consolas, -apple-system, sans-serif" font-size="17" font-weight="600" fill="url(#h3-shimmer)" letter-spacing="0.2px"><tspan fill="#618F7F" fill-opacity="0.9">{escaped_prefix}</tspan><tspan fill="url(#h3-shimmer)">{escaped_text}</tspan></text>
</svg>'''
    return svg

h2_headers = [
    ("tech-arsenal.svg", "Tech Arsenal", 200),
    ("github-stats.svg", "GitHub Stats", 180),
    ("contribution-activity.svg", "Contribution Activity", 260),
    ("find-me-online.svg", "Find Me Online", 190)
]

h3_headers = [
    ("whos-behind-the-keyboard.svg", "Who's behind the keyboard?"),
    ("languages.svg", "Languages"),
    ("frontend.svg", "Frontend"),
    ("backend-database-auth.svg", "Backend, Database & Auth"),
    ("cloud-baas.svg", "Cloud & BaaS"),
    ("integrations-payments.svg", "Integrations & Payments"),
    ("automation-tools-environment.svg", "Automation, Tools & Environment"),
    ("ai-dev-partners.svg", "AI Dev Partners")
]

for filename, title, lw in h2_headers:
    content = create_h2_svg(title, "## ", lw)
    with open(f"d:/githubreadme/wazed-md-abdul/assets/headers/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

for filename, title in h3_headers:
    content = create_h3_svg(title, "❯ ")
    with open(f"d:/githubreadme/wazed-md-abdul/assets/headers/{filename}", "w", encoding="utf-8") as f:
        f.write(content)

print("Generated all header SVGs with proper escaping!")
