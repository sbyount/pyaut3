from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree
from pprint import pprint as pp

# Disable Self-signed Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

'''
7. NX-API using XML and the nxapi_plumbing library

7a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be
"xml" and the transport should be "https" (port 8443). Use getpass() to capture
the device's password. Send the "show interface Ethernet2/1" command to the device,
parse the output, and print out the following information:

Interface: Ethernet2/1; State: up; MTU: 1500


7b. Run the following two show commands on the nxos1 device using a single method
and passing in a list of commands: "show system uptime" and "show system resources".
Print the XML output from these two commands.


7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on
nxos1 including interface descriptions. Pick random loopback interface numbers
between 100 and 199.
'''
device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

intf_output = device.show("show interface Ethernet2/1")

print('7a')
print(f'Interface: {intf_output.find(".//interface").text}')
print(f'State: {intf_output.find(".//state").text}')
print(f'MTU: {intf_output.find(".//eth_mtu").text}')

print('7b')
show_output = device.show_list(["show system uptime", "show system resources"])
for output in show_output:
    print(etree.tostring(output, encoding="unicode"))

commands = [
    "interface loopback151",
    "description loopback151",
    "no shutdown",
    "interface loopback152",
    "description loopback152",
    "no shutdown",
]

print('7c')
output = device.config_list(commands)
# Look at the output XML for each configuration command
for msg in output:
    print(etree.tostring(msg, encoding="unicode"))
