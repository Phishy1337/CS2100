from itertools import permutations


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
        print(f"\nTotal permutations of {self.pc}({self.n}, {self.r}) is {self.count}\n")
        return


def permutations_with_r(n, r, count=None):
    if count is None:
        count = Count()

    values = list(range(n))

    for perm in permutations(values, r):
        print(", ".join(map(str, perm)))
        count.increment()

    return count


def getInput(prompt):
    while True:
        userInput = input(prompt).strip()

        try:
            value = int(userInput)
        except ValueError:
            print("Value must be an integer.")
            continue

        if not 1 <= value <= 9:
            print("Value must be integer 1 to 9.")
            continue

        return value


def getRInput(n):
    while True:
        r = getInput("Enter R (1-N): ")
        if r > n:
            print("R must be less than or equal to N.")
            continue
        return r


def main():
    n = getInput("Enter N (1-9): ")
    r = getRInput(n)

    count = permutations_with_r(n, r)
    count.setN(n)
    count.setR(r)
    count.printCount()


if __name__ == "__main__":
    main()
