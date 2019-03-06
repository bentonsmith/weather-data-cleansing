def removeAggregate(file):
    DAILY_COL = "REPORTTPYE"

    f = open(file)

    header = f.readline().split(",")

    dailyIndex = header.index(DAILY_COL)

    print(",".join(header), end="")

    for line in f:
        newLine = line.split(",")
        keepLine = True
        if newLine[dailyIndex] == "SOD":
            keepLine = False
        if keepLine:
            print(",".join(newLine), end="")

    f.close()
