from getpass import getpass
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

'''
6. Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration
into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address.
Print out the interface name and IP address for each interface. Your solution should
work if there is more than one IP address configured on Cisco4. For example, if
you configure a loopback interface on Cisco4 with an IP address, then your solution
should continue to work. The output from this program should look similar to the
following:

$ python confparse_ex6.py

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
'''
password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device)

show_run = net_connect.send_command("show run")
net_connect.disconnect()
cisco_cfg = CiscoConfParse(show_run.splitlines())

interfaces = cisco_cfg.find_objects_w_child(parentspec=r"^interface",
    childspec=r"^\s+ip address")

print()
for intf in interfaces:
    print("Interface: {}".format(intf.text))
    ip_address = intf.re_search_children(r"ip address")[0].text
    print("IP Address: {}".format(ip_address))
    print()
print()
