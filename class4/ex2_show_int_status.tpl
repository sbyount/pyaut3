Value PORT_NAME (\S+)
Value STATUS (\S+)
Value VLAN (\d+)
Value DUPLEX (\S+)
Value SPEED (\S+)
Value PORT_TYPE (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntTbl

ShowIntTbl
  ^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${PORT_TYPE}$$ -> Record

#  2. Expand the TextFSM template created in exercise1 such that you extract the
#  Port, Status, Vlan, Duplex, Speed, and Type columns. For the purposes of this
#  exercise you can ignore the 'Name' column and assume it will always be empty.
#  The output of the FSM table should look similar to the following:
