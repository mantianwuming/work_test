def match(s,source):
    if len(source) == 0:
        return False
    if len(source) == 1:
        if s in source[0]:
            return True
        else:
            return False

    s_start = []
    for i in range(len(source)-1):
        s_start.append(source[i])
        s_start.append(source[i][0])
    s_end = []
    for i in range(len(source[-1])):
        se = source[-1][:i+1]
        s_end.append(se)

    while s != '':
        if s_start != [] and s[0:len(source[0])] == s_start[0]:
            s = s[len(source[0]):]
            s_start.remove(s_start[0])
            s_start.remove(s_start[0])
            source.remove(source[0])
        elif s_start != [] and s[0] == s_start[1]:
            s = s[1:]
            s_start.remove(s_start[0])
            s_start.remove(s_start[0])
            source.remove(source[0])
        elif s_start == [] and s in s_end:
            return True
        else:
            return False
    return True



if __name__ == "__main__":
    source = ["wang", "hai", "bao"]
    s = "whb" # "wanghb" "wanghbao" "wanghaiba" 'wh'
    print(match(s,source))
