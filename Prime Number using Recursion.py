def isPrime(n, i=2):
    if n == i:
        return True
    elif n%i == 0:
        return False
    else:
        return isPrime(n,i+1)
    return True
if __name__ == '__main__':
    n = int(input())
    if isPrime(n):
        print('Yes prime number')
    else:
        print('Not a prime number')