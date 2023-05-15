def LCMis(num1, num2):
    hcf = 1
    for i in range(2,max(num1,num2)):
        if num1%i==0 and num2%i==0:
            hcf = i
    return (num1*num2)//hcf
if __name__ == '__main__':
    num1,num2 = input().split()
    print(LCMis(int(num1),int(num2)))