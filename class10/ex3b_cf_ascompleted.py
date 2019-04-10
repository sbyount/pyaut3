from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from my_devices import network_devices as devices
from my_functions import ssh_command2

'''
3b. Instead of waiting for all of the futures to complete, use "as_completed" to
print the future results as they come available. Reuse your "ssh_command2"
function to accomplish this. Once again use the concurrent futures
"ThreadPoolExecutor" and print the "show version" results to standard output.
Additionally, print the total execution time to standard output.
'''

def main():
    start_time = datetime.now()
    max_threads = 5

    # Create the thread pool
    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for device in devices:
        future_list.append(pool.submit(ssh_command2, device, "show version"))

    for future in as_completed(future_list):
        print("Result: " + future.result())

    end_time = datetime.now()
    print(f"Total time: {end_time - start_time}")

if __name__ == '__main__':
    main()
