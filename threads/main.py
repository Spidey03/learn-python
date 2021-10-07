"""
Threading..
when we are going to significantly speed up program, that is running process parllel or concurrently..
"""
import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds} second..")
    time.sleep(seconds)
    print("Done sleeping :)")

threads = []
for i in range(10):
    t = threading.Thread(target=do_something, args=[i])
    t.start()
    threads.append(t)

# map(lambda thread: thread.join(), threads)
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
