n,m = map(int, input().split())
dis = []
for i in range(m):
    d = int(input())
    dis.append(d)

length = len(dis)
new_length = 2 ** length
res = float('inf')
for i in range(new_length):
    temp = i
    result = 0
    max_num = 0
    min_num = 0
    for j in range(length):
        if temp % 2 == 1:
            result += dis[j]
        else:
            result -= dis[j]
        if result > max_num:
            max_num = result
        if result < min_num:
            min_num = result
        temp //= 2
    if max_num - min_num < res and max_num - min_num < n:
        res = max_num - min_num
if res >= n:
    print(0)
else:
    res = (n-res + 1) * 2
    print(res)
class solution:
    def __init__(self):
        self.setx = [] 
    def dp(self, dis, index, position, n, x):
        if index >= len(dis) and position >= 0 and position < n:
            self.setx.append(position)
            return

        if dis[index] <= position:
            self.dp(dis, index+1, position - dis[index], n, x)
        
        if dis[index] <= n - position -1:
            self.dp(dis, index+1, position + dis[index], n, x)

