# coding = gbk
# 平安果
# 简要描述：
# 给定一个M行N列的矩阵（M*N个格子），每个格子中放着一定数量的平安果。
# 你从左上角的各自开始，只能向下或者向右走，目的地是右下角的格子。
# 每走过一个格子，就把格子上的平安果都收集起来。求你最多能收集到多少平安果。
# 注意：当经过一个格子时，需要一次性把格子里的平安果都拿走。
# 限制条件：1<N,M<=50；每个格子里的平安果数量是0到1000（包含0和1000）.
# 输入描述：
# 输入包含两部分：
# 第一行M, N
# 接下来M行，包含N个平安果数量
# 输出描述：
# 一个整数
# 最多拿走的平安果的数量
# 示例：
# 输入
# 2 4
# 1 2 3 40
# 6 7 8 90
# 输出
# 136
#
# 思路：动态规划
# 动态方程：当前位置能够获得的最大苹果数=max(从上面走能够获得最大苹果+从左边走能获得最大苹果）
# dp(0,0)=app[0][0]

import numpy as np
m,n = map(int, input().split())
x = np.zeros((m,n))
for i in range(m):
    x[i] = list(map(int,input().split()))

def max_x(m,n,x):
    if m == n == 0:
        return x[0][0]
    if m == 0:
        return x[m][n] + max_x(m, n-1, x)
        # print(res)
    if n == 0:
        return x[m][n] + max_x(m-1, n, x)
        # print(res)
    else:
        return max(x[m][n] + max_x(m-1,n,x), x[m][n] + max_x(m, n-1, x))

def max_x(m,n,x):
    if m == 0 and n == 0:
        return x[0][0]
    elif m == 0:
        return x[m][n] + max_x(m, n-1, x)
    elif n == 0:
        return x[m][n] + max_x(m-1, n ,x)
    else:
        return max(x[m][n] + max_x(m, n-1, x), x[m][n] + max_x(m-1, n, x))

res = max_x(m-1,n-1,x)
print(res)
