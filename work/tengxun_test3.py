import sys
class jie:
    def __init__(self):
        self.jies = [1]
        self.ind = 0
    def get(self, n):
        if n > self.ind:
            for i in range(self.ind+1, n+1):
                cur = self.jies[-1] * i
                self.jies.append(cur)
                self.ind += 1
        return self.jies[n]    

def cal_c(jie, down, up):
    res = jie.get(down) / (jie.get(up) * jie.get(down-up))
    # print('C', down, up, res)
    return res
# jie = jie()
# print(cal_c(jie, 10,1))
def cal_g(num1, num2):
    num1, num2 = max(num1, num2), min(num1, num2)
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def cal_res(res, total):
    n = 0
    while (1000000007 * n + res) % total != 0:
        n += 1
    return (1000000007 * n + res) / total

[n, p, q] = [int(i) for i in sys.stdin.readline().split()]
p_l = []
jie = jie()
for i in range(p, n-q+1):
    num = cal_c(jie, n, i)
    p_l.append(num)

total = sum(p_l)
res = 0 
for i in range(p, n-q+1):
    res = res + i * p_l[i-p]
g = cal_g(res, total)
res = res / g 
total = total / g
res = round(cal_res(res, total))
print(res)