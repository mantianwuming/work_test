import sys
t = int(sys.stdin.readline().strip())

def cal_xor(s):
    xr = 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            xr += 1
    return xr

def cal_zero_one(s):
    zeros = 0
    ones = 0
    for i in range(len(s)):
        if s[i] == 1:
            ones += 1
        if s[i] == 0:
            zeros += 1
    if zeros >= ones:
        return ones
    else:
        return zeros

def cal_min_xr(s):
    min_xr = len(s)
    min_s = []
    flag = cal_zero_one(s)
    for i in range(len(s)):
        x = s[:i] + s[i+1:]
        xr = cal_xor(x)
        if xr < min_xr:
            min_xr = xr
            min_s = x
    return min_xr, min_s

def solution(s):
    klist = [len(s) for _ in range(len(s))]
    xr = cal_xor(s)
    for i in range(xr, len(klist)):
        klist[i] = 0
    time = 0
    min_s = s
    min_xr = xr
    while min_xr > 0:
        min_xr, min_s = cal_min_xr(min_s)
        print(min_xr, min_s)
        time += 1
        for i in range(min_xr, len(klist)):
            if klist[i] == len(s):
                klist[i] = time
    klist[0] = cal_zero_one(s)
    return klist

for i in range(t):
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    s = []
    for j in range(len(line)):
        s.append(int(line[j]))
    klist = solution(s)
    print('Case #' + str(i+1) + ':')
    for i in range(len(klist)):
        print(klist[i], end = ' ')



# import sys
# t = int(sys.stdin.readline().strip())

# def cal_xor(s):
#     xr = 0
#     for i in range(1, len(s)):
#         if s[i] != s[i-1]:
#             xr += 1
#     return xr

# def cal_min_xr(s):
#     min_xr = len(s)
#     min_s = []
#     for i in range(len(s)):
#         x = s[:i] + s[i+1:]
#         xr = cal_xor(x)
#         if xr < min_xr:
#             min_xr = xr
#             min_s = x
#     return min_xr, min_s

# def solution(s):
#     klist = [len(s) for _ in range(len(s))]
#     xr = cal_xor(s)
#     for i in range(xr, len(klist)):
#         klist[i] = 0
#     time = 0
#     min_s = s
#     min_xr = xr
#     while min_xr > 0:
#         min_xr, min_s = cal_min_xr(min_s)
#         time += 1
#         for i in range(min_xr, len(klist)):
#             if klist[i] == 5:
#                 klist[i] = time
#     klist[0] = 
#     return klist

# for i in range(t):
#     n = int(sys.stdin.readline().strip())
#     line = sys.stdin.readline().strip()
#     s = []
#     for j in range(len(line)):
#         s.append(int(line[j]))
#     klist = solution(s)
#     print('Case #' + str(i+1) + ':')
#     for i in range(len(klist)):
#         print(klist[i], end = ' ')