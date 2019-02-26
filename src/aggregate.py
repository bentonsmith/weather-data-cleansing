def removeAggregate(file):
    #  REMOVE_LIST = ['DAILYMaximumDryBulbTemp', 'MonthlyMaximumTemp']
    DAILY_COL = "REPORTTPYE"

    #  indexList = []

    f = open(file)

    header = f.readline().split(",")

    dailyIndex = header.index(DAILY_COL)

    # for element in REMOVE_LIST:
    #     indexList.append(header.index(element))

    print(",".join(header), end="")

    for line in f:
        newLine = line.split(",")
        keepLine = True
        if newLine[dailyIndex] == "SOD":
            keepLine = False
        # for i in indexList:
        #     if newLine[i] != '' or newLine[dailyIndex] == "SOD":
        #         keepLine = False
        if keepLine:
            print(",".join(newLine), end="")

    f.close()
