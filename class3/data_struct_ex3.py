import json
from pprint import pprint

'''
3. NAPALM using nxos_ssh has the following data structure in one of its unit
tests (the below data is in JSON format).

> napalm_data.json

Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are used
on this NXOS device. From this data create two lists: 'ipv4_list' and 'ipv6_list'.

The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes;
the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.

'''
json_file = 'napalm_data.json'
with open(json_file) as f:
        json_data = json.load(f)

ipv4_list = []
ipv6_list = []

for intf, ipaddr_dict in json_data.items():
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict["prefix_length"]
            if ipv4_or_ipv6 == "ipv4":
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
            elif ipv4_or_ipv6 == "ipv6":
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))
