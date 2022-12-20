import threading
import time
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeeping in {seconds} second...')
    time.sleep(seconds)
    print("DOne Sleeping")

# t1 = threading.Thread(target=do_something) # just name of function not execution (parantheses)
# t2 = threading.Thread(target=do_something)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start,2)} seconds')
