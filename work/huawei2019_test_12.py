import sys
line = sys.stdin.readline().strip()
low, high = map(int, line.split())

def get_prime(low, high):
    primes = []
    for i in range(low, high):
        flag = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = 1
                break
        if i != 1 and i != 0 and flag == 0:
            primes.append(i)
    return primes

def isPrime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:   # 两个较小的数进行处理
        return True
    if num % 6 != 1 and num % 6 != 5:  # 不在6的倍数的两侧的一定不是质数
        return False
    tmp = int(num ** 0.5)
    for i in range(5, tmp+1):  # 在6的倍数两侧的也可能不是质数
        if num % i == 0 or num % (i+2) == 0:
            return False
    return True  # 剩下的全是质数

primes = []
for i in range(low, high):
    if isPrime(i):
        primes.append(i)


print(primes)
# primes = get_prime(low, high)
x = 0
y = 0
for i in range(len(primes)):
    x += primes[i] % 10
    primes[i] = primes[i] // 10
    y += primes[i] % 10
    
print(min(x,y))

