def fact(num):
    if num==0:
        return 1
    return num * fact(num-1)


if __name__ == '__main__':
    num = int(input())
    print(fact(num))

    ########### METHOD 2 #############
    # factorial = 1
    # for i in range(1,num+1):
    #     factorial *= i
    # print(factorial)
