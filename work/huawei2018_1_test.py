# coding = gbk
# 括号匹配
# 给定一个字符串，里边可能包含“()”、“[]”、“{}”三种括号，请编写程序检查该字符串中的括号是否成对出现，且嵌套关系正确。
# 输出：true:若括号成对出现且嵌套关系正确，或该字符串中无括号字符；
# false:若未正确使用括号字符。
# 实现时，无需考虑非法输入。
# 输入描述：
# 输入为：
# 字符串
# 例子：(1+2)/(0.5+1)
# 输出描述：
# 输出为：true
#
# 思路：栈
# 遇到左符号，则压入，遇到右符号，弹出顶层的符号和右符号比对，如果符合，则继续，
# 否则输出false

s = input()
# s1 = list(s)

# voc1 = ['(', '[', '{']
# voc2 = [')', ']', '}']
# def judge_s(s):
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     for i in s:
#         if (i == ')' and count1 == 0) or (i == ']' and count2 == 0) or (i == '}' and count3 == 0):
#             return False
#         elif i == '(':
#             count1 += 1
#         elif i == ')':
#             count1 -= 1
#         elif i == '[':
#             count2 += 1
#         elif i == ']':
#             count2 -= 1
#         elif i == '{':
#             count3 += 1
#         elif i == '}':
#             count3 -= 1
#
#     if count1 == 0 and count2 == 0 and count3 == 0:
#         return True
#     else:
#         return False

def judge_rl(a, b):
    if a == '(' and b == ')':
        return 1
    if a == '[' and b == ']':
        return 1
    if a == '{' and b == '}':
        return 1
    else:
        return 0
def judge_s(s):
    x = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            x.append(i)
        elif i == ')' or i == ']' or i == '}':
            if x != [] and judge_rl(x[-1], i) == 1:
                return True
            else:
                return False
                break
print(judge_s(s))
