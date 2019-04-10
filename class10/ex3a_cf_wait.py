from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
from my_devices import network_devices as devices
from my_functions import ssh_command2

'''
3a. Create a new function that is a duplicate of your "ssh_command" function.
Name this function "ssh_command2". This function should eliminate all printing
to standard output and should instead return the show command output. Note, in
general, it is problematic to print in the child thread as you can get into race
conditions between the threads. Using the "ThreadPoolExecutor" in Concurrent
Futures execute "show version" on each of the devices defined in my_devices.py.
Use the 'wait' method to ensure all of the futures have completed. Concurrent
futures should be executing the ssh_command2 function in the child threads.
Print the total execution time required to accomplish this task.
'''

def main():
    start_time = datetime.now()
    max_threads = 5

    # Create the thread pool
    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for device in devices:
        future_list.append(pool.submit(ssh_command2, device, "show version"))

    # Wait until all threads are completed
    wait(future_list)

    for future in future_list:
        print("Result: " + future.result())

    end_time = datetime.now()
    print(f"Total time: {end_time - start_time}")

if __name__ == '__main__':
    main()
