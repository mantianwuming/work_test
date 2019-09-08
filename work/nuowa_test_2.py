def max_price(numbers):
    max_number = 0
    cost = numbers[0]
    sold = 0
    for i in range(1, len(numbers)):
        if numbers[i] < cost:
            cost = numbers[i]
        if numbers[i] > sold:
            sold = numbers[i]
        if sold - cost > max_number:
            max_number = sold - cost
    return max_number

if __name__ == "__main__":
    numbers = [1,7,1,5,3,6,4]
    print(max_price(numbers))