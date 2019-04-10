from my_devices import network_devices as devices
from netmiko import ConnectHandler
from datetime import datetime


'''
1a. As you have done in previous classes, create a Python file named "my_devices.py".
In this file, define the connection information for: 'cisco3', 'arista1', 'arista2',
and 'srx2'. This file should contain all the necessary information to create a
Netmiko connection. Use getpass() for the password handling. Use a global_delay_factor
of 4 for both the arista1 device and the arista2 device. This Python module should
be used to store the connection information for all of the exercises in this lesson.

1b. Create a Python script that executes "show version" on each of the network
devices defined in my_devices.py. This script should execute serially i.e. one
SSH connection after the other. Record the total execution time for the script.
Print the "show version" output and the total execution time to standard output.
As part of this exercise, you should create a function that both establishes a
Netmiko connection and that executes a single show command that you pass in as
argument. This function's arguments should be the Netmiko device dictionary and
the "show-command" argument. The function should return the result from the show
command.
'''

def ssh_command(device, command):
    """Establish an SSH connection. Execute command, return results."""
    device = ConnectHandler(**device)
    output = device.send_command(command)
    device.disconnect()
    return output

def main():
    '''1b Interate through the list of devices and send the show version cmd '''
    start_time = datetime.now()
    for device in devices:
        output = ssh_command(device, 'show version')
        print('*' * 20 + device['host'] + '*' * 20)
        print(output)
        print('#' * 60)
    end_time = datetime.now()
    print(f'Total time: {end_time - start_time}')

if __name__ == "__main__":
    main()
