def removeAggregate(file, destination):
    DAILY_COL = "REPORTTPYE"

    f = open(file)
    f2 = open(destination, "w")

    header = f.readline().split(",")

    dailyIndex = header.index(DAILY_COL)

    print(",".join(header), end="", file=f2)

    for line in f:
        newLine = line.split(",")
        keepLine = True
        if newLine[dailyIndex] == "SOD":
            keepLine = False
        if keepLine:
            print(",".join(newLine), end="", file=f2)

    f.close()
    f2.close()
