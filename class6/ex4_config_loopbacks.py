import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

'''
4. Note, this exercise might be fairly challenging. Construct a new YAML file
that contains the four Arista switches. This YAML file should contain all of the
connection information need to create a pyeapi connection using the connect method.
Using this inventory information and pyeapi, create a Python script that configures
the following on the four Arista switches:

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).
The {{ intf_ip }} should be an address from the 172.31.X.X address space.
The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.
You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML
file and should be associated with each individual Arista device. For example,
here is what 'arista4' might look like in the YAML file:

​arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30

Use pyeapi to push this configuration to the four Arista switches. Use pyeapi
and "show ip interface brief" to display the IP address table after the
configuration changes have been made.
'''

def main():

    password = getpass()
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
    template_file = "loopback_intf.j2"

    yaml_out = yaml_load_devices("arista_devices_full.yml")
    my_devices = yaml_out["my_devices"] # Get the names from the yaml file

    eapi_devices = []
    for device_name in my_devices: # for each named device
        device_dict = yaml_out[device_name] # get the dictionary for each device
        device_dict["password"] = password # add the password

        # Generate config from template
        j2_vars = device_dict.pop("data") # pop off the data sub dictionary
        template = env.get_template(template_file) # open the .j2 template
        cfg_lines = template.render(**j2_vars) # render the device config
        cfg_lines = cfg_lines.strip() # strip off any whitespace
        cfg_lines = cfg_lines.splitlines() # split into lines

        # Establish eAP connection and push config
        eapi_conn = pyeapi.client.connect(**device_dict)
        device_obj = pyeapi.client.Node(eapi_conn)
        eapi_devices.append(device_obj) # keep track of the devices
        output = device_obj.config(cfg_lines) # push the config
        print(output)

    # Verify interfaces
    for device_obj in eapi_devices: # for each switch
        output = device_obj.enable("show ip interface brief")
        print()
        print("-" * 50)
        print(output[0]["result"]["output"].rstrip())
        print("-" * 50)
    print()

if __name__ == "__main__":
    main()
