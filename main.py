from typing import Dict

if __name__ == '__main__':
    sentence = input("Enter Your Text")
    translated_sentence = ""
    dictionary = Dict["a": "a'", "all": "es", "always":"hei", "am": "misain", "and": "e", "another": "sovya",
                 "as":"sene", "attack": "baijan"]
    if sentence in dictionary.keys():
        translated_sentence = dictionary[sentence]

    print(translated_sentence)
