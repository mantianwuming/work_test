import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
distance = list(map(int, line.split()))
line = sys.stdin.readline().strip()
ei = list(map(int, line.split()))
new_distance = distance[:]
new_ei = ei[:]

def get_order(distance, ei):
    orders = []
    while distance and ei:
        length = len(distance)
        now_ex = 0
        max_ex = 0
        order = -1
        for i in range(length):
            now_ex = 2 * distance[i] + ei[i]
            if now_ex > max_ex:
                max_ex = now_ex
                order = i
        orders.append(order)
        distance.remove(distance[order])
        ei.remove(ei[order])
    return orders

def print_ei(order, distance, ei, num):
    new_order = order[:num]
    max_dis = 0
    choice_i = -1
    for i in new_order:
        if distance[i] > max_dis:
            max_dis = distance[i]
            choice_i = i
        distance.remove(distance[choice_i])
    sum = 0
    for i in new_order:
        sum += ei[i]
        ei.remove(ei[choice_i])
    get_ei = 2 * distance[choice_i] + sum
    return get_ei

orders = get_order(distance, ei)
print(orders)
for i in range(n):
    get_ei = print_ei(orders, new_distance, new_ei, i+1)
    print(get_ei)


