from napalm import get_network_driver
from my_devices import network_devices
from pprint import pprint as pp

'''
1. Simple NAPALM Connections and Facts

1a. Create a Python file named "my_devices.py" that defines the NAPALM connection
information for both the 'cisco3' device and the 'arista1' device. Use getpass()
for the password handling. This Python module should be used to store the device
connection information for all of the exercises in this lesson.

1b. Create a simple function that accepts the NAPALM device information from the
my_devices.py file and creates a NAPALM connection object. This function should
open the NAPALM connection to the device and should return the NAPALM connection
object.

1c. Using your "my_devices.py" file and your NAPALM connection function, create
a list of NAPALM connection objects to 'cisco3' and 'arista1'.

1d. Iterate through the connection objects, print out the device's connection
object itself. Additionally, pretty print the facts for each device and also
print out the device's NAPALM platform type (ios, eos, et cetera).

'''

# 1b
def open_napalm_connection(device):
    """Funtion to open napalm connection and return connection object"""
    # Copy dictionary to ensure original object is not modified
    device = device.copy()
    # Pop "platform" as this is an invalid kwarg to napalm
    platform = device.pop("platform")
    driver = get_network_driver(platform)
    conn = driver(**device)
    conn.open()
    return conn

if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)

    for conn in connections:
        print(f"Connection Object: {conn}")
        print()
        print(f"Platform type: {conn.platform}")
        print("Facts:")
        pp(conn.get_facts())
        print()

        # Close the NAPALM connection
        conn.close()
