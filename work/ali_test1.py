weights = [1,2,3,4,5,6]

def permutations(arr, position, end):
 
    if position == end:
        # if arr[0] * 3 + arr[1] * 2 + arr[2] * 1 == arr[3] * 1 + arr[4] * 2 + arr[5] * 3:
        #     print(arr)
        print(arr)
 
    else:
        for index in range(position, end):
 
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]

print(permutations(weights, 0, 6))
