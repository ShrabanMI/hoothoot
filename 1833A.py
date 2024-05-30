def solve():
    n = int(input())
    s = input()
    freq_mel = {s[i]+s[i+1]: 1 for i in range(n-1)}
    print(len(freq_mel))


for _ in range(int(input())):
    solve()