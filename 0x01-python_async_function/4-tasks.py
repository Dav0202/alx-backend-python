#!/usr/bin/env python3
""" async basics """

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    call task_wait_random n times with max_delay.
    """
    que, array = [], []

    for _ in range(n):
        que.append(task_wait_random(max_delay))

    for p in asyncio.as_completed(que):
        result = await p
        array.append(result)

    return array
