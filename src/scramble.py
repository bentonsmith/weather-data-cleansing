import random

FILE_LENGTH = 115_000


def addErrors(file):
    f = open(file)

    header = f.readline().split(",")

    print(",".join(header), end="")

    randomErrors = [random.randint(1, FILE_LENGTH) for i in range(20)]

    lineCounter = 0

    for line in f:
        lineCounter += 1
        if lineCounter in randomErrors:
            changeLine = line.split(",")
            errorNumber = random.randint(1, 5)
            printLine = ",".join(makeError(errorNumber, changeLine, header))
            print(printLine, end="")
        else:
            print(line, end="")


def makeError(errorNumber, line, header):
    errorLine = line
    if errorNumber == 1:
        column = header.index("HOURLYDRYBULBTEMPF")
        errorLine[column] = str(random.randint(500, 1_000))
        return errorLine
    elif errorNumber == 2:
        column = header.index("HOURLYRelativeHumidity")
        errorLine[column] = str(random.randint(500, 1_000))
        return errorLine
    elif errorNumber == 3:
        column = header.index("ELEVATION")
        errorLine[column] = str(random.randint(2_000, 30_000))
        return errorLine
    elif errorNumber == 4:
        column = header.index("LATITUDE")
        errorLine[column] = str(random.randint(50, 100))
        return errorLine
    elif errorNumber == 5:
        column = header.index("LONGITUDE")
        errorLine[column] = str(random.randint(1, 100))
        return errorLine
