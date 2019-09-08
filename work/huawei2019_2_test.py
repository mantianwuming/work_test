# coding = gbk
import numpy as np

s = input()

voc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

num = np.zeros(26)

# s1 = ''
# for i in s:
#     if i not in s1:
#         s1 += i
s1 = set(s)
slist = list(s1)

for i in range(0, 26):
    if voc[i] in slist and voc[i+26] in slist:
        num[i] = 1
# print(num)
# def find_voc(s):

sum_num = sum(num)
res_list = []
while sum_num > 0:
    res = ''
    max_len = 1
    zero_list = [-1]
    sum_num = sum(num)


    for i in range(26):
        if num[i] == 0:
            zero_list.append(i)
    # print(zero_list)


    for j in range(len(zero_list)-1):
        length = zero_list[j+1] - zero_list[j]
        if max_len < length:
            max_len = length
            for l in range(1, max_len):
                res += (voc[zero_list[j] + l] + voc[zero_list[j] + l + 26])
            res_list.append(res)
    # print(res_list)
    res = list(res)
    for i in range(len(res)):
        if res[i] in slist:
            slist.remove(res[i])
    # print(slist)
    num = np.zeros(26)
    for i in range(0, 26):
        if voc[i] in slist and voc[i+26] in slist:
            num[i] = 1
    # print(num)
    sum_num = sum(num)
    # print(slist)


for i in range(len(res_list)):
    print(res_list[i])
# print(max_len)
# print(res)
