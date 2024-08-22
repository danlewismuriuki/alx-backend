#!/usr/bin/python3

"""class MRUCache that inherits from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    Implements an MRU (Most Recently Used) caching system.
    """
    def __init__(self):
        """
        Initializes the MRUCache with an empty OrderedDict for
            storing cache data.
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
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
