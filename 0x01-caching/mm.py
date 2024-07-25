#!/usr/bin/python3
"""
Create a class LIFOCache that inherits from BaseCaching
"""


from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    initialization
    """

    def __init__(self):
        """
        initialization
        """
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """
        put method
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.queue:
            self.queue.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            latest_key = self.queue.pop()
            if latest_key in self.cache_data:
                del self.cache_data[latest_key]
                print(f"DISCARD: {latest_key}")

    def get(self, key):
        """
        get method
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
