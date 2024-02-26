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
    
        

