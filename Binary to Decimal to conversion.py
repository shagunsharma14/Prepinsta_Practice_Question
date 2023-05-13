def ToDecimal(binNum):
    base = 1
    res = 0
    temp = binNum
    while temp > 0:
        rem = temp%10
        res = res + rem * base
        temp = temp//10
        base *= 2
    return res

if __name__ == '__main__':
    print(ToDecimal(int(input())))