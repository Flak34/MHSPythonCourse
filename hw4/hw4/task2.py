import math
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from integrate import integrate_parallel

CPU_NUM = os.cpu_count()
N_ITER = 10_000_000


def measure(func):
    start = time.perf_counter()
    result = func()
    end = time.perf_counter()
    return result, end - start


if __name__ == "__main__":
    results = []
    results.append(f"CPU cores: {CPU_NUM}")
    results.append("n_jobs | ThreadPool (s) | ProcessPool (s)")
    results.append("-" * 40)

    for n_jobs in range(1, CPU_NUM * 2 + 1):
        _, t_thread = measure(
            lambda: integrate_parallel(
                math.cos,
                0,
                math.pi / 2,
                n_jobs=n_jobs,
                n_iter=N_ITER,
                executor_cls=ThreadPoolExecutor,
            )
        )

        _, t_proc = measure(
            lambda: integrate_parallel(
                math.cos,
                0,
                math.pi / 2,
                n_jobs=n_jobs,
                n_iter=N_ITER,
                executor_cls=ProcessPoolExecutor,
            )
        )

        results.append(f"{n_jobs:6} | {t_thread:14.2f} | {t_proc:15.2f}")

        print(results[-1])

    output = "\n".join(results)

    with open("task2.txt", "w") as f:
        f.write(output)