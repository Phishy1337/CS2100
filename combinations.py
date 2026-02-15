class Count:
    def __init__(self):
        self.count = 0
        self.pc = "C"
        self.n = 0
        self.r = 0

    def increment(self, n=1):
        self.count += n

    def setN(self, n):
        self.n = n

    def setR(self, r):
        self.r = r

    def printCount(self):

        if self.pc == "P":
            print(f"\nTotal permutations of {self.pc}({self.n}, {self.n}) is {self.count}\n")
            
        if self.pc == "C":
            print(f"\nTotal combinations of {self.pc}({self.n}, {self.r}) is {self.count}\n")
        return       


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


def printCombinations(n, r, count=None):
    if count is None:
        count = Count()

    if r > n:
        return

    values = list(range(1, r + 1))
    print(", ".join(map(str, values)))
    count.increment()

    while nextCombination(n, values):
        print(", ".join(map(str, values)))
        count.increment()
    
    return count

def getInput(string):
    while True:
        userInput = input(string).strip()

        try:
            value = int(userInput)
        except valueError:
            print("N must be an integer.")
            continue

        return value


if __name__ == "__main__":
    n = getInput("total size of combinations: ")
    r = getInput(f"number of picks 1-{n}: ")

    count = printCombinations(n, r)
    count.setN(n)
    count.setR(r)
    count.printCount()
