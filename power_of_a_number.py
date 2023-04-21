def powerIs(num, power):
    if power == 0:
        return 1
    return num * powerIs(num, power-1)
if __name__ == '__main__':
    num, power = input().split()
    ########## METHOD 1 ##########
    # res = 1
    # for _ in range(int(power)):
    #     res  *= int(num)
    # print(res)

    ########## METHOD 2 ##########
    print(powerIs(int(num),int(power)))