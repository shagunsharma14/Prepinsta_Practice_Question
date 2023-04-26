# Friendly Pair Numbers
# The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.


# Example
# Input : 6 28
# Output : Yes, they are a friendly pair
# Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively.
# When we divide the sums with the numbers we get 1 and 1 respectively.
# As the ratio of both the number match, they are considered as a friendly pair.
def factor_sum(num):
    num = int(num)
    ls = []
    for i in range(1,num):
        if num%i==0:
            ls.append(i)
    return sum(ls)


if __name__ == '__main__':
    num1, num2 = input().split()
    print('friendly pairs'if factor_sum(num1) / int(num1) == factor_sum(num2) / int(num2) else 'not a friendly pairs')
