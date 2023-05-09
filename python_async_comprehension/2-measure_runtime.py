#!/usr/bin/env python3
''' A coroutine called measure_runtime that executes
async_comprehension four times in parallel, measures the total
runtime, and returns it. '''

import asyncio
import time
from typing import List, Tuple
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measures the total runtime of executing async_comprehension
    four times in parallel and returns it as a float. '''

    start_time: float = time.perf_counter()

    coroutines: List = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)

    end_time: float = time.perf_counter()
    total_runtime: float = end_time - start_time
    return total_runtime
