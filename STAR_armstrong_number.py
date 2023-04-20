if __name__ == '__main__':
    ######### METHOD 1 ###############
    # 1234 = 1^4+2^4+3^4+4^4

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
