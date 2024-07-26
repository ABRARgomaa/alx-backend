#!/usr/bin/env python3
"""
MRU Cache Module
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    and implements a MRU caching system.
    """

    def __init__(self):
        """
        Initialize the LIFOCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache with the given key.

        If the cache exceeds the maximum size,
        the last item inserted is discarded.

        Args:
            key (str): The key of the item.
            item (any): The item to be stored.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
