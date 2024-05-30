primes = [0 for i in range(3, 1000000)]
def isPrime(n):
    if primes[n] == 1:
        return True
    for i in range(2, int(n**.5)+1, 1):
        if n % i == 0:
            return False
    primes[n] = 1
    return True

def solve(n):
    for i in range(2, n):
        if isPrime(i) and isPrime(n-i):
            print(f"{n} = {i} + {n-i}")
            return
    print("Goldbach's conjecture is wrong.")
    return


while True:
    n = int(input())
    if n == 0:
        break
    solve(n)