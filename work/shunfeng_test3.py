n, m, k = map(int, input().split())
peoples = [i for i in range(n+1)]
language_info = [0 for i in range(m+1)]

def find(peoples, i):
    cur = i
    while peoples[cur] != cur:
        cur = peoples[cur]
    return cur

for _ in range(k):
    u, v = map(int, input().split())
    if language_info[v] == 0:
        language_info[v] = u
        continue
    if peoples[u] == u:
        peoples[u] = language_info[v]
    else:
        # temp = find(peoples, u)
        # peoples[language_info[v]] = temp
        # language_info[v] = temp
        head_u = find(peoples, u)
        peoples[language_info[v]] = head_u
        change_head = language_info[v]
        for i in range(len(language_info)):
            if language_info[i] == change_head:
                language_info[i] = head_u
res = [0 for i in range(n + 1)]
for i in range(1, n+1):
    x = find(peoples, i)
    if res[x] == 0:
        res[x] = 1
result = sum(res) - 1
print(result)
