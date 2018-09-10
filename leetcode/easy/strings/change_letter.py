#rotate value of string based on rotateValue


def rotate(s, rotateValue):

    new_word = ''
    lower_case = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_case = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    lst_words = s.split(' ')
    print lst_words
    return_lst = []
    
    for word in lst_words:
        first_letter = word[0]

        if first_letter in lower_case:
            for letter in word:

                indx = 0
                while lower_case[indx] != letter:
                        if indx == 25:
                            indx = 0
                        else:
                            indx += 1

                new_indx = indx + rotateValue
                if new_indx > 25:
                    indx = new_indx - 25
                new_word += lower_case[indx]

            return_lst.append(new_word)
            new_word = ''

        elif first_letter in upper_case:
            for letter in word:

                indx = 0
                while upper_case[indx] != letter:
                        if indx == 25:
                            indx = 0
                        else:
                            indx += 1

                new_indx = indx + rotateValue
                if new_indx > 25:
                    indx = new_indx - 25
                    new_word += upper_case[indx]
            return_lst.append(new_word)
            new_word = ''
        else:
            return_lst.append(word)

    print return_lst
    return ' '.join(return_lst)







            