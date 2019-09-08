#nums代表一个列表，比如[1,2,3,4]
k = int(input())
def solution(nums):
    x = nums
    if x == sorted(nums) or x == sorted(nums,reverse=True):
        return 'Yes'
    else:
        return 'No'
for i in range(k):
    n = int(input())
    line = input()
    nums = list(map(int, line.split()))
    print(solution(nums))



# def solution(nums):
#     x = nums
#     if x == sorted(nums) or x == sorted(nums,reverse=True):
#         return 'YES'
#     else:
#         return 'NO'

# nums = [4,3,2,1] #[1,2,3,4]
# print(solution(nums))
