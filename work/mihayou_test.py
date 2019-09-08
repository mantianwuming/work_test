import sys
r, c = map(int, sys.stdin.readline().strip().split())
matrix = []
for i in range(r):
    line = sys.stdin.readline().strip()
    row = []
    for i in line:
        row.append(i)
    matrix.append(row)
a, b, c, d = map(int, sys.stdin.readline().strip().split())
matrix[a][b], matrix[c][d] = matrix[c][d], matrix[a][b]

def eliminate(matrix):
    h = len(matrix)
    w = len(matrix[0])
    flag = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            find(matrix, flag, i, j)
    down(matrix, flag)
    return matrix, flag

def down(matrix, flag):
    h = len(matrix)
    w = len(matrix[0])
    for i in range(h):
        for j in range(w):
            if flag[i][j] == 1:
                matrix[i][j] = '#'
    for i in range(h-1, 0, -1):
        for j in range(w):
            if matrix[i][j] == '#' and matrix[i-1][j] != '#':
                matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j]
    for i in range(h-1):
        for j in range(w):
            if matrix[i][j] != '#' and matrix[i+1][j] == '#':
                matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

def judge(flag):
    h = len(flag)
    w = len(flag[0])
    for i in range(h):
        for j in range(w):
            if flag[i][j] == 1:
                return True
    return False
            
def find(matrix, flag, i, j):
    h = len(matrix)
    w = len(matrix[0])
    if flag[i][j] == 1:
        return
    if matrix[i][j] == '#':
        return
    if i - 2 >= 0 and matrix[i][j] == matrix[i-1][j] and matrix[i][j] == matrix[i-2][j]:
        flag[i][j] = 1
        flag[i-1][j] = 1
        flag[i-2][j] = 1
    if i + 2 < h and matrix[i][j] == matrix[i+1][j] and matrix[i][j] == matrix[i+2][j]:
        flag[i][j] = 1
        flag[i+1][j] = 1
        flag[i+2][j] = 1
    if j - 2  >= 0 and matrix[i][j] == matrix[i][j-1] and matrix[i][j] == matrix[i][j-2]:
        flag[i][j] = 1
        flag[i][j-1] = 1
        flag[i][j-2] = 1
    if j + 2 < w and matrix[i][j] == matrix[i][j-1] and matrix[i][j] == matrix[i][j+2]:
        flag[i][j] = 1
        flag[i][j+1] = 1
        flag[i][j+2] = 1

def count(matrix):
    h = len(matrix)
    w = len(matrix[0])
    count = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '#':
                count += 1
    return count
    
_, flag = eliminate(matrix)
while judge(flag):
    matrix, flag = eliminate(matrix)
print(count(matrix))