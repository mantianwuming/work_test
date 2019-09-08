def get_min_route(map1):
    dis = map1
    ans = max_dis
    for k in range(1, n+1):
        for i in range(1, k):
            for j in range(i+1, k):
                if ans > dis[i][j] + map1[i][k] + map1[k][j]:
                    ans = dis[i][j] + map1[i][k] + map1[k][j]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    if ans == max_dis:
        return -1
    else:
        return ans

n = int(input())
m = int(input())
max_dis = 999999999
map1 = [[max_dis for _ in range(105)] for _ in range(105)]
for _ in range(m):
    line = input()
    [a, b, t] = [int(i) for i in line.split()]
    map1[a][b] = t
    map1[b][a] = t

ans = get_min_route(map1)
print(ans)