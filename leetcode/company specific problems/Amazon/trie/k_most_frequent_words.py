# Given a non-empty list of words, return the k most frequent elements.

# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower
# alphabetical order comes first.



class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.is_end_node = False
        self.frequency = 0


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def char_to_indx(self, char):
        """A returns a char indx """
        #Ord() return an integer representing the Unicode code point

        return ord(char) - ord('a')

    def insert(self, key):
        """if key not present inserts key
        into trie, if key is prefix, marks as leaf node"""

        curr = self.root
        for indx in range(len(key)):
            char = key[indx]
            alphabet_indx = self.char_to_indx(char)
            if curr.children[alphabet_indx] == None:
                curr.children[alphabet_indx] = TrieNode()

            curr = curr.children[alphabet_indx]

        curr.is_end_node = True


    def search(self, key):
        """Search key in Trie
        return True if key found, else False"""

        curr = self.root
        for indx in range(len(key)):
            char = key[indx]
            alphabet_indx = self.char_to_indx(char)
            if curr.children[alphabet_indx] == None:
                return False

            curr = curr.children[alphabet_indx]

        return curr != None and curr.is_end_node

    def topKFrequent(self, words, k):
        return_lst = [None] * k

        curr = self.root
        
        for key in keys:
            if self.search(key):
                curr.frequency +=1

            else:
                self.insert(key) 





     
if __name__ == '__main__':

  
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2


