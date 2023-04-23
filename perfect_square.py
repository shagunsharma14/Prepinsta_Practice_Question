import math


def is_perfect_square(num):
    if num >= 0:
        sr = math.sqrt(num)
        return (sr * sr) == num
    return False

if __name__ == '__main__':
    num = int(input())
    if is_perfect_square(num):
        print('Perfect Square')
    else:
        print('Not a perfect Square')