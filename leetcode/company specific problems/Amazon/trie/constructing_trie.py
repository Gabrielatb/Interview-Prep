# Add and Search Word - Data structure design

import collections


class WordDictionary(object):
    def __init__(self):
        self.len_to_words = collections.defaultdict(set)

    def addWord(self, word):
        self.len_to_words[len(word)].add(word)


    def search(self, word):
        length = len(word)

        p = self.len_to_words[length]
        if not p:
            return False 
        if word in p:
            return True
        for i in range(length):
            if word[i] == '.':
                continue

            

if __name__ == '__main__':
    word = WordDictionary()
    print word.addWord("bad")
    print word.addWord("dad")
    print word.addWord("mad")
    print word.search("pad") #-> false
    # print word.search("bad") #-> true
    # print word.search(".ad") #-> true
    # print word.search("b..") #-> true
