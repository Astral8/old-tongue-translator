import dictionary.a_old_tongue_dict as a_dict
import dictionary.b_old_tongue_dict as b_dict



def check_dict(word):
    if word[0] == 'a':
        return a_dict.check_a_dict(word)
    elif word[0] == 'b':
        return b_dict.check_b_dict(word)
    else:
        return "not in dictionary"