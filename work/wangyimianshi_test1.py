'''
投n个骰子，求和大于x的概率。

思路：我们知道，如果只有一个骰子，那么它的可能区间是1到6，如果两个骰子，那么可能的区间是是2到12，如果是3个骰子，那么可能的区间是3到18，如果是n个骰子，那么可能的区间是n到6*n。
我们创建一个数组，每一行代表每一种情况，第一行代表一个骰子的情况，第二行代表两个投资的情况，第三行代表三个骰子的情况。。。

我们假设有n个骰子，总的点数和为sum，那么在前面n-1个骰子的情况，最后一个可以有Sum-1、Sum-2、Sum-3、Sum-4、Sum-5、Sum-6的六种情况，而最后的那个骰子有下面的情况：

（n-1，sum-1）：第n个骰子扔出了1，等同n-1个骰子扔出了sum-1的情况。

（n-1，sum-2）：第n个骰子扔出了2，等同n-1个骰子扔出了sum-2的情况。

（n-1，sum-3）：第n个骰子扔出了3，等同n-1个骰子扔出了sum-3的情况。

（n-1，sum-4）：第n个骰子扔出了4，等同n-1个骰子扔出了sum-4的情况。

（n-1，sum-5）：第n个骰子扔出了5，等同n-1个骰子扔出了sum-5的情况。

（n-1，sum-6）：第n个骰子扔出了6，等同n-1个骰子扔出了sum-6的情况。

那么n个骰子扔出了sum的情况等于上面六种情况相加。

 n = 1时：f(1,1) = f(1,2) = f(1,3) = f(1,4) = f(1,5) = f(1,6) = 1
而 n = 2时：f(2,2) = f(1,1) = 1

f(2,3) = f(1,2) + f(1,1) = 2

...
f(2,6) = f(1,5) + f(1,4) + f(1,3) + f(1,2) + f(1,1)
f(2,7) = f(1,6) + f(1,5) + f(1,4) + f(1,3) + f(1,2) + f(1,1) = 6


'''
def larger_than_x(n, x):
    dp = [[0 for _ in range(6*n + 1)] for _ in range(n+1)]
    dp[1][1], dp[1][2], dp[1][3], dp[1][4], dp[1][5], dp[1][6] = 1, 1, 1, 1, 1, 1
    for i in range(2, n+1):
        for j in range(i, 6*i + 1):
            x1, x2, x3, x4, x5, x6 = 0, 0, 0, 0, 0, 0
            if j - 1 > 0:
                x1 = dp[i-1][j-1]
            if j - 2 > 0:
                x2 = dp[i-1][j-2]
            if j - 3 > 0:
                x3 = dp[i-1][j-3]
            if j - 4 > 0:
                x4 = dp[i-1][j-4]
            if j - 5 > 0:
                x5 = dp[i-1][j-5]
            if j - 6 > 0:
                x6 = dp[i-1][j-6]
            dp[i][j] = x1 + x2 + x3 + x4 + x5 + x6
    
    total = sum(dp[-1])
    larger_num = 0
    for i in range(9, len(dp[-1])):
        larger_num += dp[-1][i]
    prob = larger_num / total
    return prob



if __name__ == "__main__":
    print(larger_than_x(3, 9))
    