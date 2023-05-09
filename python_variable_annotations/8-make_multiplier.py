#!/usr/bin/env python3
'''A type-annotated function that takes a float
and returns a function to multiply it by another float.'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that returns the multiplication of float
    multiplier with float input'''
    def multiply_this(input: float) -> float:
        '''Returns the multiplication of float input with float
        multiplier'''
        return input * multiplier
    return multiply_this