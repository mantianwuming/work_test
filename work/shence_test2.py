import sys

def string2dec(string):
    n = len(string)
    sum = 0
    for i in range(n):
        sum += (ord(string[i]) - 97) * (26 ** (n-i-1))
    return sum


string = sys.stdin.readlines()
for i in string:
    i = i.strip()
    print(string2dec(i))