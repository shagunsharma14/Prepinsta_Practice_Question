def check_equal(arr):
    
    for i in range(len(arr)):
        
        while arr[i]%2 == 0:
            arr[i] //= 2
            
            while arr[i]%3 == 0:
                arr[i] //= 3
                
        if arr[i] != arr[0]:
            return False
    return True

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    
    if check_equal(arr):
        print("Yes, all the elements of an array can be made equal")
    else:
        print("No, all the elements of an array cannot be made equal")