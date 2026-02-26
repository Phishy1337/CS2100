# Write a Python program that generates and prints all of the C(5,3),
# all the CR(5,3), all the P(5,3), and all the PR(5,3) using nested for loops.
# 5, 3

# Combinations: n!/(n-r)!r!
# CombinationsR: C(n+r-1, r)
# Permutations: n!/(n-r)!

LINE_WIDTH = 72

def printDivider(char="="):
    print(char * LINE_WIDTH)

def printSection(title):
    print()
    printDivider()
    print(title.center(LINE_WIDTH))
    printDivider()
    print()

def groupByFirstIndex(results):
    grouped = {}
    for result in results:
        first = result[0]
        if first not in grouped:
            grouped[first] = []
        grouped[first].append(result)
    return grouped

def printGroupedTable(grouped, col_width=18):
    headers = sorted(grouped)
    print("".join(str(h).center(col_width) for h in headers))
    print("-" * (col_width * len(headers)))

    max_rows = max(len(grouped[h]) for h in headers)
    for row_index in range(max_rows):
        row = ""
        for h in headers:
            if row_index < len(grouped[h]):
                row += str(grouped[h][row_index]).center(col_width)
            else:
                row += "".center(col_width)
        print(row)

def printCombinations(n, r):
    results = []
    for i in range(1, r + 1):
        for j in range(i, r + 1):
            for k in range(j, r + 1):
                results.append((i, j + 1, k + 2))
    grouped = groupByFirstIndex(results)
    printGroupedTable(grouped)

def printCombinationsR(n, r):
    results = []
    for i in range(1, r + 1):
        for j in range(i, r + 1):
            for k in range(j, r + 1):
                results.append((i, j, k))
    grouped = groupByFirstIndex(results)
    printGroupedTable(grouped)

def printPermutations(n, r):
    results = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and i != k and j != k:
                    results.append((i, j, k))
    grouped = groupByFirstIndex(results)
    printGroupedTable(grouped)

def printPermutationsR(n, r):
    results = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                results.append((i, j, k))
    grouped = groupByFirstIndex(results)
    printGroupedTable(grouped)

if __name__ == "__main__":
    printSection("COMBINATIONS")
    printCombinations(5, 3)
    printSection("COMBINATIONS WITH REPETITION")
    printCombinationsR(5, 3)
    printSection("PERMUTATIONS")
    printPermutations(5, 3)
    printSection("PERMUTATIONS WITH REPETITION")
    printPermutationsR(5, 3)
