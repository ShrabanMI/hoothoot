def solve(n):
    s = input()
    if 'L' not in s or 'R' not in s:
        return -1
    if (s[0] == 'R' and s[-1] == 'L') or 'RL' in s:
        return 0
    else:
        return s.find('R')


for i in range(int(input())):
    print(solve(n=int(input())))
