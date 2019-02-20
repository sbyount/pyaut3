Value MAC_ADDR (\S+)
Value ADDRESS (\S+)
Value NAME (\S+)
Value INTERFACE (\S+)

Start
  ^MAC.*Flags.*$$ -> ArpTable

ArpTable
  ^${MAC_ADDR}\s+${ADDRESS}\s+${NAME}\s+${INTERFACE}\s* -> Record

# 4. Use TextFSM to parse the 'show arp' output from a Juniper SRX
# (see link below). Extract the following fields into tabular data:
# MAC Address, Address, Name, Interface.'''
