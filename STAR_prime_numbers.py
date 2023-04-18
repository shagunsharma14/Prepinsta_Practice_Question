if __name__ == '__main__':
    n = int(input())
    flag = 0
    if n<2:
        flag = 1
    else:
        for i in range(2,int(n/2)+1): #n/2 iterations only no need to loop over every iteration
            if n%i==0:
                flag = 1
                break
    print('Prime Number' if flag==0 else 'Not a Prime Number')