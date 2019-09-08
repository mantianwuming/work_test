def deleteZeroOne(s):
    i = 0
    while i < len(s)-1 and len(s) >= 2:

        if s[i] == '1' and s[i+1] == '0':
            s = s[:i] + s[i+2:]
        else:
            i += 1
    return s

def deleteAgain(s):
    while( s != deleteZeroOne(s)):
        s = deleteZeroOne(s)
    return s

s = '1101010001'
print(deleteAgain(s))
