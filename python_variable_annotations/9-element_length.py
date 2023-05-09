#!/usr/bin/env python3
'''A type-annotated function that takes a list of str and
returns a list of tuples of the str and index in the list.'''

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''Returns a list of tuples from list lst where each
    tuple contains a str from lst and its corresponding length'''
    return [(i, len(i)) for i in lst]
