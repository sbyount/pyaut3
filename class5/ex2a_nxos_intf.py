from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

'''
2a. Use Python and Jinja2 to generate the below NX-OS interface configuration.
You should use an external template file and a Jinja2 environment to accomplish
this. The interface, ip_address, and netmask should all be variables in the
Jinja2 template.

nxos1
interface Ethernet2/1
  ip address 10.1.100.1/24

nxos2
interface Ethernet2/1
  ip address 10.1.100.2/24
 '''

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

interface = "Ethernet2/1"
nxos1 = {"interface": interface, "ipv4_address": "10.1.100.1", "ipv4_netmask": "24"}
nxos2 = {"interface": interface, "ipv4_address": "10.1.100.2", "ipv4_netmask": "24"}

template_file = "nxos_ipv4_intf.j2"
template = env.get_template(template_file)

for j2vars in (nxos1, nxos2):
    output = template.render(**j2vars)
    print(output)
print()
