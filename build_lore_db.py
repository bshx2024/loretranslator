import json
import os

db_path = "E:/kaifa/loretranslator/dict_db.json"

db = {
    "elvish": {
        "sindarin": {
            # Core Dictionary (150+ Words)
            "love": "meleth", "friend": "mellon", "star": "el", "water": "nen", "sun": "anor", "moon": "ithil",
            "shadow": "dae", "dark": "mór", "light": "calen", "flower": "loth", "shield": "eramath", "king": "aran",
            "hope": "estel", "heart": "gûr", "gold": "glor", "white": "nim", "girl": "sell", "boy": "pennic",
            "earth": "amar", "sky": "menel", "fire": "naur", "wind": "gwaew", "eternal": "uireb", "life": "cuil",
            "death": "gorth", "soul": "fae", "dream": "oltha", "family": "nos", "wisdom": "ist", "peace": "sîdh",
            "war": "ohtar", "mother": "naneth", "father": "adar", "brother": "muindor", "sister": "muinthel",
            "son": "ion", "daughter": "iell", "man": "benn", "woman": "bess", "child": "henn", "queen": "bereth",
            "lord": "brannon", "lady": "brennil", "enemy": "coth", "warrior": "maethor", "sword": "megil",
            "bow": "cû", "arrow": "pilin", "horse": "roch", "wolf": "drafn", "eagle": "thoron", "dragon": "lhûg",
            "beast": "lavan", "forest": "taur", "tree": "galadh", "leaf": "las", "branch": "golf", "stone": "sarn",
            "metal": "tinc", "iron": "ang", "silver": "celeb", "ring": "cor", "crown": "rî", "city": "ost",
            "tower": "barad", "house": "car", "home": "bar", "road": "men", "path": "râd", "river": "sîr",
            "sea": "aear", "ocean": "aearon", "rain": "ross", "snow": "los", "ice": "heleg", "cloud": "faun",
            "day": "aur", "night": "du", "morning": "arin", "evening": "aduial", "year": "idhrin", "time": "lû",
            "book": "parf", "word": "peth", "song": "laer", "voice": "lam", "hate": "delos", "fight": "maeth",
            "see": "cen-", "hear": "lathra-", "speak": "ped-", "write": "teitha-", "read": "parf-", "sing": "linna-",
            "run": "nor-", "walk": "pada-", "fly": "rev-", "go": "men-", "come": "tol-", "make": "car-",
            "give": "anna-", "take": "mab-", "find": "rada-", "seek": "nestag-", "know": "ista-", "think": "nauth-",
            "good": "maer", "bad": "um", "beautiful": "bain", "strong": "bell", "weak": "lhêw", "brave": "astald",
            "wise": "sael", "old": "iphant", "young": "neth", "new": "sain", "big": "daer", "small": "pigen",
            "high": "brand", "low": "tofn", "deep": "nûr", "black": "mór", "red": "caran", "green": "calen",
            "blue": "luin", "yellow": "malen", "hot": "brassen", "cold": "ring", "warm": "laug", "sweet": "lend",
            "true": "thand", "free": "lain"
        },
        "quenya": {
            "love": "melme", "friend": "nildo", "star": "elen", "water": "nén", "sun": "anar", "moon": "isil",
            "shadow": "lëo", "dark": "mórë", "light": "cálë", "flower": "lóte", "shield": "turma", "king": "aran",
            "hope": "estel", "heart": "hórë", "gold": "laurë", "white": "ninquë", "wedding": "veryandë",
            "girl": "seldë", "boy": "seldo", "earth": "ambar", "sky": "menel", "fire": "nár", "wind": "súre",
            "eternal": "tennoio", "life": "coivië", "death": "qualme", "soul": "fëa", "dream": "olor",
            "family": "nossë", "wisdom": "nolmë", "peace": "sére", "war": "ohta", "mother": "amil",
            "father": "atar", "brother": "tôr", "sister": "seler", "son": "yondo", "daughter": "yeldë",
            "man": "nér", "woman": "nis", "child": "hina", "queen": "tari", "lord": "heru", "lady": "heri",
            "enemy": "cotumo", "warrior": "ohtar", "sword": "macil", "bow": "quinga", "arrow": "pilin",
            "horse": "rocco", "wolf": "ráca", "eagle": "soron", "dragon": "lócë", "beast": "laman",
            "forest": "taurë", "tree": "alda", "leaf": "lassë", "branch": "olva", "stone": "sardo",
            "metal": "tinco", "iron": "anga", "silver": "telpë", "ring": "corma", "crown": "rië",
            "city": "osto", "tower": "mindo", "house": "coa", "home": "már", "road": "tië", "path": "vanda",
            "river": "sírë", "sea": "ear", "ocean": "earon", "rain": "mistë", "snow": "lossë", "ice": "helcë",
            "cloud": "fanya", "day": "aurë", "night": "lómë", "morning": "arin", "evening": "andúnië",
            "year": "loa", "time": "lú", "book": "parma", "word": "quetta", "song": "lírë", "voice": "óma",
            "hate": "tëon", "fight": "mahta-", "see": "cen-", "hear": "hlar-", "speak": "queta-",
            "write": "tec-", "read": "parma-", "sing": "lir-", "run": "yor-", "walk": "vanta-",
            "fly": "wil-", "go": "lelya-", "come": "tul-", "make": "car-", "give": "anta-",
            "take": "map-", "find": "hir-", "seek": "sacc-", "know": "ista-", "think": "sana-",
            "good": "mára", "bad": "ulca", "beautiful": "vanya", "strong": "polda", "weak": "limpa",
            "brave": "canya", "wise": "saila", "old": "yerna", "young": "nessa", "new": "vinya",
            "big": "alta", "small": "pitya", "high": "tára", "low": "nacca", "deep": "nura",
            "black": "morë", "red": "carnë", "green": "laica", "blue": "luin", "yellow": "malina",
            "hot": "urya", "cold": "ringa", "warm": "lauca", "sweet": "lissa", "true": "nanwa",
            "free": "mirima"
        },
        "character_map": {
            "a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i", "j": "j",
            "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t",
            "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"
        }
    },
    "sumerian": {
        "dictionary": {
            "love": "ki-ag2 (𒆠𒉘)", "friend": "ku3-li (𒆪𒇷)", "star": "mul (𒀯)", "water": "a (𒀀)",
            "sun": "utu (𒌓)", "moon": "nanna (𒋀)", "king": "lugal (𒈗)", "god": "dingir (𒀭)",
            "house": "e2 (𒂍)", "man": "lu2 (𒇽)", "woman": "munus (𒊩)", "land": "kur (𒆳)",
            "strength": "a2 (𒀀)", "gold": "ku3-sig17 (𒆬𒄀)", "silver": "ku3-babbar (𒆬𒌓)",
            "great": "gal (𒃲)", "earth": "ki (𒆠)", "sky": "an (𒀭)", "fire": "izi (𒉈)",
            "wind": "lil2 (𒆤)", "life": "nam-ti (ナムティ)", "death": "ush2 (𒁁)", "soul": "zi (𒍣)",
            "dream": "ma-muda (𒈠𒈬𒁕)", "family": "im-ri-a (𒅎𒊑𒀀)", "wisdom": "nam-zu (𒉆𒍪)"
        },
        "syllabary": {
            "a": "𒀀", "b": "🇧", "c": "ⵛ", "d": "𒁕", "e": "𒂊", "f": "𒅁", "g": "𒂵", "h": "𒄩", "i": "𒄿", "j": "ជ្ជ",
            "k": "𒅗", "l": "𒆷", "m": "𒈠", "n": "𒈾", "o": "𒌋", "p": "🇵", "q": "𒋡", "r": "𒊏", "s": "𒊓", "t": "ତା",
            "u": "𒌋", "v": "𒉿", "w": "𒉿", "x": "க்ஸ", "y": "𒅀", "z": "𒍝",
            "ba": "🇧", "da": "𒁕", "ga": "𒂵", "ma": "𒈠", "na": "𒈾", "sa": "𒊓", "ta": "ତା", "ka": "𒅗", "la": "𒆷",
            "bi": "𒁉", "di": "𒁲", "gi": "𒄀", "mi": "𒈪", "ni": "𒉌", "si": "𒋛", "ti": "ତି", "ki": "𒆠", "li": "𒇷",
            "bu": "𒁍", "du": "𒁺", "gu": "𒄖", "mu": "𒈬", "nu": "nu", "su": "𒋢", "tu": "図", "ku": "𒆪", "lu": "𒇻"
        }
    },
    "navajo": {
        "dictionary": {
            "hello": "yá'át'ééh", "love": "ayóó'ó'ní", "friend": "shik'is", "water": "tó", "sun": "shá",
            "moon": "ooljéé'", "star": "sǫ'", "mountain": "dził", "strength": "bidziil", "fire": "kǫ'",
            "earth": "kéyah", "sky": "yá", "wind": "níyol", "life": "iiná", "death": "ánnoonééł",
            "dream": "na'alye'", "family": "hooghan", "wisdom": "bil hózhǫ́"
        },
        "virtual_keyboard": ["ą́", "ę́", "į́", "ǫ́", "ł", "á", "é", "í", "ó", "ú"]
    },
    "navi": {
        "dictionary": {
            "hello": "kaltxì", "love": "yawne", "friend": "tsmukan", "water": "pay", "sun": "tsawke",
            "moon": "krra", "star": "tahay", "forest": "na'vi", "spirit": "tirea", "life": "tìrey",
            "mother": "sa'nok", "father": "sewkey", "earth": "kaltxi", "sky": "ta'leng", "fire": "txep",
            "wind": "hufwe", "eternal": "tirey", "death": "tìlor", "dream": "spaw", "family": "so'ha"
        },
        "ipa_pronunciation": {
            "kaltxì": "/kal.tʼɪ/", "yawne": "/ˈjaw.nɛ/", "tsmukan": "/ˈt͡smuk.an/", "pay": "/paj/",
            "tsawke": "/ˈt͡saw.kɛ/", "tahay": "/ta.haj/", "tirea": "/ti.ɾɛ.a/", "tìrey": "/tɪ.ɾɛj/"
        }
    },
    "runic": {
        "elder_futhark": {
            "a": "ᚠ", "b": "ᚢ", "c": "ᚦ", "d": "ᚬ", "e": "ᚱ", "f": "ᚴ", "g": "ᚼ", "h": "ᚾ", "i": "ᛁ", "j": "ᛅ",
            "k": "ᛋ", "l": "ᛏ", "m": "ᛒ", "n": "ᛘ", "o": "ᛚ", "p": "ᛦ", "q": "ᚴ", "r": "ᚱ", "s": "ᛋ", "t": "ᛏ",
            "u": "ᚢ", "v": "ᚢ", "w": "ᚢ", "x": "ᛋ", "y": "ᛁ", "z": "ᛦ"
        },
        "younger_futhark": {
            "a": "ᚢ", "b": "ᛒ", "c": "ᚦ", "d": "ᛏ", "e": "ᛁ", "f": "ᚠ", "g": "ᚴ", "h": "ᚼ", "i": "ᛁ", "j": "ᛁ",
            "k": "ᚴ", "l": "ᛚ", "m": "ᛘ", "n": "ᚾ", "o": "ᚢ", "p": "ᛒ", "q": "ᚴ", "r": "ᚱ", "s": "ᛋ", "t": "ᛏ",
            "u": "ᚢ", "v": "ᚢ", "w": "ᚢ", "x": "ᛋ", "y": "ᛁ", "z": "ᛋ"
        },
        "concepts": {
            "valhalla": "ᚢᛅᛚᚼᛅᛚᛅ", "viking": "ᚢᛁᚴᛁᚾᚴ", "love": "ᛅᛋᛏ", "strength": "ᚦᚢᚱᛘᚢᚦᚱ",
            "protection": "ᛅᛚᚴᛁᛋ", "warrior": "ᚱᛁᚾᚴᚱ"
        }
    },
    "alien": {
        "character_map": {
            "a": "⏃", "b": "⏁", "c": "⏂", "d": "⏃", "e": "⏄", "f": "⏅", "g": "⏆", "h": "⏇", "i": "⏈", "j": "⏉",
            "k": "⏊", "l": "⏋", "m": "⏌", "n": "⏍", "o": "⏎", "p": "⏏", "q": "⏐", "r": "⏑", "s": "⏒", "t": "⏓",
            "u": "⏔", "v": "⏕", "w": "⏖", "x": "⏗", "y": "⏘", "z": "⏙"
        }
    },
    "old_english": {
        "dictionary": {
            "hello": "wes hāl", "love": "lufu", "friend": "frēond", "water": "wæter", "sun": "sunne",
            "moon": "mōna", "star": "steorra", "king": "cyning", "queen": "cwēn", "strength": "strengðu",
            "gold": "gold", "wedding": "gýfta", "earth": "eorðe", "sky": "heofon", "fire": "fȳr",
            "wind": "wind", "eternal": "ēce", "life": "līf", "death": "dēað", "soul": "gāst",
            "dream": "drēam", "family": "mægð", "wisdom": "wīsdōm"
        }
    },
    "aramaic": {
        "dictionary": {
            "love": "chuba (ܚܘܒܐ)", "friend": "chabra (ܚܒܪܐ)", "god": "alaha (ܐܠܗܐ)", "spirit": "rucha (ܪܘܚܐ)",
            "peace": "shlama (ܫܠܡܐ)", "truth": "shrara (ܫܪܪܐ)", "earth": "ara (ܐܪܥܐ)", "sky": "shmaya (ܫܡܝܐ)",
            "fire": "nura (ܢܘܪܐ)", "wind": "rucha (ܪܘܚܐ)", "eternal": "alam (ܥܠܡ)", "life": "chaye (ܚܝܐ)",
            "death": "mawta (ܡܘܬܐ)", "dream": "chelma (ܚ流)", "family": "bait (ܒܝܬܐ)", "wisdom": "chochma (ܚܟܡܬܐ)"
        },
        "character_map": {
            "a": "ܐ", "b": "ܒ", "g": "ܓ", "d": "ܕ", "h": "ܗ", "w": "ܘ", "z": "ܙ", "ch": "ܚ", "t": "ܛ", "y": "ܝ",
            "k": "ܟ", "l": "ܠ", "m": "ܡ", "n": "ܢ", "s": "ܣ", "e": "ܥ", "p": "ܦ", "ts": "ܨ", "q": "ܩ", "r": "ܪ",
            "sh": "ܫ", "th": "ܬ"
        }
    },
    "coptic": {
        "dictionary": {
            "love": "agape (ⲁⲅⲁⲲⲏ)", "peace": "hirene (ϩⲓⲣⲏⲛⲏ)", "god": "nouti (ⲛⲟⲩⲧⲓ)", "father": "iot (ⲓⲫⲧ)",
            "spirit": "pneuma (ⲡⲛⲉⲩⲙⲁ)", "life": "onkh (ⲱⲛϧ)", "earth": "kahi (ⲕⲁϩⲓ)", "sky": "phe (ⲫⲏ)",
            "fire": "krom (ⲕⲣⲱⲙ)", "wind": "te (ⲧⲏ)", "eternal": "eneh (ⲉⲛⲉϩ)", "death": "mou (ⲙⲟⲩ)",
            "dream": "rasou (ⲣⲁⲥⲟⲩ)", "family": "mêt (ⲙⲏⲧ)"
        },
        "character_map": {
            "a": "ⲁ", "b": "ⲕ", "g": "ⲅ", "d": "ⲇ", "e": "ⲉ", "z": "ⲯ", "h": "ⲏ", "th": "ⲑ", "i": "ⲓ", "k": "ⲕ",
            "l": "ⲗ", "m": "ⲙ", "n": "ⲛ", "x": "ⲝ", "o": "ⲟ", "p": "ⲡ", "r": "ⲣ", "s": "ⲥ", "t": "ⲧ", "u": "ⲩ",
            "ph": "ⲫ", "ch": "ⲭ", "ps": "ⲱ", "sh": "ϣ", "f": "ϥ", "kh": "ϧ", "h_alt": "ϩ", "j": "ϫ", "tch": "ϭ",
            "ti": "ϯ"
        }
    },
    "name_generator": {
        "prefixes": [
            {"term": "el", "meaning": "star"}, {"term": "glor", "meaning": "gold/light"},
            {"term": "mith", "meaning": "gray"}, {"term": "tin", "meaning": "sparkle"},
            {"term": "aran", "meaning": "king"}, {"term": "nim", "meaning": "white"},
            {"term": "mor", "meaning": "dark"}, {"term": "fin", "meaning": "hair"},
            {"term": "celeb", "meaning": "silver"}, {"term": "gil", "meaning": "bright star"},
            {"term": "legol", "meaning": "green leaf"}, {"term": "thrand", "meaning": "vigorous"}
        ],
        "suffixes": [
            {"term": "wen", "meaning": "maiden"}, {"term": "ion", "meaning": "son"},
            {"term": "iel", "meaning": "daughter"}, {"term": "dir", "meaning": "man"},
            {"term": "dur", "meaning": "servant"}, {"term": "las", "meaning": "leaf"},
            {"term": "rod", "meaning": "noble"}, {"term": "el", "meaning": "elf"},
            {"term": "dhel", "meaning": "elf-lady"}, {"term": "born", "meaning": "hot/red"}
        ]
    }
}

try:
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
    print(f"Successfully compiled {db_path} with massive expanded vocabulary!")
except Exception as e:
    print(f"Failed to compile database: {e}")
