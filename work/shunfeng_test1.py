num = int(input())
line = input()
pass_self = []
for i in range(len(line)):
    pass_self.append(line[i])
line = input()
pass_peo = list(map(int, line.split()))

def get_ans(pass_self, pass_peo):
    x = -1
    new_pass_self = []
    for i in range(len(pass_self)):
        x = ord(pass_self[i]) - ord('A')
        new_pass_self.append(x)

    new_pass_peo = []
    for i in range(len(pass_peo)):
        if i not in new_pass_self:
            new_pass_peo.append(pass_peo[i])

    max_peo = max(new_pass_peo)
    max_index = pass_peo.index(max_peo)
    max_num = chr(ord('A')+max_index)
    return max_num
max_num = get_ans(pass_self, pass_peo)
print(max_num)