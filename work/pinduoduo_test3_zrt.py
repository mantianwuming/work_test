import sys 
n = int(sys.stdin.readline())
nums = [int(i) for i in sys.stdin.readline().split()]

h = n 
w = max(nums)
dp = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    dp[i][0] = 1
for i in range(nums[0]):
    dp[0][i] = 1
for i in range(1, h):
    for j in range(1, w):
        if j < nums[i]:
            dp[i][j] = sum(dp[i-1][0:j+1]) + dp[i-1][j] * j
        else:
            dp[i][j] = dp[i-1][j] * nums[i]

ps = dp[-1]
total = sum(ps)
res = 0
for i in range(len(ps)):
    val = i+1
    res += val * ps[i] / total
res = round(res, 2)
print(res)