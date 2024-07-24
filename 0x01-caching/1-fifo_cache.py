#!/usr/bin/env python3
""" FIFO Caching."""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Implementation of FIFO caching"""
    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Assign to the dictionary."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_order.pop(0)
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """ Return the value in self.cache_data."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
