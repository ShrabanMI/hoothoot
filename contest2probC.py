def solve():
    p, s, r = [int(x) for x in input().split()]
    if p == s:
        if r == 1:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'Yes'


for i in range(int(input())):
    print(f'Case {i+1}:', solve())