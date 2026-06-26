import json
import re
import os

jens_metrics_path = r"e:\BaiduNetdiskDownload\Danny Postma – SEO Blueprint\Danny Postma - SEO Blueprint\skills-blueprint\seo-niche-research\references\language_translator_competitor_metrics.txt"
comp1_path = r"C:\Users\Administrator\.gemini\antigravity\brain\cf037292-d6e2-42a2-bf00-a8aeff1ad4a3\scratch\ofelvenmake_domain_positions_parsed.json"
comp2_path = r"C:\Users\Administrator\.gemini\antigravity\brain\cf037292-d6e2-42a2-bf00-a8aeff1ad4a3\scratch\realelvish_positions_parsed.json"

# 1. Load Jens Hansen keywords from metrics file
with open(jens_metrics_path, "r", encoding="utf-8") as f:
    jens_text = f.read()

# Parse keywords using markdown link patterns
jens_kws = re.findall(r"\[([^\]]+)\]\(https://sem\.3ue\.co/analytics/keywordoverview/", jens_text)
jens_kws_set = {k.strip().lower() for k in jens_kws}
print(f"Jens Hansen Page-level keywords count: {len(jens_kws_set)}")
print("Jens Hansen Keywords:", sorted(list(jens_kws_set)))

# 2. Load Competitor 1: ofelvenmake.com
with open(comp1_path, "r", encoding="utf-8") as f:
    comp1_data = json.load(f)

# 3. Load Competitor 2: realelvish.net
with open(comp2_path, "r", encoding="utf-8") as f:
    comp2_data = json.load(f)

# Combine competitor keywords
all_comp_kws = {}

for item in comp1_data:
    kw = item["keyword"].strip().lower()
    if kw not in all_comp_kws:
        all_comp_kws[kw] = {
            "keyword": item["keyword"],
            "volume": item.get("volume", 0),
            "kd": item.get("kd", 0),
            "comp1_rank": item.get("rank", 999),
            "comp1_traffic": item.get("traffic", 0),
            "comp2_rank": 999,
            "comp2_traffic": 0
        }
    else:
        # Update if rank is better
        if item.get("rank", 999) < all_comp_kws[kw]["comp1_rank"]:
            all_comp_kws[kw]["comp1_rank"] = item["rank"]
            all_comp_kws[kw]["comp1_traffic"] = item.get("traffic", 0)

for item in comp2_data:
    kw = item["keyword"].strip().lower()
    if kw not in all_comp_kws:
        all_comp_kws[kw] = {
            "keyword": item["keyword"],
            "volume": item.get("volume", 0),
            "kd": item.get("kd", 0),
            "comp1_rank": 999,
            "comp1_traffic": 0,
            "comp2_rank": item.get("rank", 999),
            "comp2_traffic": item.get("traffic", 0)
        }
    else:
        # Update comp2 info
        if item.get("rank", 999) < all_comp_kws[kw]["comp2_rank"]:
            all_comp_kws[kw]["comp2_rank"] = item["rank"]
            all_comp_kws[kw]["comp2_traffic"] = item.get("traffic", 0)
        # Ensure volume and kd are populated if they weren't before
        if not all_comp_kws[kw]["volume"] and item.get("volume", 0):
            all_comp_kws[kw]["volume"] = item["volume"]
        if not all_comp_kws[kw]["kd"] and item.get("kd", 0):
            all_comp_kws[kw]["kd"] = item["kd"]

# 4. Find the Gap (Keywords that competitors rank for, but Jens Hansen doesn't rank for)
gaps = []
for kw_lower, info in all_comp_kws.items():
    if kw_lower not in jens_kws_set:
        gaps.append(info)

# Sort gaps by volume descending
gaps.sort(key=lambda x: x["volume"], reverse=True)

print(f"\nTotal unique competitor keywords: {len(all_comp_kws)}")
print(f"Total keyword gaps for Jens Hansen: {len(gaps)}")

print("\n--- Goldmine Keyword Gaps (KD <= 30, Vol >= 100) ---")
print("-" * 110)
print(f"{'Keyword':<35} | {'Vol':<6} | {'KD':<4} | {'Comp1 Rank (ofelven)':<20} | {'Comp2 Rank (realelvish)':<23}")
print("-" * 110)
goldmine_count = 0
goldmines = []
for item in gaps:
    if item["kd"] <= 30 and item["volume"] >= 100:
        goldmines.append(item)
        comp1_rank = item["comp1_rank"] if item["comp1_rank"] != 999 else "-"
        comp2_rank = item["comp2_rank"] if item["comp2_rank"] != 999 else "-"
        print(f"{item['keyword']:<35} | {item['volume']:<6} | {item['kd']:<3}% | {str(comp1_rank):<20} | {str(comp2_rank):<23}")
        goldmine_count += 1
print("-" * 110)
print(f"Found {goldmine_count} goldmine keywords.")

# Save the detailed gap analysis to json
out_json_path = r"C:\Users\Administrator\.gemini\antigravity\brain\cf037292-d6e2-42a2-bf00-a8aeff1ad4a3\scratch\elvish_content_gap_analysis.json"
with open(out_json_path, "w", encoding="utf-8") as f:
    json.dump({
        "target_page_keywords": list(jens_kws_set),
        "total_competitor_keywords": len(all_comp_kws),
        "total_gaps": len(gaps),
        "goldmine_keywords": goldmines,
        "all_gaps": gaps
    }, f, ensure_ascii=False, indent=2)
print(f"Saved complete gap analysis to {out_json_path}")
