def nextCombination(values):
    """
    for C(5, 3), set starts at {0, 1, 2}, final would be {3, 4, 5}
    try to increase the 1's digit up to n, so long as item 
    to the left is less than it.  if not, move to 10's place, etc.
    """
    i = len(values) - 1

def printCombinations(n, r):
    values = list(range(r))
    print(", ".join(map(str, values)))

    while nextCombination(values):
        

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

