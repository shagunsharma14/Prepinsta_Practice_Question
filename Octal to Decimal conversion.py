def oct_to_dec(num):
    base = 1
    temp = num
    res = 0
    while temp > 0:
        rem = temp%10
        res = res + (rem * base)
        base *= 8
        temp //= 10
    return res

num = int(input())
print(oct_to_dec(num))