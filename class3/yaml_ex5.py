import yaml
from os import path
from netmiko import ConnectHandler

'''
5. In your lab environment, there is a file located at ~/.netmiko.yml. This file
contains all of the devices used in the lab. Create a Python program that processes
this YAML file and then uses Netmiko to connect to the Cisco3 router. Print out
the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs
designed to work directly with Netmiko. The .netmiko.yml also contains group
definitions for: cisco, arista, juniper, and nxos groups. These group definitions
are lists of devices. Once again, don't check the .netmiko.yml into GitHub.

help(os.path)
    expanduser(path)
        Expand ~ and ~user constructions.  If user or $HOME is unknown,
        do nothing.
    join(a, *p)
        Join two or more pathname components, inserting '/' as needed.
        If any component is an absolute path, all previous path components
        will be discarded.  An empty last part will result in a path that
        ends with a separator.
'''
home_dir = path.expanduser("~")
yaml_file = path.join(home_dir, ".netmiko.yml")

#yaml_file = "~/.netmiko.yml"
with open(yaml_file) as f:
        lab_data = yaml.load(f)

cisco3 = lab_data["cisco3"]
net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()
