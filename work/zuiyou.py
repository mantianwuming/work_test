source = ['wang', 'hai', 'bao']
string = "whb"

def match(source, string):
    # print(source, string)
    if len(source) == 0:
        return False
    if len(source) == 1:
        if string in source[0]:
            return True
        else:
            return False
    judge1, judge2 = False, False
    if source[0] == string[:len(source[0])]:
        judge1 = match(source[1:], string[len(source[0]):])
    if source[0][0] == string[0]:
        judge2 = match(source[1:], string[1:])
    return judge1 or judge2

print(match(source, string))