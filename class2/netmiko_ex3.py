from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

'''

Create a script using Netmiko that executes 'show version' and 'show lldp neighbors'
against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors'
(dictionary, list, string, something else)? The Cisco4 device should only have one
LLDP entry (the HPE switch that this router connects to). From this LLDP data, print out
the remote device's interface. In other words, print out the port number on the HPE
switch that Cisco4 connects into.

'''

device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command(
    "show version", use_textfsm=True
)
pprint(output)
print("#" * 80)

output = net_connect.send_command(
    "show lldp neighbors", use_textfsm=True
)
net_connect.disconnect()
pprint(output)
print("#" * 80)

print("LLDP Data Structure Type: {}".format(type(output)))
print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

#cmds = ["show version", "show lldp neighbors"]
#for cmd in cmds:
#    output = net_connect.send_command(cmd, use_textfsm=True)
#    print("#" * 80)
#    print(cmd)
#    print("#" * 80)
