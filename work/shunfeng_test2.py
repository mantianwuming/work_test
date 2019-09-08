n,m,k = map(int, input().split())
list_a = [-1 for i in range(n)]
dic = {}
for _ in range(k):
    u, v = map(int, input().split())
    if v not in dic.keys():
        dic[v] = []
    dic[v].append(u-1)
def find(list_a, num):
    while list_a[num] != -1:
        num = list_a[num]
    return num

for item in dic.keys():
    if len(dic[item]) > 1:
        length = len(dic[item])
        for i in range(length - 1):
            for j in range(i + 1, length):
                item0 = find(list_a, dic[item][i])
                item1 = find(list_a, dic[item][j])
                if item0 != item1:
                    list_a[item0] = item1
if k == 0:
    print(n)
else:
    res = 0
    for x in list_a:
        if x == -1:
            res += 1
        else:
            res += 0
    print(max(res - 1, 0)) 