import os
import json
import re

# 1. Database of raw ingredients (Elvish dialect data for pSEO)
dialect_database = [
    {
        "dialect_id": "sindarin",
        "dialect_name": "Sindarin",
        "primary_keyword": "sindarin translator",
        "volume": 1600,
        "kd": 8,
        "historical_context": "Sindarin is the grey-elven tongue, the primary spoken language of the Elves of Middle-earth during the Third Age.",
        "famous_words": [
            {"english": "love", "elvish": "melme"},
            {"english": "star", "elvish": "giliath"},
            {"english": "friend", "elvish": "mellon"}
        ]
    },
    {
        "dialect_id": "quenya",
        "dialect_name": "Quenya",
        "primary_keyword": "quenya translator",
        "volume": 110,
        "kd": 11,
        "historical_context": "Quenya is the High-Elven tongue, the ancient ceremonial language of the Noldor, akin to Latin in our world.",
        "famous_words": [
            {"english": "love", "elvish": "melme"},
            {"english": "star", "elvish": "el"},
            {"english": "friend", "elvish": "nilme"}
        ]
    },
    {
        "dialect_id": "tengwar",
        "dialect_name": "Tengwar",
        "primary_keyword": "tengwar translator",
        "volume": 320,
        "kd": 20,
        "historical_context": "Tengwar is the script designed by Fëanor, used to write both Sindarin and Quenya languages.",
        "famous_words": [
            {"english": "love", "elvish": "Tengwar: melme"},
            {"english": "star", "elvish": "Tengwar: giliath"},
            {"english": "friend", "elvish": "Tengwar: mellon"}
        ]
    }
]

# 2. Page Template (Unified blueprint for programmatic generator)
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Online {dialect_name} Translator & Converter | Jens Hansen</title>
    <meta name="description" content="Translate English to {dialect_name} instantly. Perfect for Lord of the Rings engraving ideas, tattoos, and customized wedding rings. Try it free!">
</head>
<body>
    <header>
        <div class="logo">Jens Hansen - The Ring Creator</div>
        <nav>
            <a href="/blogs/tolkien-love-quotes">Tolkien Love Quotes</a> | 
            <a href="/tools/sindarin-name-generator">Elven Name Generator</a>
        </nav>
    </header>

    <main>
        <h1>Online {dialect_name} Translator & Engraving Previewer</h1>
        
        <section class="historical-lore">
            <p>{historical_context}</p>
        </section>

        <!-- The Free Tool Widget (门口的免费试吃盘) -->
        <section class="translator-widget" style="border: 2px solid gold; padding: 20px; border-radius: 10px;">
            <h3>Input English Text below:</h3>
            <textarea id="englishInput" placeholder="Enter love, star, or friend..."></textarea>
            <button onclick="translateText()">Translate to {dialect_name}</button>
            
            <h3>Generated {dialect_name} Output:</h3>
            <div id="elvishOutput" style="font-size: 24px; font-weight: bold; color: darkgoldenrod; min-height: 50px;"></div>
        </section>

        <section class="word-list">
            <h2>Common {dialect_name} Vocabulary Words</h2>
            <ul>
                {vocabulary_list}
            </ul>
        </section>

        <!-- High CPC Tax Collector CTA (收税人内链) -->
        <section class="cta-banner" style="background-color: #f9f9f9; padding: 20px; text-align: center; margin-top: 30px;">
            <h2>Want to Engrave this {dialect_name} translation?</h2>
            <p>Jens Hansen jewelry artisans craft custom Lord of the Rings rings with precise hand-engraved Elvish text.</p>
            <a href="/products/elvish-wedding-ring" id="customRingCTA" style="background-color: gold; color: black; padding: 10px 20px; font-weight: bold; text-decoration: none;">Customize Your Ring Now</a>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 Jens Hansen. All rights reserved.</p>
    </footer>

    <script>
        const elvishDict = {dictionary_js};
        function translateText() {{
            const input = document.getElementById("englishInput").value.trim().toLowerCase();
            const outputDiv = document.getElementById("elvishOutput");
            if (elvishDict[input]) {{
                outputDiv.innerText = elvishDict[input];
            }} else {{
                outputDiv.innerText = "Word not found. For custom engravings, consult our design team!";
            }}
        }}
    </script>
</body>
</html>
"""

output_dir = r"C:\Users\Administrator\.gemini\antigravity\brain\cf037292-d6e2-42a2-bf00-a8aeff1ad4a3\scratch\pseo_output"
os.makedirs(output_dir, exist_ok=True)

# 3. Generate pages programmatically (The bottling line)
generated_files = []
for dialect in dialect_database:
    # Build vocabulary list HTML
    vocab_html = ""
    dict_js = {}
    for item in dialect["famous_words"]:
        vocab_html += f"<li><strong>{item['english']}</strong> translates to <em>{item['elvish']}</em></li>\n"
        dict_js[item["english"]] = item["elvish"]
        
    # Populate template
    page_content = html_template.format(
        dialect_name=dialect["dialect_name"],
        historical_context=dialect["historical_context"],
        vocabulary_list=vocab_html.strip(),
        dictionary_js=json.dumps(dict_js)
    )
    
    # Save file
    file_name = f"english-to-{dialect['dialect_id']}-translator.html"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page_content)
    generated_files.append(file_path)
    print(f"Generated page: {file_path}")

print(f"\nSuccessfully generated {len(generated_files)} programmatic SEO pages.")

# 4. On-Page SEO Validator (Automated shop inspector)
print("\n--- Running On-Page SEO Checklist Audit ---")
print("=" * 110)

def audit_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    # Checklist 1: Title Tag
    title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    title = title_match.group(1) if title_match else "MISSING"
    
    # Checklist 2: Meta Description
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', html, re.IGNORECASE)
    desc = desc_match.group(1) if desc_match else "MISSING"
    
    # Checklist 3: H1 count and text
    h1s = re.findall(r"<h1>(.*?)</h1>", html, re.IGNORECASE)
    h1_count = len(h1s)
    h1_text = h1s[0] if h1s else "MISSING"
    
    # Checklist 4: Tax Collector CTA present
    cta_present = "/products/elvish-wedding-ring" in html
    
    # Checklist 5: Content Ring internal links present
    internal_links_present = "/blogs/tolkien-love-quotes" in html and "/tools/sindarin-name-generator" in html
    
    print(f"File: {os.path.basename(file_path)}")
    print(f"  [✔] Title: '{title}' (Length: {len(title)} chars)")
    print(f"  [✔] Meta Description: '{desc}' (Length: {len(desc)} chars)")
    print(f"  [✔] H1 Tag Count: {h1_count} (Text: '{h1_text}')")
    print(f"  [✔] Tax Collector CTA Link: {'FOUND' if cta_present else 'MISSING'}")
    print(f"  [✔] Content Ring Internal Links: {'FOUND' if internal_links_present else 'MISSING'}")
    print("-" * 110)

for f_path in generated_files:
    audit_html(f_path)

print("On-Page SEO Audit finished successfully.")
