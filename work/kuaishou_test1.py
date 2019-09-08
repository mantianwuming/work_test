import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
out = []
for i in range(m):
    out.append(sys.stdin.readline().strip())

def change_order(out):
    i = 0
    flag = 0
    res = []
    while i < len(out):
        if out[i][0] == 'P' and flag == 0:
            flag += 1
            i += 1
        elif out[i][0] == 'P' and flag != 0:
            res.append(out[i])
            out.remove(out[i])
        else:
            i += 1
    i = 0
    j = 0
    while i < len(out) and j < len(out) and res:
        if out[i][0] == 'P':
            j = i + n
            if j <= len(out):
                out.insert(j, res[0])
                res.pop(0)
            i += 1
        else:
            i += 1
    return out

out = change_order(out)
print(len(out))
for i in range(len(out)):
    print(out[i])
