import a_old_tongue_dict as a_ot_dict

if __name__ == '__main__':
    sentence = input("Enter Your Text\n")
    sentence = sentence.lower()
    translated_sentence = ""
    words = sentence.split()
    for word in words:
        if word == words[0]:
            translated_sentence = a_ot_dict.check_a_dict(word)
        else:
            translated_sentence = translated_sentence + " " + a_ot_dict.check_a_dict(word)
    print(translated_sentence)
