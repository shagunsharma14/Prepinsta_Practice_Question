def reverse_array(arr, start, end):
    if start >= end:
        return arr
    # swap the first and last element
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_array(arr, start+1, end-1)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print('reversed array: ',reverse_array(arr, 0, len(arr)-1))