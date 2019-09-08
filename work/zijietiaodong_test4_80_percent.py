import sys
s = sys.stdin.readline().strip()
a_asc = ord('A')

class solution:
    def __init__(self):
        self.res = []
    
    def part(self, s, index, cur):
        if index == len(s):
            if cur not in self.res:
               self.res.append(cur[:])
        else:
            if int(s[index]) == 0:
                new_cur = cur[:]
                self.part(s, index+1, new_cur)
            elif int(s[index]) == 1:
                if index+1 < len(s):
                    if not (index+1 < len(s) and int(s[index+1] == 0)):
                        res = int(s[index:index+2])
                        new_cur = cur[:] + chr(a_asc - 1 + res)
                        self.part(s, index+2, new_cur)
                res = int(s[index:index+1])
                new_cur = cur + chr(a_asc - 1 + res)
                self.part(s, index+1, new_cur)
            elif int(s[index]) == 2:
                if index + 1 < len(s) and 0 <= int(s[index+1]) <= 6:
                    if not (index+1 < len(s) and int(s[index+1] == 0)):
                        res = int(s[index:index+2])
                        new_cur = cur[:] + chr(a_asc - 1 + res)
                        self.part(s, index+2, new_cur)
                res = int(s[index:index+1])
                new_cur = cur + chr(a_asc - 1 + res)
                self.part(s, index + 1, new_cur)
            else:
                res = int(s[index:index+1])
                new_cur = cur + chr(a_asc -1 + res)
                self.part(s, index+1, new_cur)

so = solution()
so.part(s, 0, '')
res = sorted(so.res)
for i in res:
    print(i)