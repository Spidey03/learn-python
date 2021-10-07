"""
Threading..
when we are going to significantly speed up program, that is running process parllel or concurrently..
"""
import concurrent.futures
import time


def do_something(seconds: int) -> str:
    print(f"Sleeping for {seconds} second..")
    time.sleep(seconds)
    return "Done sleeping :)"


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    # The processes starts and the completes small process first, it takes less time
    start = time.perf_counter()
    results = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")

    print("-"*20)
    # The process are completed in the order that they started
    start = time.perf_counter()
    results = executor.map(do_something, secs)
    for result in results:
        print(result)
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")

