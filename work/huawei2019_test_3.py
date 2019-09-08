import sys
line = sys.stdin.readline().strip()
line = line.split('@')
left = line[0]
right = line[1]
left = left.split(',')
right = right.split(',')

if right == ['']:
    print(line[0])
else:
    dict_left = {}
    dict_right = {}
    list_left = []
    list_right = []
    for i in range(len(left)):
        num = left[i].index(':')
        dict_left[left[i][:num]] = int(left[i][num+1:])
        list_left.append(left[i][:num])
    for i in range(len(right)):
        num = right[i].index(':')
        dict_right[right[i][:num]] = int(right[i][num+1:])
        list_right.append(right[i][:num])

    for i in list_left:
        if i in list_right:
            dict_left[i] -= dict_right[i]
    out = ''
    for i in list_left:
        if dict_left[i] <= 0:
            continue
        out += (i + ':' + str(dict_left[i]) + ',')
    out = out[:-1]
    print(out)
