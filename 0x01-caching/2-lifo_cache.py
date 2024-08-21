#!/usr/bin/python3

"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements
    a caching system using the Last-In-First-Out (LIFO) approach.

    The most recently added item will be the first one to be discarded
    when the cache exceeds the maximum number of allowed items.
    """

    def __init__(self):
        """
        Initialize the LIFOCache with the inherited BaseCaching attributes.
        Also initializes an empty list `order` to track the order of keys
        as they are added to the cache.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache.
        """
        if key is None or item is None:
            return

        # If key already exists just update the item
        if key in self.cache_data:
            self.cache_data[key] = item

            self.order.remove(key)
            self.order.append(key)
            return

        # Check if we need to discard an item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        # Add the new item
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
