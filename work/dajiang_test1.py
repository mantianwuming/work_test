def solution(nums):
    if nums == []:
        return 0
    dp = [0 for _ in range(len(nums))]
    max_len = 0
    for i in range(len(nums)):
        dp[i] = 1
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        if dp[i] > max_len:
            max_len = dp[i]
    return max_len