import sys
line = sys.stdin.readline().strip()
n, a, b, c, f0 = map(int, line.split())

f = []
f0 = 100
f.append(f0)
f1 = a * f0 + 2 * 1 * 1 - 1 + 32767
print(f1)
f.append(f1)
f2 = a * f1 + b * f0 + 2 * 2 * 2 - 2 + 32767
print(f2)
f.append(f2)
f3 = a * f2 + b * f1 + c * f0 + 2 * 3 * 3 - 3 + 32767
print(f3)
i = 3
while i <= n:
    fi = a * f[i-1] + b*f[i-2] + c*f[i-3] + 2 * i * i - i + 32767
    f.append(fi)
    i += 1

fn = f[n] % 1000000007
print(f)

import sys
def cal(n, a, b, c, f0):
    f = [0, 0 , f0]
    m = [0, 0, 1]
    for i in range(3, n+3):
        f.append(a * f[i-1] + b * f[i-2] + c * f[i-3] + (i-2) * (i-2) * 2 - (i-2))
    for j in range(3, n + 3):
        m.append(a * m[j-1] + b * m[j-2] + c*m[j-3] + 1)
    return (f[-1] + m[-2]*32767)%1000000007
print(cal(n,a,b,c,f0))