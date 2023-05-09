#!/usr/bin/env python3
''' A coroutine called async_comprehension that collects 10 random
numbers using an async comprehension over async_generator and
returns the 10 random numbers. '''

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Returns a list of 10 random numbers collected using an
    async comprehension over the async_generator coroutine. '''

    random_numbers: List[float] = [number async for number in async_generator()]
    return random_numbers
