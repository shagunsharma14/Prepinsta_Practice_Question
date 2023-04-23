# The number that is divisible by the sum of it's digits
# 21 , 2+1 = 3, 21%3 = 0

if __name__ == '__main__':
    num = int(input())
    temp = num
    sum_is  = 0
    while temp > 0:
        r  = temp%10
        sum_is += r
        temp //= 10

    print('Harshad number' if num%sum_is==0 else 'Not harshad number')