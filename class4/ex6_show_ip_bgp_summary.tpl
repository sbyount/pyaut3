Value Filldown ROUTER_ID ([0-9\.]+)
Value Filldown LOCAL_AS (\d+)
Value NEIGHBOR ([0-9\.]+)
Value REMOTE_AS (\d+)
Value UP_DOWN (\S+)
Value STATE_PREFIX (\S+)


Start
  ^BGP router identifier ${ROUTER_ID}, local AS number ${LOCAL_AS}\s*$$ -> HeaderRow

HeaderRow
  ^Neighbor.*State/PfxRcd$$ -> BGPTable

BGPTable
  ^${NEIGHBOR}\s+\d\s+${REMOTE_AS}\s+\d*\s+\d*\s+\d*\s+\d*\s+\d*\s+${UP_DOWN}\s+${STATE_PREFIX} -> Record

EOF

#6. Parse the following 'show ip bgp summary' output (see link below). From this
#output, extract the following fields: Neighbor, Remote AS, Up_Down, and
#State_PrefixRcvd. Also include the Local AS and the BGP Router ID in each row
#of the tabular output (hint: use filldown for this). Note, in order to simplify
#this problem only worry about the data shown in the output (in other words,
#don't worry about all possible values that could be present in the output).

#Second hint: remember there is an implicit 'EOF -> Record' at the end of the
#template (by default).
