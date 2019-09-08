h, w = map(int, input().split())
grid = []
for i in range(h):
    rows = list(map(int, input().split()))
    grid.append(rows)

m = int(input())
kernal = []
for i in range(m):
    rows = list(map(float, input().split()))
    kernal.append(rows)

def conv(grid, kernal, h, w, m):
    cons =[]
    for i in range(h - m + 1):
        rows = []
        for j in range(w - m + 1):
            x = 0
            for l in range(m):
                for k in range(m):
                    x += grid[i+l][j+k] * kernal[l][k]
            rows.append(int(x))
        cons.append(rows)
    return cons
if m > h or m > w:
    print('')
else:
    cons = conv(grid, kernal, h, w, m)
    for i in cons:
        s = ''
        for n in i:
            s += str(n) + ' '
        print(s[:-1])