import sys
r, c = map(int, sys.stdin.readline().strip().split())
graph = []
for i in range(r):
    line = sys.stdin.readline().strip()
    row = []
    for i in line:
        row.append(i)
    graph.append(row)
a, b, c, d = map(int, sys.stdin.readline().strip().split())
graph[a][b], graph[c][d] = graph[c][d], graph[a][b]

def find(graph, flag, i, j):
    if flag[i][j] == 1 or graph[i][j] == '#':
        return
    h = len(graph)
    w = len(graph[0])
    if i-2 >= 0 and graph[i][j] == graph[i-1][j] and graph[i][j] == graph[i-2][j]:
        ind = i 
        while ind >= 0 and graph[ind][j] == graph[i][j]:
            flag[ind][j] = 1
            ind -= 1
    if i+2 < h and graph[i][j] == graph[i+1][j] and graph[i][j] == graph[i+2][j]:
        ind = i 
        while ind < h and graph[ind][j] == graph[i][j]:
            flag[ind][j] = 1
            ind += 1
    if j-2 >= 0 and graph[i][j] == graph[i][j-1] and graph[i][j] == graph[i][j-2]:
        ind = j
        while ind >= 0 and graph[i][ind] == graph[i][j]:
            flag[i][ind] = 1
            ind -= 1
    if j+2 < w and graph[i][j] == graph[i][j+1] and graph[i][j] == graph[i][j+2]:
        ind = j
        while ind < w and graph[i][ind] == graph[i][j]:
            flag[i][ind] = 1
            ind += 1

def find_all(graph):
    h = len(graph)
    w = len(graph[0])
    flag = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            find(graph, flag, i, j)
    return flag

def xiaoxiao(cur_graph, flag):
    h = len(cur_graph)
    w = len(cur_graph[0])
    for i in range(h):
        for j in range(w):
            if flag[i][j] == 1:
                cur_graph[i][j] = '#'

    for i in range(0, h-1):
            for j in range(w):
                if cur_graph[i][j] != '#' and cur_graph[i+1][j] == '#':
                    cur_graph[i][j], cur_graph[i+1][j] = cur_graph[i+1][j], cur_graph[i][j]
    for i in range(h-1, 0, -1):
        for j in range(w):
            if cur_graph[i-1][j] != '#' and cur_graph[i][j] == '#':
                cur_graph[i][j], cur_graph[i-1][j] = cur_graph[i-1][j], cur_graph[i][j]
    return cur_graph

def judge(flag):
    h = len(flag)
    w = len(flag[0])
    for i in range(h):
        for j in range(w):
            if flag[i][j] == 1:
                return True 
    return False

def count(graph):
    h = len(graph)
    w = len(graph[0])
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                count += 1
    return count

# graph = [
#     ['H','F','C','E'], 
#     ['G','C','A','C'], 
#     ['G','F','A','D'], 
#     ['D','C','A','B']
# ]
flag = find_all(graph)
while judge(flag):
    cur_graph = xiaoxiao(graph, flag)
    graph = cur_graph
    # for l in cur_graph:
    #     print(l)
    # print()
    flag = find_all(graph)
print(count(graph))