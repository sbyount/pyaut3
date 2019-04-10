import threading
from datetime import datetime
from my_devices import network_devices as devices
from my_functions import ssh_command

'''
2. Create a new file named my_functions.py. Move your function from exercise1 to
this file. Name this function "ssh_command". Reuse functions from this file for
the rest of the exercises. Complete the same task as Exercise 1b except this time
use "legacy" threads to create a solution. Launch a separate thread for each
device's SSH connection. Print the time required to complete the task for all of
the devices. Move all of the device specific output printing to the called
function (i.e. to the child thread).
'''

def main():

    start_time = datetime.now()
    # Create list to append threads to
    threads = []
    # Loop through each device and spawn a thread to get show version
    for device in devices:
        my_thread = threading.Thread(target=ssh_command, args=(device, "show version"))
        threads.append(my_thread)
        my_thread.start()

    # Once all threads are complete, join them up and continue.
    for thread in threads:
        my_thread.join()

    end_time = datetime.now()
    print(f'Total time: {end_time - start_time}')

if __name__ == "__main__":
    main()
