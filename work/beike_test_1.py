# import sys
# k = int(sys.stdin.readline().strip())

# n = 0
# sum = 0
# while True:
#     n += 1
#     sum += 1/n
#     if sum > k:
#         break

# print(n)

def GetResult(K):
    n = 0
    sum = 0
    while True:
        n += 1
        sum += 1/n
        if sum > K:
            break
    return n
print(GetResult(3))