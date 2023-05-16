from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if not key or not item:
            return

        if key in self.cache_data:
            self.keys.remove(key)  # Move the updated key to the end
        elif len(self.keys) == BaseCaching.MAX_ITEMS:
            discarded_key = self.keys.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        return self.cache_data.get(key, None)
