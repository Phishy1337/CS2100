def nextPermutation(values):
    
    i = len(values) - 2

    while i >= 0 and values[i] > values[i + 1]:
        i -= 1

    if i < 0:
        return False

    j = len(values) - 1

    while j >= 0 and values[j] < values[i]:
        j -= 1

    values[i], values[j] = values[j], values[i]
    values[i + 1:] = reversed(values[i + 1:])

    return True 

def printPermutations(n):
    values = list(range(n))

    print(", ".join(map(str, values)))

    while nextPermutation(values):
        print(", ".join(map(str, values)))

if __name__ == "__main__":
    user_input = input("Enter an integer 1-9: ").strip()
    printPermutations(int(user_input))
