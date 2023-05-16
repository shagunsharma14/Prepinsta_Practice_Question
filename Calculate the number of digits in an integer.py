def countDigit(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return  count

n = 12345
print(countDigit(n))
        