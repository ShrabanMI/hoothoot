def solve():
    n = int(input())
    n = bin(n)
    x = n.count('1')
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'


for i in range(1, int(input())+1):
    print(f"Case {i}:", solve())