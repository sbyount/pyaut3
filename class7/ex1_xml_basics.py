from lxml import etree

'''
1a. Using the show_security_zones.xml file, read the file contents and parse the
file using etree.fromstring(). Print out the newly created XML variable and also
print out the variable's type. Your output should look similar to the following:
​<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>

1b. Using your XML variable from exercise 1a, print out the entire XML tree in a
readable format (ensure that the output string is a unicode string).

1c. Print out the root element tag name (this tag should have a value of
"zones-information"). Print the number of child elements of the root element
(you can retrieve this using the len() function).


1d. Using both direct indices and the getchildren() method, obtain the first
child element and print its tag name.


1e. Create a variable named "trust_zone". Assign this variable to be the first
"zones-security" element in the XML tree. Access this newly created variable and
print out the text of the "zones-security-zonename" child.


1f. Iterate through all of the child elements of the "trust_zone" variable. Print
out the tag name for each child element.
'''

# Using a context manager read in the XML file
with open("show_security_zones.xml", "r") as infile:
    # Parse string using etree.fromstring
    show_security_zones = etree.fromstring(infile.read())

# Exercise 1A
print()
print("1A: Print type and object")
print(type(show_security_zones))
print(show_security_zones)

# Exercies 1B
print()
print("1B: Print the tree")
print(etree.tostring(show_security_zones).decode())

# Exercies 1C
print()
print("1C: Print the root tag and number of children")
print(show_security_zones.tag)
print(len(show_security_zones))

# Exercies 1D
print()
print("1D: Print the first child element")
print(show_security_zones[0].tag)
print(show_security_zones.getchildren()[0].tag)

# Exercies 1E
print()
print("1E: Print the first child element text")
trust_zone = show_security_zones[0]
print(trust_zone[0].text)

# Exercies 1F
print()
print("1F: Print out the zones:")
for child in trust_zone:
    print(f"{child.tag}: {child.text}")
