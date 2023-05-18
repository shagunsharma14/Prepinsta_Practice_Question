import math

def printOrder(arr, n):
    arr.sort()
    for i in range(math.floor(n/2)):
        print(arr[i], end=' ')
    print(":",end=' ')
    for i in reversed(range(math.floor(n/2), n)):
        print(arr[i], end=' ')
    
if __name__ == '__main__':
    arr =  input().split(',')
    n = len(arr)
    printOrder(arr, n)  


