Value INTERFACE_NAME (\S+)
Value LINE_STATUS ((up|down))
Value ADMIN_STATE ((up|down))
# Value MAC_ADDR ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})
Value MAC_ADDR (\S+)
Value MTU (\d+)
Value DUPLEX ((full|half)-duplex)
Value SPEED (\d+)

Start
  ^${INTERFACE_NAME} is ${LINE_STATUS}$$
  ^admin state is ${ADMIN_STATE},
  # 2 spaces prepend next section
  ^  Hardware:.*address: ${MAC_ADDR}\s
  ^  MTU ${MTU} bytes
  ^  ${DUPLEX}, ${SPEED} Mb/s -> Record

# 3. Using the 'show interface Ethernet2/1' output from nxos1 (see link below),
# extract the interface name, line status, admin state, MAC address, MTU, duplex,
# and speed using TextFSM.
