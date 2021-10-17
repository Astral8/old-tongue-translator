class Word:
    eng_word: str
    ot_word: str
    alt_ot_word: str
    type: str
    type2: str = ""
    type3: str = ""
    definition: str
    synonym: []
    valid_types = {"adjective", "adverb", "relative pronoun", "preposition", "noun", "verb", "conjunction", "pronoun",
                   "possessive"}

    def __init__(self, word, ot_word, type, definition="Not Defined", synonym=[]):
        self.word = word
        self.ot_word = ot_word
        if self.check_valid(type):
            self.type = type
        else:
            return "This is not a valid type"
        self.definition = definition
        self.synonym = synonym

    def __repr__(self):
        return str(self.word)

    def __str__(self):
        return str(self.word)

    def add_second_type(self, type2):
        if self.check_valid(type2):
            self.type2 = type2
        else:
            return "This is not a valid type"

    def add_third_type(self, type3):
        if self.check_valid(type3):
            self.type3 = type3
        else:
            return "This is not a valid type"

    def add_alt_ot_word(self, ot_word, type):
        self.alt_ot_word = ot_word
        if self.type2 == "":
            self.type2 = type
        else:
            self.type3 = type

    def check_valid(self, unknown_type):
        if unknown_type not in self.valid_types:
            return False
        else:
            return True
