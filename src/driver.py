import sys
from cols import removeNames
from aggregate import removeAggregate

if sys.argv[1] == "remove":
    removeNames(sys.argv[2])
elif sys.argv[1] == "removeAggregate":
    removeAggregate(sys.argv[2])
