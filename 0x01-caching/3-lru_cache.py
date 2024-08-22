#!/usr/bin/python3

"""class LRUCache that inherits from BaseCaching and is a caching system:
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Implements an LRU (Least Recently Used) caching system.
    Inherits from BaseCaching and uses an OrderedDict to maintain the order
    of items based on their usage. The least recently used item will be
    evicted when the cache exceeds the maximum number of items allowed.
    """
    def __init__(self):
        """
        Initializes the LRUCache with an empty OrderedDict for storing
            cache data
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
