n = int(input())
alist = []
for i in range(n):
    line = input()
    values = list(map(int, line.split()))
    alist.append(values)

def get_min_time(alist):
    n = len(alist)
    xsum = 0
    for i in range(n):
        xsum += sum(alist[i])
    dp = [[xsum for _ in range(2)] for _ in range(n)]
    dp[0][0] = alist[0][0] + alist[0][2]
    dp[0][1] = alist[0][1]
    for i in range(1,n):
        for j in range(2):
            t1 = dp[i-1][j] + alist[i][j]
            t2 = dp[i-1][1-j] + alist[i][j] + alist[i][2]
            print(i,j)
            dp[i][j] = min(t1, t2)
    return min(dp[n-1][0], dp[n-1][1])

print(get_min_time(alist))
