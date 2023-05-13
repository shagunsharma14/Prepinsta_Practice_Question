def getLCM(a,b):
    for i in range(2,max(a, b)):
        if a%i==0 and b%i==0:
            hcf = i
    return a*b//hcf

if __name__ == '__main__':
    a,b = map(int,input().split())
    print(getLCM(a, b))