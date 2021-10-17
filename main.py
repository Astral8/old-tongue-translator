import ot_dict

if __name__ == '__main__':
    sentence = input("Enter Your Text\n")
    sentence = sentence.lower()
    translated_sentence = ""
    words = sentence.split()
    for word in words:
        if word == words[0]:
            translated_sentence = ot_dict.check_dict(word)
        else:
            translated_sentence = translated_sentence + " " + ot_dict.check_dict(word)
    print(translated_sentence)
