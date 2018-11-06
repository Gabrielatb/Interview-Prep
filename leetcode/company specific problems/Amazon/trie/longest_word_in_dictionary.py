class TrieNode(object):
    def __init__(self, word=''):
        self.children = [None] * 26
        self.is_end_node = False
        self.word = word


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
                curr.children[alphabet_indx] = TrieNode(key)

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



    def longestWord(self):

        curr = self.root
        stack = [x for x in curr.children if x is not None]
        result = ''
        while stack:
            print stack
            node = stack.pop()
            if node.is_end_node:
                if len(result) < len(node.word) or  len(result) == len(node.word) and result > node.word:
                    result = node.word
                stack.extend([x for x in node.children if x is not None])

        return result

if __name__ == '__main__':
    t = Trie() 
  
    # word = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    word = ["w","wo","wor","worl", "world"]
    # Construct trie 
    for w in word: 
        t.insert(w) 

    print t.longestWord()




