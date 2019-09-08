def get_subset(a):
    res = []
    length = len(a)
    n_length = 2 ** length
    for i in range(n_length):
        temp = i
        result = []
        for j in range(length):
            if temp % 2 == 1:
                result.append(a[j])
            temp //= 2
        res.append(result)
    return res

if __name__ == "__main__":
    a = [1,2,3]
    res = get_subset(a)
    print(res)