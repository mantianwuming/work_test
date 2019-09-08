# import sys
# graph = []
# for i in range(5):
#     line = sys.stdin.readline().strip()
#     values = list(map(int, line.split()))
#     graph.append(values)

class Solution:
    def __init__(self):
        self.visited = []
        self.max_res = 25

    def connected(self,graph, i, j):
        num = graph[i][j]
        if 0 <= i + 1 <= 4 and 0 <= j <= 4 and graph[i+1][j] == num and [i + 1,j] not in self.visited:
            self.visited.append([i + 1,j])
            self.connected(graph, i+1, j)
        if 0 <= i - 1 <= 4 and 0 <= j <= 4 and graph[i-1][j] == num and [i - 1,j] not in self.visited:
            self.visited.append([i - 1,j])
            self.connected(graph, i-1, j)
        if 0 <= i <= 4 and 0 <= j + 1 <= 4 and graph[i][j+1] == num and [i,j + 1] not in self.visited:
            self.visited.append([i,j + 1])
            self.connected(graph, i, j+1)
        if 0 <= i <= 4 and 0 <= j - 1 <= 4 and graph[i][j-1] == num and [i,j - 1] not in self.visited:
            self.visited.append([i,j - 1])
            self.connected(graph, i, j-1)
        return self.visited

    def eliminate(self,graph):
        for i in range(5):
            for j in range(5):
                self.visited = []
                res = 0
                cons = self.connected(graph, i, j)
                if len(cons) >= 3:
                    for m in range(len(cons)):
                        graph[cons[m][0]][cons[m][1]] = 0
                    self.after(graph)
                    for x in range(5):
                        for y in range(5):
                            if graph[x][y] != 0:
                                res += 1

                    
                                


    def after(self,graph):
        for i in range(4):
            for j in range(5):
                if graph[i][j] != 0 and graph[i+1][j] == 0:
                    graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
        

            
    

if __name__ == "__main__":
    s = Solution()
    graph = [[3, 1, 2, 1, 1], [1, 1, 1, 1, 3], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [3, 1, 2, 2, 2]]
    s.eliminate(graph)
    print(graph)