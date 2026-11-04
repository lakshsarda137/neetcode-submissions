class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.queue.remove(key)       # fix 1
        self.queue.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)              # fix 6: refresh existing key
        elif len(self.queue) >= self.capacity:  # fix 2
            lru_key = self.queue.pop(0)         # fix 3, 4: evict from front
            del self.cache[lru_key]             # fix 5
        self.queue.append(key)                  # fix 7
        self.cache[key] = value