def addSum(n, target):
    if nums[n] == target:
        flag = True
    elif n == 1:
        return
    else:
        addSum(n-1, target-nums[n])
        addSum(n-1, target)

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    n = len(nums) -1
    target = 12
    flag = False
    addSum(n, target)
    if flag:
        print('yes')
    else:
        print('no')
