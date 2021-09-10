def getNumbers():
    numbersList = []
    count = 0
    howMany = int(input("How many numbers would you like to compare? "))
    while count < howMany:
        numbersList.append(input("Enter a number: "))
        count = count + 1
    numbersList.sort()
    print(numbersList)


def scanNumbers(numbersList):
    maximum = numbersList[0]
    minimum = numbersList[-1]
    print("The maximum number was", maximum)
    print("The minimum number was", minimum)


def playGame():
    scanNumbers(getNumbers())


getNumbers()