from my_devices import network_devices
from my_functions import open_napalm_connection, create_backup
from pprint import pprint as pp

'''
2. NAPALM Getters

2a. Create a new file named "my_functions.py" that will store a set of reusable
functions. Move the "open_napalm_connection" function from exercise1 into this
Python file. Import the network devices once again from my_devices.py and create
a list of connection objects (once again with connections to both cisco3 and
arista1).

2b. Pretty print the arp table for each of these devices. Gather this information
 using the appropriate NAPALM Getter.

2c. Attempt to use the get_ntp_peers() method against both of the devices. Does
this method work? Your code should gracefully handle any exceptions that occur.
In other words, an exception that occurs due to this get_ntp_peers() method,
should not cause the program to crash.

2d. Create another function in "my_functions.py". This function should be named
"create_backup" and should accept a NAPALM connection object as an argument.
Using the NAPALM get_config() method, the function should retrieve and write
the current running configuration to a file. The filename should be unique for
each device. In other words, "cisco3" and "arista1" should each have a separate
file that stores their running configuration. Note, get_config() returns a
dictionary where the running-config is referenced using the "running" key.
'''

# 2a
if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)
    # # 2b
    # for conn in connections:
    #     hostname = conn.get_facts()["hostname"]
    #     arp_table = conn.get_arp_table()
    #     print(f"----{hostname}----")
    #     pp(arp_table)

    # # 2c
    # for conn in connections:
    #     try:
    #         pp(conn.get_ntp_peers())
    #     except NotImplementedError:
    #         print(f"NTP Peers Getter not implemented for device type {conn.platform}")

    # 2d
    for conn in connections:
        create_backup(conn)
