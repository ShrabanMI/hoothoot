def solve():
    n, k, q = [int(x) for x in input().split()]
    recipes = {}
    for i in range(n):
        l, r = [int(x) for x in input().split()]
        for j in range(l, r+1):
            if j not in recipes:
                recipes[j] = 1
            else:
                recipes[j] += 1
    de = []
    for key in recipes:
        if recipes[key] < k:
            de.append(key)
    for x in de:
        del recipes[x]

    for i in range(q):
        a, b = [int(x) for x in input().split()]
        count = 0
        for key in recipes:
            if a <= key <= b:
                count += 1
        print(count)


solve()