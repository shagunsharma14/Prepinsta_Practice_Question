def bubble_sort(arr):
    n = len(arr)
    for i in range(n) :
        # swaped = False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                # swaped = True
        # if swaped!=True:
        #     break

arr = list(map(int,input().split(',')))
bubble_sort(arr)
print(*arr)