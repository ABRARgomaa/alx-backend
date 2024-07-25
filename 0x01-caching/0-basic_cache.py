#!/usr/bin/python3
"""
Create a class BasicCache that inherits from BaseCaching
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache
    """

    def put(self, key, item):
        """
        put method
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get method
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
