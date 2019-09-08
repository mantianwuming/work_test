def solution(n, m, a='A', b='B'):
    if m > n:
        return solution(m, n, b, a)
    if n > m * 2:
        return (a + a + b) * m + a * (n - m * 2)
    return (a + a + b) * (n - m) + (a + b) * (m * 2 - n)

print(solution(3,1))