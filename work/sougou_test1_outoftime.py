import sys

x = int(sys.stdin.readline().strip())

def get_dic(x):
    res = []
    for i in range(1, x):
        for j in range(1, x):
            if i+j <= x:
                res.append([i,j])
    result = []
    for m in range(len(res)):   
        [i,j] = res[m]
        num = get_index(i,j,x)
        if num != -1:
            result.append(num+1)

    dic = {}
    for i in result:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic


def get_index(i,j, x):
    alist = [i, j]
    while j < x:
        i, j = j, i+j
        alist.append(j)
    if x in alist:
        xindex = alist.index(x)
        return xindex
    else:
        return -1

dic = get_dic(x)
keys = []
for key in dic.keys():
    keys.append(key)
keys.sort()
for i in keys:
    print(str(i) + ' ' + str(dic[i]))