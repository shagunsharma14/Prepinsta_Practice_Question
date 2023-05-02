def after_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':
    arr = list(map(int, input().split(',')))
    arr = after_sort(arr)
    print(after_sort(arr))
    n = len(arr)
    i = 0
    while i < n:
        count = 1
        while i < n-1 and arr[i] == arr[i+1]:
            count += 1
            i += 1
            
        print("{0}: {1}".format(arr[i], count))
        i += 1
