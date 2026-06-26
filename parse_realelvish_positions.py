import re
import json
import os

path = r"C:\Users\Administrator\.gemini\antigravity\brain\cf037292-d6e2-42a2-bf00-a8aeff1ad4a3\scratch\realelvish_positions_scraped.txt"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Parse Total Domain Traffic from header
traffic_header_match = re.search(r"流量(\d+(?:\.\d+)?[KM]?)", content)
total_domain_traffic = 1300  # Default fallback
if traffic_header_match:
    t_str = traffic_header_match.group(1)
    if 'K' in t_str:
        total_domain_traffic = int(float(t_str.replace('K', '')) * 1000)
    elif 'M' in t_str:
        total_domain_traffic = int(float(t_str.replace('M', '')) * 1000000)
    else:
        total_domain_traffic = int(t_str)
print(f"Detected Total Domain Traffic: {total_domain_traffic}")

# 2. Match each keyword block
# Pattern: Keyword link, metrics text, competitor URL link
pattern = r"\[([^\]]+)\]\(https://sem\.3ue\.co/analytics/keywordoverview/[^)]+\)\s*([ICNT]\d+\.\d{2}[^[]+)\s*\[(realelvish\.net/[^\]]+)\]"
matches = re.findall(pattern, content)

print(f"Matched {len(matches)} keyword-URL blocks in file.")

parsed_results = []
unparsed_count = 0

for i, (kw, metrics_text, ranking_url) in enumerate(matches):
    metrics_text = metrics_text.strip()
    ranking_url = ranking_url.strip()
    
    split_match = re.search(r"^([ICNT])(\d+)\.(\d{2})(.*)$", metrics_text)
    if split_match:
        intent = split_match.group(1)
        digits_before_dot = split_match.group(2)
        fractional_part = split_match.group(3)
        right_part = split_match.group(4).strip()
        
        best_split = None
        min_error = float('inf')
        
        for share_len in [1, 2]:
            if len(digits_before_dot) < share_len + 2:
                continue
            share_whole = digits_before_dot[-share_len:]
            r_digits = digits_before_dot[:-share_len]
            share_pct = float(f"{share_whole}.{fractional_part}")
            
            for rank_len in [1, 2, 3]:
                if len(r_digits) < rank_len + 2:
                    continue
                rank_str = r_digits[:rank_len]
                sf_str = r_digits[rank_len:rank_len+1]
                traffic_str = r_digits[rank_len+1:]
                
                try:
                    rank = int(rank_str)
                    sf = int(sf_str)
                    traffic = int(traffic_str)
                    
                    expected_traffic = total_domain_traffic * (share_pct / 100.0)
                    error = abs(traffic - expected_traffic)
                    
                    if rank <= 100 and share_pct <= 100.0:
                        if error < min_error:
                            min_error = error
                            best_split = {
                                "rank": rank,
                                "sf": sf,
                                "traffic": traffic,
                                "traffic_share_pct": share_pct
                            }
                except ValueError:
                    continue
        
        # Split right_part into Volume and KD
        volume = 0
        kd = 0
        if right_part.endswith(tuple(str(x) for x in range(10))):
            km_match = re.search(r"([KM])(\d+)$", right_part)
            if km_match:
                volume_str = right_part[:km_match.start() + 1]
                kd_str = km_match.group(2)
            else:
                if len(right_part) >= 3:
                    volume_str = right_part[:-2]
                    kd_str = right_part[-2:]
                else:
                    volume_str = right_part
                    kd_str = "0"
            
            try:
                kd = int(kd_str)
                if 'K' in volume_str:
                    volume = int(float(volume_str.replace('K', '')) * 1000)
                elif 'M' in volume_str:
                    volume = int(float(volume_str.replace('M', '')) * 1000000)
                else:
                    volume = int(volume_str)
            except ValueError:
                pass
        
        if best_split:
            parsed_results.append({
                "keyword": kw,
                "intent": intent,
                "rank": best_split["rank"],
                "sf": best_split["sf"],
                "traffic": best_split["traffic"],
                "traffic_share_pct": best_split["traffic_share_pct"],
                "volume": volume,
                "kd": kd,
                "ranking_url": ranking_url
            })
        else:
            unparsed_count += 1
            parsed_results.append({
                "keyword": kw,
                "intent": intent,
                "rank": 0,
                "sf": 0,
                "traffic": 0,
                "traffic_share_pct": 0.0,
                "volume": volume,
                "kd": kd,
                "ranking_url": ranking_url,
                "raw_metrics_text": metrics_text
            })
    else:
        unparsed_count += 1
        parsed_results.append({
            "keyword": kw,
            "intent": "Unknown",
            "rank": 0,
            "sf": 0,
            "traffic": 0,
            "traffic_share_pct": 0.0,
            "volume": 0,
            "kd": 0,
            "ranking_url": ranking_url,
            "raw_text": metrics_text
        })

print(f"Parsed {len(parsed_results) - unparsed_count} keywords successfully.")
print(f"Failed to parse: {unparsed_count} keywords.")

# Save results
out_json_path = r"C:\Users\Administrator\.gemini\antigravity\brain\cf037292-d6e2-42a2-bf00-a8aeff1ad4a3\scratch\realelvish_positions_parsed.json"
with open(out_json_path, "w", encoding="utf-8") as f:
    json.dump(parsed_results, f, ensure_ascii=False, indent=2)

# Print first 20 results
print("\nFirst 20 Correctly Parsed Keywords:")
print("-" * 115)
print(f"{'Keyword':<25} | {'Vol':<6} | {'KD':<4} | {'Rank':<4} | {'Traffic':<7} | {'Share%':<6} | {'Ranking URL':<50}")
print("-" * 115)
for item in parsed_results[:20]:
    kw = item['keyword']
    vol = item.get('volume', 0)
    kd = item.get('kd', 0)
    rank = item.get('rank', 0)
    traffic = item.get('traffic', 0)
    share = item.get('traffic_share_pct', 0.0)
    url_short = item.get('ranking_url', '').replace("realelvish.net/", "")
    print(f"{kw:<25} | {vol:<6} | {kd:<3}% | {rank:<4} | {traffic:<7} | {share:<6.2f} | {url_short:<50}")
print("-" * 115)
