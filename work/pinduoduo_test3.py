n = int(input())
max_values = list(map(int, input().split()))
max_values.sort()

def get_expectation(n, max_values):
    max_num = max(max_values)
    dp = [[0 for _ in range(max_num+1)] for _ in range(n+1)]
    for i in range(1, max_values[0]+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, max_values[i-1] + 1):
            # if j <= max_values[i-2]:
            #     dp[i][j] = sum(dp[i-1][:j+1]) + dp[i-1][j] * (j-1)
            # else:
            #     total = 1
            #     for m in range(i):
            #         total *= max_values[m]
            #     dp[i][j] = (total - sum(dp[i][:max_values[i-2]+ 1])) // (max_values[i-1] - max_values[i-2])
            dp[i][j] = sum(dp[i-1][:j+1]) + dp[i-1][j] * (j-1)
    return dp


dp = get_expectation(n, max_values)
sum = 0
for i in range(1, max(max_values)+ 1):
    sum = sum + dp[-1][i] * i
total = 1
for m in range(len(max_values)):
    total *= max_values[m]
num = sum / total
num = round(num, 2)
print(num)
