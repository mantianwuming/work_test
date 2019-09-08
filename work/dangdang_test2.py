#荷兰三色旗问题
import sys

def sort_in_place(nums):
    cur = 0
    l = 0
    r = len(nums) - 1
    while cur <= r:
        if nums[cur] == 0:
            nums[l], nums[cur] = nums[cur], nums[l]
            l += 1
            cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[r] = nums[r], nums[cur]
            r -= 1
        else:
            cur += 1
    return nums

line = sys.stdin.readline().strip()
nums = list(map(int, line.split(',')))
nums = sort_in_place(nums)
s = ''
for i in nums:
    s = s + str(i) + ','
print(s[:-1])