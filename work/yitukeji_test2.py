import sys

def dijkstra(graph, start, cake):
    min_dis = [0 for _ in range(len(graph))]
    flag = [True for _ in range(len(graph))]
    cake_num = [cake[start] for _ in range(len(graph))]
    for i in range(len(min_dis)):
        min_dis[i] = graph[start][i]
    flag[start] = False

    for p in range(1, len(graph)):
        min_val = 99999999
        min_ind = 0
        for i in range(len(min_dis)):
            if min_dis[i] < min_val and flag[i]:
                min_val = min_dis[i]
                min_ind = i
        flag[min_ind] = False
        if p < len(graph) - 1:
            cake_num[min_ind] += cake[min_ind]
        for i in range(len(graph)):
            if i != min_ind and min_dis[min_ind] + graph[min_ind][i] <= min_dis[i]:
                min_dis[i] = min_dis[min_ind] + graph[min_ind][i]
                if cake_num[min_ind] + cake[i] > cake_num[i]:
                    cake_num[i] = cake_num[min_ind] + cake[i]
    return min_dis, cake_num

line = sys.stdin.readline().strip()
n, m, s, d = map(int, line.split())
line = sys.stdin.readline().strip()
cake = list(map(int, line.split()))

graph = [[9999999 for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    line = sys.stdin.readline().strip()
    i, j, t = map(int, line.split())
    graph[i-1][j-1] = t
    graph[j-1][i-1] = t

min_dis, cake = dijkstra(graph, s-1, cake)
print(min_dis[d-1], cake[d-1])