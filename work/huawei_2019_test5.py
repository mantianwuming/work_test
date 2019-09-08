import sys
line = sys.stdin.readline().strip()

words = []
flag = 0
i = 0
j = 0
while i < len(line) and j < len(line):
    if line[i] == '"':
        flag += 1
    if flag % 2 == 0 and line[i] == ',':
        words.append(line[j:i])
        j = i+1
    if i == len(line) - 1:
        words.append(line[j:])
    i += 1

t_or_f = True
for i in range(len(words)):
    if t_or_f == False:
        break
    if words[i] == '':
        continue
    elif (words[i][0] == '"' and words[i][-1] != '"') or (words[i][0] != '"' and words[i][-1] == '"'):
        t_or_f = False
        break
    j = 0
    x = ''
    while j < len(words[i]):
        if words[i][0] == words[i][-1] == '"':
            words[i] = words[i][1:-1]
            continue
        if j < len(words[i]) - 1 and words[i][j] == '"' and words[i][j+1] == '"':
            x += words[i][j]
            j += 2
        elif j < len(words[i]) - 1 and words[i][j] == '"' and words[i][j+1] != '"':
            t_or_f = False
            break
        else:
            x += words[i][j]
            j += 1
    words[i] = x
if t_or_f:
    print(len(words))
    for i in range(len(words)):
        if words[i] == '':
            print('--')
        else:
            print(words[i])
else:
    print('ERROR')
        
            

# import sys
# s = sys.stdin.readline()
# # s = 'a,,1,"b,"""'

# def divide(s):
#     res = []
#     count = 0
#     l = 0
#     i = 0
#     while i < len(s):
#         c = s[i]
#         if c == '"':
#             count += 1
#         if c == ',' and count % 2 == 0:
#             res.append(s[l:i])
#             l = i + 1
#         i += 1
#     res.append(s[l:i])
#     return res 

# def judge(strs):
#     for i in range(len(strs)):
#         s = strs[i]
#         if s != '':
#             if s[0] == '"' and s[-1] == '"':
#                 strs[i] = strs[i][1:-1]
#             elif s[0] == '"' and s[-1] != '"':
#                 return False 
#             elif s[0] != '"' and s[-1] == '"':
#                 return False 
#         s = strs[i]
#         j = 0
#         new_s = ''
#         while j < len(s):
#             if s[j] == '"' and s[j+1] == '"':
#                 new_s += s[j]
#                 j += 2
#             elif s[j] == '"' and s[j+1] != '"':
#                 return False 
#             else:
#                 new_s += s[j]
#                 j += 1
#         strs[i] = new_s
#     return True

# strs = divide(s)
# # print(strs)
# if not judge(strs):
#     print('ERROR')
# else:
#     print(len(strs))
#     for s in strs:
#         if s == '':
#             print('--')
#         elif s.isdigit():
#             print(int(s))
#         else:
#             print(s)