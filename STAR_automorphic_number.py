# Automorphic number is a number whose square ends with the same digits as number itself
# pow(5,2) = 2'5'
# pow(76, 2) = 57'76'

def is_automorphic(num):
    if num >= 0:
        mod = pow(10, len(str(num)))
        return True if pow(num, 2) % mod == num else False

if __name__ == '__main__':
    num = int(input())
    print('Automorphic Number' if is_automorphic(num) else 'Not a Automorphic Number')

############## METHOD 2 ##############
# num = 376
# a = str(num)
#
# num1 = num ** 2
# b = str(num1)
#
# if b.endswith(a):
#     print("It's an Automorphic Number")
# else:
#     print("It's not an Automorphic Number")