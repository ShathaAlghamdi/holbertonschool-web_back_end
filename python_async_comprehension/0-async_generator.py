#!/usr/bin/env python3
"""Defines an asynchronous generator."""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random float values between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
