# coding=gbk

# 数组中任意几个元素的和是否等于m

def addSum(nums, target):
    nums = sorted(nums)
    loc = 0
    init_loc = 0
    sum = nums[loc]
    stack = []
    stack.append([nums[loc], loc]);
    loc += 1
    while sum != target:
        if loc < len(nums) and sum + nums[loc] <= target:
            sum += nums[loc]
            stack.append([nums[loc], loc])
            loc += 1
        else:
            if stack:
                v = stack.pop()
                sum -= v[0]
                loc = v[1] + 1
            else:
                sum = 0;
                init_loc += 1
                loc = init_loc
    res = []
    while stack:
        res.append(stack.pop()[0])
    return res

nums = [1,2,3,4,5,6]
target = 13
res = addSum(nums, target)
print(res)
