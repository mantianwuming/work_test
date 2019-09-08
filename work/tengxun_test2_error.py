import sys

t, k = map(int, sys.stdin.readline().strip().split())
while t > 0:
    t -= 1
    a, b = map(int, sys.stdin.readline().strip().split())
    res = 0
    for num in range(a, b+1):
        max_k = num // k
        temp = 1
        for i in range(1, max_k):
            l = num - i * k
            temp += (l+1)
        res += temp
    print(res)
