import sys
from scipy.special import comb
t, k = [int(i) for i in sys.stdin.readline().split()]
l = []
for _ in range(t):
    l.append([int(i) for i in sys.stdin.readline().split()])
def solution(l, k):
    if k == 0:
        n = 0
        for i in range(l[0], l[1] + 1):
            n += i
        return n
    res = 0
    for i in range(l[0], l[1] + 1):
        for j in range(i // k + 1):
            res += comb(i - j * (k - 1), j)
    return int(res)
for i in range(t):
    print(solution(l[i], k))
