import sys
s = sys.stdin.readline().strip()
def findlongest(s):
    l, r = 0, -1
    res = 0
    strings = ''
    while l < len(s):
        if r + 1 < len(s) and s[r + 1] not in strings:
            r += 1
            strings += s[r]
        else:
            l += 1
            strings = s[l:r+1]
        if len(strings) > res:
            res = len(strings)
    return res

print(findlongest(s))