from math import pi

def solve(idx):
    r = float(input())
    s = 2*r
    ans = s ** 2 - (pi * r ** 2)
    ans = round(ans, 2)
    return f"Case {idx}: {ans}"


for i in range(int(input())):
    print(solve(i+1))