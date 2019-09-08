import sys

n = sys.stdin.readline().strip()
n = float(n)
su = list(range(1,10000))
x = 0
z = 100
y = 0
for i in range(len(su)):
    z1 = abs(n*su[i] - int(n*su[i]))
    z2 = abs(n*su[i]-int(n*su[i])-1)
    if z > min(z1,z2):
        z = min(z1, z2)
        if z1 >= z2:
            x = int(n*su[i])+1
            y = su[i]
        else:
            x = int(n*su[i])
            y = su[i]
print(x,y)