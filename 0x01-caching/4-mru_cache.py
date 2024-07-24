#!/usr/bin/env python3
""" MRU Caching."""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    A caching system that uses the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        """
        Initializes the MRUCache instance
        """
        super().__init__()
        self.cache_order = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache

        If key or item is None, does nothing
        If the cache is full, discards the most recently used item
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_order.move_to_end(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = next(reversed(self.cache_order))
            print(f"DISCARD: {discarded_key}")
            del self.cache_data[discarded_key]
            del self.cache_order[discarded_key]

        self.cache_data[key] = item
        self.cache_order[key] = None

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_order.move_to_end(key)
        return self.cache_data.get(key)
