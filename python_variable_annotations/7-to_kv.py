#!/usr/bin/env python3
'''A type-annotated function that takes a str
and an int and returns them as a tuple.'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a str k and an int OR float v and
    returns them as a tuple'''
    return k, v ** 2
