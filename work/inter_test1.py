import sys
num = sys.stdin.readline()[:-1]
k = int(sys.stdin.readline())
class Solution:
    def minSwap(self, num):
        '''
        若最高位数字不是最大，则将其余位中的最大数字与最高位交换。
        若其余位中的最大数字不止一个，则将位数最低的那个与最高位交换。
        若最高位数字是最大，则对除去最高位的剩余数字进行递归操作。
        '''
        a = []
        for val in num:
            a.append(int(val))
        b = sorted(a)
        if a == b:
            return num
        i, l = 0, len(a)
        while i < l:
            if a[i] == b[i]:
                i += 1
            else:break
        for j in range(l-1, -1, -1):
            if a[j] == b[i]:
                a[j] = a[i]
                a[i] = b[i]
                break
        s = ''
        for x in a:
            s += str(x)
        return s
s = Solution()
for _ in range(k):
    num = s.minSwap(num)
print(num)