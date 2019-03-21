import pyeapi
from getpass import getpass
# from pprint import pprint

'''
1. Using the pyeapi library, connect to arista3.lasthop.io and execute
'show ip arp'. From this ARP table data, print out a mapping of all of the
IP addresses and their corresponding MAC addresses.

'''

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

arp_list = output[0]["result"]["ipV4Neighbors"]
# pprint(arp_list)

print()
print('=' * 32)
for arp_entry in arp_list:
    mac_address = arp_entry['hwAddress']
    ip_address = arp_entry['address']
    print(f"{ip_address} --> {mac_address}")
print('=' * 32)
print()
