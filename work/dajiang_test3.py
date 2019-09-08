from collections import Counter
def reorder(N):
    
    num_digits = len(str(N))
    counter = Counter(str(N))
    power = 1

    while True:
        num_power = len(str(power))
        if num_power > num_digits:
            break
        if num_power == num_digits and Counter(str(power)) == counter:
            return True
        power = power * 2
    return False
    
# counter = Counter(str(128))
# print(counter)
print(reorder(1))