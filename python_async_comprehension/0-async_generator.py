#!/usr/bin/env python3
''' A coroutine called async_generator that asynchronously waits
1 second and yields a random number between 0 and 10, and repeats
this process 10 times. '''

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    ''' Asynchronously waits 1 second and yields a random number
    between 0 and 10 (inclusive) for 10 iterations. '''

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
