def solve():
    n = int(input())
    li = [n]

    while True:
        if n == 1:
            break
        if n & 1:
            n = (3*n)+1
        else:
            n = n//2
        li.append(n)

    print(*li)


solve()