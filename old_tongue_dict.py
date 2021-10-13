a_dictionary = {"a": "a'", "all": "es", "always": "hei", "am": "misain", "and": "e", "another": "sovya",
                "as": "sene", "attack": "baijan"}


def check_a_dict(word):
    if word in a_dictionary:
        return a_dictionary.get(word)
