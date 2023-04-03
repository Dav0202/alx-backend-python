#!/usr/bin/env python3
""" async basics"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_random n times with the max_delay.
    """
    que, array = [], []

    for _ in range(n):
        que.append(wait_random(max_delay))

    for p in asyncio.as_completed(que):
        result = await p
        array.append(result)

    return array
