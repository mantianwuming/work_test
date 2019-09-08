import sys

def judge(t, word):
    n = len(t)
    s = word
    while len(s) < n:
        s += s
        if len(s) <= n:
            if s != t[:len(s)]:
                return False
    s = s[:n]
    if s == t:
        return True
    else:
        return False

n = int(sys.stdin.readline().strip())
t = sys.stdin.readline().strip()
m = int(sys.stdin.readline().strip())
words = []
for i in range(m):
    word = sys.stdin.readline().strip()
    words.append(word)
count = 0
for word in words:
    if judge(t, word):
        count += 1
print(count)



