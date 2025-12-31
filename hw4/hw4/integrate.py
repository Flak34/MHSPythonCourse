import math
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate_chunk(f, a, step, start, end):
    acc = 0.0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate_parallel(
    f,
    a,
    b,
    *,
    n_jobs=1,
    n_iter=10_000_000,
    executor_cls=ThreadPoolExecutor,
):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs

    tasks = []
    for i in range(n_jobs):
        start = i * chunk_size
        end = n_iter if i == n_jobs - 1 else (i + 1) * chunk_size
        tasks.append((f, a, step, start, end))

    with executor_cls(max_workers=n_jobs) as executor:
        results = executor.map(integrate_chunk, *zip(*tasks))

    return sum(results)