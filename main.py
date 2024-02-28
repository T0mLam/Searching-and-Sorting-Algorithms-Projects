from word_dictionary import WordDictionary
from timer import timer


class WordLadder:
    @timer
    def __init__(self):
        self.word_dict = WordDictionary() 

    @timer
    def find_shortest_path(self, src, dst):
        # Find the shortest path from the source to the destination using BFS
        pass

    @timer
    def find_k_shortest_paths(self, src, dst, k):
        # Optional
        pass