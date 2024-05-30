def solve():
    n = int(input())
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return "No"
    return "Yes"


print(solve())