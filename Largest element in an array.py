def find_max_elem(arr,n):
    if n == 0:
        return arr[0]
    return max(arr[n-1],find_max_elem(arr, n-1))
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(find_max_elem(arr,len(arr)))