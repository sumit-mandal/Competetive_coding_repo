import concurrent.futures
import time
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeeping in {seconds} second...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something,1.5)
    # f2 = executor.submit(do_something,1.5)

    secs = [5,4,3,2,1]
    # results = [executor.submit(do_something,sec) for sec in secs]
    results = executor.map(do_something,secs)

    # for result in results:
    #     print(result)

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # print(f1.result())
    # print(f2.result())

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')
