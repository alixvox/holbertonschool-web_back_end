#!/usr/bin/env python3
''' A coroutine that takes two integers, n and max_delay,
creates asyncio.Tasks using task_wait_random n times with
the specified max_delay, and returns a List of all the delays
in ascending order. '''

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Returns a List of float values representing the delays
    obtained from performing task_wait_random n times with the
    specified max_delay, sorted in ascending order. '''
    async def gather_results(task: asyncio.Task) -> float:
        return await task

    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = await asyncio.gather(
        *(gather_results(task) for task in tasks))
    return sorted(delays)
