from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

# with open("my_creds.txt", "r") as f:
#    f.read(pw_input)
'''

cisco4#ping
Protocol [ip]:
Target IP address: 8.8.8.8
Repeat count [5]:
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!

'''

device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command(
    "ping", expect_string=r"Protocol", strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"#", strip_prompt=False, strip_command=False
)
net_connect.disconnect()

print
print(output)
print
