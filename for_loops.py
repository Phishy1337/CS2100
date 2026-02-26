# Write a Python program that generates and prints all of the C(5,3), 
# all the CR(5,3), all the P(5,3), and all the PR(5,3) using nested for loops.
# 5, 3

# Combinations: n!/(n-r)!r!
# CombinationsR: C(n+r-1, r)
# Permutations: n!/(n-r)!

LINE_WIDTH = 72

def printDivider(char="="):
    print (char * LINE_WIDTH)

def printSection(title):
    print()
    printDivider()
    print(title.center(LINE_WIDTH))
    printDivider()
    print()


def printCombinations(n, r):
    for i in range(1, r + 1):
        for j in range(i, r + 1):
            for k in range(j, r + 1):
                print(i, j + 1, k + 2)

def printCombinationsR(n, r):
    for i in range(1, r + 1):
        for j in range(i, r + 1):
            for k in range(j, r + 1):
                print(i, j, k)

def printPermutations(n, r):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    print(i, j, k)

def printPermutationsR(n, r):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

if __name__ == "__main__":
    printSection("COMBINATIONS")
    printCombinations(5, 3)
    printSection("COMBINATIONS WITH REPETITION")
    printCombinationsR(5, 3)
    printSection("PERMUTATIONS")
    printPermutations(5, 3)
    printSection("PERMUTATIONS WITH REPETITION")
    printPermutationsR(5, 3)
