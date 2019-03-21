import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices, output_printer

'''
Create a new Python program based
on exercise2a except the YAML file loading and the output printing is accomplished
using the functions defined in my_funcs.py.
'''

def main():

    devices = yaml_load_devices()
    password = getpass()

    # Loop through each device, connect with passowrd and sh ip arp.
    for name, device_dict in devices.items():
        device_dict["password"] = password # add the password to device_dict
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip arp")
        # Pull out the dictionary contents
        arp_list = output[0]["result"]["ipV4Neighbors"]
        output_printer(name, arp_list)

if __name__ == "__main__":
    main()
