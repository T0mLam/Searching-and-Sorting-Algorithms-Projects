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

        while queue:
            current_word, path = queue.popleft()
            for neighbor in self.word_dictionary.find_neighbors(current_word):
                if neighbor == dst:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
        return []

    @timer
     def find_k_shortest_paths(self, src, dst, k):
       if src == dst:
           return [[src]]
          
       shortest_path = self.find_shortest_path(src, dst)
       if not shortest_path:
           return []
       
       k_shortest_paths = [shortest_path]
       
       visited = set(shortest_path)
       
       queue = deque([(len(shortest_path), shortest_path)])
       while queue and len(k_shortest_paths) < k:
           _, path = queue.popleft()
           for i in range(len(path)):
               for neighbor in self.word_dictionary.get_neighbors(path[i]):
                   if neighbor not in visited:
                       new_path = path[:i] + [neighbor] + path[i+1:]
                       if new_path not in k_shortest_paths:
                           k_shortest_paths.append(new_path)
                           visited.add(neighbor)
                           queue.append((len(new_path), new_path))
                           
                           queue = deque(sorted(queue))
       return k_shortest_paths

if __name__ == '__main__':
    wl = WordLadder()
    print(wl.find_shortest_path('cow', 'man'))