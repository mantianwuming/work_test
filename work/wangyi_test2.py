import sys

n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

numbers = []
for i in range(1, n+1):
    numbers.append(i)

def ordered(numbers):
    all_order = []
    # def permute(all_order, l, r, n, max):
    #     if n == max:
    #         all_order.append(l)
    #     for i in range(0, len(r)):
    #         permute(all_order, l+[r[i]], r[:i] + r[i+1:], n+1, max)
    permute(all_order, [], numbers, 0, len(numbers))
    return all_order

def permute(all_order, l, r, n, max):
    if n == max:
        all_order.append(l)
    for i in range(0, len(r)):
        permute(all_order, l+[r[i]], r[:i] + r[i+1:], n+1, max)

all_order = ordered(numbers)
# print(all_order)
q = all_order.index(values)
# print(q)
need_number = all_order[-q-1]

for i in need_number:
    print(i, end=' ')
        
