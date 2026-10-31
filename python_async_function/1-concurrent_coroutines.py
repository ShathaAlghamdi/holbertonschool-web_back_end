#!/usr/bin/env python3
"""Execute multiple coroutines concurrently."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Run wait_random n times and return delays in ascending order."""
    tasks = [
        asyncio.create_task(wait_random(max_delay))
        for _ in range(n)
    ]

    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
