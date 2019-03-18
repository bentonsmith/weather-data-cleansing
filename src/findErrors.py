def findErrors(file):
    f = open(file)

    header = f.readline().split(",")

    for element in range(len(header)):
        print(str(element + 1) + ") " + header[element])

    valid = False

    while not valid:
        column = input("Enter the column you would like to clean: ")
        if column.isdigit():
            column = int(column) - 1
            valid = True
        else:
            print("Please enter a valid integer.")

    valid = False
    print("You have selected the " + header[column] + " column.")
    while not valid:
        maxVal = input("Enter the maximum acceptable value: ")
        try:
            maxVal = float(maxVal)
            valid = True
        except ValueError:
            print("Please enter a valid number.")
            continue

    valid = False
    while not valid:
        minVal = input("Enter the minimum acceptable value: ")
        try:
            minVal = float(minVal)
            valid = True
        except ValueError:
            print("Please enter a valid number.")
            continue


    lineNumber = 0
    for line in f:
        lineNumber += 1

        newLine = line.split(",")
        checkItem = newLine[column]

        try:
            checkItem = float(checkItem)
        except ValueError:
            continue

        if minVal <= checkItem <= maxVal:
            continue
        else:
            print("\n\nError found on line: " + str(lineNumber))
            print("The item has a value of " + str(checkItem))
