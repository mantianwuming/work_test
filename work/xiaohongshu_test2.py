import sys 
n = int(sys.stdin.readline().strip())4
nums = [int(i) for i in sys.stdin.readline().split()]

# def solution(nums):
#     length = len(nums)
#     profit = [[0, 0] for _ in range(length+1)]
#     number = [[0, 0] for _ in range(length+1)]
#     for i in range(1, length+1):
#         if profit[i-1][0] > profit[i-1][1]:
#             profit[i][0] = profit[i-1][0]
#             number[i][0] = number[i-1][0]
#         else:
#             profit[i][0] = profit[i-1][1]
#             number[i][0] = number[i-1][1]
#         profit[i][1] = nums[i-1] + profit[i-1][0]
#         number[i][1] = number[i-1][0] + 1
#     # print(profit)
#     # print(number)
#     if profit[-1][0] > profit[-1][1]:
#         return profit[-1][0], number[-1][0]
#     else:
#         return profit[-1][1], number[-1][1]

# p, n = solution(nums)
# print(p, n)

def solution(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [[0,0] for i in range(n+1)]
    dp[1] = [nums[0], 1]
    for i in range(2, n+1):
        dp[i][0] = max(dp[i-1][0], dp[i-2][0] + nums[i-1])
        if dp[i][0] == dp[i-1][0]:
            dp[i][1] = dp[i-1][1]
        else:
            dp[i][1] = dp[i-2][1] + 1
    return dp[-1]

res = solution(nums)
print(res[0], res[1])

    