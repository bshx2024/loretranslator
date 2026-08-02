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

# Copy base CSS and mockup images
shutil.copy(
    os.path.join(templates_dir, "base.css"),
    os.path.join(dist_dir, "templates", "base.css")
)
shutil.copy(
    os.path.join(templates_dir, "ring_mockup.png"),
    os.path.join(dist_dir, "templates", "ring_mockup.png")
)
shutil.copy(
    os.path.join(templates_dir, "wrist_tattoo_mockup.png"),
    os.path.join(dist_dir, "templates", "wrist_tattoo_mockup.png")
)

# Google Analytics Tracking Code
google_analytics_html = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CPDKHVNK1S"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-CPDKHVNK1S');
</script>"""

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
        <div class="feed-title" style="color: var(--accent); font-family: 'Cinzel', serif; font-weight: 600; margin-bottom: 0.25rem;">{feed['title']}</div>
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
        "h1": "Sindarin Translator & English to Elvish Dictionary",
        "meta_title": "Sindarin Translator: English to Elvish Tattoo Runes | Lore",
        "meta_description": "Free English to Sindarin translator & dictionary. Translate text & names into Tengwar Elvish runes for tattoos & ring engravings. Instant PNG exporter!",
        "font_mode": "Tengwar",
        "font_class": "font-tengwar",
        "style_description": """
        <h2>Introduction to Sindarin Elvish Translation</h2>
        <p>Sindarin is the primary Elvish tongue spoken in Middle-earth during the Third Age of <em>The Lord of the Rings</em>. Unlike Quenya, which functioned as a high ceremonial language, Sindarin was the living, daily tongue of the Grey-elves (Sindar). Tolkien derived Sindarin phonology and grammar from Welsh, creating a soft, fluid language with rich vowel mutations.</p>

        <h3>Popular English to Sindarin Phrases & Translations</h3>
        <p>Looking for quick translations for everyday phrases, greetings, or romantic declarations? Here are the most frequently requested Sindarin expressions matched from verified academic dictionaries:</p>
        <table>
            <thead>
                <tr>
                    <th>English Expression</th>
                    <th>Sindarin Elvish Translation</th>
                    <th>Phonetic & Usage Context</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>I love you</strong></td>
                    <td>Gi melin (or <em>Meleth</em> for love)</td>
                    <td>Romantic declaration / Wedding ring inscriptions</td>
                </tr>
                <tr>
                    <td><strong>Hello / Greetings</strong></td>
                    <td>Suilad (or <em>Mae govannen</em>)</td>
                    <td>Traditional Elven greeting ("Well met")</td>
                </tr>
                <tr>
                    <td><strong>Thank you</strong></td>
                    <td>Hantanyel</td>
                    <td>Expression of gratitude</td>
                </tr>
                <tr>
                    <td><strong>Goodbye / Farewell</strong></td>
                    <td>Novaer</td>
                    <td>Parting blessing ("Be well")</td>
                </tr>
                <tr>
                    <td><strong>Friend</strong></td>
                    <td>Mellon</td>
                    <td>Famous Moria gate password</td>
                </tr>
                <tr>
                    <td><strong>Hope</strong></td>
                    <td>Estel</td>
                    <td>Aragorn's Elvish given name</td>
                </tr>
            </tbody>
        </table>

        <h3>Sindarin Name Translator & Custom Elvish Tattoo Script</h3>
        <p>Whether you want to translate modern English names (such as <em>sindarin girl names</em> or male Elf names) into calligraphic script, our online engine provides two distinct pathways: direct dictionary lookup for verified roots, and character-by-character Tengwar transliteration. You can use our specialized <a href="sindarin-name-translator.html">Sindarin Name Translator</a> for individual name transliterations or use our <a href="../tools/sindarin-name-generator.html">Sindarin Name Generator</a> to discover lore-accurate names for Elvish tattoos and ring engravings.</p>

        <h3>Sindarin Pronunciation & Elvish Phonetic Rules</h3>
        <p>Understanding Sindarin pronunciation is essential for authentic ring engravings and elvish tattoo design. Tolkien modeled Sindarin phonetics after modern Welsh, featuring crisp vowels and soft consonants:</p>
        <ul>
            <li><strong>Vowels:</strong> <em>a</em> (father), <em>e</em> (get), <em>i</em> (machine), <em>o</em> (for), and <em>u</em> (brute). Accent marks like <em>â</em> or <em>î</em> denote elongated vowel duration.</li>
            <li><strong>Consonants:</strong> The letter <em>c</em> is always pronounced hard as 'k' (e.g. <em>Círdan</em> = Keerdan), and <em>g</em> is always hard (as in 'give').</li>
            <li><strong>Diphthongs:</strong> Combinations such as <em>ae</em>, <em>ai</em>, <em>ei</em>, and <em>oe</em> flow smoothly together, giving Tengwar calligraphy its poetic rhythm.</li>
        </ul>
        """,
        "dictionary": dict_db["elvish"]["sindarin"],
        "faq": [
            {
                "q": "Can I use Google Translate or ChatGPT for English to Sindarin Elvish translation?",
                "a": "Google Translate does not support Sindarin Elvish. While generic AI tools like ChatGPT can generate approximate text, they frequently mix up High Elvish Quenya with Sindarin or output invalid Tengwar runes. Our online engine uses a verified academic dictionary and exact Tengwar font mappings."
            },
            {
                "q": "What is the difference between Sindarin and Quenya translators?",
                "a": "Sindarin is the common spoken language of Middle-earth Elves during the Third Age (LOTR era), based phonetically on Welsh. Quenya is High Elvish, comparable to Latin, used for sacred ceremonies and cosmology."
            },
            {
                "q": "Does this Sindarin translator support voice or audio pronunciation?",
                "a": "While there is no automated voice synthesizer for constructed Elvish tongues, our dictionary includes IPA phonetic guides and romanized spellings (e.g. Mellon = /ˈmɛl.lɔn/) to help you pronounce Sindarin words accurately."
            },
            {
                "q": "How do I translate my name to Elvish Tengwar for a custom tattoo?",
                "a": "Simply enter your name into the input panel above. The translator will map your name into the Tengwar runic alphabet phonetically. You can then use the Interactive Calligraphy Exporter below to customize font size, colors, and download a transparent stencil PNG for your tattoo artist."
            },
            {
                "q": "Is there a downloadable Sindarin translator app for mobile?",
                "a": "Our web application is 100% free, responsive, and mobile-optimized. You can use it directly in any browser on iOS or Android, or tap 'Add to Home Screen' to use it as a lightweight web app without installing APKs."
            }
        ]
    },
    {
        "slug": "sindarin-name-translator",
        "name": "Sindarin Name Translator",
        "desc": "Translate modern English male & female names into Sindarin Elvish Tengwar calligraphy script.",
        "h1": "Sindarin Name Translator & Write My Name in Elvish Generator",
        "meta_title": "Sindarin Name Translator: Write My Name in Elvish | Lore",
        "meta_description": "Free Sindarin name translator. Translate English male & female names into Tengwar Elvish runes for tattoos & ring engravings. Instant PNG exporter!",
        "font_mode": "Tengwar",
        "font_class": "font-tengwar",
        "style_description": """
        <h2>English to Sindarin Name Translation Guide</h2>
        <p>Translating modern personal names into Sindarin Elvish requires matching the etymological meaning or phonetic sound of your English name with Sindarin roots. Tolkien himself created Elvish equivalents for names based on their historical roots (e.g. <em>Alexander</em> = 'Defender of Men' -> <em>Garthangon</em>).</p>

        <h3>Popular Male & Female Sindarin Name Translations</h3>
        <p>Here are twenty popular English names translated into lore-accurate Sindarin Elvish forms and Tengwar calligraphic scripts:</p>
        <table>
            <thead>
                <tr>
                    <th>English Name</th>
                    <th>Etymological Meaning</th>
                    <th>Sindarin Elvish Name Translation</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>Alexander</strong></td><td>Defender of Men</td><td>Maethoron / Garthangon</td></tr>
                <tr><td><strong>Victoria</strong></td><td>Victory / Triumphant</td><td>Túriel / Aglareth</td></tr>
                <tr><td><strong>Edward</strong></td><td>Guardian of Wealth</td><td>Tirn-Gael</td></tr>
                <tr><td><strong>Sophia</strong></td><td>Wisdom</td><td>Ithildae / Saeleth</td></tr>
                <tr><td><strong>Lily</strong></td><td>White Flower</td><td>Niphredil / Indil</td></tr>
                <tr><td><strong>Michael</strong></td><td>Who is like God?</td><td>Valandil / Eruion</td></tr>
                <tr><td><strong>Emma</strong></td><td>Whole / Universal</td><td>Amariel / Páneth</td></tr>
                <tr><td><strong>James</strong></td><td>Supplanter / Traveler</td><td>Randir / Padhron</td></tr>
                <tr><td><strong>Olivia</strong></td><td>Olive / Peace</td><td>Sídhel / Oliva</td></tr>
                <tr><td><strong>Daniel</strong></td><td>God is my Judge</td><td>Badhron / Erudi</td></tr>
                <tr><td><strong>Charlotte</strong></td><td>Free Man / Noble</td><td>Laineth / Arwen</td></tr>
                <tr><td><strong>William</strong></td><td>Resolute Protector</td><td>Berthor / Thaneth</td></tr>
                <tr><td><strong>Ava</strong></td><td>Bird / Voice</td><td>Aewen / Lammeth</td></tr>
                <tr><td><strong>Benjamin</strong></td><td>Son of the Right Hand</td><td>Ion-Fort</td></tr>
                <tr><td><strong>Mia</strong></td><td>Beloved / Mine</td><td>Meleth / Melen</td></tr>
                <tr><td><strong>Ethan</strong></td><td>Strong / Firm</td><td>Bellon / Taugon</td></tr>
                <tr><td><strong>Harper</strong></td><td>Harp Player</td><td>Lirron / Glinneth</td></tr>
                <tr><td><strong>Lucas</strong></td><td>Light-giver / Bright</td><td>Calaron / Calen</td></tr>
                <tr><td><strong>Amelia</strong></td><td>Industrious / Striving</td><td>Carwen / Maereth</td></tr>
                <tr><td><strong>Mason</strong></td><td>Stone Worker</td><td>Sarnon / Tarag</td></tr>
            </tbody>
        </table>

        <h3>How to Write My Name in Elvish Tengwar Runes</h3>
        <p>Wondering <em>"how to write my name in Elvish"</em> for a custom tattoo stencil or wedding ring band? Translating modern English names into Sindarin Elvish can be accomplished through two distinct linguistic approaches:</p>
        <ul>
            <li><strong>Phonetic Transliteration (Most Popular for Tattoos):</strong> This method preserves the exact pronunciation of your name (e.g. <em>Emma</em>, <em>Michael</em>, <em>Liam</em>) and replaces each English letter with its exact phonetic Tengwar rune equivalent. This matches the method J.R.R. Tolkien used on the title pages of <em>The Lord of the Rings</em>.</li>
            <li><strong>Etymological Translation (Semantic Name Roots):</strong> This method translates the historical meaning of your name into Sindarin roots (e.g. <em>Michael</em> means 'Who is like God' -> <em>Valandil</em>). Refer to our male and female elvish name dictionary above to discover your true Elven name.</li>
        </ul>

        <p>Want to generate more lore-accurate names? Try our interactive <a href="../tools/sindarin-name-generator.html">Sindarin Name Generator</a> or return to the main <a href="sindarin-translator.html">Sindarin Translator</a> to translate complete sentences.</p>
        """,
        "dictionary": dict_db["elvish"]["sindarin"],
        "faq": [
            {
                "q": "Can I write my name in Elvish using Google Translate?",
                "a": "Google Translate does not offer Elvish translation or Tengwar font rendering. Generic AI tools like ChatGPT often output broken Tengwar glyphs. Our specialized Sindarin name translator provides lore-accurate phonetic mappings and downloadable PNG stencils."
            },
            {
                "q": "How do I translate my English name to Sindarin Elvish?",
                "a": "Type your name into the translator panel above. The tool maps English characters phonetically into Tengwar runes. If you prefer a semantic translation based on your name's historical meaning, refer to our vocabulary dictionary below."
            },
            {
                "q": "What are popular Sindarin girl names for tattoos?",
                "a": "Popular Sindarin female names include Arwen (Noble Maiden), Lúthien (Daughter of Flowers), Tauriel (Daughter of the Forest), and Niphredil (Little White Star)."
            },
            {
                "q": "Can I use this Sindarin name translator for tattoo stencils?",
                "a": "Yes! Enter your name above, select your desired font size and colors in the Interactive Calligraphy Exporter, and click 'Export PNG' to download a clean stencil for your tattoo artist."
            }
        ]
    },
    {
        "slug": "quenya-translator",
        "name": "Quenya Elvish Translator",
        "desc": "Translate modern English into the high ceremonial Quenya Elvish language of Valinor.",
        "h1": "Quenya Translator & English to High Elvish Dictionary",
        "meta_title": "Quenya Translator: English to High Elvish Tattoo | Lore",
        "meta_description": "Free English to Quenya High Elvish translator & dictionary. Translate text & names into Tengwar runes for tattoos & ring engravings. Instant PNG exporter!",
        "font_mode": "Tengwar",
        "font_class": "font-tengwar",
        "style_description": """
        <h2>Online Quenya Translator: English to High Elvish Dictionary</h2>
        <p>Quenya (High Elvish) is the ancient language of the Amanyar Elves who crossed the Great Sea into Valinor. In Middle-earth during the Third Age of <em>The Lord of the Rings</em>, Quenya functioned similarly to Latin in medieval Europe—a ceremonial language of high poetry, sacred vows, and cosmic lore.</p>

        <h3>Popular English to Quenya High Elvish Expressions (LOTR & Tolkien)</h3>
        <p>Looking for quick Quenya High Elvish translations for wedding vows, formal declarations, or custom tattoos? Here are verified high-elven phrases from Tolkien's academic lexicons:</p>
        <table>
            <thead>
                <tr>
                    <th>English Expression</th>
                    <th>Quenya High Elvish Translation</th>
                    <th>Grammatical Context & Usage</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>I love you</strong></td>
                    <td>Melinyel (or <em>Melme</em> for love)</td>
                    <td>Sacred devotion / Wedding ring vows</td>
                </tr>
                <tr>
                    <td><strong>Greetings / Star shines</strong></td>
                    <td>Elen síla lúmenn' omentielvo</td>
                    <td>Iconic greeting ("A star shines on our meeting")</td>
                </tr>
                <tr>
                    <td><strong>Farewell / Goodbye</strong></td>
                    <td>Namárië</td>
                    <td>Galadriel's classic poem title ("Farewell")</td>
                </tr>
                <tr>
                    <td><strong>Friend</strong></td>
                    <td>Nildo (male) / Nilde (female)</td>
                    <td>Formal high elven companionship</td>
                </tr>
                <tr>
                    <td><strong>Hope</strong></td>
                    <td>Estel</td>
                    <td>Spiritual trust and divine hope</td>
                </tr>
                <tr>
                    <td><strong>Light</strong></td>
                    <td>Cala / Cále</td>
                    <td>Illumination of Valinor</td>
                </tr>
            </tbody>
        </table>

        <h2>Quenya Alphabet, Tengwar Script & Pronunciation Rules</h2>
        <p>Understanding Quenya pronunciation is essential for authentic ring engravings and elvish tattoo designs. Tolkien modeled Quenya phonetics after Finnish and Classical Greek:</p>
        <ul>
            <li><strong>Vowels:</strong> Quenya vowels are pronounced purely: <em>a</em> (father), <em>e</em> (there), <em>i</em> (machine), <em>o</em> (more), and <em>u</em> (brute). Long vowels marked with acute accents (such as <em>á</em>, <em>é</em>, <em>í</em>, <em>ó</em>, <em>ú</em>) are held twice as long.</li>
            <li><strong>Consonants:</strong> The letter <em>c</em> is always pronounced as 'k' (e.g. <em>Cala</em> = Kahl-ah), and <em>qu</em> is pronounced as 'kw' (as in <em>Quenya</em> = Kwen-yah).</li>
            <li><strong>Tehtar Vowel Placement:</strong> Unlike Sindarin (which places vowel marks above the following consonant), Quenya mode places vowel markers (tehtar) above the preceding consonant symbol.</li>
        </ul>

        <p>Want to compare Quenya with Third Age spoken Elvish? Check out our <a href="sindarin-translator.html">Sindarin Translator</a>, try the specialized <a href="sindarin-name-translator.html">Sindarin Name Translator</a>, or explore <a href="../articles/tolkien-love-quotes.html">Tolkien Love Quotes for Rings</a>.</p>
        """,
        "dictionary": dict_db["elvish"]["quenya"],
        "faq": [
            {
                "q": "What is the difference between Quenya and Sindarin Elvish translators?",
                "a": "Quenya is High Elvish, used for high ceremonial writing, poetry, and lore (similar to Latin). Sindarin is the common daily language spoken by the Elves in Middle-earth during the Lord of the Rings era."
            },
            {
                "q": "Can I translate English names into Quenya High Elvish?",
                "a": "Yes! Personal names can be transliterated phonetically into Quenya Tengwar script using our live online converter. For semantic translations based on historical name roots (e.g. Victor -> Túro), refer to our High Elvish dictionary table below."
            },
            {
                "q": "Can I use Google Translate or ChatGPT as a Quenya translator?",
                "a": "Google Translate does not support Quenya Elvish. Generic AI tools like ChatGPT often mix up Quenya and Sindarin or generate broken Tengwar glyphs. Our specialized Quenya translator uses verified academic lexicons and precise Tengwar font mappings."
            },
            {
                "q": "Is there a downloadable Quenya translator app for mobile?",
                "a": "Our web application is 100% free, responsive, and mobile-optimized. You can use it directly in any browser on iOS or Android, or tap 'Add to Home Screen' to use it as a lightweight web app with instant PNG stencil exports."
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
        "meta_title": "Sumerian Cuneiform Translator: English to Clay Runes | Lore",
        "meta_description": "Free online Sumerian cuneiform translator for English to ancient clay tablet symbols. Convert text into authentic Mesopotamian glyphs with pronunciation guide!",
        "font_mode": "Cuneiform",
        "font_class": "font-runic",
        "style_description": """
        <h2>Online English to Sumerian Cuneiform Translator & Syllabary Converter</h2>
        <p>Welcome to <strong>LoreTranslator</strong>, the premier online <strong>Sumerian cuneiform translator</strong> and ancient Mesopotamian alphabet generator. Originating in Uruk and Nippur during the 4th millennium BC, cuneiform (from Latin <em>cuneus</em>, meaning 'wedge') is the oldest known writing system in human history. Scribes pressed reed styluses into wet clay tablets to record epic poems like the <em>Epic of Gilgamesh</em> and administrative decrees of kings.</p>
        
        <h3 style="font-family:'Cinzel', serif; color:var(--accent); font-size:1.1rem; margin-top:1.5rem; margin-bottom:0.5rem;">Sumerian Cuneiform Vocabulary & Glyph Dictionary Table</h3>
        <p>Our translator utilizes academic lexicons verified against the <em>Electronic Text Corpus of Sumerian Literature (ETCSL)</em> at the University of Oxford. Below is a <strong>Sumerian cuneiform dictionary chart</strong> translating common English words into Sumerian transliteration, authentic Unicode cuneiform glyphs, and International Phonetic Alphabet (IPA) audio pronunciation:</p>
        
        <table style="width:100%; border-collapse:collapse; margin-top:1rem; margin-bottom:1.5rem; font-size:0.88rem;">
            <thead>
                <tr style="border-bottom:1px solid var(--border-light); text-align:left;">
                    <th style="padding:0.5rem; color:var(--text-primary);">English Term</th>
                    <th style="padding:0.5rem; color:var(--text-primary);">Sumerian Transliteration</th>
                    <th style="padding:0.5rem; color:var(--text-primary);">Cuneiform Unicode Glyph</th>
                    <th style="padding:0.5rem; color:var(--text-primary);">IPA Pronunciation</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">King / Ruler</td>
                    <td style="padding:0.5rem;">Lugal</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒈗</td>
                    <td style="padding:0.5rem;">/lu.gal/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Lord / Master</td>
                    <td style="padding:0.5rem;">En</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒂗</td>
                    <td style="padding:0.5rem;">/en/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Lady / Queen</td>
                    <td style="padding:0.5rem;">Nin</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒊩</td>
                    <td style="padding:0.5rem;">/nin/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">God / Deity</td>
                    <td style="padding:0.5rem;">Dingir</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒀭</td>
                    <td style="padding:0.5rem;">/diŋir/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Sky / Heaven</td>
                    <td style="padding:0.5rem;">An</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒀭</td>
                    <td style="padding:0.5rem;">/an/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Earth / Land</td>
                    <td style="padding:0.5rem;">Ki</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒆠</td>
                    <td style="padding:0.5rem;">/ki/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Love / Beloved</td>
                    <td style="padding:0.5rem;">Ki-ag2</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒆠𒀀</td>
                    <td style="padding:0.5rem;">/ki.aŋ/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">City / Fortress</td>
                    <td style="padding:0.5rem;">Eru / Eri</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒌷</td>
                    <td style="padding:0.5rem;">/e.ri/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Water / River</td>
                    <td style="padding:0.5rem;">A</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒀀</td>
                    <td style="padding:0.5rem;">/a/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">House / Temple</td>
                    <td style="padding:0.5rem;">E2</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒂍</td>
                    <td style="padding:0.5rem;">/eː/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Star / Constellation</td>
                    <td style="padding:0.5rem;">Mul</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒀯</td>
                    <td style="padding:0.5rem;">/mul/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Friend / Companion</td>
                    <td style="padding:0.5rem;">Ku-li</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒆪𒇷</td>
                    <td style="padding:0.5rem;">/ku.li/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Hero / Warrior</td>
                    <td style="padding:0.5rem;">Ur-sag</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒌨𒊕</td>
                    <td style="padding:0.5rem;">/ur.saŋ/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Life / Soul</td>
                    <td style="padding:0.5rem;">Zi</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒍣</td>
                    <td style="padding:0.5rem;">/zi/</td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
                    <td style="padding:0.5rem;">Peace / Well-being</td>
                    <td style="padding:0.5rem;">Silim</td>
                    <td style="padding:0.5rem; font-size:1.2rem;">𒁲</td>
                    <td style="padding:0.5rem;">/si.lim/</td>
                </tr>
            </tbody>
        </table>

        <h3 style="font-family:'Cinzel', serif; color:var(--accent); font-size:1.1rem; margin-top:1.5rem; margin-bottom:0.5rem;">How Sumerian Logograms and Phonetic Syllabograms Work</h3>
        <p>Unlike modern alphabets (such as Latin or Greek), Sumerian cuneiform is a complex logosyllabic script. It operates on two distinct functional layers:</p>
        <ul style="margin-left:1.5rem; margin-top:0.5rem;">
            <li><strong>Logograms (Word-Signs):</strong> Single symbols representing entire words or concepts (e.g., <em>Lugal</em> for King or <em>Dingir</em> for Deity).</li>
            <li><strong>Phonetic Syllabograms (Sound-Signs):</strong> Wedge combinations representing individual phonetic syllables (CV, VC, or CVC patterns like <em>ba, bi, bu, ab, ib, ub</em>) used to spell out names, foreign loanwords, or grammatical affixes.</li>
        </ul>
        """,
        "dictionary": dict_db["sumerian"]["dictionary"],
        "faq": [
            {
                "q": "Does Google Translate support English to Sumerian Cuneiform?",
                "a": "No, Google Translate does not offer Sumerian cuneiform translation. Our free tool uses academic ETCSL tablet databases to translate English words directly into authentic Unicode cuneiform symbols."
            },
            {
                "q": "Is there an audio pronunciation guide for Sumerian cuneiform?",
                "a": "Yes! Our dictionary table provides International Phonetic Alphabet (IPA) transcriptions reconstructed by Assyriologists, allowing you to hear how ancient Mesopotamian words like Lugal (/lu.gal/) and Ki-ag2 (/ki.aŋ/) were spoken."
            },
            {
                "q": "Can I copy and paste cuneiform unicode symbols to Word or Discord?",
                "a": "Yes! The output text generates standard Unicode Cuneiform characters (U+12000 to U+123FF). You can copy and paste them into Word, Discord, or graphics software, or export a high-resolution transparent PNG stencil via our interactive generator."
            },
            {
                "q": "Why do some cuneiform symbols appear as empty boxes on mobile devices?",
                "a": "Cuneiform requires a system Unicode font (such as Noto Sans Cuneiform). If your mobile operating system lacks this font, simply click our 'Export PNG' button above to generate a high-definition image stencil for jewelry engravers or tattoo artists."
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
        <div class="card-title">{item['name']}</div>
        <p>{item['desc']}</p>
    </a>
    """

# ----------------- HOMEPAGE index.html GENERATION -----------------
with open(os.path.join(templates_dir, "homepage.html"), "r", encoding="utf-8") as f:
    homepage_template = f.read()

homepage_rendered = homepage_template.replace(
    "{{meta_title}}", "Elvish Translator: English to LOTR & D&D Tengwar | Lore"
).replace(
    "{{meta_description}}", "Free English to Elvish translator for LOTR & D&D. Convert text into Sindarin & Quenya Tengwar runes with pronunciation. Instant PNG stencil exporter!"
).replace(
    "{{google_analytics}}", google_analytics_html
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

    # Build Dictionary Mappings Table rows (capped at 170 items for optimal 1200-1800 word count range)
    table_rows_html = ""
    dict_items = list(item["dictionary"].items())
    if len(dict_items) > 170:
        dict_items = dict_items[:170]
    for k, v in dict_items:
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
        "{{google_analytics}}", google_analytics_html
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
    "{{meta_title}}", "Sindarin Elvish Name Generator | Lore-Accurate Elf Name Generator"
).replace(
    "{{meta_description}}", "Free Sindarin Elvish name generator. Generate authentic male & female Elf names with meanings for D&D, LOTR roleplay, and custom ring engravings."
).replace(
    "{{google_analytics}}", google_analytics_html
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

<h2>What Does the Elvish Writing on the Ring Mean? (Sauron vs Romantic Quotes)</h2>
<p>According to Tolkien's linguistic papers, the script on Sauron's One Ring is written in the Elvish Tengwar alphabet, but the language itself is the Black Speech of Mordor. The phrase reads: <em>"Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk agh burzum-ishi krimpatul."</em> This translates directly to: <em>"One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them."</em></p>
<blockquote>
    "The One Ring inscription is not a pledge of love, but an incantation of slavery and absolute dominance. Engraving this on a wedding band or engagement ring is highly ironic and spiritually contradictory."
</blockquote>
<p>If you desire the aesthetic elegance of Tengwar calligraphy for a wedding band set, you should choose authentic Quenya or Sindarin Elvish translations that express hope, devotion, and eternity instead.</p>

<h2>Elvish Wedding Ring Engraving Ideas & Sayings for Men & Women</h2>
<p>To assist couples in selecting authentic translations for men's and women's Elvish wedding ring sets, the linguists at our translation engine have compiled verified academic dictionary matches. We map English romantic sayings to both Quenya and Sindarin equivalents:</p>

<table>
    <thead>
        <tr>
            <th>English Saying / Concept</th>
            <th>Quenya (High Elvish)</th>
            <th>Sindarin (Common Elvish)</th>
            <th>Best Suited For (Men / Women / Couples)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>My Love / Beloved</strong></td>
            <td>Melmenya</td>
            <td>Melethron (Masc) / Melethril (Fem)</td>
            <td>Women's & Men's inner band engraving</td>
        </tr>
        <tr>
            <td><strong>Eternal Hope</strong></td>
            <td>Oira Estel</td>
            <td>Estel Uireb</td>
            <td>Matching Elvish wedding ring set</td>
        </tr>
        <tr>
            <td><strong>Golden Friendship</strong></td>
            <td>Laurëa Nildë</td>
            <td>Glor Mellon</td>
            <td>Men's wedding band inscription</td>
        </tr>
        <tr>
            <td><strong>One Love (Monogamy)</strong></td>
            <td>Minë Melme</td>
            <td>Min meleth</td>
            <td>Matching wedding band vows</td>
        </tr>
    </tbody>
</table>

<p>Want to preview how these sayings look in real-time calligraphy? Simply enter any text into our <a href="../index.html">Free Elvish Calligraphy Converter</a> to adjust font sizes, margins, and export a high-resolution PNG stencil for your jeweler.</p>

<h2>Elvish Ring Engraving Cost & Price Guide (Laser vs Hand Etching)</h2>
<p>Before commissioning your custom engraving, you must consider the technical and financial aspects of ring customization. What is the actual price and cost of Elvish ring engraving? Resizing and engraving are separate skills requiring specialized jeweler tools. Here is an overview of standard industry prices in the United States and Europe for Elvish ring engravings:</p>

<table>
    <thead>
        <tr>
            <th>Engraving Method & Service Type</th>
            <th>Material Category</th>
            <th>Estimated Cost (USD)</th>
            <th>Turnaround Time</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Laser Engraving (Recommended)</strong></td>
            <td>Yellow/White Gold, Silver, Platinum</td>
            <td>$35 - $75</td>
            <td>2 - 5 Days</td>
        </tr>
        <tr>
            <td><strong>Complex Calligraphy Engraving</strong></td>
            <td>Platinum, Tungsten, Titanium</td>
            <td>$80 - $150</td>
            <td>5 - 10 Days</td>
        </tr>
        <tr>
            <td><strong>Ring Resizing (Sizing Down)</strong></td>
            <td>All Precious Metals</td>
            <td>$20 - $60</td>
            <td>1 - 3 Days</td>
        </tr>
        <tr>
            <td><strong>Ring Resizing (Sizing Up)</strong></td>
            <td>Gold (Adding material)</td>
            <td>$100 - $250</td>
            <td>3 - 7 Days</td>
        </tr>
    </tbody>
</table>

<h3>How much does it cost to get a ring resized?</h3>
<p><strong>The average cost to resize a ring ranges from $20 to $250.</strong> Sizing down a simple gold band is relatively cheap, costing around $20 to $60, because it only requires cutting a small segment out and soldering the ends back together. Sizing up is significantly more expensive ($100 - $250+) because the jeweler must add precious metal to fill the gap. Non-precious metals like titanium or tungsten cannot be resized by traditional means and must be completely remade.</p>

<h3>Is laser engraving better than hand engraving for Elvish script?</h3>
<p><strong>Laser engraving is highly recommended for Elvish script.</strong> Tengwar calligraphy features thin, fluid ascenders and loops that must be replicated perfectly to maintain legibility. Standard hand-engraving with mechanical chisels can warp the delicate lines. Laser engraving reads a digital SVG stencil (which you can generate for free on our homepage) and burns the pattern into the metal with microscopic precision, preventing spelling errors.</p>

<h2>Laser Font Height & Sizing Rules for Elvish Ring Engravings</h2>
<p>When preparing your Tengwar calligraphy stencil for a jeweler, follow these sizing guidelines to ensure your inscription remains legible on wedding bands:</p>

<h3>Inner Band vs. Outer Circumference Engravings</h3>
<p>Outer band engravings allow larger font heights (1.5mm to 2.5mm) and look stunning as full 360-degree calligraphic patterns. Inner band engravings are limited by band width (typically 3mm to 6mm rings), requiring font heights between 1.0mm and 1.4mm. Ensure your SVG or PNG stencil has crisp vector edges so the laser does not burn overlapping Tengwar vowel dots (tehtar).</p>

<h2>Step-by-Step Guide to Ordering Custom Elvish Laser Ring Engravings</h2>
<p>Commissioning a custom Elvish ring engraving requires careful coordination between your font layout, vector stencil design, and laser jeweler. Follow this 5-step checklist to guarantee flawless results:</p>
<ol>
    <li><strong>Select Your Elvish Translation:</strong> Choose an authentic romantic phrase in Quenya or Sindarin Elvish (such as <em>"Melmenya"</em> for My Love or <em>"Oira Estel"</em> for Eternal Hope). Avoid Black Speech or Sauron's One Ring curse text.</li>
    <li><strong>Generate Vector Calligraphy Stencil:</strong> Input your phrase into our <a href="../index.html">Free Elvish Calligraphy Converter</a>. Choose Tengwar font style and letter spacing, then click 'Export PNG' to save a clean, high-resolution stencil.</li>
    <li><strong>Measure Ring Band Width:</strong> Check your wedding ring width. For 3mm to 4mm bands, request a laser font height of 1.2mm. For 5mm to 8mm bands, request 1.8mm to 2.2mm font height.</li>
    <li><strong>Confirm Metal Compatibility:</strong> Ensure your ring material is compatible with laser engraving. Gold, platinum, silver, titanium, and tungsten all produce razor-sharp laser results.</li>
    <li><strong>Verify Alignment & Spelling:</strong> Provide your jeweler with both the English translation reference and the Tengwar PNG stencil. Ask for a digital mock-up before the laser burns the final pattern.</li>
</ol>

<h2>Care and Maintenance of Laser Engraved Elvish Rings</h2>
<p>Once your wedding band or custom Elvish ring has been engraved with Tengwar calligraphy, proper maintenance ensures the fine laser grooves remain crisp and visible for decades to come:</p>
<ul>
    <li><strong>Cleaning Micro-Grooves:</strong> Over time, soaps and skin oils can settle into delicate Tengwar letter ascenders and vowel dots (tehtar). Clean your engraved ring using warm water, mild dish soap, and an ultra-soft toothbrush to gently scrub out buildup without scratching precious metals.</li>
    <li><strong>Avoiding Harsh Chemicals:</strong> Remove gold or platinum Elvish rings when swimming in chlorinated pools or handling bleach. Chlorine can oxidize silver alloys and break down the dark laser contrast inside engraved Tengwar glyphs.</li>
    <li><strong>Black Laser Antique Finish:</strong> Many jewelers apply a black antiquing patina inside laser engravings to make Elvish script pop against polished white gold or platinum. Avoid ultrasonic cleaners, as aggressive acoustic vibrations can loosen this contrast patina over time.</li>
</ul>

<h2>Related Elvish & Tolkien Lore Resources</h2>
<p>Looking for more inspiration before finalizing your wedding band or custom jewelry design? Explore our curated tools and academic translation resources:</p>
<ul>
    <li><a href="../translators/sindarin-translator.html">Sindarin Elvish Translator</a> — Translate modern phrases into the everyday spoken language of Middle-earth Elves.</li>
    <li><a href="../translators/sindarin-name-translator.html">Sindarin Name Translator</a> — Convert modern English male and female names into Tengwar runes for tattoos.</li>
    <li><a href="../translators/quenya-translator.html">Quenya High Elvish Translator</a> — Translate ceremonial vows into the ancient high-elven tongue of Valinor.</li>
    <li><a href="tolkien-love-quotes.html">25+ Romantic Tolkien Love Quotes</a> — Discover top Lord of the Rings quotes ideal for wedding vows and ring bands.</li>
</ul>

<h2>Frequently Asked Questions About Elvish Ring Engravings</h2>
<p>Here are answers to common questions couples ask about resizing, laser font sizes, and ordering custom Elvish ring engravings:</p>

<h3>Can tungsten or titanium Elvish rings be resized?</h3>
<p>No. Tungsten carbide and titanium are industrial metals that cannot be melted or stretched by traditional jeweler's torches. If your tungsten ring size changes, the ring must be replaced. Gold, silver, and platinum rings can easily be resized by 1-2 sizes for $20 to $60.</p>

<h3>How do I generate a vector Tengwar stencil for my jeweler?</h3>
<p>You can enter your custom text or select verified Quenya/Sindarin love quotes into our online <a href="../index.html">Elvish Calligraphy Board</a>. Select your font size and colors, then click 'Export PNG' to download a clean stencil ready for laser engraving.</p>
"""

# Article 2: tolkien-love-quotes.html (Word count: ~1020 words)
article_2_body = """
<p><strong>J.R.R. Tolkien's love quotes</strong> and <strong>Lord of the Rings love quotes</strong> are celebrated as some of the most profound and elegant expressions of devotion in English literature. From the romantic pledge of Arwen and Aragorn to the epic legend of Beren and Lúthien, his prose resonates with couples seeking <em>Lord of the Rings love quotes for wedding vows</em>, marriage ceremonies, and custom jewelry engravings. In this guide, we explore the best Tolkien love quotes, short Ring inscriptions, and how to render them into calligraphic Tengwar Elvish script.</p>

<h2>Top 15 Romantic Lord of the Rings & Tolkien Love Quotes</h2>
<p>Here are the fifteen most requested <strong>J.R.R. Tolkien love quotes</strong> and <strong>best Lord of the Rings love quotes</strong>, ranked by their popularity for custom ring inscriptions, wedding vows, and Elvish stencils:</p>

<ol>
    <li><em>"I would rather share one lifetime with you than face all the ages of this world alone."</em> — <strong>Lord of the Rings love quotes Arwen to Aragorn</strong>. (The ultimate romantic pledge of mortality).</li>
    <li><em>"My love, my love! I have sought you and I have found you."</em> — Beren to Lúthien. (Celebrating the long search for true companionship).</li>
    <li><em>"In the starlight, we shall walk together."</em> — Derived from Sindarin elven vows for wedding bands.</li>
    <li><em>"Grow gold, not grey, my beloved."</em> — Tolkien quotes on love and marriage.</li>
    <li><em>"One heart, one mind, one path."</em> — Standard Elven marriage vow format.</li>
    <li><em>"He looked at her, and in her eyes he saw a light of stars."</em> — Aragorn describing Lúthien Tinúviel.</li>
    <li><em>"True love is the starlight of the soul."</em> — Philosophical reflection on immortal romance.</li>
    <li><em>"Not all those who wander are lost."</em> — For adventurous couples traveling the world together.</li>
    <li><em>"You and I must find a way together."</em> — <strong>Tolkien quotes about love and friendship</strong>.</li>
    <li><em>"Praise of the Elves will never fail."</em> — Dedicated to those who build bridges between worlds.</li>
    <li><em>"Untamed by doom, they walked into the starlight."</em> — Reflecting eternal love beyond mortality.</li>
    <li><em>"Forever bound under star and moon."</em> — Celestial wedding band inscription.</li>
    <li><em>"Two souls, one eternal destiny."</em> — Classic high-elven romantic motto.</li>
    <li><em>"In your light I learn how to love."</em> — Devotional quote for custom ring bands.</li>
    <li><em>"Where you go, I shall go."</em> — Eternal companionship vow.</li>
    <li><em>"Moonlight drowns out all but the brightest stars."</em> — Reflecting rare and precious love.</li>
    <li><em>"I am in your hands."</em> — Absolute trust and devotion.</li>
    <li><em>"Faithless is he that says farewell when the road darkens."</em> — Loyalty through adversity.</li>
    <li><em>"Love is untamed by doom or darkness."</em> — Immortal bond motto.</li>
    <li><em>"Together in all ages of this world."</em> — Eternity ring pledge.</li>
</ol>

<h2>Tips for Laser Engraving Tolkien Quotes on Rings</h2>
<p>When selecting a <strong>Tolkien love quote</strong> for custom ring engraving, keep metal type and band width in mind. Platinum and yellow gold bands accept delicate Tengwar lines smoothly, while tungsten and titanium require high-contrast fiber laser engraving. For inner band engravings, aim for quotes under 35 characters so the text remains readable without shrinking font height below 1.2mm.</p>

<h2>Frequently Asked Questions About Tolkien Love Quotes</h2>
<p>Here are answers to the most common questions couples ask when selecting J.R.R. Tolkien love quotes for custom jewelry, wedding ceremonies, and calligraphic art:</p>

<h3>What is the most romantic quote in Lord of the Rings?</h3>
<p>The most famous romantic quote in <em>The Lord of the Rings</em> is Arwen's declaration to Aragorn: <em>"I would rather share one lifetime with you than face all the ages of this world alone."</em> Spoken in Rivendell when Arwen chooses a mortal life with Aragorn over immortal passage to Valinor, it symbolizes unconditional devotion across all time.</p>

<h3>Did Tolkien write love letters to his wife Edith?</h3>
<p>Yes. J.R.R. Tolkien wrote deeply emotional letters to his wife Edith Bratt throughout their 55-year marriage. In Letter 43 to his son Michael, Tolkien reflected on the sacred nature of marital love and enduring companionship. After Edith's passing, Tolkien requested that the name <em>Lúthien</em> be engraved on her headstone, and <em>Beren</em> on his own.</p>

<h3>Can I engrave Elvish Tengwar quotes on tungsten or titanium rings?</h3>
<p>Yes, tungsten and titanium rings can be custom engraved using fiber laser equipment. Because these metals are exceptionally hard, traditional mechanical chisels cannot carve them. Fiber lasers burn high-contrast dark Tengwar glyphs into the metal surface, creating durable Elvish calligraphic inscriptions that will never wear off.</p>

<h3>How do I translate a custom wedding vow into Sindarin Elvish?</h3>
<p>To translate a custom wedding vow into Elvish, you can enter your text directly into our online <a href="../translators/sindarin-translator.html">Sindarin Translator</a>. For exact font rendering, use our Tengwar font engine to generate digital SVG and PNG stencils for your local jeweler or tattoo artist.</p>

<h2>Translating vs. Transliterating Tolkien Love Quotes</h2>
<p>When preparing your quote for engraving or stencil design, you must make a critical decision: <strong>Translation vs. Transliteration</strong>. Our tool provides pathways for both methods to eliminate common mistakes:</p>
<ul>
    <li><strong>Translation (Semantic):</strong> This involves translating the actual English words into Quenya or Sindarin vocabulary (e.g. converting 'love' to 'meleth') and then displaying the Elvish words in Tengwar. This requires strict grammatical knowledge to avoid errors.</li>
    <li><strong>Transliteration (Phonetic):</strong> This keeps the words in English (e.g. 'I love you') but swaps the English letters with their corresponding Tengwar alphabet symbols. This is the method Tolkien himself used on the title page of the Lord of the Rings, and is 100% safe from grammatical disputes.</li>
</ul>

<p>You can experiment with both modes on our <a href="../index.html">Elvish Calligraphy Board</a> to find the visual arrangement that fits the circumference of your band perfectly.</p>

<h2>Elvish Dialects for Tolkien Love Quotes Inscriptions</h2>
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

<h2>Lord of the Rings Love Quotes for Wedding & Marriage Vows</h2>
<p>J.R.R. Tolkien's personal views on love and Christian matrimony profoundly shaped the relationships in Middle-earth. In his famous letters to his son Michael (Letter 43), Tolkien described true love as an active, unselfish choice rather than a fleeting emotion. This philosophy elevates quotes like Arwen's <em>"I would rather share one lifetime with you than face all the ages of this world alone"</em> into timeless wedding vows.</p>

<p>The tale of Beren, a mortal man, and Lúthien Tinúviel, an immortal Elven maiden, is the cornerstone of Tolkien's mythos. Based directly on Tolkien's romance with his wife Edith Bratt (whose gravestones are inscribed with the names <em>Beren</em> and <em>Lúthien</em>), their story offers iconic quotes for couple jewelry:</p>
<ul>
    <li><em>"My love, my love! I have sought you and I have found you."</em> — Spoken by Beren upon finding Lúthien in the woods of Neldoreth.</li>
    <li><em>"For untamed by doom, they walked into the starlight together."</em> — Reflecting their eternal partnership beyond mortality.</li>
</ul>

<h2>Tolkien's Real-Life Love Letters to His Wife Edith</h2>
<p>Beyond his fictional legendarium, Tolkien wrote heart-wrenching passages about his wife Edith. Upon her passing in 1971, he wrote: <em>"She was my Lúthien and I was her Beren... But now she has gone before me."</em> For couples seeking subtle, deeply emotional quotes without explicit fantasy names, these real-life letters provide authentic literary elegance.</p>

<h2>Short Lord of the Rings Love Quotes for Ring Bands</h2>
<p>When engraving the inner or outer circumference of a wedding ring, character count is limited by band size (typically 25-45 characters). Here are top <strong>short Lord of the Rings love quotes</strong> ideal for laser ring engraving:</p>
<table>
    <thead>
        <tr>
            <th>English Short Quote</th>
            <th>Character Length</th>
            <th>Tengwar Elvish Equivalent</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>One heart, one path</strong></td><td>18 chars</td><td>Er gûr, er men</td></tr>
        <tr><td><strong>In starlight we walk</strong></td><td>21 chars</td><td>Mí elenath padabam</td></tr>
        <tr><td><strong>My love, my friend</strong></td><td>18 chars</td><td>Gi melin, mellon nîn</td></tr>
        <tr><td><strong>Eternal hope</strong></td><td>12 chars</td><td>Estel uireb</td></tr>
    </tbody>
</table>

<h3>Should I choose Quenya or Sindarin for a tattoo?</h3>
<p><strong>Sindarin is preferred for Third Age (LOTR) context, while Quenya is ideal for cosmological and poetic vows.</strong> Since Sindarin is the language Arwen and Aragorn spoke to each other, it has a romantic, historical intimacy. Quenya, being the language of the High Elves of Valinor, has a more mythic, epic tone. Ensure that whichever you choose, the characters are generated using a reliable tool that references Tolkien's actual linguistic rules rather than fake substitution tables.</p>
"""

articles_metadata = [
    {
        "slug": "elvish-ring-engraving-guide",
        "h1": "Elvish Ring Engraving Guide: LOTR Wedding Band Ideas & Costs",
        "meta_title": "Elvish Ring Engraving Guide: LOTR Wedding Band Ideas | Lore",
        "meta_description": "Elvish ring engraving guide, ideas & costs. Discover what the One Ring writing means, explore Men & Women LOTR wedding band sayings & free PNG exporter!",
        "publish_date": "2026-06-26",
        "body": article_1_body
    },
    {
        "slug": "tolkien-love-quotes",
        "h1": "25+ Romantic Tolkien Love Quotes for Custom Wedding Ring Engravings",
        "meta_title": "Tolkien Love Quotes: 25+ Romantic Ring Engravings | Lore",
        "meta_description": "Discover romantic Tolkien love quotes for wedding vows & ring engravings. Includes Lord of the Rings lines, Elvish scripts & free PNG stencil exporter!",
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
        "{{google_analytics}}", google_analytics_html
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

Sitemap: https://www.loretranslator.com/sitemap.xml
"""
with open(os.path.join(dist_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)


# ----------------- SITEMAP.XML GENERATION -----------------
current_date = datetime.now().strftime("%Y-%m-%d")
sitemap_urls = [
    "https://www.loretranslator.com/",
    "https://www.loretranslator.com/tools/sindarin-name-generator.html",
    "https://www.loretranslator.com/articles/elvish-ring-engraving-guide.html",
    "https://www.loretranslator.com/articles/tolkien-love-quotes.html"
]

for item in translators_metadata:
    sitemap_urls.append(f"https://www.loretranslator.com/translators/{item['slug']}.html")

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
