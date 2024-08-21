#!/usr/bin/python3

"""
class FIFOCache that inherits from BaseCaching and is a caching system:
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class inherits from BaseCaching and
        follows FIFO eviction policy.
    """

    def __init__(self):
        """Initialize the FIFO Cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache is full (i.e., it contains the maximum
            number of items defined by BaseCaching.MAX_ITEMS),
        the oldest item (first inserted) will be removed
            to make space for the new item.

        Parameters:
        key (str): The key to store the item.
        item (any): The item to be stored in the cache.

        Returns:
        None

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.

        Parameters:
        key (str): The key for the item to be retrieved.

        Returns:
        The value associated with the key in the cache,
            or None if the key does not exist or is None.
        """
        return self.cache_data.get(key, None)
