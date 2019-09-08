line = input()
n, m, d = map(int, line.split())
line = input()
specials = list(map(int, line.split()))
line = input()
father_node = list(map(int, line.split()))

def get_dis(alist, i, special):
    new_list = [i]
    cur = i
    while alist[cur] != cur:
        cur = alist[cur]
        new_list.append(cur)

    list_special = [special]
    cur = special
    while alist[cur] != cur:
        cur = alist[cur]
        list_special.append(cur) 

    for i in range(len(new_list)):
        for j in range(len(list_special)):
            if new_list[i] == list_special[j]:
                return i + j
    
    return 100000

alist = [i for i in range(n + 1)]
for i in range(n-1):
    alist[i+2] = father_node[i]

count = 0
for i in range(1, n+1):
    flag = True
    for special in specials:
        if get_dis(alist, i, special) > d:
            flag = False
            break
    if flag:
        count += 1
print(count)