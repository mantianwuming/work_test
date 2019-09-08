import sys
n = int(sys.stdin.readline().strip())
a = [n]
for i in range(n):
    value = list(map(int, sys.stdin.readline().split()))
    a.append(value)
# print(a)
def fun(a):
    if a[0] == 1:
        return 1
    a_temp = a[2:]
    ha = list()
    ha.append(a[1])
    cut = list()
    cut.append([0,0,0,0])
    flag = False
    for a, b in a_temp:
        for i,(c,d) in enumerate(ha):
            if a == c:
                flag = True
                if cut[i][0] == 0:
                    cut[i][0] = 1
                break
            if b == d:
                flag = True
                if cut[i][1] == 0:
                    cut[i][1] = 1
                break
            if (c-a) == (b-d):
                flag = True
                if cut[i][2] == 0:
                    cut[i][2] = 1
                break
            if (a-c) == (b-d):
                flag = True
                if cut[i][3] == 0:
                    cut[i][3] = 1
                break

        if not flag:
            ha.append([a, b])
            cut.append([0,0,0,0])
        flag = False
    num = 0
    for h,s,p,n in cut:
        if [h,s,p,n] == [0,0,0,0]:
            num += 1
        else:
            num += (h+s+p+n)
    return num

n = fun(a)
print(n)
