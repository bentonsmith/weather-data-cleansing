import sys
import os
from cols import removeNames, removeColumns
from aggregate import removeAggregate
from scramble import addErrors
from usage import usage


if len(sys.argv) <= 1:
    usage()
elif sys.argv[1] == "prepareFile":
    removeAggregate(sys.argv[2], "temp1.csv")
    removeNames("temp1.csv", "temp2.csv")
    removeColumns("temp2.csv", sys.argv[3])
    os.remove("temp1.csv")
    os.remove("temp2.csv")
elif sys.argv[1] == "addErrors":
    addErrors(sys.argv[2])
else:
    usage()
    print(sys.argv)
