import sys

def get_lastNumber(n):
    if(n < 1):
        return - 1
    last_number = 0
    for i in range(2, n+1):
        last_number = (last_number + 3) % i
    return last_number+1

n = int(sys.stdin.readline().strip())
ans = get_lastNumber(n)
print(ans)