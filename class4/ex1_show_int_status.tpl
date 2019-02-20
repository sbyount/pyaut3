Value PORT_NAME (\S+)

Start
  ^Port.*Type\s*$$ -> ShowIntTbl

ShowIntTbl
  ^${PORT_NAME} -> Record
