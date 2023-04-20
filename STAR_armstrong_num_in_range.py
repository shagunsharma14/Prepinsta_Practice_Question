if __name__ == '__main__':
    low, high = input().split()
    for num in range(int(low), int(high)+1):
        sum_is = 0
        num_len = len(str(num))
        temp = num
        while temp>0:
            digit  = temp%10
            sum_is += pow(digit, num_len)
            temp = temp//10

            if num == sum_is:
                print(num, end=', ')