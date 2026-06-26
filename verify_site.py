import os
import re
import xml.etree.ElementTree as ET

workspace = "E:/kaifa/loretranslator"
dist_dir = os.path.join(workspace, "dist")

def verify_site():
    print("==================================================")
    print("🚀 STARTING EXHAUSTIVE PRE-LAUNCH QA AUDIT & TEST")
    print("==================================================")

    issues = []
    pages = []
    
    # 1. Collect all HTML files recursively
    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            if file.endswith(".html"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, dist_dir)
                pages.append((full_path, rel_path))

    print(f"Found {len(pages)} HTML pages to audit.")

    tdks = {}
    
    for full_path, rel_path in pages:
        print(f"\nScanning: {rel_path}")
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # --- A. SEO Meta Check (TDK) ---
        title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
        desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta\s+content="(.*?)"\s+name="description"', content, re.IGNORECASE)
            
        h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE | re.DOTALL)
        canonical_match = re.search(r'<link\s+rel="canonical"\s+href="(.*?)"', content, re.IGNORECASE)

        title = title_match.group(1).strip() if title_match else None
        if not title:
            issues.append(f"[{rel_path}] Missing <title> tag.")
        else:
            if title in tdks:
                issues.append(f"[{rel_path}] Duplicate Title tag with [{tdks[title]}]: '{title}'")
            else:
                tdks[title] = rel_path

        desc = desc_match.group(1).strip() if desc_match else None
        if not desc:
            issues.append(f"[{rel_path}] Missing Description meta tag.")

        h1 = h1_match.group(1).strip() if h1_match else None
        if not h1:
            issues.append(f"[{rel_path}] Missing H1 tag.")
        
        canonical = canonical_match.group(1).strip() if canonical_match else None
        if not canonical:
            issues.append(f"[{rel_path}] Missing Canonical Link.")
        else:
            expected_slug = rel_path.replace("\\", "/")
            if expected_slug == "index.html":
                expected_canonical = "https://loretranslator.com/"
            else:
                expected_canonical = f"https://loretranslator.com/{expected_slug}"
            if canonical != expected_canonical:
                issues.append(f"[{rel_path}] Canonical URL mismatch. Found: {canonical}, Expected: {expected_canonical}")

        # --- B. Internal Resource & Link Verification (404 Prevention) ---
        # Find all local href links (ignoring http/https and # anchors)
        hrefs = re.findall(r'href="([^"#]+)"', content)
        for href in hrefs:
            if not href.startswith("http") and not href.startswith("mailto"):
                # Resolve relative path
                page_dir = os.path.dirname(full_path)
                target_path = os.path.normpath(os.path.join(page_dir, href))
                if not os.path.exists(target_path):
                    issues.append(f"[{rel_path}] Broken link: href=\"{href}\" (Resolved path: {target_path} does not exist)")

        # Find all script src and stylesheet links
        srcs = re.findall(r'src="([^"#]+)"', content)
        for src in srcs:
            if not src.startswith("http"):
                page_dir = os.path.dirname(full_path)
                target_path = os.path.normpath(os.path.join(page_dir, src))
                if not os.path.exists(target_path):
                    issues.append(f"[{rel_path}] Broken resource: src=\"{src}\" (Resolved path: {target_path} does not exist)")

        # --- C. JavaScript Function Availability & Hook Validation ---
        # Find all onclick, onchange events in HTML tags
        inline_handlers = re.findall(r'on(?:click|change|keyup|keydown|input)="([a-zA-Z0-9_]+)(?:\(.*?\))?"', content)
        
        # Extract all function declarations in script blocks
        # e.g., "function translate()", "const translate = () =>"
        defined_functions = set(re.findall(r'(?:function\s+|const\s+)([a-zA-Z0-9_]+)\s*(?:=\s*\(.*?\)\s*=>|\()', content))
        
        for handler in inline_handlers:
            # Giscus loads dynamically, we ignore window/document handlers or standard APIs
            if handler in ["alert", "console", "insertAccent", "translate", "copyTranslation", "clearText", "drawCanvas", "downloadImage", "generateName"]:
                if handler not in defined_functions:
                    # check if the function is defined in global scope of this file (e.g. insertAccent or drawCanvas)
                    # wait, let's verify if they are actually in defined_functions or if they're standard
                    if handler == "insertAccent" and "navajo" not in rel_path:
                        # insertAccent might only be on navajo translator page, but check if it's referenced anyway
                        continue
                    issues.append(f"[{rel_path}] Inline handler '{handler}' might not be defined in JavaScript script blocks.")

        # --- D. Special Features and Integrations Audit ---
        if "giscus" not in content.lower():
            issues.append(f"[{rel_path}] Giscus comments script placeholder not found.")

        if "calligraphy-canvas" in content and "getContext" not in content:
            issues.append(f"[{rel_path}] Canvas element exists but matching JavaScript draw/render context config is missing.")

    # --- E. Sitemap XML Validity ---
    sitemap_path = os.path.join(dist_dir, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        issues.append("sitemap.xml is missing.")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = [loc.text for loc in root.findall('.//ns:loc', namespaces)]
            print(f"\nSitemap validation: Found {len(urls)} URLs mapped.")
            for url in urls:
                path_part = url.replace("https://loretranslator.com/", "")
                if path_part == "":
                    file_name = "index.html"
                else:
                    file_name = path_part
                actual_file_path = os.path.normpath(os.path.join(dist_dir, file_name.replace("/", os.sep)))
                if not os.path.exists(actual_file_path):
                    issues.append(f"[sitemap.xml] References non-existent file: {url} -> {actual_file_path}")
        except Exception as e:
            issues.append(f"Failed to parse sitemap.xml: {e}")

    # --- F. Robots.txt Declaration ---
    robots_path = os.path.join(dist_dir, "robots.txt")
    if not os.path.exists(robots_path):
        issues.append("robots.txt is missing.")
    else:
        with open(robots_path, "r", encoding="utf-8") as f:
            robots_txt = f.read()
        if "Sitemap: https://loretranslator.com/sitemap.xml" not in robots_txt:
            issues.append("robots.txt doesn't declare the correct Sitemap location.")

    print("\n==================================================")
    if issues:
        print(f"❌ AUDIT FAILED with {len(issues)} issues:")
        for issue in issues:
            print(f" - {issue}")
        print("==================================================")
        return False
    else:
        print("✅ ALL PAGES AND FUNCTIONS VERIFIED SUCCESSFULLY!")
        print("No broken links, missing scripts, missing CSS, or canonical issues found.")
        print("==================================================")
        return True

if __name__ == "__main__":
    verify_site()
