#!/usr/bin/env python3
''' A function that takes two integers, n and max_delay,
measures the total execution time for wait_n(n, max_delay),
and returns the average execution time as a float. '''

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> List[float]:
    ''' Returns the average execution time as a float
    obtained by measuring the total execution time for
    wait_n(n, max_delay) and dividing it by n. '''

    start_time: float = time.time()

    async def main():
        await wait_n(n, max_delay)

    asyncio.run(main())

    end_time: float = time.time()
    total_time: float = end_time - start_time
    average_time: float = total_time / n
    return average_time
