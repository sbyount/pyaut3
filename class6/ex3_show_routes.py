import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices

'''
3. Using your external YAML file and your function located in my_funcs.py, use
pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". From this
routing table data, extract all of the static and connected routes from the
default VRF. Print these routes to the screen and indicate whether the route is
a connected route or a static route. In the case of a static route, print the
next hop address.

'''

def main():

    devices = yaml_load_devices()
    password = getpass()

    # Loop through each device, connect with passowrd and sh ip route.
    for name, device_dict in devices.items():
        device_dict["password"] = password # add the password to device_dict
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        # Pull out the dictionary contents
        route_list = output[0]["result"]["vrfs"]["default"]["routes"]

    for prefix, route_dict in route_list.items():
        route_type = route_dict["routeType"]
        print()
        print(prefix)
        print("-" * 12)
        print(route_type)
        print(">" * 6)
        print(route_dict["vias"][0]["interface"])
        if route_dict["routeType"] == "static":
            print(route_dict["vias"][0]["nexthopAddr"])
        print("-" * 12)
    print()

if __name__ == "__main__":
    main()
