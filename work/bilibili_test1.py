class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        temp = [1 for i in range(n+1)]
        for i in range(1, n):
            if s[i-1] == '0' and s[i] == '0':
                return 0
            if s[i] == '0' and s[i-1] >= '3':
                return 0
            if s[i] == '0':
                temp[i+1] = temp[i-1]
            elif s[i-1] == '1':
                temp[i+1] = temp[i] + temp[i-1]
            elif s[i-1] == '2' and  '1' <= s[i] <= '6':
                temp[i+1] = temp[i] + temp[i-1]
            else:
                temp[i+1] = temp[i]
        return temp[-1]