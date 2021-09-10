import string

Alpha = []
alphabet = sorted(set(string.ascii_lowercase))


def getScrambledAlpha():
    scrambledAlpha = input("Enter your scrambled alphabet: ").lower()
    for letter in alphabet:
        if letter not in scrambledAlpha or not scrambledAlpha.isalpha():
            print("Please make sure you have entered all letters of the alphabet.")
            scrambledAlpha = input("Enter your scrambled alphabet: ").lower()
    else:
        for letter in scrambledAlpha:
            Alpha.append(letter)


def getUserPhrase():
    indices = []
    userPhrase = input("Please input the phrase you wish to scramble: ").lower()
    for letter in userPhrase:
        if letter == " ":
            indices.append(26)
        else:
            indices.append(alphabet.index(letter))
    return indices


def matchIndices(indices):
    for index in indices:
        if index == 26:
            print(" ", end="")
        else:
            print(Alpha[index], end="")


def playGame():
    answer = input("Do you wish to start scrambling? (y/n)").lower()
    getScrambledAlpha()
    while answer == "y":
        matchIndices(getUserPhrase())
        answer = input("\nDo you wish to scramble another word? (y/n)").lower()


playGame()
