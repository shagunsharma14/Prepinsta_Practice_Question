arr = input().split()
visited = [False for _ in arr]
new_arr = []

for i in range(len(arr)):
    if visited[i] == True:
        continue
    for j in range(i+1, len(arr)):
        if arr[i]==arr[j]:
            visited[j] = True
    new_arr.append(arr[i])      
print(new_arr)
            