def sumIs(n):
    if n<=1:
        return n
    return n + sumIs(n-1)


if __name__=='__main__':
    print(sumIs(int(input())))
