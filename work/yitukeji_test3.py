import sys
line = sys.stdin.readline().strip()
n, k = map(int, line.split())
line = sys.stdin.readline().strip()
nums = list(map(int, line.split()))

def max_d(nums, k):
    for i in range(n):
        nums[i] = nums[i] % 3
    res = 0
    operation = 0
    i = 0

    while operation < k and i < len(nums):
        if nums[i] == 0:
            res += 1
            i += 1
        elif (3 - nums[i]) in nums:
            operation += 1
            nums.remove(3 - nums[i])
            nums.remove(nums[i])
            res += 1
        else:
            if k - operation >= 2 * (nums.count(nums[i]) // 3):
    
                res += nums.count(nums[i]) // 3
            else:
                res += (k - operation)//2

            break
    for j in nums[i:]:
        if j == 0:
            res += 1
    return res

print(max_d(nums, k))