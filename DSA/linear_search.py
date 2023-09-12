def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    else:
        return i

arr = list(map(int,input().split()))
key = int(input('Enter key: '))
if linear_search(arr,key):
    print("Key found at index:",linear_search(arr,key))
else:
    print('Not found!')