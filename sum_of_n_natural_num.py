def sumupto(n):
    if n==1:
        return n
    return n+sumupto(n-1)

if __name__ == '__main__':
    print(sumupto(int(input())))