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

    def Encrypt(self, inFile, outFile):
        fin = open(inFile, "rb")
        plainTextBinary = fin.read()
        plainText = plainTextBinary.decode("utf-8")
        fin.close()

        plainTextBlockSize = 216
        count = 0
        total_indexes = (len(plainText) + plainTextBlockSize - 1) // plainTextBlockSize
        plainTextBlocks = [[] for _ in range(total_indexes)]
        current_index = 0

        for char in plainText:
            plainTextBlocks[current_index].append(char)
            count += 1

            if count == plainTextBlockSize:
                count = 0
                current_index += 1

        plainTextBlocks = [''.join(sublist) for sublist in plainTextBlocks]
        toEncrypt = ["" for _ in range(total_indexes)]
        
        with open("public.txt", "r") as fin:
            n = fin.readline().strip()
            e = fin.readline().strip()

        fout = open(outFile, "wb")
        current_index = 0
        for block in plainTextBlocks:
            encrypted = pow(toBase(block, self.alphabet2), int(e), int(n))
            encrypted = fromBase(encrypted, self.alphabet2)
            toEncrypt[current_index] = encrypted
            current_index += 1
            
        
        for encryptedBlock in toEncrypt:
            fout.write(f"{encryptedBlock}$".encode("utf-8"))

        fout.close()

    def Decrypt(self, inFile, outFile):
        fin = open(inFile, "rb")
        encryptedTextBinary = fin.read()
        encryptedText = encryptedTextBinary.decode("utf-8")
        fin.close()

        total_indexes = encryptedText.count("$")
        encryptedTextBlocks = ["" for _ in range(total_indexes)]
        current_index = 0
        current_block = ""

        for char in encryptedText:
            if char == "$":
                encryptedTextBlocks[current_index] = current_block
                current_index += 1
                current_block = ""
            else:
                current_block += char

        toDecrypt = ["" for _ in range(total_indexes)]

        with open("private.txt", "r") as fin:
            n = fin.readline().strip()
            d = fin.readline().strip()

        fout = open(outFile, "wb")
        current_index = 0
        for block in encryptedTextBlocks:
            decrypted = pow(toBase(block, self.alphabet2), int(d), int(n))
            decrypted = fromBase(decrypted, self.alphabet2)
            toDecrypt[current_index] = decrypted
            current_index += 1
            
        for decryptedBlock in toDecrypt:
            fout.write(decryptedBlock.encode("utf-8"))

        fout.close()
