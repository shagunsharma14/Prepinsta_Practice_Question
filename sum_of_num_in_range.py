def sumragne(num1,num2):
    if num2==num1:
        return num1
    return num2+sumragne(num1,num2-1)


if __name__ == '__main__':
    num1,num2 = input().split()
    print(sumragne(int(num1),int(num2)))