#!/usr/bin/env python3
""" BasicCache class that inherits from BaseCaching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implement BasicCache class"""
    def put(self, key, item):
        """Add an item to the cache without limit"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
