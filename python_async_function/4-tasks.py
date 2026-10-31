#!/usr/bin/env python3
"""Execute multiple tasks concurrently."""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """Run n tasks and return delays in ascending completion order."""
    tasks = [
        task_wait_random(max_delay)
        for _ in range(n)
    ]

    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
