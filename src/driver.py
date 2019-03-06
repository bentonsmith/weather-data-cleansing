import sys
from cols import removeNames, removeColumns
from aggregate import removeAggregate
from scramble import addErrors
from usage import usage


if len(sys.argv) <= 1:
    usage()
elif sys.argv[1] == "removeAggregate":
    removeAggregate(sys.argv[2])
elif sys.argv[1] == "prepare":
    removeNames(sys.argv[2])
elif sys.argv[1] == "removeColumns":
    removeColumns(sys.argv[2])
elif sys.argv[1] == "addErrors":
    addErrors(sys.argv[2])
else:
    usage()
