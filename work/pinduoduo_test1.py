def edit_distance(a, b):
    if a == b:
        return 0
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    
    flag = 1
    if a[-1] == b[-1]:
        flag = 0 

    return min(edit_distance(a, b[:-1]) + 1,
            edit_distance(a[:-1], b) + 1,
            edit_distance(a[:-1], b[:-1]) + flag)

if __name__ == '__main__':
    a = 'xx' #apple
    b = 'axxa' #banana
    print(edit_distance(a,b))