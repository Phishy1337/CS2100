import random
import math

def print_divider():
    print("="*50)

def isPrimeMontyCarlo(n, repeats):
    for i in range(repeats):
        if millersTest(n) == False:
            return False
    return True
    
def millersTest(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    power, multiple = findPowerAndMultiple(n)
    
    base = random.randint(2, n-1)

    x = pow(base, multiple, n)

    if x == 1 or x == n - 1:
        return True
    
    for i in range(power - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True
    
    return False

def findPowerAndMultiple(n):
    multiple = n - 1
    power = 0
    
    while multiple % 2 == 0:
        multiple //= 2
        power += 1
        
    return power, multiple

def sqrtPrimeTest(n):
    maxTest = int(math.sqrt(n))
    for i in range(2, maxTest + 1):
        if n % i == 0:
            return False
    
    return True

def testMillionPrimes():
    f = 0
    for n in range(3, 1000001):
        if sqrtPrimeTest(n) != isPrimeMontyCarlo(n, 10):
            print(f"INEQUALITY AT {n}")
            f += 1

    return f"{f} inequal tests"
    

def main():
    print_divider()
    print("Testing 3-1000000...")
    print(testMillionPrimes())
    print_divider()
    print("Testing 100 digit primes...")
    print(f"445... prime? : {millersTest(4458173553346974938725485632314376561863949441170519135039453771102529122118151140980538513284447609)}")
    print(f"731... prime? : {millersTest(7319408322642723009608583435984440971562091061166124237575283628077055753633679626993086661668754787)}")
    print_divider()
    print("\nTesting 200 digit composite...")
    print(f"326... prime? : {millersTest(32631192610153530043597319943629381137053889489503184204722447935630006815747010842497146933731771407414481038309001310779116651410466709333322201862408523625694566390353782747517457848080980169454283)}")

if __name__ == "__main__":
    main()


