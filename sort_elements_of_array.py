if __name__ == '__main__':
    arr = list(map(int, input().split(',')))
    # selection sort
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)