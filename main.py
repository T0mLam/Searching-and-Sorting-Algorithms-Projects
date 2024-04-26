from collections import deque

from timer import timer
from word_dictionary import WordDictionary


class WordLadder:
    @timer
    def __init__(self):
        self.word_dictionary = WordDictionary()

    @timer
    def find_shortest_path(self, src, dst):
        if src == dst:
            return src
        
        queue = deque([(src, [src])])
        visited = set()
        visited.add(src)

        while queue:
            current_word, path = queue.popleft()
            for neighbor in self.word_dictionary.find_neighbors(current_word):
                if neighbor in visited:
                    continue
                if neighbor == dst:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
        return []


# Testing
if __name__ == '__main__':
    wl = WordLadder()
    print(wl.find_shortest_path('eeee', 'ffff'))
