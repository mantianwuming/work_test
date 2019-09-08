import sys

def judge(t, word):
    n = len(t)
    length = len(word)
    if n % length == 0:
        times = n // length
    else:
        times = n // length + 1
    s = ''
    for i in range(times):
        s += word
        if i < times - 1:
            if s != t[:length*(i+1)]:
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