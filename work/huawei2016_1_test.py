# coding = gbk
# �����������������ݡ�
# ÿ�������һ��������������N��M��0 < N <= 30000,0 < M < 5000��,�ֱ����ѧ������Ŀ�Ͳ�������Ŀ��
# ѧ��ID��Ŵ�1�ൽN��
# �ڶ��а���N��������������N��ѧ���ĳ�ʼ�ɼ������е�i��������IDΪi��ѧ���ĳɼ�
# ��������M�У�ÿһ����һ���ַ�C��ֻȡ��Q����U������������������A,B,��CΪ'Q'��ʱ��, ��ʾ����һ��ѯ�ʲ�������ѯ��ID��A��B������A,B����ѧ�����У��ɼ���ߵ��Ƕ���
# ��CΪ��U����ʱ�򣬱�ʾ����һ�����²�����Ҫ���IDΪA��ѧ���ĳɼ�����ΪB��

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
