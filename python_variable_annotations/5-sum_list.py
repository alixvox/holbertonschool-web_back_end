#!/usr/bin/env python3
'''A type-annotated function that takes a list
of floats and returns the sum of all floats.'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Returns sum of all floats in list input_list as a float'''
    return sum(input_list)
