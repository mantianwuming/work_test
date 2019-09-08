import sys
t = int(sys.stdin.readline().strip())
for i in range(t):
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    nums = list(map(int, line.split()))

    print(sum(nums))

t = int(input())
for i in range(t):
    n = int(input())
    line = input()
    nums = list(map(int, line.split()))

    print(sum(nums))