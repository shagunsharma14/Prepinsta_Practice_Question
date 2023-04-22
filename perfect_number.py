if __name__ == '__main__':
    num = int(input())
    i = 1
    sum_is = 0
    while i < num:
        if num % i == 0:
            sum_is += i
        i += 1
    print('perfect number' if num == sum_is else 'not a perfect number')

    ########## METHOD 2 ##########
    # sum = 0
    #
    # for i in range(1,num):
    #     if num%i==0:
    #         sum += i
    # print('perfect number' if num == sum else 'not a perfect number')
