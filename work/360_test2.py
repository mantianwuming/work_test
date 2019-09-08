import sys


def change(a, b, n, m):
    num = 0
    alist = []
    while a and b:
        for i in range(len(a)):
            for j in range(len(b)):
                sum = a[i] + b[j]
                if sum%m > num:
                    num = sum % m
                    x = a[i]
                    y = b[j]
        a.remove(x)
        b.remove(y)
        alist.append(num)
        num = 0
    return alist
        

if __name__ == '__main__':
    a = [4,4,1,1,1]
    b = [4,3,0,1,2]
    m = 5
    n = 5
    print(change(a,b,m,n))