def divide_groups(line):
    dic = {}
    for i in range(len(line)-1, -1, -1):
        if line[i] not in dic:
            dic[line[i]] = i
    begin = 0
    end = 0
    res = []
    for x, y in enumerate(line):
        if dic[y] > end:
            end = dic[y]
        if x == end:
            res.append(end - begin + 1)
            begin, end = x + 1, x + 1
    return res

line = input()
res = divide_groups(line)
s = ''
for i in res:
    s += (str(i) + ',')
print(s[:-1])