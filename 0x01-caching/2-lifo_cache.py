#!/usr/bin/env python3
""" LIFO Caching."""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    A caching system that uses the Last-In-First-Out (LIFO) algorithm
    """

    def __init__(self):
        """
        Initializes the LIFOCache instance
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Adds an item to the cache

        If key or item is None, does nothing
        If the cache is full, discards the last item added (LIFO algorithm)
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.cache_order.pop()
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
