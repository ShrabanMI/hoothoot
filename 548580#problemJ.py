def get_primes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime


def get_prime_divs(n, is_prime):
    divisors = set()
    for p in range(2, int(n**0.5)+1):
        if is_prime[p]:
            if n % p == 0:
                divisors.add(p)
                while n % p == 0:
                    n //= p
    if n > 1:
        divisors.add(n)
    return divisors


def solve():
    n = int(input())
    primes = get_primes(n)
    count = 0
    for i in range(1, n+1):
        if len(get_prime_divs(i, primes)) == 2:
            count += 1

    return count


print(solve())