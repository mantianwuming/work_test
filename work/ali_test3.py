list1 = input().split(',')
list2 = input().split(',')
x = int(input())

def calc_similar(string1, string2):
    count = []
    total = []
    for i in string1:
        if i in string2:
            count.append(i)
        total.append(i)
    for j in string2:
        total.append(j)
    count = set(count)
    total = set(total)
    res = len(count) / len(total)
    return res

def get_index(list1, list2, x):
    list_similar = []
    for i in range(len(list1)):
        max_similar = 0
        max_similar_index = 0
        if i + (i+1) * x < len(list2):
            for j in range(i, i + (i+1) * x):
                similar = calc_similar(list1[i], list2[j])
                if similar >= max_similar:
                    max_similar = similar
                    max_similar_index = j
            list_similar.append(max_similar_index)
        else:
            for j in range(i, len(list2)):
                similar = calc_similar(list1[i], list2[j])
                if similar >= max_similar:
                    max_similar = similar
                    max_similar_index = j
            list_similar.append(max_similar_index)
    return list_similar

list_similar = get_index(list1, list2, x)
s = ''
for i in list_similar:
    s += (str(i) + ',')
print(s[:-1])