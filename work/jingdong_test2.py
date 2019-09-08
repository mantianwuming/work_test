class solution:
    def __init__(self):
        self.res = 999

    def find(self, cur_graph, i, j, flag):
        if i - 1 >= 0 and flag[i-1][j] and cur_graph[i][j] == cur_graph[i-1][j]:
            flag[i-1][j] = False
            self.cur.append([i-1, j])
            self.find(cur_graph, i-1, j, flag)
        if j - 1 >= 0 and flag[i][j-1] and cur_graph[i][j] == cur_graph[i][j-1]:
            flag[i][j-1] = False
            self.cur.append([i, j-1])
            self.find(cur_graph, i, j-1, flag)
        if i + 1 < 5 and flag[i+1][j] and cur_graph[i][j] == cur_graph[i+1][j]:
            flag[i+1][j] = False
            self.cur.append([i+1, j])
            self.find(cur_graph, i+1, j, flag)
        if j + 1 < 5 and flag[i][j+1] and cur_graph[i][j] == cur_graph[i][j+1]:
            flag[i][j+1] = False
            self.cur.append([i, j+1])
            self.find(cur_graph, i, j+1, flag)
    
    def find_all(self, cur_graph):
        ops = []
        flag = [[True for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if flag[i][j] and cur_graph[i][j] != 0:
                    self.cur = [[i, j]]
                    flag[i][j] = False
                    self.find(cur_graph, i, j, flag)
                    if len(self.cur) >= 3:
                        ops.append(self.cur[:])
        return ops, flag
    
    def xiaoxiao(self, cur_graph, op):
        for i, j in op:
            cur_graph[i][j] = 0
        for i in range(4):
            for j in range(5):
                if cur_graph[i][j] != 0 and cur_graph[i+1][j] == 0:
                    cur_graph[i][j], cur_graph[i+1][j] = cur_graph[i+1][j], cur_graph[i][j]
        return cur_graph
    
    def main(self, cur_graph):
        ops, flag = self.find_all(cur_graph)
        if len(ops) == 0:
            for l in cur_graph:
                print(l)
            print()
            count = 0
            for i in range(5):
                for j in range(5):
                    if cur_graph[i][j] != 0:
                        count += 1
            if count < self.res:
                self.res = count
            return 
        # print(ops)
        for op in ops:
            # print(op)
            # for l in cur_graph:
            #     print(l)
            # print()
            temp_graph = [] 
            for l in cur_graph:
                temp_graph.append(l[:])
            temp_graph = self.xiaoxiao(temp_graph, op)
            self.main(temp_graph)
    


graph = [[3, 1, 2, 1, 1], \
     [1, 1, 1, 1, 3], \
     [1, 1, 1, 1, 1], \
     [1, 1, 1, 1, 1], \
     [3, 1, 2, 2, 2]]
s = solution()
s.main(graph)
print(s.res)
