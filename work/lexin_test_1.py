import sys

n = int(sys.stdin.readline().strip())
heights = []
for i in range(n):
    height = int(sys.stdin.readline().strip())
    heights.append(height)

# print(heights)

number = n

for i in range(n):
    x = 0
    j = 1
    while 1 <= j and j < i: 
        if heights[j] > heights[j-1]:
            x += 1
        j += 1
    while i <= j and j < n:
        if heights[j] < heights[j-1]:
            x += 1
        j += 1
    print(x)
    if x < number:
        number = x
print(number)