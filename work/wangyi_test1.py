import sys

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

numbers = []
for i in range(1, n+1):
    numbers.append(i)

def ordered(numbers):
    all_order = []
    if len(numbers) <= 1:
        return [numbers]
    for i in range(n):
        s = numbers[:i] + numbers[i+1:]
        p = ordered(s)
        for m in p:
            all_order.append(numbers[i:i+1] + m)
    return all_order

all_order = ordered(numbers)
q = all_order.index(values)
need_number = all_order[-q]

for i in need_number:
    print(i, end=' ')
        
