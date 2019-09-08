def divide_groups(line):
    l1, l2 = 0, 0
    r = len(line)
    res = []
    while l1 < r:
        for i in range(l1, r):
            if line[i] == line[l1]:
                l2 = i
        x = line[l1:l2+1]
        for j in range(l2+1, r):
            if line[j] in x:
                l2 = j
        res.append(line[l1:l2+1])
        l2 += 1
        l1 = l2
    return res

line = input()
res = divide_groups(line)
print(res)
s = ''
for i in res:
    s += (str(len(i)) + ',')
print(s[:-1])
     