def solve():
    s = input()
    freq = {}
    for x in s:
        try:
            freq[x] += 1
        except KeyError:
            freq[x] = 1

    freqList = tuple(freq.values())
    l_odd = 0
    ans = 0
    for x in freqList:
        if x % 2 == 0:
            ans += x
        if x % 2 == 1:
            if x > l_odd:
                l_odd = x
    ans += l_odd
    return ans


print(solve())