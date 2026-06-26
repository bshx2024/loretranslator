import os
import json
import urllib.request
import xml.etree.ElementTree as ET
import re

db_path = "E:/kaifa/loretranslator/dict_db.json"
eldamo_xml_url = "https://raw.githubusercontent.com/pfstrack/eldamo/master/src/data/eldamo-data.xml"

def download_eldamo_xml():
    print(f"Downloading Eldamo Lexicon XML from {eldamo_xml_url}...")
    req = urllib.request.Request(
        eldamo_xml_url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    try:
        # Some corporate networks might block, using raw urllib
        with urllib.request.urlopen(req, timeout=30) as response:
            xml_data = response.read()
            print("Successfully downloaded Eldamo XML database!")
            return xml_data
    except Exception as e:
        print(f"Failed to download Eldamo XML: {e}")
        return None

def import_vocab():
    xml_data = download_eldamo_xml()
    if not xml_data:
        print("Fallback database remains active.")
        return
        
    sindarin_words = {}
    quenya_words = {}
    
    try:
        root = ET.fromstring(xml_data)
        # Find all word/entry elements
        # In Eldamo XML, elements are usually <word>
        words = root.findall(".//word")
        print(f"Found {len(words)} word entries in XML.")
        
        for w_elem in words:
            # Get language: s = Sindarin, q = Quenya
            lang = w_elem.attrib.get("l")
            if lang not in ["s", "q"]:
                continue
                
            # Speech category: noun, verb, adj
            speech = w_elem.attrib.get("speech", "").strip().lower()
            if not speech or not any(speech.startswith(prefix) for prefix in ["n", "v", "adj"]):
                continue
                
            # Word spelling
            word = w_elem.attrib.get("v", "")
            if not word:
                continue
            clean_word = re.sub(r'[*?]', '', word).strip()
            
            # Gloss (meaning)
            gloss = w_elem.attrib.get("gloss")
            
            if not gloss:
                continue
                
            # Extract clean English word
            clean_gloss = re.split(r'[,;()\[\]]', gloss)[0].strip().lower()
            if clean_gloss.startswith("to "):
                clean_gloss = clean_gloss[3:].strip()
            if clean_gloss.startswith("a "):
                clean_gloss = clean_gloss[2:].strip()
            if clean_gloss.startswith("the "):
                clean_gloss = clean_gloss[4:].strip()
                
            if not clean_gloss or " " in clean_gloss or len(clean_gloss) < 2:
                continue
                
            if lang == "s":
                sindarin_words[clean_gloss] = clean_word
            elif lang == "q":
                quenya_words[clean_gloss] = clean_word

    except Exception as e:
        print(f"Failed to parse XML: {e}")
        return

    print(f"Extracted {len(sindarin_words)} Sindarin words and {len(quenya_words)} Quenya words.")

    if not sindarin_words or not quenya_words:
        print("No words extracted. Check XML structure matches.")
        return

    # Load existing dict_db
    with open(db_path, "r", encoding="utf-8") as f:
        dict_db = json.load(f)
        
    original_sindarin = dict_db["elvish"]["sindarin"]
    original_quenya = dict_db["elvish"]["quenya"]
    
    # Merge and update
    added_s = 0
    for k, v in sindarin_words.items():
        if k not in original_sindarin:
            original_sindarin[k] = v
            added_s += 1
            
    added_q = 0
    for k, v in quenya_words.items():
        if k not in original_quenya:
            original_quenya[k] = v
            added_q += 1
            
    dict_db["elvish"]["sindarin"] = original_sindarin
    dict_db["elvish"]["quenya"] = original_quenya
    
    # Save back to dict_db.json
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(dict_db, f, indent=4, ensure_ascii=False)
        
    print(f"Integrated vocabulary successfully!")
    print(f"Added {added_s} new Sindarin words. Total: {len(original_sindarin)}")
    print(f"Added {added_q} new Quenya words. Total: {len(original_quenya)}")

if __name__ == "__main__":
    import_vocab()
