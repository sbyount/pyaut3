from netmiko import ConnectHandler
from getpass import getpass

with open("my_creds.txt", "r") as f:
    f.read(pw_input)

device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": pw_input,
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command_timing(
    "ping", strip_prompt=False, strip_command=False
