class WordMaps:
    words = {}
    special_contexts = {}

    def __init__(self):
        self.words = {}

        for key in self.complete:
            self.words[key] = self.complete[key]
            self.words[self.complete[key]] = key
            self.words[key + 's'] = self.complete[key] + 's'
            self.words[self.complete[key] + 's'] = key + 's'
            # improper plurals are sometimes generated, however will just be cruft in the dictionary

        for key in self.simple_compund:
            self.words[key + 'man'] = key + 'woman'
            self.words[key + 'woman'] = key + 'man'
            self.words[key + 'men'] = key + 'women'
            self.words[key + 'women'] = key + 'men'
            # Still not convinced a regex suffix is not better for capturing all cases

        for key in self.simple_plurals:
            self.words[key] = self.simple_plurals[key]
            self.words[self.simple_plurals[key]] = key
            self.words[key + 's'] = self.simple_plurals[key] + 'es'
            self.words[self.simple_plurals[key] + 'es'] = key + 's'

        for key in self.other:
            self.words[key] = self.other[key]
            self.words[self.other[key]] = key

    def swap(self, input_word):
        # hyphenated words or punctuated like he'd or she'll are handled at WordSplitter level

        new_word = input_word
        word_match = input_word.lower()

        for match in self.special:
            if word_match == match[0]:
                new_word = match[1]

        try:
            found_word = self.words[word_match]
            new_word = found_word
        except KeyError:
            pass

        # TODO improve for all caps words
        if input_word and input_word[0].isupper():
            first = new_word[0]
            rest = new_word[1:]

            new_word = "{0}{1}".format(first.upper(), rest.lower())

        return new_word

    # All dictionaries should be stored MtF

    # TODO handle this better as we should figure out his/him as replacements for her
    special = [("him", "her"), ("his", "her"), ("her", "his"), ("her", "him")]

    other = {
        "bro-whore": "sorostitute",
        "masculinly": "femininely",
        "masculine": "feminine",
        "masculize": "feminize",
        "masculise": "feminise",
        "patriarchy": "matriarchy",
        "patriarchal": "matriarchal",
        "patricide": "matricide",
        "patronize": "matronize",
        "patronized": "matronized",
        "patronizing": "matronizing",
        "misandry": "misogyny",
        "misandrist": "misogynist",
        "masc": "fem",
    }

    complete = {
        "bachelor": "bachelorette",
        "beau": "belle",
        "billygoat": "nannygoat",
        "bloke": "gal",
        "blond": "blonde",
        "boar": "sow",
        "boy": "girl",
        "boyfriend": "girlfriend",
        "boyhead": "maidenhead",
        "boyhood": "girlhood",
        "boyish": "girly",
        "bridegroom": "bride",
        "bro": "sis",
        "brogrammer": "sistagrammer",
        "bromance": "lady-romance",
        "bros": "sistas",
        "brother": "sister",
        "buck": "doe",
        "bull-calf": "cow-calf",
        "bull": "cow",
        "bullock": "heifer",
        "colt": "filly",
        "comte": "comtesse",
        "czar": "czarina",
        "d00dz": "laydeez",
        "dad": "mom",
        "daddies": "mommies",
        "daddy": "mommy",
        "drake": "duck",
        "dude": "lady",
        "dudebro": "galpal",
        "dudelier": "girlier",
        "dudeliest": "girliest",
        "dudely": "womanly",
        "dudes": "ladies",
        "father": "mother",
        "fellow": "gal",
        "fiance": "fiancee",
        "friar": "nun",
        "gander": "goose",
        "gentleman": "lady",
        "gentlemen": "ladies",
        "godfather": "godmother",
        "godhead": "goddesshead",
        "godhood": "goddesshood",
        "godliness": "goddessliness",
        "godly": "goddessly",
        "gods": "goddesses",
        "gramps": "grandma",
        "grandfather": "grandmother",
        "grandpa": "grandma",
        "grandson": "granddaughter",
        "groom": "bride",
        "guy": "gal",
        "hart": "hind",
        "he": "she",
        "hero": "heroine",
        "heroes": "heroines",
        "heros": "heroines",
        "himself": "herself",
        "hound": "brach",
        "husband": "wife",
        "husbandly": "wifely",
        "husbands": "wives",
        "king": "queen",
        "knight": "dame",
        "lad": "lass",
        "lads": "lassies",
        "landlord": "landlady",
        "lord": "lady",
        "lords": "ladies",
        "male": "female",
        "maleness": "femaleness",
        "males": "females",
        "man": "woman",
        "manhood": "womanhood",
        "mankind": "womankind",
        "manliness": "womanliness",
        "manly": "ladylike",
        "manservant": "maidservant",
        "mansplain": "ladysplain",
        "margrave": "margravine",
        "marquess": "marchioness",
        "marquis": "marquise",
        "marquise": "marquise",
        "masculine": "feminine",
        "masseur": "masseuse",
        "men": "women",
        "menz": "ladiez",
        "monk": "nun",
        "mr": "ms",
        "nephew": "niece",
        "papa": "mama",
        "paternal": "maternal",
        "paternity": "maternity",
        "poet": "poetess",
        "poppa": "momma",
        "ram": "ewe",
        "sir": "ma'am",
        "sire": "dam",
        "son": "daughter",
        "squire": "damsel",
        "stag": "hind",
        "stallion": "mare",
        "steer": "heifer",
        "sultan": "sultana",
        "uncle": "aunt",
        "whitemaleness": "whitefemaleness",
        "widower": "widow",
        "widows": "widowers",
        "wizardly": "witchy"
    }

    simple_plurals = {
        "abbot": "abbess",
        "actor": "actress",
        "archduke": "archduchess",
        "author": "authoress",
        "baron": "baroness",
        "baronet": "baronetess",
        "conductor": "conductress",
        "count": "countess",
        "deacon": "deaconess",
        "duke": "duchess",
        "earl": "countess",
        "emperor": "empress",
        "enchanter": "enchantress",
        "god": "goddess",
        "headmaster": "headmistress",
        "heir": "heiress",
        "host": "hostess",
        "hunter": "huntress",
        "lion": "lioness",
        "master": "mistress",
        "mayor": "mayoress",
        "postmaster": "postmistress",
        "priest": "priestess",
        "prince": "princess",
        "prophet": "prophetess",
        "shepherd": "shepherdess",
        "sorcerer": "sorceress",
        "steward": "stewardess",
        "tiger": "tigress",
        "tutor": "governess",
        "viscount": "viscountess",
        "waiter": "waitress",
        "wizard": "sorceress",

    }

    simple_compund = [
        "air",
        "alder",
        "anchor",
        "assembly",
        "bogey",
        "bonds",
        "business",
        "camera",
        "cave",
        "chair",
        "clergy",
        "congress",
        "council",
        "country",
        "crafts",
        "door",
        "fire",
        "fisher",
        "fore",
        "fresh",
        "garbage",
        "handy",
        "hang",
        "hench",
        "journey",
        "kins",
        "klans",
        "lay",
        "mad",
        "mail",
        "marks",
        "middle",
        "milk",
        "noble",
        "ombuds",
        "police",
        "post",
        "repair",
        "sales",
        "sand",
        "service",
        "show",
        "snow",
        "space",
        "spokes",
        "sports",
        "states",
        "super",
        "un",
        "washer",
        "watch",
        "weather",
        "work"]
