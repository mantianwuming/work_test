import sys

class Solution:
    def __init__(self):
        self.roads = []
        self.time = []
    
    def dps(self, graph, cur, flag, start, end):
        if cur[-1] == end:
            self.roads.append(cur[:])
            time = 0
            for i in range(1, len(cur)):
                time += graph[cur[i-1]][cur[i]]
            self.time.append(time)
        else:
            temp = cur[-1]
            for i in range(len(graph)):
                if flag[i] and 0 < graph[temp][i] < 9999999999:
                    temp_cur = cur[:]
                    temp_cur.append(i)
                    cur_flag = flag[:]
                    cur_flag[i] = False
                    self.dps(graph, temp_cur, cur_flag, start, end)
        
    def so(self, graph, start, end):
        flag = [True for _ in range(len(graph))]
        flag[start] = False
        cur = [start]
        self.dps(graph, cur, flag, start, end)

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

x = Solution()
x.so(graph, s-1, d-1)
min_time = min(x.time)
res = 0
for i in range(len(x.time)):
    if x.time[i] == min_time:
        num = 0
        for ind in x.roads[i]:
            num += cake[ind]
        if num > res:
            res = num
print(min_time, res)