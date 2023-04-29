import math

if __name__ == '__main__':
    arr = map(int, input().split(','))
    min1_is = math.inf
    min2_is = math.inf

    for i in arr:
        if min1_is > i:
            min2_is = min1_is
            min1_is = i
        elif min1_is < i < min2_is:
            min2_is = i
    print(min2_is)





