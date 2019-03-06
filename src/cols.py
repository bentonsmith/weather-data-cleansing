def removeNames(file, destination):

    REMOVE_LIST = ['STATION', 'REPORTTPYE', 'HOURLYPRSENTWEATHERTYPE',
                  'HOURLYDRYBULBTEMPC', 'HOURLYWETBULBTEMPC', 'HOURLYDewPointTempC',
                  'HOURLYWindGustSpeed', 'HOURLYStationPressure', 'HOURLYPressureTendency',
                  'HOURLYPressureChange', 'HOURLYSeaLevelPressure', 'HOURLYAltimeterSetting']

    indexList = []

    f = open(file)
    f2 = open(destination, "w")

    header = f.readline().split(",")

    for element in REMOVE_LIST:
        indexList.append(header.index(element))

    newHeader = []

    for index in range(len(header)):
        if index not in indexList:
            newHeader.append(header[index])
    print(",".join(newHeader), end="", file=f2)

    for line in f:
        tmpLine = []
        newLine = line.split(",")
        for index in range(len(newLine)):
            if index not in indexList:
                tmpLine.append(newLine[index])
        print(",".join(tmpLine), end="", file=f2)

    f.close()
    f2.close()

def removeColumns(file, destination):
    LAST_COLUMN = "HOURLYPrecip"

    f = open(file)
    f2 = open(destination, "w")

    header = f.readline().split(",")

    removeIndex = header.index(LAST_COLUMN)

    print(",".join(header[:removeIndex + 1]), file=f2)

    for line in f:
        splitLine = line.split(",")

        print(",".join(splitLine[:removeIndex + 1]), file=f2)

    f.close()
    f2.close()
