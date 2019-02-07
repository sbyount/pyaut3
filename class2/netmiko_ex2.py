from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

'''

2. Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2.
Execute 'show lldp neighbors detail' and print the returned output to standard outputself.
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor
of 8.  Print the output of this command to standard output.
Use the Python datetime library to record the execution time of both of these commands.
Print these execution times to standard output.

'''

password = getpass()

device = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device)

cmd = "show lldp neighbors detail"
start_time = datetime.now()
output = net_connect.send_command(cmd)
end_time = datetime.now()

print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

cmd = "show lldp neighbors detail"
start_time = datetime.now()
output = net_connect.send_command(cmd, delay_factor=8)
net_connect.disconnect()
end_time = datetime.now()

print("#" * 80)
print(output)
print("#" * 80)
print("\nExecution Time: {}".format(end_time - start_time))
print()
