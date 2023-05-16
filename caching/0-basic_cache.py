#!/usr/bin/env python3
"""
This module implements the BasicCache class which inherits from BaseCaching.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class.
    This class provides basic caching functionality with no limit to
    the number of items it can hold.
    """

    def put(self, key, item):
        """
        Put item in cache.
        If key or item is None, this method does nothing.
        Otherwise, it adds the item to the cache_data dictionary,
        using the key as the key for the dictionary.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item from cache.
        If key is None or the key does not exist in cache_data, returns None.
        Otherwise, it returns the value linked to the key in cache_data.
        """
        return self.cache_data.get(key, None)
