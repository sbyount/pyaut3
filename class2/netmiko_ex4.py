from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

'''
4. Use Netmiko and the send_config_set() method to configure the following on
the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute
(with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping google.com'.
Verify from this that you receive a ping response back.
'''

device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "fast_cli": True,
}

net_connect = ConnectHandler(**device)
start_time = datetime.now()
output = net_connect.send_config_from_file(config_file="config_set.txt")
output += net_connect.send_command("ping google.com")
end_time = datetime.now()
print(output)
print("\nExecution Time: {}".format(end_time - start_time))

net_connect.disconnect()
