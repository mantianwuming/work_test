def is_coor(sentence):
    stack = []
    for i in sentence:
        if i == '{':
            stack.append('{')
        if i == '}':
            if not stack:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False

if __name__ == '__main__':
    sentence = input()
    print(is_coor(sentence))