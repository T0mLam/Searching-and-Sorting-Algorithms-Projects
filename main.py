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
        queue = deque([(src, [src])])
        visited = set([src])
        while queue:
            current_word, path = queue.popleft()
            for neighbor in self.word_dictionary.find_neighbors(current_word):
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


if __name__ == '__main__':
    wl = WordLadder()
    print(wl.find_shortest_path('cow', 'hi'))