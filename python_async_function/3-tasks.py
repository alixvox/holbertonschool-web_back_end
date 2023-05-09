#!/usr/bin/env python3
''' A regular function that takes an integer max_delay and
returns an asyncio.Task created from the wait_random coroutine. '''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' Returns an asyncio.Task created from the wait_random coroutine
    by awaiting wait_random with the given max_delay. '''

    async def main():
        return await wait_random(max_delay)

    return asyncio.create_task(main())
