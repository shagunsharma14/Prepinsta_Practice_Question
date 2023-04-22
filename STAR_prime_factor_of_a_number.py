if __name__ == '__main__':
    num = int(input())
    prime_fact = []
    i = 2
    while num > 1:
        if num % i == 0:
            prime_fact.append(i)
            num /= i
        else:
            i += 1
    print(prime_fact)

#This is to implement same logic on  same number
# In case of for loop it'll check condition apply and
# increment and apply logic to num again which is wrong
# coz we want if num is divisible by i then change num
# and apply same logic on the changed value of num
