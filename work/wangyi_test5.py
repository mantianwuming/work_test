import sys

t = int(sys.stdin.readline().strip())
for i in range(t):
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()
    
    
    def res(S):
        X = ''
        for i in S:
            if i == '1':
                X += '0'
            if i == '0':
                X += '1'
        Y = ''
        i = 0 
        while X[i] == '0':
            i += 1
        Y = X[i:]
        return Y
    
    def judge(S, T):
        if S == T:
            return 'YES'
        if S + res(S) == T:
            return 'YES'
        else:
            return 'NO'
    
    print(judge(S,T))