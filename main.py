from word_dictionary import WordDictionary
from timer import timer
from collections import deque

class WordLadder:
    def __init__(self):
        # Create instance of the WordDictionary
        self.word_dictionary = WordDictionary()
        pass

    def find_shortest_path(self, src, dst):
        if src == dst:
            return src
    queue = ([(src, [src])])
    visited = set([src])
    while queue:
        current_word, path = queue.popleft()
        for neighbor in self.WordDictionary.get_neighbors(current_node):
            if neighbor == dst:
                return path + [neighbor]
        if neighbor  not in visited:
            visited.add(neighbor)
            queue.append((neighbor, path + [neighbor]))
    return []






        # Find the shortest path from the source to the destination using BFS
        pass

    def find_k_shortest_paths(self, src, dst, k):
        # Optional
        pass

    def run(self):
        # User input
        pass

'''
Hi Artem, can you create a GUI for the project please :)
1. 2 text input fields (1 for the starting word, 1 for the ending word)
2. Display the shortest path, and other possible paths (if you have time)
'''
