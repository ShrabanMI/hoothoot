def solve():
    dec = [int(x) for x in input().split('.')]
    bin = [x for x in input().split('.')]
    for i in range(4):
        bin[i] = int(bin[i], 2)

    if bin == dec:
        return 'Yes'
    return 'No'


for idx in range(int(input())):
    print(f"Case {idx+1}: {solve()}")