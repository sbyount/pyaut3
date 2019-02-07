from netmiko import ConnectHandler
from getpass import getpass

'''
5. On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN
names (just pick 5 VLAN numbers between 100 - 999). Use Netmiko's send_config_from_file()
method to accomplish this. Also use Netmiko's save_config() method to save the
changes to the startup-config.
'''

password = getpass()

routers = ["nxos1.lasthop.io", "nxos2.lasthop.io"]
for router in routers:
    device = {
        "device_type": "cisco_nxos",
        "host": router,
        "username": "pyclass",
        "password": password,
        "fast_cli": True,
        }
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file("config_set2.txt")
    net_connect.save_config()
    print(output)
    print("*" * 40)

net_connect.disconnect()
