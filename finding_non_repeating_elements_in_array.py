if __name__ == '__main__':
    arr = list(map(int, input().split(',')))
    visited = [False for _ in range(len(arr))]
    for i in range(len(arr)):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        if count == 1:
            print(arr[i])
                