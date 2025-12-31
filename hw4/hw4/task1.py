import time
from threading import Thread
from multiprocessing import Process
from fib import fib

N = 35
TASKS = 10


def run_fib():
    fib(N)


def sync_run():
    for _ in range(TASKS):
        run_fib()


def threading_run():
    threads = []
    for _ in range(TASKS):
        t = Thread(target=run_fib)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def multiprocessing_run():
    processes = []
    for _ in range(TASKS):
        p = Process(target=run_fib)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


def measure(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    results = []

    sync_time = measure(sync_run)
    results.append(f"Sync:           {sync_time:.2f} seconds")

    thread_time = measure(threading_run)
    results.append(f"Threading:      {thread_time:.2f} seconds")

    process_time = measure(multiprocessing_run)
    results.append(f"Multiprocessing:{process_time:.2f} seconds")

    output = "\n".join(results)

    print(output)

    with open("task1.txt", "w") as f:
        f.write(output)