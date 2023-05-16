from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        if not key or not item:
            return

        if (len(self.keys) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data):
            discarded_key = self.keys.popleft()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
            self.keys.append(key)

        self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)

    def get(self, key):
        return self.cache_data.get(key, None)
