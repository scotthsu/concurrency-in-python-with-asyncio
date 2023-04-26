import threading
import time
times1 = []
try_count = 10000
def hello_from_thread():    
    for i in range(1,try_count):
        for j in range(2,100):
            x = 3.1 * 9.2 / 1.5 * 900.0/j
        times1.append(time.time())

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Python is currently running {total_threads} thread(s)')
times2 = []
for i in range(1,try_count):
    #print(f'+++++ count={i}, {thread_name}')
    for j in range(2,100):
        x = 3.1 * 9.2 / 1.5 * 900.0/j
    times2.append(time.time())

hello_thread.join()
i = 0
j = 0
main_printed = False
thread_printed = False
for k in range(1,try_count):
    if times1[i] > times2[j]:
        if not main_printed:
            print(f'main[{j}], worker[{i}] = {times2[j]},{times1[i]}')
            main_printed = True
            thread_printed = False
        j += 1
    elif times1[i] < times2[j]:
        if not thread_printed:
            print(f'worker[{i}], main[{j}] = {times1[i]},{times2[j]}')
            main_printed = False
            thread_printed = True
        i += 1
    else:
        i += 1
        j += 1

if i >= len(times1):
    i -= 1
if j >= len(times2):
    j -= 1

print(f'worker thread: times[{i}]={times1[i]}')
print(f'main thread: times[{j}]={times2[j]}')


