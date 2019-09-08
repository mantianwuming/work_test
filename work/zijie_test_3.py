import sys
nums = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
years = list(map(int, line.split()))

salary = [100 for _ in range(len(years))]
for i in range(1, len(years)):
    if years[i] > years[i-1]:
        if salary[i] <= salary[i-1]:
            salary[i] = salary[i-1] + 100
    elif years[i] < years[i-1]:
        if salary[i-1] <= salary[i]:
            salary[i-1] = salary[i] + 100
    else:
        salary[i] = salary[i-1]

for j in range(len(years)-1, 0, -1):
    if years[j-1] > years[j]:
        if salary[j-1] <= salary[j]:
            salary[j-1] = salary[j] + 100
    elif years[j-1] < years[j]:
        if salary[j] <= salary[j-1]:
            salary[j] = salary[j-1] + 100
    else:
        salary[j-1] = salary[j]

print(salary)
print(sum(salary))