import threading 
import time 
task=[
    ("task1",2),
    ("task2",3),
    ("task3",1)
]
def do_task(task_name, wait_time):
    print(f"{task_name} started, will take {wait_time} seconds.")
    time.sleep(wait_time)

    print(f"{task_name} completed.")

threads = []
for task_name, wait_time in task:
    t = threading.Thread(target=do_task, args=(task_name, wait_time))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

def single_threaded():
        print("\n---Single Threaded Demo---")
        start_time = time.perf_counter()

        for task_name, wait_time in task:
            do_task(task_name, wait_time)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(f"single-threaded execution time: {elapsed_time:.2f} seconds")

        return elapsed_time

def multithreaded():
        print("\n---Multithreaded Demo---")
        start_time = time.perf_counter()
        threads = []

        for task_name, wait_time in task:
            thread = threading.Thread(target=do_task, args=(task_name, wait_time))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"multithreaded execution time: {elapsed_time:.2f} seconds")

        return elapsed_time

def main():
    single_time = single_threaded()
    multi_time = multithreaded()

    print("\n=======COMPARISION=========")
    print(f"Single-Threaded : {single_time:.2f} seconds")
    print(f"Multithreaded: {multi_time:.2f} seconds")

    print("\n All worker threads completed sucessfully")

if __name__== "__main__":
    main()