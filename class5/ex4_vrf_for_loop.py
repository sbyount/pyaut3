from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

'''
4. Expand on exercise3 except use a for-loop to configure five VRFs. Each VRF
should have a unique name and a unique route distinguisher. Each VRF should once
again have the IPv4 and the IPv6 address families controlled by a conditional-variable
passed into the template.

Note, you will want to pass in a list or dictionary of VRFs that you loop over
in your Jinja2 template.
'''

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])

# List of dictionarys for each iteration
my_vrfs = [
    {"vrf_name": "mars", "rd_number": "64800:001", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "jupiter", "rd_number": "64800:002", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "neptune", "rd_number": "64800:003", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "saturn", "rd_number": "64800:004", "ipv4_af": True, "ipv6_af": True},
    {"vrf_name": "mercury", "rd_number": "64800:005", "ipv4_af": True, "ipv6_af": True},
]

# Put entire list into a string to render
my_vars = {"my_vrfs": my_vrfs}

template_file = "ios_vrf_for_loop.j2"
template = env.get_template(template_file)
output = template.render(**my_vars)

print(output)
