def minorder(line):
    stack1 = []
    j = 1
    x = 0
    character = line[j]
    flag = -1
    while x < len(line) and j < len(line):
        while j < len(line) and line[j] == character:
            j += 2
        if character == '*' :
            for i in range(x, j, 2):
                stack1.append(int(line[i]))
                flag = 1
        elif character == '+':
            for i in range(x, j-2, 2):
                stack1.append(int(line[i]))
                flag = 1
        elif character == '/':
            for i in range(x, j, 2):
                stack1.append(int(line[i]))
                flag = 0
        elif character == '-':
            for i in range(x, j-2, 2):
                stack1.append(int(line[i]))
                flag = 0
        if flag == 1:
            stack1.sort()
        while stack1:
            num = stack1.pop(0)
            line[x] = num
            x += 2
        if j < len(line):
            character = line[j]
    return line

n = int(input())
line = input()
line = line.split()
minorder(line)
s = ''
for i in range(len(line)):
    s += str(line[i]) + ' '
print(s[:-1])


    



# while i < len(line):
#     j = i + 1
#     if line[j] in add_min:
#         stack1.append(int(line[i]))
#     else:
#         stack2.append(int(line[i]))
#     i += 2