import numpy as np
num = 6
arr = [11,13,15,15,15,15,15,15,15,17,19,21]
target = 15

def search(arr, target):
    if len(arr) <= 0:
        return -1
    mid = (0 + len(arr))//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return search(arr[:mid], target) 
    else:
        return search(arr[mid+1:],target) + mid + 1

# import sys 
# n = int(sys.stdin.readline())
# nums = [int(i) for i in sys.stdin.readline().split()]
# target = int(sys.stdin.readline())
# # n = 5
# # target = 19
# # nums = [11,13,15,17,21]
# def solution(nums, low, high, target):
#     if low <= high:
#         mid = (low + high) // 2
#         if nums[mid] == target:
#             return mid 
#         elif nums[mid] > target:
#             return solution(nums, low, mid-1, target)
#         elif nums[mid] < target:
#             return solution(nums, mid+1, high, target)
#     else:
#         return -1
# res = solution(nums, 0, n-1, target)
# print(res)

if __name__ == "__main__":
    print(search(arr, target))