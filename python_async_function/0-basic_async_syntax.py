#!/usr/bin/env python3
''' An coroutine that takes an int (default 10),
waits a random amount of seconds between 0 and the int,
and returns the amount of time delayed as a float. '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Returns the float amount of time that asyncio.sleep waits
    calculated randomly between int 0 and max_delay. '''
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
