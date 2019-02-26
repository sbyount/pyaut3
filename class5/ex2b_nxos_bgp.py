from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

'''
2b. Expand your Jinja2 template such that both the following interface and BGP
configurations are generated for nxos1 and nxos2. The interface name, IP address,
netmask, local_as, and peer_ip should all be variables in the template. This is
iBGP so the remote_as will be the same as the local_as.

nxos1
interface Ethernet2/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast

nxos2
interface Ethernet2/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast
 '''

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

interface = "Ethernet2/1"

nxos1 = {
    "device_name": "nxos1",
    "ibgp_as": "22",
    "interface": interface,
    "ipv4_address": "10.1.100.1",
    "ipv4_netmask": "24"
}
nxos2 = {
    "device_name": "nxos2",
    "ibgp_as": "22",
    "interface": interface,
    "ipv4_address": "10.1.100.2",
    "ipv4_netmask": "24"
}

nxos1["peer_ip"] = nxos2["ipv4_address"]
nxos2["peer_ip"] = nxos1["ipv4_address"]

template_file = "nxos_intf_bgp.j2"
template = env.get_template(template_file)

for device in (nxos1, nxos2):
    print(f" {device['device_name']} ".center(40, "-"))
    output = template.render(**device)
    print(output)
    print()
