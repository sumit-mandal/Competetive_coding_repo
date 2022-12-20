import time
import multiprocessing
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping in {seconds} seconds..')
    time.sleep(seconds)
    print('Done Sleeping..')


# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()

processes = []

for i in range(10):
    p = multiprocessing.Process(target=do_something,args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
