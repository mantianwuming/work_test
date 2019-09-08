n = 5
nums = [i for i in range(n)]
all_pum = []
def pum(all_pum, nums, index):
    if index == len(nums):
        all_pum.append(nums[:])
    else:
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            pum(all_pum, nums, index+1)
            nums[i], nums[index] = nums[index], nums[i]
    return all_pum

all_pum = pum(all_pum, nums, 0)
print(all_pum)