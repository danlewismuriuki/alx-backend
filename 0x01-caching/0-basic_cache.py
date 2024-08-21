#!/usr/bin/python3

"""
Class BasicCache that inherits from BaseCaching
    and is a caching system:
"""
BaseCaching = __import__("base_caching").BaseCaching
# from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache implementaion class

    Attributes:
    MAX_ITEMS: number of items that can be store in the cache
    """

    def __init__(self):
        """Initialize the BasicCache class."""
        super().__init__()  # Get the Base class attributes

    def put(self, key, item):
        """Assign item to the cache_data dictionary for the given key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value from cache_data for the given key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
