import sys
s = sys.stdin.readline().strip()
a_asc = ord('A')

class solution:
    def __init__(self):
        self.res = []
    
    def part(self, s, index, cur):
        if index == len(s):
            self.res.append(cur[:])
        else:
            if int(s[index]) == 0:
                res = int(s[index-1:index+1])
                new_cur = cur + chr(a_asc - 1 + res)
                self.part(s, index+1, new_cur)
            elif int(s[index]) > 6:
                if index - 1 >= 0 and int(s[index-1]) == 1:
                    res = int(s[index-1:index+1])
                    new_cur = cur[:-1] + chr(a_asc - 1 + res)
                    slef.part(s, index+1, new_cur)
                res = int(s[index:index+1])
                new_cur = cur + chr(a_asc - 1 + res)
                self.part(s, index + 1, new_cur)
            else:
                if index - 1 >= 0 and int(s[index-1]) in [1, 2]:
                    res = int(s[index-1:index+1])
                    new_cur = cur[:-1] + chr(a_asc - 1 + res)
                    self.part(s, index+1, new_cur)
                res = int(s[index:index+1])
                new_cur = cur + chr(a_asc - 1 + res)
                self.part(s, index+1, new_cur)

so = solution()
so.part(s, 0, '')
res = sorted(so.res)
for i in res:
    print(i)