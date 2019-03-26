import xmltodict
from pprint import pprint as pp
'''
2. xmltodict basics

2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary.
Print out this new variable and its type. Note, the newly created object is an
OrderedDict; not a traditional dictionary.


2b. Print the names and an index number of each security zone in the XML data
from Exercise 2a. Your output should look similar to the following (tip, enumerate
will probably help):
Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host
'''

# Using a context manager read in the XML file
with open("show_security_zones.xml", "r") as infile:
    # Parse string using xmltodict.parse
    show_security_zones = xmltodict.parse(infile.read())

# 2A
pp('Type is:')
pp(type(show_security_zones))
pp(show_security_zones)
print()

# 2B
zones = show_security_zones["zones-information"]["zones-security"]
# for zone in zones:
#     name = zone['zones-security-zonename']
#     pp(zone)
#     pp([zone])
for index, zone in enumerate(zones):
    print(f"Security Zone #{index + 1}: {zone['zones-security-zonename']}")
print("\n\n")
