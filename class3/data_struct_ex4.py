import json
import yaml
from pprint import pprint

'''
4. You have the following JSON ARP data from an Arista switch:

>arp_data.json

From a file, read this JSON data into your Python program. Process this ARP
data and return a dictionary where the dictionary keys are the IP addresses
and the dictionary values are the MAC addresses. Print this dictionary to
standard output.
'''

json_file = 'arp_data.json'
with open(json_file) as f:
        arp_data = json.load(f)

arp_dict = {}
arp_entries = arp_data["ipV4Neighbors"]

for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    intf = entry["interface"]
    arp_dict[ip_addr] = mac_addr, intf

yaml_file = 'arp_data.yml'
with open(yaml_file, "w") as f:
        f.write(yaml.dump(arp_dict, default_flow_style=False))

print()
pprint(arp_dict)
print()
