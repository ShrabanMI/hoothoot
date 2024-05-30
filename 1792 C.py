def solve(n):
    p = [int(i) for i in input().split()]
    ans = 0
    if p == sorted(p) or n == 1:
        return 0
    if n <= 3:
        return 1
    for i in range(n//2):



for i in range(int(input())):
    print(solve(n=int(input())))
