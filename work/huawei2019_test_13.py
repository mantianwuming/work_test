import sys
first_peo = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
classes = []
for i in range(n):
    line = sys.stdin.readline().strip()
    line = line.split(',')
    classes.append(line)

visited = []
ready_to_visit = [first_peo]
while ready_to_visit:
    now_peo = ready_to_visit[0]
    if now_peo not in visited:
        visited.append(now_peo)qqqq
    for i in range(len(classes)):
        if now_peo in classes[i]:
            for j in range(len(classes[i])):
                if classes[i][j] not in visited and classes[i][j] not in ready_to_visit:
                    ready_to_visit.append(classes[i][j])
    ready_to_visit.pop(0)

print(len(visited))


        