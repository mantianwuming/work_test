# coding = gbk
s = input()
s = list(s)
add = []
minus = []
for i in range(len(s)):
    if s[i] == "+":
        add.append(i)
        s[i] = " "
    elif s[i] == "-":
        minus.append(i)
        s[i] = " "

s = ''.join(s)
alist = list(map(int, s.split()))
a_m = add+minus
a_m = sorted(a_m)
res = alist[0]
for j in range(len(a_m)):
    if a_m[j] in add:
        res += alist[j+1]
    else:
        res -= alist[j+1]

print(res)
