def solution(num1, num2):
    s1 = str(num1)
    s2 = str(num2)
    r = 0
    for i in range(num2):
        s = str(i)
        for j in range(len(s)):
            if s1 == s[j]:
                r += 1
    return r

print(solution(2, 23456))