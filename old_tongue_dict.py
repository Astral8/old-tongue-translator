a_dictionary = {"a": "o", "able": "folyt", "about": "tiel", "account": "norvenne",
                "acid": "ghar", "across": "gaen", "act": "bunok", "addition": "einto",
                "adjustment": "faerstin", "after": "widon", "again": "nye", "against": "bat",
                "agony": "dha", "agreement": "o'vin", "air": "raia", "all": "aes", "all-powerful": "ghraem",
                "almost": "sast", "always": "hei", "am": "misain", "among": "tom", "amount": "abakran",
                "amusement": "seel", "and": "e", "angle": "lato", "angry": "cavastu", "anguish": "dha",
                "animal": "ubunto", "annihilation": "bhan", "anniversary": "shanna'har", "another": "sovya",
                "answer": "conagh", "ant": "pizar", "anxiety": "cuande", "any": "shak", "apparatus": "jobei",
                "apple": "melimo", "approval": "modan", "arch": "onadh", "argument": "zeshi", "arm": "bazam",
                "army": "dumki", "arrow": "vasen", "art": "beatha", "as": "sene", "ask": "devor", "asked": "devoriska",
                "at": "thaz", "attack": "baijan", "attempt": "gomaen", "attention": "sahlan", "attraction": "amotath",
                "aunt": "shaendi", "authority": "rahtsi", "automatic": "n'baid", "awake": "aagret"
                }


# Note: all-powerful, the
# Note: am
# Note: am no(t)
# Note: Anniversary Marriage Celebration *implemented anniversary
# Note: any other
# Note: arrow of time
# Note: asked *implemented it
def check_a_dict(word):
    if word in a_dictionary:
        return a_dictionary.get(word)
