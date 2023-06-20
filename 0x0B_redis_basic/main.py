#!/usr/bin/env python3
""" main.py """

from exercise import Cache, replay

# Create a Cache instance
cache = Cache()

# Call the store method a few times
cache.store("foo")
cache.store("bar")
cache.store("egg")
cache.store("eggsperiment")

# Now replay the store method
replay(cache.store)
