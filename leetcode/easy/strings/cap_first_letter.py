#capitalize all first letters of words that start with alphabet


def cap(s):

    new_lst = s.split(' ')
    lower_case = []
    return_lst = []
    for word in new_lst:
        letter = word[0]
        if letter.isalpha() == True:
            upper_letter = letter.upper()
            new_word = upper_letter + word[1:]
            return_lst.append(new_word)
        else:
            return_lst.append(word)

    return ' '.join(return_lst)
