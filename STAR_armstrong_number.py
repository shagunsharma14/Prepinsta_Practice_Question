if __name__ == '__main__':
    ######### METHOD 1 ###############
    num = input()
    temp = num
    num_len = len(num)
    sum = 0
    for _ in num:
        digit = int(temp)%10
        power = pow(digit, num_len)
        sum += power
        temp  = int(temp)/10
    print("armstrong number" if sum == int(num) else "not a armstrong number")
