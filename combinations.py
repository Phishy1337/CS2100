def nextCombination(n, values):
    r = len(values)

    i = r - 1
    while i >= 0 and values[i] == n - r + i + 1:
        i -= 1

    if i < 0:
        return False

    values[i] += 1
    for j in range(i + 1, r):
        values[j] = values[j - 1] + 1

    return True


def printCombinations(n, r):
    if r > n:
        return

    values = list(range(1, r + 1))
    print(", ".join(map(str, values)))

    while nextCombination(n, values):
        print(", ".join(map(str, values)))


def getInput(string):
    while True:
        userInput = input(string).strip()

        try:
            value = int(userInput)
        except ValueError:
            print("N must be an integer.")
            continue

        return value


if __name__ == "__main__":
    userInputN = getInput("Total size of combinations: ")
    userInputR = getInput("Number of Picks 1-N: ")

    printCombinations(userInputN, userInputR)
