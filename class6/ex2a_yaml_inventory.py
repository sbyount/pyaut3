import pyeapi
import yaml
from getpass import getpass

'''
2a. Define an Arista device in an external YAML file (use arista4.lasthop.io for
the device). In your YAML file, make sure the key names exactly match the names
required for use with pyeapi and the connect() method. In other words, you should
be able to execute 'connect(**device_dict)' where device_dict was retrieved from
your YAML file. Do not store the lab password in this YAML file, instead set the
password using getpass() in your Python program. Using this Arista device
information stored in a YAML file, repeat the 'show ip arp' retrieval using
pyeapi. Once again, from this ARP table data, print out a mapping of all of the
IP addresses and their corresponding MAC addresses.
'''

# Open the yaml file and read in the devices
yaml_file = 'arista_devices.yml'
with open(yaml_file, "r") as f:
        devices = yaml.load(f)

password = getpass()

# Loop through each device, connect with passowrd and sh ip arp.
for name, device_dict in devices.items():
    device_dict["password"] = password
    connection = pyeapi.client.connect(**device_dict)
    device = pyeapi.client.Node(connection)
    output = device.enable("show ip arp")

    # Pull out the dictionary contents
    arp_list = output[0]["result"]["ipV4Neighbors"]

    # Loop through each arp entry and print out mac and ip
    print()
    print('=' * 32)
    for arp_entry in arp_list:
        mac_address = arp_entry['hwAddress']
        ip_address = arp_entry['address']
        print(f"{ip_address} --> {mac_address}")
    print('=' * 32)
    print()
