import sys
line = sys.stdin.readline().strip()
def get_x_val(line, var = 'X'):
    line1 = line.replace('=', '-(') + ')'
    val = eval(line1, {var:1j})
    # val = eval(line1)
    try:
        x_val = -val.real / val.imag
    except:
        x_val = -1
    if int(x_val) == x_val and int(x_val) > 0:
        return int(x_val)
    else:
        return -1
print(get_x_val(line))
