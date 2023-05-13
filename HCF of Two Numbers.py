def getHCF(a,b):
    hcf = 1
    for i in range(2,min(a,b)):
        if a%i == 0 and b%i==0:
            hcf = i
    return hcf

if __name__ == '__main__':
    a,b = map(int,input().split())
    print(getHCF(a,b))