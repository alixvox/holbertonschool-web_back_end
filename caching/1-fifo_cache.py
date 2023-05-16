#!/usr/bin/env python3
"""
This module implements the FIFOCache class which inherits from BaseCaching.
"""

from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class.
    This class provides a caching system following a First-In-First-Out
    (FIFO) replacement algorithm.
    """

    def __init__(self):
        """
        Initialize the class instance.
        """
        super().__init__()
        self.keys = deque()

    def put(self, key, item):
        """
        Put item in cache following FIFO replacement algorithm.
        If key or item is None, this method does nothing.
        If cache has reached its item limit (BaseCaching.MAX_ITEMS)
        and the key is not in the cache, it will discard the oldest item
        in cache to accommodate the new item.
        """
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
        """
        Get item from cache.
        If key is None or the key does not exist in cache_data, returns None.
        Otherwise, it returns the value linked to the key in cache_data.
        """
        return self.cache_data.get(key, None)
