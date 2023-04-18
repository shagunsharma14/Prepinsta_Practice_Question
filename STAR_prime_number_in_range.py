if __name__ == '__main__':
    low, high = input().split()
    prime_nums = []
    if int(low) == 2:
        prime_nums.append(int(low))
    for num in range(int(low), int(high)+1):
        flag = 0
        if num<2:
            flag = 1
        if num%2==0:
            continue
        else:
            for i in range(2,int(num/2)+1):
                if num%i==0:
                    flag=1
                    break
            if flag==0:
                prime_nums.append(num)
    print(prime_nums)