def nextPermutation(values):
    i = len(values) - 2

    while i >= 0 and values[i] >= values[i + 1]:
        i -= 1

    if i < 0:
        return False

    j = len(values) - 1
    while values[j] <= values[i]:
        j -= 1

    values[i], values[j] = values[j], values[i]
    values[i + 1:] = reversed(values[i + 1:])
    return True


def printPermutations(n):
    values = list(range(n))
    print(", ".join(map(str, values)))

    while nextPermutation(values):
        print(", ".join(map(str, values)))

def getInput(string):
    while True:
        userInput = input(string).strip()

        try:
            value = int(userInput)
        except ValueError:
            print("N must be an integer.")
            continue

        if not 1 <= value <= 9:
            print("N must be integer 1 to 9.")
            continue

        return value

def main():
    n = getInput("Enter N (1-9): ")
    printPermutations(n)

if __name__ == "__main__":
    main()
