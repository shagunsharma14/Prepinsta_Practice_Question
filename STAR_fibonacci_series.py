def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(fib(_), end=' ')

########### METHOD 2 #################
    # n1 = 0
    # n2 = 1
    # for i in range(2,n):
    #     n3 = n1+n2
    #     n1 = n2
    #     n2 = n3
    #     print(n3, end=" ")
    # print()