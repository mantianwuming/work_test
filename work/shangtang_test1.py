import sys
line = sys.stdin.readline().strip()
n, m = map(int, line.split())
watermelons = []
for i in range(n):
    line = sys.stdin.readline().strip()
    watermelon = list(map(int, line.split()))
    watermelons.append(watermelon)

for i in range(m):
    time = int(sys.stdin.readline().strip())
    max_melon = -1
    for j in range(len(watermelons)):
        if watermelons[j][0] >= time:
            if watermelons[j][1] >= max_melon:
                max_melon = watermelons[j][1]
    print(max_melon)