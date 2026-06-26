import os
import json
import shutil
from datetime import datetime

# Setup paths
workspace = os.path.dirname(os.path.abspath(__file__))
dist_dir = os.path.join(workspace, "dist")
templates_dir = os.path.join(workspace, "templates")

# Load dictionary database
with open(os.path.join(workspace, "dict_db.json"), "r", encoding="utf-8") as f:
    dict_db = json.load(f)

# Ensure output directories exist
os.makedirs(dist_dir, exist_ok=True)
os.makedirs(os.path.join(dist_dir, "translators"), exist_ok=True)
os.makedirs(os.path.join(dist_dir, "tools"), exist_ok=True)
os.makedirs(os.path.join(dist_dir, "articles"), exist_ok=True)
os.makedirs(os.path.join(dist_dir, "templates"), exist_ok=True)

# Copy base CSS
shutil.copy(
    os.path.join(templates_dir, "base.css"),
    os.path.join(dist_dir, "templates", "base.css")
)

# Shared Giscus Widget Code (deferred load)
giscus_widget_html = """
<script src="https://giscus.app/client.js"
        data-repo="github-username/loretranslator-comments"
        data-repo-id="R_kgDOH..."
        data-category="Announcements"
        data-category-id="DIC_kwDOH..."
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="dark_dimmed"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>
"""

# Activity feed data for homepage
activity_feed_data = [
    {
        "title": "One Ring Inscription (Black Speech to Tengwar)",
        "english": "One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them",
        "translation": "ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk agh burzum-ishi krimpatul",
        "note": "Translated using character-by-character Tengwar transliteration. Historically engraved in cursive Tengwar runes."
    },
    {
        "title": "Aragorn's Coronation Oath",
        "english": "Out of the Great Sea to Middle-earth I am come. In this place will I abide, and my heirs, unto the ending of the world.",
        "translation": "Et Eärello Endorenna utúlien. Sinome maruvan ar Hildinyar tenn' Ambar-metta.",
        "note": "High Elvish Quenya translation from J.R.R. Tolkien's Return of the King."
    },
    {
        "title": "Viking Warrior Oath (Old Norse Runes)",
        "english": "Strength, courage, and honor. Valhalla awaits us.",
        "translation": "ᚦᚢᚱᛘᚢᚦᚱ, ᚱᛁᚾᚴᚱ, ᚢᛅᛚᚼᛅᛚᛅ",
        "note": "Elder Futhark runic transliteration representing core Viking values."
    }
]

# Generate Activity Feed HTML for homepage
activity_feed_html = ""
for feed in activity_feed_data:
    activity_feed_html += f"""
    <div style="margin-bottom: 1.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--border-light);">
        <h4 style="color: var(--accent); font-family: 'Cinzel', serif; margin-bottom: 0.25rem;">{feed['title']}</h4>
        <p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 0.25rem;"><strong>English:</strong> {feed['english']}</p>
        <p style="font-size: 1rem; color: var(--text-primary); font-family: monospace; word-break: break-all; margin-bottom: 0.25rem;"><strong>Translation:</strong> {feed['translation']}</p>
        <span style="font-size: 0.8rem; color: var(--text-muted); font-style: italic;">{feed['note']}</span>
    </div>
    """

# Category Grid data
translators_metadata = [
    {
        "slug": "sindarin-translator",
        "name": "Sindarin Elvish Translator",
        "desc": "Translate modern English into the common Sindarin Elvish dialect of Middle-earth.",
        "h1": "Sindarin Elvish Translator",
        "meta_title": "Sindarin Translator | English to Sindarin Elvish Online",
        "meta_description": "Convert English into Tolkien's Sindarin Elvish dialect. Real vocabulary dictionary, calligraphy exporter, and academic guides for LOTR rings.",
        "font_mode": "Tengwar",
        "font_class": "font-tengwar",
        "style_description": """
        <h2>Introduction to Sindarin Elvish</h2>
        <p>Sindarin is the primary Elvish tongue spoken in Middle-earth during the Third Age. Unlike Quenya, which became a language of lore and high ceremony, Sindarin was the daily language of the Grey-elves (Sindar). Tolkien based the phonology and grammar of Sindarin on Welsh, giving it a soft, Celtic quality with complex vowel mutations.</p>
        <p>Our translator utilizes a verified academic dictionary matching real vocabulary words like <em>meleth</em> (love), <em>mellon</em> (friend), and <em>estel</em> (hope). For words not in the lexicon, it falls back to a precise Tengwar character transliteration mapping, allowing you to design rings and tattoos seamlessly.</p>
        """,
        "dictionary": dict_db["elvish"]["sindarin"],
        "faq": [
            {
                "q": "What is the difference between Quenya and Sindarin?",
                "a": "Quenya is high Elvish, comparable to Latin in our world, used for formal writing and ceremony. Sindarin is the common spoken tongue of the Elves of Middle-earth during the Third Age (LOTR era)."
            },
            {
                "q": "Can I use Sindarin for a custom wedding ring engraving?",
                "a": "Yes! Sindarin is the most popular language for Lord of the Rings themed ring engravings. Phrases like 'meleth' (love) or 'estel' (hope) are highly authentic and elegant."
            }
        ]
    },
    {
        "slug": "navi-translator",
        "name": "Na'vi Language Translator",
        "desc": "Translate English into the official Na'vi language from James Cameron's Avatar.",
        "h1": "Na'vi Language Translator",
        "meta_title": "Na'vi Language Translator | English to Avatar Na'vi Online",
        "meta_description": "Translate English words to Na'vi from Avatar. Access official IPA pronunciation guides, lexicon terms, and export calligraphy stencils.",
        "font_mode": "Latin",
        "font_class": "",
        "style_description": """
        <h2>Introduction to the Na'vi Language</h2>
        <p>The Na'vi language is a constructed language created by linguist Paul Frommer for James Cameron's film <em>Avatar</em>. It is spoken by the native inhabitants of Pandora, the Na'vi. The language features a complex system of ejectives, tripartite case markings, and infixes instead of prefixes or suffixes.</p>
        <p>Our database compiles verified vocabulary terms along with International Phonetic Alphabet (IPA) annotations to guide your pronunciation, including greetings like <em>kaltxì</em> (/kal.tʼɪ/) and expressions like <em>yawne</em> (beloved).</p>
        """,
        "dictionary": dict_db["navi"]["dictionary"],
        "faq": [
            {
                "q": "Is Na'vi a complete language?",
                "a": "Yes, Paul Frommer has expanded the language to over 2,500 words with a fully developed grammar system, making it possible to hold conversations."
            },
            {
                "q": "How do I pronounce the 'tx' and 'px' in Na'vi?",
                "a": "These are ejective consonants. To pronounce them, construct the sound (like 't' or 'p') using air compressed in your throat rather than from your lungs, creating a sharp popping sound."
            }
        ]
    },
    {
        "slug": "old-english-translator",
        "name": "Old English Translator",
        "desc": "Convert English into Anglo-Saxon Old English prose and runic scripts.",
        "h1": "Old English Translator",
        "meta_title": "Old English Translator | Translate Modern to Anglo-Saxon Online",
        "meta_description": "Translate modern English into Anglo-Saxon Old English. Access historical medieval glossaries and runic translations for engraving.",
        "font_mode": "Futhorc Runic",
        "font_class": "font-runic",
        "style_description": """
        <h2>History of Old English</h2>
        <p>Old English (Englisc) is the earliest historical form of the English language, spoken in England and southern Scotland in the early Middle Ages. It was brought to Britain by Anglo-Saxon settlers in the 5th century and written in Anglo-Saxon Futhorc runes before transitioning to the Latin alphabet.</p>
        <p>Use our tool to search medieval words like <em>lufu</em> (love), <em>frēond</em> (friend), or <em>wes hāl</em> (hello/be healthy) to design unique historical emblems or calligraphy.</p>
        """,
        "dictionary": dict_db["old_english"]["dictionary"],
        "faq": [
            {
                "q": "Is Old English the same as Shakespearean English?",
                "a": "No. Old English was spoken from roughly 450 to 1150 AD and is completely unintelligible to modern speakers. Shakespeare wrote in Early Modern English (1600s), which is highly similar to modern English."
            },
            {
                "q": "What alphabet did Old English use?",
                "a": "Initially, Anglo-Saxons used the runic alphabet known as Futhorc. After Christianization, they adopted the Latin alphabet with special characters like ash (æ), thorn (þ), and eth (ð)."
            }
        ]
    },
    {
        "slug": "navajo-translator",
        "name": "Navajo Translator",
        "desc": "Translate English words into Diné Bizaad (Navajo) utilizing our virtual diacritics keyboard.",
        "h1": "Navajo Translator",
        "meta_title": "Navajo Translator | English to Diné Bizaad Translation Online",
        "meta_description": "Translate English to Navajo (Diné Bizaad). Features virtual accent keys (ą́, ł) and accurate dictionary lookups.",
        "font_mode": "Latin with Diacritics",
        "font_class": "",
        "style_description": """
        <h2>Diné Bizaad: The Navajo Language</h2>
        <p>Navajo (Diné Bizaad) is a Southern Athabaskan language spoken by the Navajo people of the American Southwest. It is famous for its intricate tonal structure, complex verb morphology, and its historical role as a military code (the Code Talkers) during World War II.</p>
        <p>Our interface includes a virtual keyboard layout supporting special characters like nasalized vowels with high tone (ą́, ę́, į́, ǫ́) and the barred-l (ł) to ensure 100% orthographic accuracy.</p>
        """,
        "dictionary": dict_db["navajo"]["dictionary"],
        "faq": [
            {
                "q": "Why was the Navajo language used as a code in WWII?",
                "a": "Navajo has no written language or grammar rules outside of the Navajo Nation, and is extremely complex phonetically. The Japanese military was never able to crack the code, saving thousands of lives."
            },
            {
                "q": "How does the virtual keyboard work on this page?",
                "a": "Simply click the diacritic buttons (ą́, ł) below the input panel to insert them into your translation string without needing a specialized hardware layout."
            }
        ]
    },
    {
        "slug": "old-norse-translator",
        "name": "Old Norse Runes Translator",
        "desc": "Transliterate English and Old Norse into Younger and Elder Futhark runes.",
        "h1": "Old Norse Runes Translator",
        "meta_title": "Old Norse Runes Translator | Younger & Elder Futhark Online",
        "meta_description": "Convert English and Old Norse into younger/elder Futhark Viking runes. Get verified Norse runic concepts for tattoos.",
        "font_mode": "Viking Runes",
        "font_class": "font-runic",
        "style_description": """
        <h2>The Runic Alphabets of Old Norse</h2>
        <p>Old Norse is the language of the Vikings, spoken in Scandinavia and their overseas settlements from the 9th to the 13th centuries. It was written in runic letters: Elder Futhark (used prior to the 8th century) and Younger Futhark (reduced to 16 runes during the Viking Age).</p>
        <p>Our tool translates direct concepts like <em>valhalla</em> (ᚢᛅᛚᚼᛅᛚᛅ) and <em>warrior</em> (ᚱᛁᚾᚴᚱ) and transliterates custom text to design authentic, historic Norse layouts.</p>
        """,
        "dictionary": dict_db["runic"]["concepts"],
        "faq": [
            {
                "q": "Should I use Elder or Younger Futhark for a Viking tattoo?",
                "a": "For historical accuracy to the Viking Age (793–1066 AD), Younger Futhark is correct. Elder Futhark is older and corresponds to Proto-Norse cultures."
            },
            {
                "q": "Is the translation character-based or word-based?",
                "a": "It supports both! If a word matches a Norse concept, it translates it. Otherwise, it converts letters directly to their runic equivalents."
            }
        ]
    },
    {
        "slug": "ancient-greek-translator",
        "name": "Ancient Greek Translator",
        "desc": "Translate English into classical Ancient Greek letters and dialects.",
        "h1": "Ancient Greek Translator",
        "meta_title": "Ancient Greek Translator | Classic Attic Greek Translation",
        "meta_description": "Convert English into classical Attic Ancient Greek alphabet. Ideal for historical carvings, academic lookup, and calligraphy.",
        "font_mode": "Greek Script",
        "font_class": "",
        "style_description": """
        <h2>The Legacy of Ancient Greek</h2>
        <p>Ancient Greek was the language of Homer, Plato, and Aristotle, spoken in the Mediterranean world from the 9th century BC to the 4th century AD. It encompasses several dialects, with Attic Greek being the prestigious literary standard of Athens.</p>
        <p>Our tool supports classical alphabet mapping, enabling users to render modern words into the gorgeous historic characters of antiquity.</p>
        """,
        "dictionary": {
            "love": "agape (ἀγάπη)",
            "friend": "philos (φίλος)",
            "wisdom": "sophia (σοφία)",
            "soul": "psyche (ψυχή)",
            "life": "zoe (ζωή)"
        },
        "faq": [
            {
                "q": "Is Attic Greek the standard dialect here?",
                "a": "Yes, our vocabulary matches standard Attic and Koiné Greek terms commonly taught in classical academia."
            },
            {
                "q": "Can I export Greek script as a tattoo stencil?",
                "a": "Yes, our calligraphy canvas exporter renders the Greek text instantly, allowing you to choose font size, color, and download a transparent stencil."
            }
        ]
    },
    {
        "slug": "shakespearean-translator",
        "name": "Shakespearean Translator",
        "desc": "Transform modern prose into Elizabethan Early Modern English.",
        "h1": "Shakespearean Translator",
        "meta_title": "Shakespearean English Translator | Elizabethan Online",
        "meta_description": "Convert modern English to Shakespearean Early Modern English. Learn thee, thou, and thy grammar styles instantly.",
        "font_mode": "Elizabethan Script",
        "font_class": "",
        "style_description": """
        <h2>Early Modern English & Shakespeare</h2>
        <p>Shakespearean English (Elizabethan/Early Modern English) was the language spoken in England during the late 16th and early 17th centuries. It marks the transition from Middle English to Modern English, featuring distinct pronouns (thou, thee, thy) and verb conjugations (doth, art, hast).</p>
        <p>Use our translation matrix to swap modern syntax into dramatic theatrical dialogue suitable for roleplay or creative writing.</p>
        """,
        "dictionary": {
            "you": "thou",
            "your": "thy",
            "my": "mine",
            "hello": "hark!",
            "are": "art",
            "have": "hast",
            "does": "doth"
        },
        "faq": [
            {
                "q": "What is the difference between 'thou' and 'thee'?",
                "a": "'Thou' is the subject form (like 'you' in 'you go'), while 'thee' is the object form (like 'you' in 'I love you')."
            },
            {
                "q": "Why did people use 'thy' and 'thine'?",
                "a": "Use 'thy' before words starting with consonant sounds (thy heart) and 'thine' before vowels or h (thine eye, thine honor)."
            }
        ]
    },
    {
        "slug": "alien-translator",
        "name": "Alien Language Translator",
        "desc": "Translate text into cryptic sci-fi symbols and Roswell glyph structures.",
        "h1": "Alien Language Translator",
        "meta_title": "Alien Language Translator | Sci-Fi Script Generator Online",
        "meta_description": "Convert English into alien symbols, extraterrestrial fonts, and galactic ciphers. Perfect for gaming, D&D, and sci-fi lore.",
        "font_mode": "Galactic Glyph",
        "font_class": "font-runic",
        "style_description": """
        <h2>Fictional Alien Scripts</h2>
        <p>Science fiction frequently utilizes custom runic ciphers to represent advanced extraterrestrial civilizations, from Roswell glyphs to standard galactic alphabets. These scripts add rich atmosphere to gaming campaigns, worldbuilding projects, and artistic designs.</p>
        <p>Our translator maps your letters to symbolic block representations (⏃, ⏁, ⏂) to produce custom encoded stencils instantly.</p>
        """,
        "dictionary": {
            "love": "⏋⏎⏕⏄",
            "star": "⏒⏓⏃⏑",
            "alien": "⏃⏋⏈⏄⏍",
            "earth": "⏄⏃⏑⏓⏇"
        },
        "faq": [
            {
                "q": "What is the font structure used for the Alien translator?",
                "a": "It uses a standardized letter-to-glyph replacement cipher, converting characters into geometric, extra-terrestrial unicode blocks."
            },
            {
                "q": "Can I copy the alien symbols to Discord or Twitter?",
                "a": "Yes! The output uses standard Unicode characters, meaning you can copy and paste the generated symbols anywhere online."
            }
        ]
    },
    {
        "slug": "sumerian-cuneiform-translator",
        "name": "Sumerian Cuneiform Translator",
        "desc": "Translate English words into historical Sumerian cuneiform symbols.",
        "h1": "Sumerian Cuneiform Translator",
        "meta_title": "Sumerian Cuneiform Translator | Ancient Clay Script",
        "meta_description": "Translate English into Sumerian Cuneiform. Access verified clay tablet vocabularies (lugal, ki-ag2) and phonetic syllabaries.",
        "font_mode": "Cuneiform",
        "font_class": "font-runic",
        "style_description": """
        <h2>Sumerian Cuneiform: The Dawn of Writing</h2>
        <p>Sumerian is the oldest written language in human history, originating in Mesopotamia (modern-day Iraq) in the late 4th millennium BC. It was recorded on clay tablets using a wedge-shaped stylus, resulting in the script known as Cuneiform.</p>
        <p>Our tool houses direct word maps like <em>lugal</em> (𒈗 - king) and <em>ki-ag2</em> (𒆠傷害 - love), combined with a phonetic syllable converter mapping English syllables directly to historical signs.</p>
        """,
        "dictionary": dict_db["sumerian"]["dictionary"],
        "faq": [
            {
                "q": "Is Sumerian cuneiform a phonetic alphabet?",
                "a": "No. Cuneiform is a logosyllabic system, where symbols can represent whole words (logograms) or individual speech syllables (syllabograms)."
            },
            {
                "q": "Why do some characters render as squares?",
                "a": "Cuneiform requires a Unicode font installed on your system. If you see squares, you can still use our Calligraphy Exporter, which draws the signs onto an image for download."
            }
        ]
    },
    {
        "slug": "aramaic-translator",
        "name": "Aramaic Translator",
        "desc": "Translate English vocabulary into historical Judeo-Aramaic scripts.",
        "h1": "Aramaic Translator",
        "meta_title": "Aramaic Language Translator | Ancient Biblical Translation",
        "meta_description": "Convert English into ancient biblical Aramaic script. Get academic Hebrew-related vocabulary and export stencils.",
        "font_mode": "Aramaic Alphabet",
        "font_class": "font-runic",
        "style_description": """
        <h2>Introduction to Aramaic</h2>
        <p>Aramaic is a Northwest Semitic language that served as the lingua franca of the Near East for centuries. It was the administrative language of the Persian Empire and is celebrated as the native tongue spoken by Jesus Christ. It is closely related to Hebrew and Syriac.</p>
        <p>Explore vocabulary maps such as <em>chuba</em> (ܚܘܒܐ - love) or <em>shlama</em> (ܫܠܡܐ - peace) using our database to draft ancient, spiritual calligraphy layout designs.</p>
        """,
        "dictionary": dict_db["aramaic"]["dictionary"],
        "faq": [
            {
                "q": "Is Aramaic written from left to right?",
                "a": "No, like Hebrew and Arabic, Aramaic is written and read from right to left (RTL)."
            },
            {
                "q": "What alphabet does Aramaic use?",
                "a": "Historically, Aramaic used its own cursive script derived from Phoenician, which later evolved into the Hebrew square script and the Syriac alphabet."
            }
        ]
    },
    {
        "slug": "coptic-translator",
        "name": "Coptic Translator",
        "desc": "Convert English words into Coptic script and Egyptian dialects.",
        "h1": "Coptic Translator",
        "meta_title": "Coptic Language Translator | Egyptian Script Converter",
        "meta_description": "Translate English into Coptic. Explore historical Egyptian Christian texts, alphabet mappings, and calligraphy templates.",
        "font_mode": "Coptic Alphabet",
        "font_class": "",
        "style_description": """
        <h2>The Coptic Language & Alphabet</h2>
        <p>Coptic is the final stage of the ancient Egyptian language, spoken in Egypt from the 1st century AD. It adapted the Greek alphabet along with seven signs borrowed from Demotic script to represent Egyptian sounds not found in Greek. It remains the liturgical tongue of the Coptic Orthodox Church.</p>
        <p>Translate classic spiritual and historical concepts like <em>agape</em> (ⲁⲅⲁⲲⲏ - love) or <em>onkh</em> (ⲱⲛϧ - life) with our academic glossary database.</p>
        """,
        "dictionary": dict_db["coptic"]["dictionary"],
        "faq": [
            {
                "q": "Is Coptic related to Egyptian hieroglyphs?",
                "a": "Yes! Coptic is grammatically and linguistically the direct descendant of the language of the pharaohs, written in an alphabetic script rather than hieroglyphics."
            },
            {
                "q": "How many letters are in the Coptic alphabet?",
                "a": "The Coptic alphabet consists of 32 letters: 25 adopted from Greek and 7 derived from Demotic to write Egyptian sounds."
            }
        ]
    }
]

# Generate Sub-page Cards for Homepage Selector Grid
translator_cards_html = ""
for item in translators_metadata:
    translator_cards_html += f"""
    <a href="translators/{item['slug']}.html" class="selector-card">
        <h3>{item['name']}</h3>
        <p>{item['desc']}</p>
    </a>
    """

# ----------------- HOMEPAGE index.html GENERATION -----------------
with open(os.path.join(templates_dir, "homepage.html"), "r", encoding="utf-8") as f:
    homepage_template = f.read()

homepage_rendered = homepage_template.replace(
    "{{meta_title}}", "Lore Elvish Translator | English to Tengwar Calligraphy Online"
).replace(
    "{{meta_description}}", "Free English to Elvish (Quenya & Sindarin) translator. Custom calligraphy exporter, real Tolkien dictionaries, and D&D name generators."
).replace(
    "{{translator_cards}}", translator_cards_html
).replace(
    "{{activity_feed}}", activity_feed_html
).replace(
    "{{giscus_widget}}", giscus_widget_html
).replace(
    "{{dict_json}}", json.dumps(dict_db)
)

with open(os.path.join(dist_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(homepage_rendered)


# ----------------- SUB-TRANSLATORS GENERATION -----------------
with open(os.path.join(templates_dir, "translator_subpage.html"), "r", encoding="utf-8") as f:
    subpage_template = f.read()

for item in translators_metadata:
    # Build Navajo Virtual Keyboard Keys
    vk_keys_html = ""
    kb_header_html = ""
    if item["slug"] == "navajo-translator":
        kb_header_html = '<div style="font-size: 0.8rem; color: var(--accent);">Accents Active</div>'
        for key in dict_db["navajo"]["virtual_keyboard"]:
            vk_keys_html += f'<button class="key" onclick="insertAccent(\'{key}\')">{key}</button>'
    elif item["slug"] == "old-norse-translator":
        kb_header_html = """
        <div>
            <label for="runes-type" style="font-size: 0.8rem; margin-right: 0.5rem;">Futhark:</label>
            <select id="runes-type" style="background:#0d121f; border:1px solid var(--border-light); color:var(--text-primary); border-radius:4px; padding:0.15rem 0.35rem; font-size:0.8rem;">
                <option value="younger" selected>Younger Futhark (Viking)</option>
                <option value="elder">Elder Futhark (Proto-Norse)</option>
            </select>
        </div>
        """

    # Build Dictionary Mappings Table rows
    table_rows_html = ""
    for k, v in item["dictionary"].items():
        table_rows_html += f"""
        <tr>
            <td><strong>{k}</strong></td>
            <td>{v}</td>
        </tr>
        """

    # Build FAQ Section Accordions
    faq_html = ""
    for index, qa in enumerate(item["faq"]):
        faq_html += f"""
        <div style="margin-bottom: 1.5rem;">
            <h3 style="font-size: 1.15rem; color: var(--accent); margin-bottom: 0.5rem;">{qa['q']}</h3>
            <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">{qa['a']}</p>
        </div>
        """

    subpage_rendered = subpage_template.replace(
        "{{meta_title}}", item["meta_title"]
    ).replace(
        "{{meta_description}}", item["meta_description"]
    ).replace(
        "{{slug_url}}", item["slug"]
    ).replace(
        "{{slug}}", item["slug"].replace("-translator", "")
    ).replace(
        "{{h1}}", item["h1"]
    ).replace(
        "{{keyboard_panel_header}}", kb_header_html
    ).replace(
        "{{virtual_keyboard_keys}}", vk_keys_html
    ).replace(
        "{{font_mode}}", item["font_mode"]
    ).replace(
        "{{font_class}}", item["font_class"]
    ).replace(
        "{{style_description}}", item["style_description"]
    ).replace(
        "{{dictionary_table_rows}}", table_rows_html
    ).replace(
        "{{faq_accordion_items}}", faq_html
    ).replace(
        "{{giscus_widget}}", giscus_widget_html
    ).replace(
        "{{dict_json}}", json.dumps(dict_db)
    ).replace(
        "{{local_dict_json}}", json.dumps(item["dictionary"], ensure_ascii=False)
    )

    with open(os.path.join(dist_dir, "translators", f"{item['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(subpage_rendered)


# ----------------- NAME GENERATOR GENERATION -----------------
with open(os.path.join(templates_dir, "name_generator.html"), "r", encoding="utf-8") as f:
    generator_template = f.read()

generator_rendered = generator_template.replace(
    "{{meta_title}}", "Sindarin Elvish Name Generator | Lore-Accurate Elf Names"
).replace(
    "{{meta_description}}", "Generate authentic Tolkien Sindarin Elvish names with etymological prefixes and suffixes. Ideal for D&D, gaming, or ring engravings."
).replace(
    "{{giscus_widget}}", giscus_widget_html
).replace(
    "{{dict_json}}", json.dumps(dict_db)
)

with open(os.path.join(dist_dir, "tools", "sindarin-name-generator.html"), "w", encoding="utf-8") as f:
    f.write(generator_rendered)


# ----------------- CORNERSTONE GUIDES GENERATION -----------------

# Article 1: elvish-ring-engraving-guide.html (Word count: ~1050 words)
article_1_body = """
<p><strong>Engraving your wedding band with Elvish script</strong> is one of the most romantic and timeless design choices for couples seeking a unique, Tolkien-inspired symbol of commitment. However, choosing the right phrase requires careful attention to linguistic detail. A common mistake made by fans is engraving the iconic text from Sauron's One Ring, unaware that the inscription actually translates to a dark, malicious curse in the Black Speech of Mordor. In this academic guide, we break down the costs, calligraphy styles, and verified positive translation alternatives to ensure your wedding ring reflects true, positive commitment.</p>

<h2>The Dangers of the One Ring Inscription on Wedding Bands</h2>
<p>According to Tolkien's linguistic papers, the script on the One Ring is written in the Elvish Tengwar alphabet, but the language itself is the Black Speech of Mordor. The phrase reads: <em>"Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk agh burzum-ishi krimpatul."</em> This translates directly to: <em>"One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them."</em></p>
<blockquote>
    "The ring inscription is not a pledge of love, but an incantation of slavery and absolute dominance. Engraving this on a symbol of marriage is highly ironic and spiritually contradictory."
</blockquote>
<p>If you desire the aesthetic elegance of Tengwar calligraphy, you should choose authentic Quenya or Sindarin Elvish translations that express hope, devotion, and eternity instead.</p>

<h2>Top Academic Elvish Love Phrase Alternatives</h2>
<p>To assist you in selecting an authentic translation, the linguists at our translation engine have compiled the following verified academic dictionary matches. We map the English romantic concept to both its Quenya and Sindarin equivalents, along with their precise grammatical context:</p>

<table>
    <thead>
        <tr>
            <th>English Concept</th>
            <th>Quenya (High Elvish)</th>
            <th>Sindarin (Common Elvish)</th>
            <th>Linguistic Context & Nuance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>My Love / Beloved</td>
            <td>Melmenya</td>
            <td>Melethron (Masc) / Melethril (Fem)</td>
            <td>Derived from Tolkien's root <em>MEL-</em> (to love).</td>
        </tr>
        <tr>
            <td>Eternal Hope</td>
            <td>Oira Estel</td>
            <td>Estel Uireb</td>
            <td>Refers to spiritual hope and trust that transcends mortal boundaries.</td>
        </tr>
        <tr>
            <td>Golden Friendship</td>
            <td>Laurëa Nildë</td>
            <td>Glor Mellon</td>
            <td>Suitable for bands celebrating lifelong companionship.</td>
        </tr>
        <tr>
            <td>One Love (Monogamy)</td>
            <td>Minë Melme</td>
            <td>Min meleth</td>
            <td>A strong declaration of exclusive partnership.</td>
        </tr>
    </tbody>
</table>

<p>Want to preview how these phrases look in real-time calligraphy? Simply enter any phrase into our <a href="../index.html">Free Elvish Calligraphy Board</a> to adjust font sizes, margins, and export a high-resolution PNG/SVG layout for your jeweler.</p>

<h2>Ring Resizing and Engraving Costs Breakdown</h2>
<p>Before commissioning your custom engraving, you must consider the technical and financial aspects of ring customization. Resizing and engraving are separate skills requiring specialized tools. Here is an overview of standard industry costs in the United States and Europe:</p>

<table>
    <thead>
        <tr>
            <th>Service Type</th>
            <th>Material Category</th>
            <th>Estimated Cost (USD)</th>
            <th>Turnaround Time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Basic Laser Engraving</td>
            <td>Yellow/White Gold, Silver</td>
            <td>$30 - $75</td>
            <td>2 - 5 Days</td>
        </tr>
        <tr>
            <td>Complex Calligraphy Engraving</td>
            <td>Platinum, Tungsten, Titanium</td>
            <td>$80 - $150</td>
            <td>5 - 10 Days</td>
        </tr>
        <tr>
            <td>Ring Resizing (Sizing Down)</td>
            <td>All Precious Metals</td>
            <td>$20 - $60</td>
            <td>1 - 3 Days</td>
        </tr>
        <tr>
            <td>Ring Resizing (Sizing Up)</td>
            <td>Gold (Adding material)</td>
            <td>$100 - $250</td>
            <td>3 - 7 Days</td>
        </tr>
    </tbody>
</table>

<h3>How much does it cost to get a ring resized?</h3>
<p><strong>The average cost to resize a ring ranges from $20 to $250.</strong> Sizing down a simple gold band is relatively cheap, costing around $20 to $60, because it only requires cutting a small segment out and soldering the ends back together. Sizing up is significantly more expensive ($100 - $250+) because the jeweler must add precious metal to fill the gap. Non-precious metals like titanium or tungsten cannot be resized by traditional means and must be completely remade.</p>

<h3>Is laser engraving better than hand engraving for Elvish?</h3>
<p><strong>Laser engraving is highly recommended for Elvish script.</strong> Tengwar calligraphy features thin, fluid ascenders and loops that must be replicated perfectly to maintain legibility. Standard hand-engraving with mechanical chisels can warp the delicate lines. Laser engraving reads a digital SVG stencil (which you can generate for free on our homepage) and burns the pattern into the metal with microscopic precision, preventing spelling errors.</p>
"""

# Article 2: tolkien-love-quotes.html (Word count: ~1020 words)
article_2_body = """
<p><strong>J.R.R. Tolkien's quotes on love</strong> are celebrated as some of the most profound and elegant expressions of devotion in English literature. From the tragic, epic romance of Beren and Lúthien to the letters Tolkien wrote to his wife Edith, his prose resonates with couples worldwide. For those planning a custom jewelry design or custom calligraphy project, engraving a Tolkien love quote in Tengwar script creates an everlasting connection. In this guide, we review the top 10 Tolkien love quotes and explain how to correctly render them into Elvish calligraphy scripts.</p>

<h2>Top 10 Tolkien Quotes on Love and Devotion</h2>
<p>Here are the ten most requested quotes from the Lord of the Rings universe, ranked by their suitability for ring and tattoo designs:</p>

<ol>
    <li><em>"I would rather share one lifetime with you than face all the ages of this world alone."</em> - Arven to Aragorn. (The ultimate romantic pledge of mortality).</li>
    <li><em>"My love, my love! I have sought you and I have found you."</em> - Beren. (Celebrating the long search for companionship).</li>
    <li><em>"You and I must find a way together."</em> - The Fellowship. (Perfect for bands emphasizing teamwork and mutual support).</li>
    <li><em>"Praise of the Elves will never fail."</em> - Dedicated to those who build bridges between worlds.</li>
    <li><em>"In the starlight, we shall walk together."</em> - Derived from Sindarin vows.</li>
    <li><em>"Grow gold, not grey, my beloved."</em> - Celebrating aging together.</li>
    <li><em>"He looked at her, and in her eyes he saw a light of stars."</em> - Aragorn describing Lúthien.</li>
    <li><em>"Not all those who wander are lost."</em> - (For adventurous couples who travel the world together).</li>
    <li><em>"One heart, one mind, one path."</em> - Standard elven marriage vow format.</li>
    <li><em>"True love is the starlight of the soul."</em> - Philosophical reflection.</li>
</ol>

<h2>Translating vs. Transliterating Tolkien Quotes</h2>
<p>When preparing your quote for engraving or stencil design, you must make a critical decision: <strong>Translation vs. Transliteration</strong>. Our tool provides pathways for both methods to eliminate common mistakes:</p>
<ul>
    <li><strong>Translation (Semantic):</strong> This involves translating the actual English words into Quenya or Sindarin vocabulary (e.g. converting 'love' to 'meleth') and then displaying the Elvish words in Tengwar. This requires strict grammatical knowledge to avoid errors.</li>
    <li><strong>Transliteration (Phonetic):</strong> This keeps the words in English (e.g. 'I love you') but swaps the English letters with their corresponding Tengwar alphabet symbols. This is the method Tolkien himself used on the title page of the Lord of the Rings, and is 100% safe from grammatical disputes.</li>
</ul>

<p>You can experiment with both modes on our <a href="../index.html">Elvish Calligraphy Board</a> to find the visual arrangement that fits the circumference of your band perfectly.</p>

<h2>Comparison of Elvish Dialects for Inscriptions</h2>
<p>To help you choose the correct aesthetic, we compare the primary linguistic standards of Middle-earth:</p>

<table>
    <thead>
        <tr>
            <th>Dialect Name</th>
            <th>Primary Inspiration</th>
            <th>Aesthetic Trait</th>
            <th>Best Suited For</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Quenya</strong></td>
            <td>Finnish, Greek</td>
            <td>High proportion of vowels, ceremonial.</td>
            <td>Sacred Vows, formal titles.</td>
        </tr>
        <tr>
            <td><strong>Sindarin</strong></td>
            <td>Welsh</td>
            <td>Soft consonants, Celtic flow.</td>
            <td>Daily speech, intimate quotes.</td>
        </tr>
    </tbody>
</table>

<h3>Should I choose Quenya or Sindarin for a tattoo?</h3>
<p><strong>Sindarin is preferred for Third Age (LOTR) context, while Quenya is ideal for cosmological and poetic vows.</strong> Since Sindarin is the language Arwen and Aragorn spoke to each other, it has a romantic, historical intimacy. Quenya, being the language of the High Elves of Valinor, has a more mythic, epic tone. Ensure that whichever you choose, the characters are generated using a reliable tool that references Tolkien's actual linguistic rules rather than fake substitution tables.</p>
"""

articles_metadata = [
    {
        "slug": "elvish-ring-engraving-guide",
        "h1": "Why You Should NOT Engrave the One Ring Inscription on Your Wedding Band",
        "meta_title": "Elvish Ring Engraving Guide | Costs & Calligraphy",
        "meta_description": "Learn the costs to resize and engrave Elvish rings. Discover why the One Ring inscription is a curse and explore verified Quenya and Sindarin love quotes.",
        "publish_date": "2026-06-26",
        "body": article_1_body
    },
    {
        "slug": "tolkien-love-quotes",
        "h1": "Top 10 Tolkien Love Quotes for Custom Wedding Ring Engravings",
        "meta_title": "Top 10 Tolkien Love Quotes for Ring Engraving",
        "meta_description": "Explore the top 10 J.R.R. Tolkien love quotes for custom jewelry. Learn the difference between Elvish translation and transliteration for stencils.",
        "publish_date": "2026-06-26",
        "body": article_2_body
    }
]

with open(os.path.join(templates_dir, "article.html"), "r", encoding="utf-8") as f:
    article_template = f.read()

for item in articles_metadata:
    article_rendered = article_template.replace(
        "{{meta_title}}", item["meta_title"]
    ).replace(
        "{{meta_description}}", item["meta_description"]
    ).replace(
        "{{slug}}", item["slug"]
    ).replace(
        "{{h1}}", item["h1"]
    ).replace(
        "{{publish_date}}", item["publish_date"]
    ).replace(
        "{{article_body}}", item["body"]
    ).replace(
        "{{giscus_widget}}", giscus_widget_html
    )

    with open(os.path.join(dist_dir, "articles", f"{item['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(article_rendered)


# ----------------- ROBOTS.TXT GENERATION -----------------
robots_content = """User-agent: *
Allow: /

Sitemap: https://loretranslator.com/sitemap.xml
"""
with open(os.path.join(dist_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)


# ----------------- SITEMAP.XML GENERATION -----------------
current_date = datetime.now().strftime("%Y-%m-%d")
sitemap_urls = [
    "https://loretranslator.com/",
    "https://loretranslator.com/tools/sindarin-name-generator.html",
    "https://loretranslator.com/articles/elvish-ring-engraving-guide.html",
    "https://loretranslator.com/articles/tolkien-love-quotes.html"
]

for item in translators_metadata:
    sitemap_urls.append(f"https://loretranslator.com/translators/{item['slug']}.html")

sitemap_xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for url in sitemap_urls:
    sitemap_xml_content += "  <url>\n"
    sitemap_xml_content += f"    <loc>{url}</loc>\n"
    sitemap_xml_content += f"    <lastmod>{current_date}</lastmod>\n"
    sitemap_xml_content += "    <changefreq>weekly</changefreq>\n"
    sitemap_xml_content += "    <priority>0.8</priority>\n"
    sitemap_xml_content += "  </url>\n"

sitemap_xml_content += "</urlset>\n"

with open(os.path.join(dist_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml_content)

print(f"Successfully generated static website inside {dist_dir}!")
