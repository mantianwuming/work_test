import sys

def cal_scores(blocks):
    i = 0
    scores = 0
    flag = 0
    while i >= 0 and i < len(blocks):
        if blocks[i] == 0:
            if flag == 0:
                blocks = blocks[:i] + blocks[i+1:]
            else:
                blocks = blocks[:i] + blocks[i+1:]
                i -= 1
        elif blocks[i] != '>' and blocks[i] != '<':
            scores += blocks[i]
            blocks[i] -= 1
            if flag == 0:
                i += 1
            else:
                i -= 1
        elif blocks[i] == '>' and i + 1 < len(blocks) and blocks[i+1] not in ['>', '<']:
            flag = 0
            i += 1
        elif blocks[i] == '>' and i + 1 < len(blocks) and blocks[i+1] in ['>','<']:
            flag = 0
            blocks = blocks[:i] + blocks[i+1:]
        elif blocks[i] == '<' and i - 1 >= 0 and blocks[i-1] not in ['>','<']:
            flag = 1
            i -= 1
        elif blocks[i] == '<' and i - 1 >= 0 and blocks[i-1] in ['>','<']:
            flag = 1
            blocks = blocks[:i] + blocks[i+1:]
            i -= 1
        else:
            if blocks[i] == '<':
                flag = 1
            if blocks[i] == '>':
                flag = 0
            if flag == 0:
                i+=1
            else:
                i -= 1
    return scores

# n, m, q = map(int, sys.stdin.readline().strip().split())
# blocks = sys.stdin.readline().strip().split()
# for i in range(len(blocks)):
#     if blocks[i] != '>' and blocks[i] != '<':
#         blocks[i] = int(blocks[i])
# for _ in range(q):
#     l, r = map(int, sys.stdin.readline().strip().split())
#     ans = cal_scores(blocks[l-1:r])
#     print(ans)

blocks = ['>',-1,'<']
print(cal_scores(blocks))