def removeNames(file):

    REMOVE_LIST = ['STATION', 'REPORTTPYE', 'HOURLYPRSENTWEATHERTYPE',
                  'HOURLYDRYBULBTEMPC', 'HOURLYWETBULBTEMPC', 'HOURLYDewPointTempC',
                  'HOURLYWindGustSpeed', 'HOURLYStationPressure', 'HOURLYPressureTendency',
                  'HOURLYPressureChange', 'HOURLYSeaLevelPressure', 'HOURLYAltimeterSetting']

    indexList = []

    f = open(file)

    header = f.readline().split(",")

    for element in REMOVE_LIST:
        indexList.append(header.index(element))

    newHeader = []

    for index in range(len(header)):
        if index not in indexList:
            newHeader.append(header[index])
    print(",".join(newHeader), end="")

    for line in f:
        tmpLine = []
        newLine = line.split(",")
        for index in range(len(newLine)):
            if index not in indexList:
                tmpLine.append(newLine[index])
        print(",".join(tmpLine), end="")

    f.close()

def removeColumns(file):
    LAST_COLUMN = "HOURLYPrecip"

    f = open(file)

    header = f.readline().split(",")

    removeIndex = header.index(LAST_COLUMN)

    print(",".join(header[:removeIndex + 1]))

    for line in f:
        splitLine = line.split(",")

        print(",".join(splitLine[:removeIndex + 1]))

