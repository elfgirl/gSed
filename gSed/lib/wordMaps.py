import re

class wordmaps:
    words = {}
    maps = {}

    def __init__(self):
        self.__loadStart()
        self.__loadAnywhere()
        self.__loadComplete()
        self.__loadEnd()
        self.__loadSpecial()

    def getRegexList(self, type):
        return self.maps[type]

    def swap(self, input_word):
        new_word = self.__flipWord(type="complete", input_word=input_word)
        if new_word != input_word:
            return new_word

        new_word = self.__flipWord(type="start", input_word=input_word)
        if new_word != input_word:
            return new_word

        new_word = self.__flipWord(type="anywhere", input_word=input_word)
        if new_word != input_word:
            return new_word

        new_word = self.__flipWord(type="end", input_word=input_word)
        if new_word != input_word:
            return new_word

        new_word = self.__flipWord(type="special", input_word=input_word)
        if new_word != input_word:
            return new_word

        return input_word

    def __flipWord(self, type, input_word):

        newWord = input_word
        wordMatch = input_word.lower()

        try:
            foundWord = self.words[type][wordMatch]
            newWord = foundWord
        except:
            return newWord

        if input_word[0].isupper():
            first = newWord[0]
            rest = newWord[1:]

            newWord = "{0}{1}".format(first.upper(), rest.lower())

        return newWord

    def __loadStart(self):
        map = self.start

        startDictionary = {}
        for key in map:
            startDictionary[key] = map[key]
            startDictionary[map[key]] = key
        self.words["start"] = startDictionary

        self.maps["start"] = []
        for key in startDictionary:
            self.maps["start"].append(re.compile(r"\b({0})(?=.*\b)".format(key)))

    def __loadEnd(self):
        map = self.end

        endDictionary = {}
        for key in map:
            endDictionary[key] = map[key]
            endDictionary[map[key]] = key
        self.words["end"] = endDictionary

        self.maps["end"] = []
        for key in endDictionary:
            self.maps["end"].append(re.compile(r"({0})\b".format(key)))

    def __loadAnywhere(self):
        map = self.anywhere

        anywhereDictionary = {}
        for key in map:
            anywhereDictionary[key] = map[key]
            anywhereDictionary[map[key]] = key
        self.words["anywhere"] = anywhereDictionary

        self.maps["anywhere"] = []
        for key in anywhereDictionary:
            self.maps["anywhere"].append(re.compile(r"({0})".format(key)))

    def __loadComplete(self):
        map = self.complete

        completeDictionary = {}
        for key in map:
            completeDictionary[key] = map[key]
            completeDictionary[map[key]] = key
        self.words["complete"] = completeDictionary

        self.maps["complete"] = []
        for key in completeDictionary:
            self.maps["complete"].append(re.compile(r"\b({0})\b".format(key)))

    def __loadSpecial(self):
        map = self.special

        specialDictionary = {}
        for key in map:
            specialDictionary[key] = map[key]
        self.words["special"] = specialDictionary

        self.maps["special"] = []
        for key in specialDictionary:
            self.maps["special"].append(re.compile(r"\b({0})\b".format(key)))

        # All dictionaries should be stored MtF

        # These are generally words with simplistic plurals, that are not used as a starting component to larger word like cocktease

    start = {
        "actors": "actresses",
        "bachelor": "bachelorette",
        "bloke": "gal",
        "boyfriend": "girlfriend",
        "boyhood": "girlhood",
        "brother": "sister",
        "comte": "comtesse",
        "gentleman": "lady",
        "grandpa": "grandma",
        "grandson": "granddaughter",
        "groom": "bride",
        "he'": "she'",
        "husband": "wife",
        "male": "female",
        "maleness": "femaleness",
        "margrave": "margravine",
        "marquess": "marchioness",
        "patriar": "matriar",
        "patroniz": "matroniz",
        "prophet": "prophetess",
        "shepherd": "shepherdess",
        "sir": "ma'am",
        "squire": "damsel",
        "uncle": "aunt",
        "waiter": "waitress",
        "widower": "widow",
        "wizardly": "witchy"
    }

    end = {
        "hero": "heroine",
        "heros": "heroines"
    }

    # Words that can appear anyword in a larger word, such as plurals or hypenates. pseudo-bromances for example
    anywhere = {
        "airman": "airwoman",
        "airmen": "airwomen",
        "alderman": "alderwoman",
        "aldermen": "alderwomen",
        "anchorman": "anchorwoman",
        "anchormen": "anchorwomen",
        "assemblyman": "assemblywoman",
        "assemblymen": "assemblywomen",
        "billy-goat": "nanny-goat",
        "billygoat": "nannygoat",
        "bogeyman": "bogeywoman",
        "bogeymen": "bogeywomen",
        "bondsman": "bondswoman",
        "bondsmen": "bondswomen",
        "bridegroom": "bride",
        "bro-whore": "sorostitute",
        "brogrammer": "sistagrammer",
        "bromance": "lady-romance",
        "businessman": "businesswoman",
        "businessmen": "businesswomen",
        "cameraman": "camerawoman",
        "cameramen": "camerawomen",
        "caveman": "cavewoman",
        "cavemen": "cavewomen",
        "chairman": "chairwoman",
        "chairmen": "chairwomen",
        "clergyman": "clergywoman",
        "clergymen": "clergywomen",
        "conductor": "conductress",
        "congressman": "congresswoman",
        "congressmen": "congresswomen",
        "councilman": "councilwoman",
        "councilmen": "councilwomen",
        "countryman": "countrywoman",
        "countrymen": "countrywomen",
        "craftsman": "craftswoman",
        "craftsmen": "craftswomen",
        "d00dz": "laydeez",
        "daddies": "mommies",
        "daddy": "mommy",
        "daughter": "son",
        "doorman": "doorwoman",
        "doormen": "doorwomen",
        "dudebro": "galpal",
        "father": "mother",
        "fireman": "firewoman",
        "firemen": "firewomen",
        "fisherman": "fisherwoman",
        "fishermen": "fisherwomen",
        "foreman": "forewoman",
        "foremen": "forewomen",
        "freshman": "freshwoman",
        "freshmen": "freshwomen",
        "garbageman": "garbagewoman",
        "garbagemen": "garbagewomen",
        "godfather": "godmother",
        "grandfather": "grandmother",
        "handyman": "handywoman",
        "handymen": "handywomen",
        "hangman": "hangwoman",
        "hangmen": "hangwomen",
        "henchman": "henchwoman",
        "henchmen": "henchwomen",
        "heroes": "heroines",
        "journeyman": "journeywoman",
        "journeymen": "journeywomen",
        "kinsman": "kinswoman",
        "kinsmen": "kinswomen",
        "klansman": "klanswoman",
        "layman": "laywoman",
        "laymen": "laywomen",
        "madman": "madwoman",
        "madmen": "madwomen",
        "mailman": "mailwoman",
        "mailmen": "mailwomen",
        "mansplain": "ladysplain",
        "marksman": "markswoman",
        "marksmen": "markswomen",
        "mascul": "femin",
        "menz": "ladiez",
        "middleman": "middlewoman",
        "middlemen": "middlewomen",
        "milkman": "milkwoman",
        "milkmen": "milkwomen",
        "misandr": "misogyn",
        "misogyn": "misandr",
        "nobleman": "noblewoman",
        "noblemen": "noblewomen",
        "ombudsman": "ombudswoman",
        "ombudsmen": "ombudswomen",
        "policeman": "policewoman",
        "policemen": "policewomen",
        "postman": "postwoman",
        "postmaster": "postmistress",
        "postmen": "postwomen",
        "repairman": "repairwoman",
        "repairmen": "repairwomen",
        "salesman": "saleswoman",
        "salesmen": "saleswomen",
        "sandman": "sandwoman",
        "sandmen": "sandwomen",
        "serviceman": "servicewoman",
        "servicemen": "servicewomen",
        "showman": "showwoman",
        "showmen": "showwomen",
        "snowman": "snowwoman",
        "spaceman": "spacewoman",
        "spacemen": "spacewomen",
        "spokesman": "spokeswoman",
        "spokesmen": "spokeswomen",
        "sportsman": "sportswoman",
        "sportsmen": "sportswomen",
        "statesman": "stateswoman",
        "statesmen": "stateswomen",
        "stepbrother": "stepsister",
        "stepfather": "stepmother",
        "steward": "stewardess",
        "superman": "superwoman",
        "supermen": "superwomen",
        "unman": "unwoman",
        "watchman": "watchwoman",
        "watchmen": "watchwomen",
        "weatherman": "weatherwoman",
        "weathermen": "weatherwomen",
        "whitemaleness": "whitefemaleness",
        "workman": "workwoman",
        "workmen": "workwomen"
    }

    # These are complete swaps, usually with specialized pluralizations
    complete = {
        "abbot": "abbess",
        "actor": "actress",
        "actors": "actresses",
        "archduke": "archduchess",
        "archdukes": "archduchesses",
        "author": "authoress",
        "authors": "authoresses",
        "baron": "baroness",
        "baronet": "baronetess",
        "baronets": "baronetesses",
        "barons": "baronesses",
        "beau": "belle",
        "beaus": "belles",
        "blond": "blonde",
        "blonds": "blondes",
        "boar": "sow",
        "boars": "sows",
        "boy": "maiden",
        "boyhood": "girlhood",
        "boyhoods": "girlhoods",
        "boyish": "girly",
        "boys": "girls",
        "bro": "sis",
        "bros": "sistas",
        "buck": "doe",
        "bull-calf": "cow-calf",
        "bull": "cow",
        "bullock": "heifer",
        "colt": "filly",
        "comte": "comtesse",
        "count": "countess",
        "counts": "countesses",
        "czar": "czarina",
        "dad": "mom",
        "dads": "moms",
        "deacon": "deaconess",
        "deacons": "deaconesses",
        "drake": "duck",
        "dude": "lady",
        "dudelier": "girlier",
        "dudeliest": "girliest",
        "dudely": "womanly",
        "dudes": "ladies",
        "duke": "duchess",
        "dukes": "duchesses",
        "earl": "countess",
        "earls": "countesses",
        "emperor": "empress",
        "emperors": "empresses",
        "enchanter": "enchantress",
        "fellow": "gal",
        "fellows": "gals",
        "fiance": "fiancee",
        "friar": "nun",
        "gander": "goose",
        "gentleman": "lady",
        "gentlemen": "ladies",
        "god": "goddess",
        "godhead": "goddesshead",
        "godheads": "goddessheads",
        "godhood": "goddesshood",
        "godliness": "goddessliness",
        "godly": "goddessly",
        "gods": "goddesses",
        "gramps": "grandma",
        "grandpa": "grandma",
        "grandpas": "grandmas",
        "guy": "gal",
        "guys": "gals",
        "hart": "hind",
        "he": "she",
        "headmaster": "headmistress",
        "heir": "heiress",
        "heirs": "heiresses",
        "hero": "heroine",
        "heros": "heroines",
        "himself": "herself",
        "host": "hostess",
        "hound": "brach",
        "hunter": "huntress",
        "husband": "wife",
        "husbandly": "wifely",
        "husbands": "wives",
        "king": "queen",
        "kings": "queens",
        "knight": "dame",
        "lad": "lass",
        "lads": "lassies",
        "landlord": "landlady",
        "lion": "lioness",
        "lord": "lady",
        "lords": "ladies",
        "male": "female",
        "males": "females",
        "man": "woman",
        "manhood": "womanhood",
        "manhoods": "womanhoods",
        "mankind": "womankind",
        "manliness": "womanliness",
        "manly": "ladylike",
        "manservant": "maidservant",
        "marquis": "marquise",
        "marquise": "marquise",
        "masc": "fem",
        "masseur": "masseuse",
        "master": "mistress",
        "mayor": "mayoress",
        "men": "women",
        "menz": "ladiez",
        "monk": "nun",
        "mr": "ms",
        "nephew": "niece",
        "nephews": "nieces",
        "papa": "mama",
        "paternal": "maternal",
        "paternity": "maternity",
        "poet": "poetess",
        "poppa": "momma",
        "priest": "priestess",
        "priests": "priestesses",
        "prince": "princess",
        "princes": "princesses",
        "radmasc": "radfem",
        "ram": "ewe",
        "sir": "ma'am",
        "sire": "dam",
        "sirs": "ma'ams",
        "son": "daughter",
        "sons": "daughters",
        "sorcerer": "sorceress",
        "stag": "hind",
        "stallion": "mare",
        "steer": "heifer",
        "step-son": "step-daughter",
        "stepson": "stepdaughter",
        "sultan": "sultana",
        "Sultan": "Sultana",
        "tiger": "tigress",
        "tutor": "governess",
        "viscount": "viscountess",
        "viscounts": "viscountesses",
        "washerman": "washerwoman",
        "washermen": "washerwomen",
        "widow": "widower",
        "widows": "widowers",
        "wizard": "sorceress"
    }
    special = {
        "cock": "hen",
        "him": "her",
        "his": "her",
        "her": "his"
    }

