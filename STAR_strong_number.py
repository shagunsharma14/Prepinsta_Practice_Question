# Strong Number
# A Number that is equal to the sum of the factorial of it's individual digits is known as Strong Number.
# Let's Try and understand it better using an example
#
# Example
# Input : 145
# Output : It's a Strong Number.
# Explanation : Number = 145
# 145 = 1! + 4! + 5!
# 145 = 1 + 24 + 120

def fact(num):
    if num==0 or num==1:
        return num
    return num * fact(num-1)

def strong_num(num):
    temp = str(num)
    sum_is = 0
    for _ in temp:
        r = int(temp) % 10
        sum_is += fact(r)
        temp = int(temp)//10
    if num == sum_is:
        return 'Strong Number'
    else:
        return 'Not a Strong Number'
if __name__ == '__main__':
    num = int(input())
    print(strong_num(num))