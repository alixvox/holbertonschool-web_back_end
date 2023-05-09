#!/usr/bin/env python3
''' A coroutine that takes two integers, n and max_delay,
performs wait_random n times with the specified max_delay,
and returns a list of all the delays in ascending order. '''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    ''' Returns a list of float values representing the delays
    obtained from performing wait_random n times with the specified
    max_delay, sorted in ascending order. '''
    tasks: list[asyncio.Task] = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
