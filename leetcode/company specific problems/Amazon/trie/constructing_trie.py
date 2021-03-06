# Add and Search Word - Data structure design

#Time complexity: O(M), M is max string length
#cons, are it stores a lot of memory, for storing string and each 
#node has several pointers, equal to number of char in alphabet

class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.is_end_node = False


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


     

def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in tire"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 

  
    # # Search for different keys 
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
  
if __name__ == '__main__': 
    main() 



