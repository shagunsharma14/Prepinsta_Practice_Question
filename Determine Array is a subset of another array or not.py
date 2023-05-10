def isSubset(arr1, arr2):
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr1[j] == arr2[i]:
                break
        if j == len(arr1):   
            return 0
    return 1


if __name__ == '__main__':
    arr1 = [11, 12, 13, 21, 30, 70]
    arr2 = [11, 30, 70, 12]
    
    m = len(arr1)
    n = len(arr2)
    
    if(isSubset(arr1, arr2)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[]")