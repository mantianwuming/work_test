import sys

def get_target(n):
    if n <= 0:
        return 0
    targets = [1]
    num = 1
    index3, index5, index11 = 0, 0, 0
    while num < n:
        m = min(targets[index3] * 3, targets[index5] * 5, targets[index11] * 11)
        targets.append(m)
        num += 1
        if targets[index3] * 3 <= m:
            index3 += 1
        if targets[index5] * 5 <= m:
            index5 += 1
        if targets[index11] * 11 <= m:
            index11 += 1
    return targets[-1]

n = int(sys.stdin.readline().strip())
print(get_target(n))