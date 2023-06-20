#!/usr/bin/env python3
""" exercise.py """

import redis
import uuid
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call history decorator """
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result

    return wrapper


class Cache:
    """ Cache class """
    def __init__(self):
        """ Constructor Method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store Method """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[
            Callable] = None) -> Union[str, bytes, int, float]:
        """ Get Method """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Get Str Method """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Get Int Method """
        value = self._redis.get(key)
        return int(value)


def replay(method: Callable):
    """ Display the history of calls of a particular function """
    # Get the Cache instance from the method's __self__ attribute
    cache = method.__self__
    inputs = cache._redis.lrange(f"{method.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{method.__qualname__}:outputs", 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode('utf-8')})")
        print(f"-> {out.decode('utf-8')}")
