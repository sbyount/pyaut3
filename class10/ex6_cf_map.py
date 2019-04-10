from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from my_devices import network_devices as devices
from my_functions import ssh_command2
'''
6. Using a context manager, the ProcessPoolExecutor, and the map() method, create
a solution that executes "show ip arp" on all of the devices defined in my_devices.py.
Note, the Juniper device will require "show arp" instead of "show ip arp" so your
solution will have to properly account for this.
'''

def main():
    start_time = datetime.now()
    max_procs = 5

    with ProcessPoolExecutor(max_procs) as pool:
        cmd_list = []
        for device in devices:
            if device["device_type"] == "juniper_junos":
                cmd_list.append('sh arp')
            else:
                cmd_list.append('sh ip arp')
        results = pool.map(ssh_command2, devices, cmd_list)

        # Results generator
        for result in results:
            print('_'*80)
            print(result)
            print('*-'*40)


        end_time = datetime.now()
        print(end_time - start_time)

if __name__ == '__main__':
    main()
