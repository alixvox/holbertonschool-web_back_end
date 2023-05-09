#!/usr/bin/env python3
'''A type-annotated function that takes a list of str and
returns a list of tuples of the str and index in the list.'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples from an Iterable of Seuqnces lst where
    each tuple contains a Sequence from lst and its corresponding length'''
    return [(i, len(i)) for i in lst]
