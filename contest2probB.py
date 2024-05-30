def solve():
    arr = [int(x) for x in input()]
    if sum(arr[:3]) == sum(arr[3:]):
        return 'YES'
    return 'NO'


for i in range(int(input())):
    print(solve())