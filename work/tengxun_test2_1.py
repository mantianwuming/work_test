import sys
maxn = 10 ** 5 + 10
mod = 10 ** 9 + 7
dp = [1 for _ in range(maxn+1)]
sum = [0 for _ in range(maxn+1)]

n, k = [int(i) for i in sys.stdin.readline().split()]
l = []
for i in range(k, maxn):
    dp[i] = dp[i-1] + dp[i-k]
    dp[i] %= mod
sum[0] = 0
for i in range(1, maxn):
    sum[i] = sum[i-1] + dp[i]
    sum[i] %= mod
for _ in range(n):
    l, r = [int(i) for i in sys.stdin.readline().split()]
    print((sum[r] - sum[l-1] + mod)%mod)