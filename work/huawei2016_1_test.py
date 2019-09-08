# coding = gbk
# 输入包括多组测试数据。
# 每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
# 学生ID编号从1编到N。
# 第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
# 接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
# 当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。

m,n = map(int,input().split())
glist = list(map(int, input().split()))
x = []
for i in range(n):
    op_list = list(input().split())
    if op_list[0] == 'Q':
        num1, num2 = int(op_list[1]), int(op_list[2])
        num1, num2= min(num1, num2), max(num1, num2)
        glist1 = glist[num1-1:num2]
        # print(glist1)
        x.append(max(glist1))
    if op_list[0] == 'U':
        num1, num2 = int(op_list[1]), int(op_list[2])
        glist[num1-1] = num2
        # print(glist)

for i in range(len(x)):
    print(x[i])
