import sys
line = sys.stdin.readline().strip()
values = list(map(str, line.split()))

num = 0
for i in range(1, len(values)):
    if values[i] == 'A':
        values[i] = '12 34'
        num += 1
    if values[i] == 'B':
        values[i] = 'AB CD'
        num += 1
x = int(values[0], 16) + num
x = str(hex(x))
x = x[2:].upper()
values[0] = x

s = ''
for i in range(len(values)):
    s += values[i] + ' '
print(s[:-1])