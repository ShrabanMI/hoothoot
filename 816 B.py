def solve():
    n, k, q = [int(x) for x in input().split()]
    recipes: dict[int, int] = {}
    for i in range(n):
        l, r = [int(x) for x in input().split()]
        for j in range(l, r + 1):
            try:
                recipes[j] += 1
            except KeyError:
                recipes[j] = 1

    de = []
    for key in recipes:
        if recipes[key] < k:
            de.append(key)
    for x in de:
        del recipes[x]

    for i in range(q):
        a, b = [int(x) for x in input().split()]
        ans = 0
        for key in recipes:
            if a <= key <= b:
                ans += 1
        print(ans)


solve()