import sys

def judge(nums, n):
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1
    num = max(dic.values())
    if num > n//2:
        return False
    else:
        return True

t = int(sys.stdin.readline().strip())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))
    if judge(nums, n):
        print('YES')
    else:
        print('NO')



