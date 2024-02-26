'''
Trie is a tree data structure.
Each node except the leaf node has 0 to 26 children, storing each alphabet of a word.

e.g.
['app', 'apps', 'apple', 'bed', 'bee'] can be stored as ...   
('*' indicates end of word)

              ROOT
              / \
            a     b
           /       \
          p         e
        /          /  \
      *p         *d    *e     
     / \
   *s   l
       /
      *e

Searching for a word: O(l), l = length of the word
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.__file_input()

    def find_neighbors(self, word):
        pass

    def __file_input(self):
        with open('words_alpha.txt', 'r') as f:
            for word in f.read().split():
                self.__insert(word)

    def __insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            
        node.end_of_word = True
    
        

