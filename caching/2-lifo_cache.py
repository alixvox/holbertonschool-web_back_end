#!/usr/bin/env python3
"""
This module implements the LIFOCache class which inherits from BaseCaching.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class.
    This class provides a caching system following a Last-In-First-Out
    (LIFO) replacement algorithm.
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Put item in cache following LIFO replacement algorithm.
        If key or item is None, this method does nothing.
        If cache has reached its item limit (BaseCaching.MAX_ITEMS)
        and the key is not in the cache, it will discard the most recently
        added item in cache to accommodate the new item.
        """
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
        """
        Get item from cache.
        If key is None or the key does not exist in cache_data, returns None.
        Otherwise, it returns the value linked to the key in cache_data.
        """
        return self.cache_data.get(key, None)
