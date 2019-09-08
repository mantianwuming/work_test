import sys

words_list = []
for i in range(4):
    word = sys.stdin.readline().strip()
    words_list.append(word)

true_word = ''

flag = 1
for i in range(len(words_list[0])):
    data = []
    for j in range(4):
        if words_list[j][i] in data:
            true_word += words_list[j][i]
            break
        else:
            data.append(words_list[i][j])
            if len(data) == 4:
                flag = 0
                break
        if flag == 0:
            break


if flag == 1:
    print(true_word)
else:
    print('Input Error')