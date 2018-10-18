
#  Build a function that is given a phrase and a vocab set. 
#  It should return a set of the possible legal phrases that can be made
# from that vocabulary.

# >>> vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to',
# ...   'night', 'ate', 'noodles', 'for', 'dinner', 'tonight'}

# >>> sentences = parse('iatenoodlesfordinnertonight', vocab)

# >>> for s in sorted(sentences):
# ...    print s
# i a ten oodles for dinner to night
# i a ten oodles for dinner tonight
# i a ten oodles ford inner to night
# i a ten oodles ford inner tonight
# i ate noodles for dinner to night
# i ate noodles for dinner tonight
# i ate noodles ford inner to night
# i ate noodles ford inner tonight


def word_break(phrase, vocab):
    """Break a string into words.

    Input:
        - string of words without space breaks
        - vocabulary (set of allowed words)

    Output:
        set of all possible ways to break this down, given a vocab
    """

    # 'set of all possible legal phrases' ---> recursion

    poss_breaks = set()

    for word in vocab:
        #base case no parsing required
        if phrase == word:
            poss_breaks.add(word)

        elif phrase.startswith(word):
            #word matches beginning of string

            #rest of the string
            rest = phrase[len(word):]

            #recurse to find the various possibilities of end of sentence

            
            for parsed in word_break(rest, vocab):
                print parsed
                # word_and_rest = [word + ' ' + parsed]

            # return_lst.append(word_and_rest)

    # return return_lst




vocab = ['i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to',
'night', 'ate', 'noodles', 'for', 'dinner', 'tonight']

sentence = 'iatenoodlesfordinnertonight'

print word_break(sentence, vocab)










