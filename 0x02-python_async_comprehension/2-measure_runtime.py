#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Four parallel comprehensions Run time """
    start = time()
    task_array = [async_comprehension() for i in range(4)]
    await gather(*task_array)
    end = time()
    return (end - start)
