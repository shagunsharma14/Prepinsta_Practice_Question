if __name__ == '__main__':
    arr = map(int, input().split(','))
############## METHOD 1 ######################
    min_is = 9999
    max_is = -9999
    for i in arr:
        if i > max_is:
            max_is = i
        elif i < min_is:
            min_is = i
    print('max is: ',max_is)
    print('min is: ',min_is)

############## METHOD 2 ######################
# arr = [10, 89, 9, 56, 4, 80, 8]
# arr.sort()
#
# print (arr[0])
# print (arr[-1])