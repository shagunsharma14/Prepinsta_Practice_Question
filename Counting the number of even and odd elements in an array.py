def count_odd_even(arr):
    even_count = 0
    odd_count = 0
    for i in range(len(arr)):
        if i%2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print('Even count is: ',even_count)
    print('Odd count is: ',odd_count)
    
if __name__ == '__main__':
    arr = list(map(int,input().split()))
    count_odd_even(arr)