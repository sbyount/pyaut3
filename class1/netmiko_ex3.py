from netmiko import ConnectHandler
from getpass import getpass

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    "device_type": "cisco_nxos",
}

net_connect = ConnectHandler(**nxos1)

output = net_connect.send_command("sh version")

with open("show_ver.txt", "w") as f:
    f.write(output)

# Close file per Kirk
net_connect.disconnect()
