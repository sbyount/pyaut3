from pprint import pprint
import yaml

'''
2a. Create a list where each of the list elements is a dictionary representing
one of the network devices in the lab. Do this for at least four of the lab devices.
The dictionary should have keys corresponding to the device_name, host (i.e. FQDN),
username, and password. Use a fictional username/password to avoid checking the
lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use
expanded YAML format. How could you re-use this YAML file later when creating
Netmiko connections to devices?

'''

cisco3 = {"device_name": "cisco3", "host_name": "cisco3.lasthop.io"}
cisco4 = {"device_name": "cisco4", "host_name": "cisco4.lasthop.io"}
nxos1 = {"device_name": "nxos1", "host_name": "nxos1.lasthop.io"}
nxos2 = {"device_name": "nxos2", "host_name": "nxos2.lasthop.io"}

device_list = [cisco3, cisco4, nxos1, nxos2]

for device in device_list:
    device["username"] = "admin"
    device["password"] = "cisco123"
print()
pprint(device_list)
print()

yaml_file = 'my_devices.yml'
with open(yaml_file, "w") as f:
        f.write(yaml.dump(device_list, default_flow_style=False))
