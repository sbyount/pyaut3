from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from my_devices import network_devices as devices
from my_functions import ssh_command2

'''
5. Using a context manager and a 'ProcessPoolExecutor', complete the same task
as Exercise 4.
'''

def main():
    start_time = datetime.now()
    max_procs = 5

    with ProcessPoolExecutor(max_procs) as pool:
        future_list = []
        for device in devices:
            future_list.append(pool.submit(ssh_command2, device, "show version"))

        for future in as_completed(future_list):
            print("Result: " + future.result())
            end_time = datetime.now()
            print(f"Total time: {end_time - start_time}")

if __name__ == '__main__':
    main()
