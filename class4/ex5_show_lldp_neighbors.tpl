Value DEVICE_ID (\S+)
Value INTERFACE (\S+)
Value CAPABILITY (\S+)
Value PORT_ID (\S+)

Start
  ^Device ID.*Port ID$$ -> LLDPTable

LLDPTable
  ^${DEVICE_ID}\s+${INTERFACE}\s+\S+\s+${CAPABILITY}\s+${PORT_ID} -> Record

#5. Parse the 'show lldp neighbors' output from nxos1 (see link below). From
#this output use TextFSM to extract the Device ID, Local Intf, Capability,
#and Port ID.
