# coding = gbk
# �����⣺��ʽ�任
# ����һ��������X��������ĵ�ʽ��ߵ�����֮�����+�Ż���-�ţ�ʹ�õ�ʽ������
# 1 2 3 4 5 6 7 8 9 = X
# ���磺
# 12-34+5-67+89 = 5
# 1+23+4-5+6-7-8-9 = 5
# ���д����ͳ������������������������������
# ���룺 ����������ʽ�ұߵ�����
# ����� ʹ�õ�ʽ�����ĸ���
# �������룺5
# ���������21
# //��̬�滮
# //��̬���̣��е�����⣩����ǰ����=����λ�Ӻ�+����Ϊ����+û�з��ŵ�����
# //dp(before,des,n,ex)= dp(before - 1, before, res + des,1) + dp(before - 1, before, res - des,1) + dp(before - 1, before*pow(10, ex)+des, res,ex+1);
# // before: ��Ҫ�ж��ķ���ǰ������ֵĸ�������ʼΪ8
# // des: ��Ҫ�ж��ķ��ź�������֣���ʼΪ9
# // n:�����ұߵĽ��
# // ex:�׳�������Ϊ���������ֿ��ܣ��Ӻţ����ţ�����û�У����û�У���ôex�����ڼ��㵱ǰֵ

x = int(input())

def count_x(before, des, res, ex):
    if before == 0:
        if des == res:
            return 1
        else:
            return 0
    else:
        return count_x(before-1, before, res+des, 1) + count_x(before-1, before, res-des,1) + count_x(before-1, before*10**ex+des, res, ex+1)

print(count_x(8,9,x,1))
