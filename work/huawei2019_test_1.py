import sys 

def rotateString(A, B):
    if B in A:
        return 1
    for i in range(len(A)):
        # words = A[i:] + A[:i]
        # if words[:len(B)] == B:
        #     return 1
        if B in (A[i:] + A[:i]):
            return 1
    return 0

alist = []
for i in range(6):
    line = sys.stdin.readline().strip()
    alist.append(line)

for i in range(len(alist)//2):
    print(rotateString(alist[2*i], alist[2*i + 1]), end='')
