#!/usr/bin/env python3
"""
This module provides the index_range function which calculates the range of
indexes for pagination given a page number and page size.

The function is useful in scenarios where data needs to be split into pages
of a certain size, such as displaying blog posts or search results.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for pagination.
    Parameters:
    page (int): The page number.
    page_size (int): The number of items per page.
    Returns:
    tuple: A tuple of the start index and end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
