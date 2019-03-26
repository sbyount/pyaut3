import xmltodict
from pprint import pprint as pp
'''
3a. Open the following two XML files: show_security_zones.xml and
show_security_zones_single_trust.xml. Use a generic function that accepts an
argument "filename" to open and read a file. Inside this function, use xmltodict
to parse the contents of the file. Your function should return the xmltodict data
structure. Using this function, create two variables to store the xmltodict data
structure from the two files.


3b. Compare the Python "type" of the elements at ['zones-information']['zones-security'].
What is the difference between the two data types? Why?


3c. Optional - create a second function that uses xmltodict to read and parse a
filename that you pass in. This function should support a "force_list" argument
that is passed to xmltodict.parse(). Reminder, the force_list argument of xmltodict
takes a dictionary where the dictionary key-name is the XML element that is required
to be a list. For example:

force_list={"zones-security": True}

Use this new function to parse the "show_security_zones_single_trust.xml". Verify
the Python data type is now a list for the ['zones-information']['zones-security']
element.
'''
# 3A
def open_file(filename):
    with open(filename, "r") as infile:
        data = xmltodict.parse(infile.read())
    return data

file1_data = open_file('show_security_zones.xml')
file2_data = open_file('show_security_zones_trust.xml')

print(type(file1_data['zones-information']['zones-security']))
print(type(file2_data['zones-information']['zones-security']))
