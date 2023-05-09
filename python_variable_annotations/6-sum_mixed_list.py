#!/usr/bin/env python3
'''A type-annotated function that takes a list
of ints and floats and returns the sum as a float.'''

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''Returns sum of all ints and floats in
    list mxd_list as a float'''
    return sum(mxd_list)
