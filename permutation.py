class Count:
    def __init__(self):
        self.count = 0
        self.pc = "P"
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


def printPermutations(n, count=None):
    if count is None:
        count = Count()

    values = list(range(n))
    print(", ".join(map(str, values)))
    count.increment()

    while nextPermutation(values):
        print(", ".join(map(str, values)))
        count.increment()

    return count

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
    count = printPermutations(n)
    count.setN(n)
    count.printCount()

if __name__ == "__main__":
    main()
