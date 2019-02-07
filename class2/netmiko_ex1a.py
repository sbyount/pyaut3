from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

#with open("my_creds.txt", "r") as f:
#    f.read(pw_input)

device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing("\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "8.8.8.8", strip_prompt=False, strip_command=False
)
output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing(
    "\n", strip_prompt=False, strip_command=False)

net_connect.disconnect()
print
print(output)
print
