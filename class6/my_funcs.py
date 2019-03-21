import yaml

'''
2b. Create a Python module named 'my_funcs.py'. In this file create two functions:
function1 should read the YAML file you created in exercise 2a and return the
corresponding data structure; function2 should handle the output printing of the
ARP entries (in other words, create a separate function that handles all printing
to standard out of the 'show ip arp' data).

'''

def yaml_load_devices(filename="arista_devices.yml"):
    # Open the yaml file and read in the devices
    with open(filename, "r") as f:
        return yaml.load(f)

def output_printer(name, arp_list):
        # Loop through each arp entry and print out mac and ip
        print()
        print('=' * 11, name, '=' * 11)
        #print('=' * 32)
        for arp_entry in arp_list:
            mac_address = arp_entry['hwAddress']
            ip_address = arp_entry['address']
            print(f"{ip_address} --> {mac_address}")
        print('=' * 32)
        print()
