#!/usr/bin/env python3
"""
This module implements the LRUCache class which inherits from BaseCaching.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class.
    This class provides a caching system following a Least Recently Used
    (LRU) replacement algorithm.
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Put item in cache following LRU replacement algorithm.
        If key or item is None, this method does nothing.
        If cache has reached its item limit (BaseCaching.MAX_ITEMS)
        and the key is not in the cache, it will discard the least recently
        used item in cache to accommodate the new item.
        """
        if key and item:
            if (key not in self.cache_data and
                    len(self.keys) == BaseCaching.MAX_ITEMS):
                discarded_key = self.keys.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
            elif key in self.cache_data:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item from cache.
        If key is None or the key does not exist in cache_data, returns None.
        Otherwise, it moves the accessed key to the end of keys list and
        returns the value linked to the key in cache_data.
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
