import sys

def cal_times(nums):
    n = len(nums)
    res = []
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if nums[j] >= nums[i]:
                res.append(j)
                break
    dic = {}
    for i in res:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    max_num = 0
    max_index = 0
    for i in dic.keys():
        if dic[i] > max_num:
            max_num = dic[i]
            max_index = i
    return nums[max_index]

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
print(cal_times(nums))