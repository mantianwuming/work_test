n = int(input())
m = int(input())
max_dis = 999999999
map1 = [[max_dis for _ in range(105)] for _ in range(105)]
for _ in range(m):
    a, b, t = map(int, input().split())
    map1[a][b] = t
    map1[b][a] = t

nums = [i for i in range(1, n)]
all_pum = []
def pum(all_pum, nums, index):
    if index == len(nums):
        x = [0] + nums[:] + [0]
        all_pum.append(x)
    else:
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            pum(all_pum, nums, index+1)
            nums[i], nums[index] = nums[index], nums[i]
    return all_pum


alist = pum(all_pum, nums, 0)
min_dis = max_dis
for i in range(len(alist)):
    dis = 0
    for j in range(1, len(alist[i])):
        dis += map1[alist[i][j-1]][alist[i][j]]
    if dis < min_dis:
        min_dis = dis
if min_dis >= max_dis:
    print(-1)
else:
    print(min_dis)    