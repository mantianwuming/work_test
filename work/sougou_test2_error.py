import sys
k, n = map(int, sys.stdin.readline().strip().split())
dic_tree = {}
for i in range(n):
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    dic_tree[line[1]] = line[2:]

def cal_time(dic_tree, k):
    res = {}
    count = 0
    for i in dic_tree.items():
        if i[0] not in res:
            res[i[0]] = count
        count += 1
        for j in i[1]:
            if j not in res:
                res[j] = count
    return count

count = cal_time(dic_tree, k)
print(count)
        