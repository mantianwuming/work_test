import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
get_in = list(map(int, line.split()))
line = sys.stdin.readline().strip()
get_out = list(map(int, line.split()))

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += (get_in[i] * i * -1)

for j in range(n):
    sum2 += (get_out[j] * j)

sum = sum1 + sum2
print(sum)
