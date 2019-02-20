def removeAggregate(file):
    REMOVE_LIST = ['DAILYMaximumDryBulbTemp', 'MonthlyMaximumTemp']

    indexList = []

    f = open(file)

    header = f.readline().split(",")

    for element in REMOVE_LIST:
        indexList.append(header.index(element))

    print(",".join(header), end="")

    for line in f:
        newLine = line.split(",")
        keepLine = True
        for i in indexList:
            if newLine[i] != '':
                keepLine = False
        if keepLine:
            print(",".join(newLine), end="")

    f.close()
