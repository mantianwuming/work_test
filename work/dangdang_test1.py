# leetcode 93
import sys

def restore(s):
    res = []
    n = len(s)

    def bt(i, temp, flag):
        if i == n and flag == 0:
            res.append(temp[:-1])
            return
        if flag < 0:
            return
        for j in range(i, i + 3):
            if j < n:
                if i == j and s[j] == '0':
                    bt(j + 1, temp + s[j] + '.', flag - 1)
                    break
                if 0 < int(s[i:j + 1]) <= 255:
                    bt(j + 1, temp + s[i:j+1] + '.', flag - 1)
    bt(0, '', 4)
    return res

s = sys.stdin.readline().strip()
res = restore(s)
x = ''
for i in res:
    x = x + i + ','
print(x[:-1])