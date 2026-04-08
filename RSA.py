import math
from monty_carlo_prime import isPrimeMontyCarlo

def fromBase(x, alphabet):
    b = len(alphabet)
    q = x
    result = ""

    while q != 0:
        r = q % b
        q //= b
        c = alphabet[r]
        result += c

    return result[::-1]

def toBase(s, alphabet):
    base = len(alphabet)
    x = 0

    for char in s:
        pos = alphabet.find(char)
        if pos != -1:
            x = x * base + pos
    return x

class RSA:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet2 = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def GenerateKeys(self, string1, string2):
        p = toBase(string1.lower(), self.alphabet)
        q = toBase(string2.lower(), self.alphabet)

        if p < 10**200 or q < 10**200:
            raise ValueError("String1 or String2 is not long enough")

        p %= 10**200
        q %= 10**200

        if p % 2 == 0:
            p += 1
        elif q % 2 == 0:
            q += 1
        
        while not isPrimeMontyCarlo(p, 10):
            p += 2

        while not isPrimeMontyCarlo(q, 10):
            q += 2

        n = p*q
        r = (p-1)*(q-1)
        e = 10**398 + 1

        while math.gcd(r, e) != 1:
            e += 1
        
        d = pow(e, -1, r)

        with open("public.txt", "w") as public:
            public.write(f"{n}\n{e}")

        with open("private.txt", "w") as private:
            private.write(f"{n}\n{d}")

    def encrypt(self, inFile, outFile):
        fin = open(inFile, "rb")
        plainTextBinary = fin.read()
        plainText = plainTextBinary.decode("utf-8")
        fin.close()

        count = 0
        total_indexes = (len(plainText) + 215) // 216
        plainTextBlocks = [[] for _ in range(total_indexes)]
        current_index = 0

        for char in plainText:
            plainTextBlocks[current_index].append(char)
            count += 1

            if count == 216:
                count = 0
                current_index += 1
        plainTextBlocks = [''.join(sublist) for sublist in plainTextBlocks]
        for v in plainTextBlocks:
            print(v)
            print("========================================================")

        encrypted = toBase(plainText, self.alphabet2)
        with open("public.txt", "r") as fin:
            n = fin.readline().strip()
            e = fin.readline().strip()

            encrypted = pow(encrypted, int(e), int(n))


        encrypted = fromBase(encrypted, self.alphabet2)
            
        fout = open(outFile, "wb")
        fout.write(encrypted.encode("utf-8"))

    def decrypt(self, message):
        return
            
