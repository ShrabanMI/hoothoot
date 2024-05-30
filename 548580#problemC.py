# def solve():
#     n, m = [int(x) for x in input().split()]
#     ans = 0
#     c = 1
#     while c != n+1:
#         for i in range(1, m+1):
#             if i % n == 1:
#                 ans -= c
#             print(i % n, c)
#             c += 1
#
#
# for idx in range(1, int(input())+1):
#     print(f"Case {idx}: {solve()}")

def solve():
    n, m = [int(x) for x in input().split()]
    return int(n/2*m)


for i in range(int(input())):
    print(f"Case {i+1}: {solve()}")