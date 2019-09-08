import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    
    values.sort(reverse=True)
    
    if values[0] < values[1] + values[2]:
        print('YES')
    else:
        print('NO')
        