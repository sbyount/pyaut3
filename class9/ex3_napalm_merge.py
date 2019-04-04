from my_devices import network_devices
from my_functions import open_napalm_connection
from pprint import pprint as pp

'''
3. NAPALM Config Merge

3a. Using your existing functions and the my_devices.py file, create a NAPALM
connection to both cisco3 and arista1.

3b. Create two new text files `arista1.lasthop.io-loopbacks` and
`cisco3.lasthop.io-loopbacks`. In each of these files, create two new loopback
interfaces with a description. Your files should be similar to the following:

interface loopback100
  description loopback100
!
interface loopback101
  description loopback101

For both cisco3 and arista1, use the load_merge_candidate() method to stage the
candidate configuration. In other words, use load_merge_candidate() and your
loopback configuration file to stage a configuration change. Use the NAPALM
compare_config() method to print out the pending differences (i.e. the
differences between the running configuration and the candidate configuration).

3c. Commit the pending changes to each device, and check the diff once again
(after the commit_config).
'''
# 3a
if __name__ == "__main__":
    connections = []
    for device in network_devices:
        conn = open_napalm_connection(device)
        connections.append(conn)
# 3b
    for conn in connections:
        conn.load_merge_candidate(filename="{}-loopbacks.txt".format(conn.hostname))
        # conn.load_merge_candidate(filename="f{conn.hostname}-loopbacks.txt")
        diff = conn.compare_config()
        print(diff)
        if diff:
            conn.commit_config()
        diff = conn.compare_config()
        print(diff)
        conn.close()
