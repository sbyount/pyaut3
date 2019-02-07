from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)

print("Current Prompt: ")
print(net_connect.find_prompt())
print("\n")

print("Config Prompt: ")
net_connect.config_mode()
print(net_connect.find_prompt())
print("\n")

print("Current Prompt: ")
net_connect.exit_config_mode()
print(net_connect.find_prompt())
print("\n")

print("User mode prompt: ")
net_connect.write_channel("disable\n")
time.sleep(2)
output = net_connect.read_channel()
print(output)
print("\n")

print("Privilaged mode prompt: ")
net_connect.enable()
print(net_connect.find_prompt())
print("\n")
