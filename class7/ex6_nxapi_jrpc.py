from getpass import getpass
from nxapi_plumbing import Device
from pprint import pprint as pp

# Disable Self-signed Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

'''
6. NX-API using json-rpc and the nxapi_plumbing library

6a. Create an nxapi_plumbing "Device" object for nxos1. The api_format should be
"jsonrpc" and the transport should be "https" (port 8443). Use getpass() to
capture the device's password. Send the "show interface Ethernet2/1" command to
the device, parse the output, and print out the following information:

Interface: Ethernet2/1; State: up; MTU: 1500
'''

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

intf_output = device.show("show interface Ethernet2/1")
intf_output = intf_output["TABLE_interface"]["ROW_interface"]

print(f'Interface: {intf_output["interface"]}')
print(f'State: {intf_output["state"]}')
print(f'MTU: {intf_output["eth_mtu"]}')
