from word import Word

b_dictionary = {}


def check_b_dict(word):
    if word in b_dictionary:
        return b_dictionary.get(word)
