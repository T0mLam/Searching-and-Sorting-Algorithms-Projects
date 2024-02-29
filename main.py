from word_dictionary import WordDictionary
from timer import timer
from collections import deque

class WordLadder:
    @timer
    def __init__(self):
        self.word_dictionary = WordDictionary()

    @timer
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



    @timer
    def find_k_shortest_paths(self, src, dst, k):
        # Optional
        pass