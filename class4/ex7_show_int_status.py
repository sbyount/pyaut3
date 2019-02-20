from pprint import pprint
import textfsm

'''
7. Using your TextFSM template and the 'show interface status' data from
exercise2, create a Python program that uses TextFSM to parse this data.
In this Python program, read the show interface status data from a file and
process it using the TextFSM template. From this parsed-output, create a list
of dictionaries. The program output should look as follows:

$ python ex7_show_int_status.py

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
...]
'''

# Open template file
template_file = "ex2_show_int_status.tpl"
template = open(template_file)

# Open interface status text file
int_status_file = 'ex2_show_int_status.txt'
with open(int_status_file, "r") as f:
        int_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(int_data)
template.close()

# Initialize list and find header
interface_list = []
table_keys = re_table.header

for fsm_list in data:
    fsm_dict = dict(zip(table_keys, fsm_list))
    interface_list.append(fsm_dict)

print()
pprint(interface_list)
