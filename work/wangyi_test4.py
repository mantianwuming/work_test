import sys

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

# print(values)
def bubble_like(valuse):
    for i in range(n):
        for j in range(i+1, n):
            if values[j-1] > values[j]:
                if (values[j-1] + values[j]) % 2 == 1:
                    values[j-1], values[j] = values[j], values[j-1]
    return values

values1 = bubble_like(values)
for i in range(len(values1)):
    print(values[i], end = ' ')