import sys
n = int(sys.stdin.readline().strip())
times = []
for i in range(n):
    line = sys.stdin.readline().strip()
    s = list(map(int, line.split()))
    times.append(s)
x = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
last_time = list(map(int, line.split()))

road_time = [0, 0]
road_time[0] += x//60
road_time[1] += x%60

sum = 1440
should_time = []
for i in range(len(times)):
    rest_time = 0
    a = times[i] + road_time
    b = (last_time[0] - a[0])*60 + (last_time[1] - a[1])
    if b > 0 and b < sum:
        sum = b
        should_time = times[i]

for i in range(len(should_time)):
    print(should_time[i], end=' ')