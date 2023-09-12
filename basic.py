# # Formatted string
# print(f"Hello, {a}!")

# # Multiple input in a list
# l = [int(x) for x in input("Enter a and b: ").split()] 
# print(l)
# print(type(l))

# # Multiple input
# a,b,c,d = [int(x) for x in input("enter 4 values: ").split(',')] 
# print(a, b, c, d)

# # Variables
# a,b,c,d = 'a','b','c','d'
# a = b = c = d ='d'
# print(a,b,c,d)

# # Integer data type representation and conversion
# a = 9   #decimal
# b = 0b10 #binary
# c = 0o10 #octal
# d = 0x10 #hexdecimal
# print(a, b, c, d)

# a = bin(a)
# print(a)
# c = hex(c)
# print(c)
# d = oct(d)
# print(d)

# # Floating point number
# a = 2.5e4 #2.5 * 10**4
# print(a)

# # Complex number
# a=3+6j    #(real part + imaginary part)*i
# print(type(a))
# print(a.real)
# print(a.imag)

# List
##NOTE: Methods and Functions are different in python unlike java where they are same.
# l = [1,2,1,1,1,3,4,5]
# print(l)
# del l[0]
# print(l)

# l.append('b')
# print(l)
# print(l.count(1))

# l.remove(1)
# print(l)
# print(l.index(1))
# l.extend([0,3])
# print(l)
# l.pop(-1)
# print(l)
# l.insert(0,'shagun')
# print(l)

# l2 = l.copy()
# print(l2)
# print(l)
# print(max(l))
# print(min(l))
# print(sorted(l))

# Tuple
# t = (1,)
# print(type(t))

# Sets and dictionary and frozen set
#NOTE-> set is mutable and frozen set is immutable
# s = {1:'a',2:'b',3:'c',4:'d'}
# l1 = [1,2,3,4,5]
# d1 = dict.fromkeys(l1)
# print(d1)
# d2 = dict.fromkeys(d1,'a','b','c','d','e')
# print(d2)
# print(1 in s)
# print(5 in s)
# print(s.keys())
# print(s.values())
# print(s.items())
# x = {5:'f',6:'g',7:'a'}
# print(x)
# print(s)
# a = s.update(x)
# print(a)
# print(s.get(1))

# s.add('e')
# print(s)
# print(s)
# s.update(x)
# print(s)
# s.pop()
# print(s)
# s.remove('a')
# print(s)
# s.discard('k')
# print(s)
# print(s.union(x))
# print(s.intersection(x))
# print(x.issubset(s))
# print(s.issuperset(x))
# print(s.isdisjoint(x))
# print(s.difference(x))
# print(s.symmetric_difference(x))

# x = 'computer' if 1<2 else 'cpu'
# print(x)

# x,y,z= 9,10,1
# if x==1:
#     print('yo')
# elif x==2:
#     print('bro')
# else:
#     print('dont waste this precious time')

# x,sum,i=10,0,1
# while i<=x:
#     sum+=i
#     i+=1
# print(sum)

# def 

# import numpy as np

# def fm(numbers):
#     f = {}
#     for num in numbers:
#         if num in f:
#             f[num] += 1
#         else:
#             f[num] = 1

#     max_frequency = max(f.values())
#     mode = [num for num, freq in f.items() if freq == max_frequency]
    
#     if len(mode) == len(numbers):
#         return "No unique mode"
    
#     return mode

# def main():
#     continue_program = True
#     while continue_program:
#         num_list = []
#         num_count = int(input("Enter the number of elements: "))
#         for _ in range(num_count):
#             num = float(input("Enter a number: "))
#             num_list.append(num)
        
#         print("\nChoose an option:")
#         print("1. Find Median")
#         print("2. Find Standard Deviation")
#         print("3. Find Mean")
#         print("4. Find Mode")
#         choice = int(input("Enter your choice: "))
        
#         if choice == 1:
#             median = np.median(num_list)
#             print("Median:", median)
#         elif choice == 2:
#             std_deviation = np.std(num_list)
#             print("Standard Deviation:", std_deviation)
#         elif choice == 3:
#             mean = np.mean(num_list)
#             print("Mean:", mean)
#         elif choice == 4:
#             mode = find_mode(num_list)
#             print("Mode:", mode)
#         else:
#             print("Invalid choice!")
        
#         c = input("Do you want to continue? (yes/no): ")
#         if c.lower() != "yes":
#             c = False
#             print("Exiting the program.")

# if __name__ == "_main_":
#     main()

# for i in range(10,4,-1):
#     print(i)

# l = [1,2,3,4,5]
# ip = int(input("enter number: "))
# for i in l:
#     if i==ip:
#         print("found")
#         break
# else:
#     print("not found")


# l = list(range(1,10,2))
# print(l)
# l[1:4] = 1,2,3
# print(l)
# print(l.reverse())
# print(id(l))
# y = l
# print(id(y))
# x = l[:]
# print(id(x))

# squares = [i**2 for i in range(1,11)]
# print(squares)
# l1 = list(range(1,10,1))
# l2 = list(range(1,10,2))
# l3 = [ num for num in l1 if num not in l2]
# print(l3)
# l1 = list(range(1,10,1))
# l2 = list(range(1,10,2))
# l1 = set(l1)
# l2 = set(l2)

#You are given a list of tuples, where each tuple represents a product and contains the following information: (product_id, product_name, price, quantity). Your task is to create a program that calculates the total cost for each product (price * quantity) and categorizes them as "expensive" or "affordable" based on a given threshold price. Write a Python program that performs these tasks.
# def categorize_products(products, threshold_price):
#     categorized_products = []

#     for product_id, product_name, price, quantity in products:
#         total_cost = price * quantity
#         if total_cost > threshold_price:
#             category = "expensive"
#         else:
#             category = "affordable"
#         categorized_products.append((product_id, product_name, total_cost, category))
    
#     return categorized_products

# products = [
#     (1, "Product A", 10, 3),
#     (2, "Product B", 5, 20),
#     (3, "Product C", 25, 2),
#     (4, "Product D", 8, 5),
# ]

# threshold_price = 50

# categorized_products = categorize_products(products, threshold_price)

# print("Product ID | Product Name | Total Cost | Category")
# print("-" * 45)

# for product_id, product_name, total_cost, category in categorized_products:
#     print(f"{product_id:^11} | {product_name:^12} | {total_cost:^10} | {category:^8}")


# You are given a dictionary representing the inventory of a store. Each item is identified by its name, and its quantity in stock is recorded. Your task is to perform several operations on the dictionary.

# a) Print the quantity of "Apples" in stock.
# b) Update the quantity of "Bananas" to 50.
# c) Add a new item "Grapes" with a quantity of 30.
# d) Remove the item "Oranges" from the inventory.
# e) Loop through the dictionary and print each item along with its quantity.
# def print_inventory(inventory):
#     print("Current Inventory:")
#     for item, quantity in inventory.items():
#         print(f"{item}: {quantity}")

# inventory = {
#     "Apples": 10,
#     "Bananas": 20,
#     "Oranges": 15,
# }

# print("Quantity of Apples:", inventory["Apples"])

# inventory["Bananas"] = 50

# inventory["Grapes"] = 30

# if "Oranges" in inventory:
#     del inventory["Oranges"]

# print_inventory(inventory)

# x = {}
# n = int(input("Enter the num of player: "))
# for i in range(n):
#     name = input("Enter naem: ")
#     score = int(input("Enter score: "))
#     d1 = {name:score}
#     x.update(d1)
# print(x)    

# x = {'a': 1, 'b': 2, 'c': 3}
# print(x.keys())
# print(x.values())
# print(x.items())

# def prime(n):
#     for i in range(1,n+1):
#         if (n%i==0):
#             print("not a prime")
#             break
#     return "prime number"        
    
# prime(7)
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*(fact(n-1))

# fact(4)

# def even(n):
#     for i in range(n+1):
#         if n%2==0:
#             return True
#         else:
#             return False

# l = list(range(1,10))
# n = list(filter(even, l))
# print(l)
# print(n)

# def toupper(s):
#     return str(s).upper()

# n = map(toupper, 'abc')
# for i in n:
#     print(i)

# l = list(range(1,10))
# n = list(filter(lambda x: x%2!=0,l))
# m = list(map(lambda x: x+1, n))
# print(m)

# class Father:
#     def __init__(self):
#         self.property = 80000
#     def display(self):
#         print("Father property = ",self.pr)

# class WholeSale(ABC):
#     @abstractmethod
#     def text_books(self):
#         pass
#     @abstractmethod
#     def stationary(self):
#         pass


# 1.
# n = int(input())
# print('Positive' if n>=0 else 'Negative')

#2
# n = int(input("enter num: "))
# # print('Odd') if n%2==0 else print('even')
# if n%2==0:
#     print("even")
# else:
#     print("odd")

# def isPallindrome(s):
#     rev =''
#     for i in s:
#         rev = i+rev
#     return rev==s

# def longest_pallindrome_in_array(a):
#     longest_string = ''
#     for str in a:
#         if isPallindrome(str) and len(str)>len(longest_string):
#             longest_string = str
#     return longest_string

# # string_array = ['1', '232', '5545455', '909090', '161']
# if longest_pallindrome_in_array(string_array):
#     print(f'longest pallindrome is: {longest_pallindrome_in_array(string_array)}')
# else:
#     print('No pallindrome in the given array')

# def isPallindrome(s):
#     return s==s[::-1]

# def longest_pallindrome_in_array(s):
#     longest_string= ''
#     for str in s:
#         if isPallindrome(str) and len(str)>len(longest_string):
#             longest_string = str
#     return longest_string

# string_array = ["racecar", "hello", "level", "world", "deified"]
# if longest_pallindrome_in_array(string_array):
#     print(longest_pallindrome_in_array(string_array))
# else:
#     print("There's not pallindrome!")

# def distinct_elem(arr):
#     count_dis=0
#     visited=[False for i in arr]
#     for i in range(len(arr)):
#         if visited[i]==True:
#             continue
#         count = 0
#         count_dis+=1
#         for j in range(i+1,len(arr)):
#             if arr[i]==arr[j]:
#                 visited[j]=True
#                 count+=1
#         print(f'{arr[i]}:{count}')
#         print(count_dis)

# arr = [10, 20, 40, 30, 50, 20, 10, 20]
# distinct_elem(arr)
        
# def repeating_elem(arr):
#     visited = [False for i in arr]
    
#     for i in range(len(arr)):
#         if visited[i]==True:
#             continue
#         count = 0
#         for j in range(i+1,len(arr)):
#             if arr[i]==arr[j]:
#                 visited[j]=True
#                 count +=1
#         if count!=1:
#             print(arr[i])
            
# arr = [10, 30, 40, 20, 10, 20, 50, 10]
# repeating_elem(arr)

# def count(arr):
#     dic = {}
#     for i in arr:
#         if i not in dic.keys():
#             dic[i] = 1
#         else:
#             dic[i] +=1
#     for k,v in dic.items():
#         if v!=1:
#             print(k)

# arr = [10, 30, 40, 20, 10, 20, 50, 10]       
# count(arr)

# def non_repeating(arr):
#     visited = [False for i in arr]
    
#     for i in range(len(arr)):
#         if visited[i]==True:
#             continue
#         count = 1
#         for j in range(i+1,len(arr)):
#             if arr[i]==arr[j]:
#                 visited[j]=True
#                 count+=1
#         if count!=1:
#             print(arr[i])
            
# arr = [10, 30, 40, 20, 10, 20, 50, 10]
# non_repeating(arr)

# def removing_dup(arr):
#     # temp = list(range(len(arr)))
#     # j= 0
#     # for i in range(0,len(arr)-1):
#     #     if arr[i]!=arr[i+1]:
#     #         temp[j] = arr[i]
#     #         j+=1
#     # temp[j] = arr[len(arr)-1]
#     # j+=1
    
#     # for i in range(0,j):
#     #     arr[i] = temp[i]
#     # return j
#     res = []
#     for i in arr:
#         if i not in res:
#             res.append(i)
#     return res
# arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
# print(removing_dup(arr))
# def count_odd_even(arr):
#     count_odd = 0
#     count_even = 0
#     for i in arr:
#         if i%2==0:
#             count_even+=1
#         else:
#             count_odd+=1
#     print(count_odd)
#     print(count_even)
# arr = [1, 7, 8, 4, 5, 16, 8]
# count_odd_even(arr)
# symmetric paris
# def symmetric_paris(arr):
#     s = set()
#     for (x,y) in arr:
#         s.add((x,y))
#         if (y,x) in s:
#             print(x,y)
# pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
# symmetric_paris(pairs)
# def disjoint(arr1,arr2):
#     arr1 = set(arr1)
#     arr2 = set(arr2)
    
#     # for i in range(len(arr1)):
#     #     for j in range(len(arr2)):
#     if arr1.intersection(arr2):
#         return False
#     return True

# arr1 = list(map(int,input('arr1: ').split()))
# arr2 = list(map(int,input('arr2: ').split()))
# if disjoint(arr1,arr2):
#     print('Disjoint')
# else:
#     print('Not Disjoint')
# def isSubset(arr1,arr2):
#     for elem in arr1:
#         if elem in arr2:
#             return True
#     return False

# a1 = list(map(int, input().split()))
# a2 = list(map(int, input().split()))
# if isSubset(a1,a2):
#     print('Subset')
# else:
#     print('Not a subset')

# def absolute_diff(arr):
#     res = 99
#     for i in arr:
#         sum = 0
#         for j in arr:
#             sum+=abs(i-j)
#         res = min(res,sum)
#     return res

# arr = [2, 5, 4, 3]
# print(absolute_diff(arr))
# def changeArr(arr):
#     new_arr= arr.copy()
#     arr.sort()
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if new_arr[i]==arr[j]:
#                 new_arr[i] = j+1
#                 break
#     return new_arr

# arr = [100, 2, 70, 12 , 90]
# print(*changeArr(arr))

# def rotate_left(arr,k):
#     rotate_arr = list(range(len(arr)))
#     for i in range(len(arr)):
#         rotate_arr[i] = arr[(i+k)%len(arr)]
#     return rotate_arr

# arr = list(map(int,input().split()))
# k = int(input())
# print(rotate_left(arr,k))

# def balanced(arr):
#     c = ['(','{','[']
#     d = [')','}',']']
#     count = 0
#     for i in arr:
#         if i in c:
#             count += 1
#         elif i in d:
#             count -= 1
#     return True if count==0 else False

# arr =  input()
# if balanced(arr):
#     print('balanced')
# else:
#     print('not balanced')
        
# def rotate(arr,k):
#     # rotated = list(range(len(arr)))
#     for i in range(len(arr)):
#         arr[i],arr[(i+k)%len(arr)] = arr[(i+k)%len(arr)],arr[i]
#     return arr

# arr = list(map(int,input().split()))
# k = int(input())
# print(rotate(arr,k))
# # Formatted string
# print(f"Hello, {a}!")

# # Multiple input in a list
# l = [int(x) for x in input("Enter a and b: ").split()] 
# print(l)
# print(type(l))

# # Multiple input
# a,b,c,d = [int(x) for x in input("enter 4 values: ").split(',')] 
# print(a, b, c, d)

# # Variables
# a,b,c,d = 'a','b','c','d'
# a = b = c = d ='d'
# print(a,b,c,d)

# # Integer data type representation and conversion
# a = 9   #decimal
# b = 0b10 #binary
# c = 0o10 #octal
# d = 0x10 #hexdecimal
# print(a, b, c, d)

# a = bin(a)
# print(a)
# c = hex(c)
# print(c)
# d = oct(d)
# print(d)

# # Floating point number
# a = 2.5e4 #2.5 * 10**4
# print(a)

# # Complex number
# a=3+6j    #(real part + imaginary part)*i
# print(type(a))
# print(a.real)
# print(a.imag)

# List
##NOTE: Methods and Functions are different in python unlike java where they are same.
# l = [1,2,1,1,1,3,4,5]
# print(l)
# del l[0]
# print(l)

# l.append('b')
# print(l)
# print(l.count(1))

# l.remove(1)
# print(l)
# print(l.index(1))
# l.extend([0,3])
# print(l)
# l.pop(-1)
# print(l)
# l.insert(0,'shagun')
# print(l)

# l2 = l.copy()
# print(l2)
# print(l)
# print(max(l))
# print(min(l))
# print(sorted(l))

# Tuple
# t = (1,)
# print(type(t))

# Sets and dictionary and frozen set
#NOTE-> set is mutable and frozen set is immutable
# s = {1:'a',2:'b',3:'c',4:'d'}
# l1 = [1,2,3,4,5]
# d1 = dict.fromkeys(l1)
# print(d1)
# d2 = dict.fromkeys(d1,'a','b','c','d','e')
# print(d2)
# print(1 in s)
# print(5 in s)
# print(s.keys())
# print(s.values())
# print(s.items())
# x = {5:'f',6:'g',7:'a'}
# print(x)
# print(s)
# a = s.update(x)
# print(a)
# print(s.get(1))

# s.add('e')
# print(s)
# print(s)
# s.update(x)
# print(s)
# s.pop()
# print(s)
# s.remove('a')
# print(s)
# s.discard('k')
# print(s)
# print(s.union(x))
# print(s.intersection(x))
# print(x.issubset(s))
# print(s.issuperset(x))
# print(s.isdisjoint(x))
# print(s.difference(x))
# print(s.symmetric_difference(x))

# x = 'computer' if 1<2 else 'cpu'
# print(x)

# x,y,z= 9,10,1
# if x==1:
#     print('yo')
# elif x==2:
#     print('bro')
# else:
#     print('dont waste this precious time')

# x,sum,i=10,0,1
# while i<=x:
#     sum+=i
#     i+=1
# print(sum)

# def 

# import numpy as np

# def fm(numbers):
#     f = {}
#     for num in numbers:
#         if num in f:
#             f[num] += 1
#         else:
#             f[num] = 1

#     max_frequency = max(f.values())
#     mode = [num for num, freq in f.items() if freq == max_frequency]
    
#     if len(mode) == len(numbers):
#         return "No unique mode"
    
#     return mode

# def main():
#     continue_program = True
#     while continue_program:
#         num_list = []
#         num_count = int(input("Enter the number of elements: "))
#         for _ in range(num_count):
#             num = float(input("Enter a number: "))
#             num_list.append(num)
        
#         print("\nChoose an option:")
#         print("1. Find Median")
#         print("2. Find Standard Deviation")
#         print("3. Find Mean")
#         print("4. Find Mode")
#         choice = int(input("Enter your choice: "))
        
#         if choice == 1:
#             median = np.median(num_list)
#             print("Median:", median)
#         elif choice == 2:
#             std_deviation = np.std(num_list)
#             print("Standard Deviation:", std_deviation)
#         elif choice == 3:
#             mean = np.mean(num_list)
#             print("Mean:", mean)
#         elif choice == 4:
#             mode = find_mode(num_list)
#             print("Mode:", mode)
#         else:
#             print("Invalid choice!")
        
#         c = input("Do you want to continue? (yes/no): ")
#         if c.lower() != "yes":
#             c = False
#             print("Exiting the program.")

# if __name__ == "_main_":
#     main()

# for i in range(10,4,-1):
#     print(i)

# l = [1,2,3,4,5]
# ip = int(input("enter number: "))
# for i in l:
#     if i==ip:
#         print("found")
#         break
# else:
#     print("not found")


# l = list(range(1,10,2))
# print(l)
# l[1:4] = 1,2,3
# print(l)
# print(l.reverse())
# print(id(l))
# y = l
# print(id(y))
# x = l[:]
# print(id(x))

# squares = [i**2 for i in range(1,11)]
# print(squares)
# l1 = list(range(1,10,1))
# l2 = list(range(1,10,2))
# l3 = [ num for num in l1 if num not in l2]
# print(l3)
# l1 = list(range(1,10,1))
# l2 = list(range(1,10,2))
# l1 = set(l1)
# l2 = set(l2)

#You are given a list of tuples, where each tuple represents a product and contains the following information: (product_id, product_name, price, quantity). Your task is to create a program that calculates the total cost for each product (price * quantity) and categorizes them as "expensive" or "affordable" based on a given threshold price. Write a Python program that performs these tasks.
# def categorize_products(products, threshold_price):
#     categorized_products = []

#     for product_id, product_name, price, quantity in products:
#         total_cost = price * quantity
#         if total_cost > threshold_price:
#             category = "expensive"
#         else:
#             category = "affordable"
#         categorized_products.append((product_id, product_name, total_cost, category))
    
#     return categorized_products

# products = [
#     (1, "Product A", 10, 3),
#     (2, "Product B", 5, 20),
#     (3, "Product C", 25, 2),
#     (4, "Product D", 8, 5),
# ]

# threshold_price = 50

# categorized_products = categorize_products(products, threshold_price)

# print("Product ID | Product Name | Total Cost | Category")
# print("-" * 45)

# for product_id, product_name, total_cost, category in categorized_products:
#     print(f"{product_id:^11} | {product_name:^12} | {total_cost:^10} | {category:^8}")


# You are given a dictionary representing the inventory of a store. Each item is identified by its name, and its quantity in stock is recorded. Your task is to perform several operations on the dictionary.

# a) Print the quantity of "Apples" in stock.
# b) Update the quantity of "Bananas" to 50.
# c) Add a new item "Grapes" with a quantity of 30.
# d) Remove the item "Oranges" from the inventory.
# e) Loop through the dictionary and print each item along with its quantity.
# def print_inventory(inventory):
#     print("Current Inventory:")
#     for item, quantity in inventory.items():
#         print(f"{item}: {quantity}")

# inventory = {
#     "Apples": 10,
#     "Bananas": 20,
#     "Oranges": 15,
# }

# print("Quantity of Apples:", inventory["Apples"])

# inventory["Bananas"] = 50

# inventory["Grapes"] = 30

# if "Oranges" in inventory:
#     del inventory["Oranges"]

# print_inventory(inventory)

# x = {}
# n = int(input("Enter the num of player: "))
# for i in range(n):
#     name = input("Enter naem: ")
#     score = int(input("Enter score: "))
#     d1 = {name:score}
#     x.update(d1)
# print(x)    

# x = {'a': 1, 'b': 2, 'c': 3}
# print(x.keys())
# print(x.values())
# print(x.items())

# def prime(n):
#     for i in range(1,n+1):
#         if (n%i==0):
#             print("not a prime")
#             break
#     return "prime number"        
    
# prime(7)
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*(fact(n-1))

# fact(4)

# def even(n):
#     for i in range(n+1):
#         if n%2==0:
#             return True
#         else:
#             return False

# l = list(range(1,10))
# n = list(filter(even, l))
# print(l)
# print(n)

# def toupper(s):
#     return str(s).upper()

# n = map(toupper, 'abc')
# for i in n:
#     print(i)

# l = list(range(1,10))
# n = list(filter(lambda x: x%2!=0,l))
# m = list(map(lambda x: x+1, n))
# print(m)

# class Father:
#     def __init__(self):
#         self.property = 80000
#     def display(self):
#         print("Father property = ",self.pr)

# class WholeSale(ABC):
#     @abstractmethod
#     def text_books(self):
#         pass
#     @abstractmethod
#     def stationary(self):
#         pass


# 1.
# n = int(input())
# print('Positive' if n>=0 else 'Negative')

#2
# n = int(input("enter num: "))
# # print('Odd') if n%2==0 else print('even')
# if n%2==0:
#     print("even")
# else:
#     print("odd")



# n,m,o = map(int, input().split(','))



# print('even') if n%2==0 else print('odd')

# sum = 0



# # print(int(n*(n+1)/2))



# for i in range(n+1):



#     sum += i
# print(sum)



# for i in range(n,m+1):



#     sum+=i
# print(sum)



# print(n) if n>m else print(m)



# print(max(n,m))




# if n>m and n>o:
#     print(n)



# elif m>n and m>o:
#     print(m)



# elif o>n and o>m:
#     print(o)



# max = n if n>m else m



# max = o if o>max else max



# print (max)

# n = int(input())1



# if n%400==0 or (n%100!=0 and n%4==0):



#     print("Leap Year")
# else:



#     print("Not a Leap Year")



# flag = 0



# if n<2:



#     flag = 1
# else:



#     for i in range (2,n//2+1):



#         if n%i==0:



#             flag = 1



#             break
            



# if flag == 1:



#     print('not prime')
# else:



# def is_prime(num):



#     if num <= 1:



#         return False



#     for i in range(2, int(num ** 0.5) + 1):



#         if num % i == 0:



#             return False



#     return True




# low, high = map(int, input("Enter the range (low and high): ").split())



# prime_numbers = [num for num in range(low, high + 1) if is_prime(num)]




# print("Prime numbers in the given range:", prime_numbers)



# n,m = map(int, input().split(','))
# sum = 0



# for i in range(n, m+1):



#     sum += i
# print(sum)
# n = int(input())



# rev = 0



# while n!=0:



#     r = int(n%10)



#     rev = rev*10+r



#     n//=10



# print(rev)
# n = (input())
# temp = n



# rev = 0



# # while temp!=0:



# #     r = int(temp%10)



# #     rev = rev*10+r



# #     temp//=10




# if n==n[::-1]:



#     print('pallindrome')
# else:



#     print('Not a pallindrome')

# n = int(input())
# temp = n
# res = 0



# while temp!=0:



#     rem = int(temp%10)



#     res = res + pow(rem, len(str(n)))



#     temp//=10
# if res == n:



#     print('Armstrong')
# else:



#     print('Not an armstrong')



# def armstrong(num):
#     temp = num
#     res = 0



#     while temp!=0:



#         rem = int(temp%10)



#         res = res+pow(rem,len(str(num)))



#         temp//=10
#     if num==res:



#         print(f'{num} is Armstrong')
    



# low, high = map(int, input().split())



# for i in range(low, high+1):



#     armstrong(i)




# def fib(n):

#     if n==0 or n==1:
#         return n
#     else:



#         return fib(n-1)+fib(n-2)

# n = int(input())



# print(fib(n))



# # for i in range(n):



#     print(f'{fib(i)}', end=' ')

# n = int(input())

# n1 = 0



# n2 = 1



# print(f"Fibonacci series: {n1} {n2}",end = ' ')



# for i in range(n-2):



#     n3 = n1+n2



#     n1 = n2



#     n2 = n3



#     print(f"{n3}",end=' ')



# def fact(n):



#     if n<=1:

#         return 1
#     else:



#         return n*fact(n-1)

# n = int(input())



# print(fact(n))




# def div(num):



#     for i in range(2,num):



#         if num%i==0:
#             print(i)

# n = int(input())



# div(n)



# import math
# def isPerfectSquare(x):
#     if x>=0:
#         sr = int(math.sqrt(x))
#         return (sr*sr) == x
#     return False



# if isPerfectSquare(84):
#     print("True")
# else:
#     print('False')

# num = int(input())
# sum = 0
# for i in range(1,num):
#     if num%i == 0:
#         sum += i
    
# if sum==num:
#     print('Perfect Number')
# else:
#     print('Not a perfect number')

# def isVowel(a):
#     a = a.upper()
#     if a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
#         return True
#     return False

# a = input()
# if not a.isalpha():
#     print("not a alphabet")
# if isVowel(a):
#     print('Vowel')
# else:
    # print('Not a Vowel')


# def swap(a):
#     str1 = str()
#     for i in a:
#         if i.isupper():
#             i = i.lower()
#             str1 += i
#         else:
#             i = i.upper()
#             str1 += i
#     return str1

# a = input()

# print(a.swapcase())

# if  65<=ord(a)<=90 or 96<=ord(a)<=122:
#     print('Alphabet')
# else:
#     print('Not a alphabet')

# print(ord(a))
# count = 0
# for i in a:
#     count += 1
# print(count)

# def count_vowel(s):
#     s= s.upper()
#     count = 0
#     for i in s:
#         if i=="A" or i== "E" or i== "I" or i== "O" or i== "U":
#             count += 1
#     return count

# a = input()
# print(count_vowel(a))

# def remove_vowel(s):
#     str1 = ''
#     vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     for i in s:
#         if i in vowel:
#             pass
#         else:
#             str1 += i
#     return str1

# a = input()
# print(remove_vowel(a))


# def isPallindrome(input_str):
#     for i in range(len(input_str)//2):
#         if input_str[i] != input_str[len(input_str)-i-1]:
#             return False
#     return True

# input_str = input()
# if isPallindrome(input_str):
#     print("Yes")
# else:
#     print("No")


# def reverse_string(input_str):
#     return ''.join([i  for i in reversed(input_str)])

# s = input()
# print(reverse_string(s))

# def only_alphabets(input_str):
#     res = ''
#     for ch in input_str:
#         if 65<=ord(ch)<=90 or 96<=ord(ch)<=122:
#             res+=ch
#     return res

# s = input()
# print (only_alphabets(s))

# def remvoe_space(input_str):
#     return "".join(input_str.split())

# n = input()
# print(remvoe_space(n))

# def remove_bracket(input_str):
#     eq= ''
#     for i in input_str:
#         if i=='(' or i==')' or i=='[' or i==']' or i=='{' or i=='}':
#             pass
#         else:
#             eq += i
#     return eq

# n = input()
# print(remove_bracket(n))

# def sum_of_num(input_str):
#     sum=0
#     for i in input_str :
#         if i.isdigit():
#             sum += int(i)
#     return sum

# n = input()
# print(sum_of_num(n))

# def cap(input_str):
#     res = input_str[0].upper()
#     res += input_str[1:len(input_str)-2]
#     res += input_str[len(input_str)-1].upper()
#     return res

# n = input()
# print(cap(n))

# def count(input_str):
#     # dic = {}
#     # for i in input_str:
#     #     if i not in dic:
#     #         dic[i] = 1
#     #     else:
#     #         dic[i] +=1
#     for i in input_str:
#         freq = input_str.count(i)
#         print(f'{i}: {freq}')
    

# n = input()
# print(count(n))

# def non_repeating(input_str):
#     char_count = {}
#     for ch in input_str:
#         if ch not in char_count:
#             char_count[ch] = 1
#         else:
#             char_count[ch] +=1
#     return [ch for ch,count in char_count.items() if count==1]
            
# n = input()
# print(*non_repeating(n))

# def anagram(str1, str2):
#     str1 = sorted(str1.lower())
#     str2 = sorted(str2.lower())
#     if str1==str2:
#         print('True')
#     else:
#         print('False')
    
# n,m = input().split()
# anagram(n, m)

# n,m,o = input().split()
# print(n.replace(m,o))

# def check_substring(str1, str2):
#     for i in str1:
#         if ord(i) not in range(65,90) or ord(i) not in range(96,122):
#             str1 = 
# n,m = input().split()
# a = [10, 89, 9, 56, 4, 80, 8]
# min_2nd = min_1st = float('inf')
# for i in a:
#     if i>max_num:
#         max_num = i
# print(max_num)
# a= sorted(a)
# print(a[-1])
# for i in a:
#     if i<min_num:
#         min_num = i
# print(min_num)
# a = sorted(a)
# print(a[0])
# for i in a:
#     if i>max_num: max_num=i
#     if i<min_num: min_num=i
# print(min_num)
# print(max_num)
# for i in a:
#     if i < min_1st:
#         min_2nd = min_1st
#         min_1st = i
#     elif i>min_1st and i<min_2nd:
#         min_2nd = i
# print(min_2nd)

# print(sum(a))
# a = [10, 89, 9, 56, 4, 80, 8]
# start = 0
# end = len(a)-1
# while start<=end:
#     temp = a[start]
#     a[start] = a[end]
#     a[end] = temp
#     start+=1
#     end-=1
# print(*a)
# def reverse_list(a,start,end):
#     while(start<=end):
#         a[start],a[end] = a[end],a[start]
#         start+=1
#         end-=1
#     return a

# a = [10, 89, 9, 56, 4, 80, 8]
# b = reverse_list(a,0,len(a)-1)
# print(*b)


# def print_order(a):
#     a.sort()
#     for i in range(len(a)//2):
#         print(a[i],end=' ')
#     for j in range(len(a)-1,len(a)//2-1,-1):
#         print(a[j],end=' ')

# a = [ 5, 4, 6, 2, 1, 3, 8, -1 ]
# # print_order(a)
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i],a[j] = a[j],a[i]
        
# print(a)

# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j] = a[j],a[i]
# print(*a)


# def count_freq(a):
#     n = len(a)
#     tup = ()
#     visited = [False for i in a]
#     for i in range(n):
#         if visited[i]==True:
#             continue
#         count = 0
#         for j in range(i+1,n):
#             if a[i]==a[j]:
#                 visited[j]=True
#                 count+=1
#         tup+=((a[i],count))
#         print(f'{a[i]}:{count}')
#     dic = dict(tup)
#     print(dic)
        
# arr = [10, 30, 10, 20, 10, 20, 30, 10]
# count_freq(arr)

# def sort_by_frequency(arr):
#     freq_map = {}
#     for el in arr:
#         if el not in freq_map:
#             freq_map[el] = 0
#         freq_map[el] += 1

#     sorted_arr = []
#     for el, freq in freq_map.items():
#         sorted_arr.append((freq, el))

#     sorted_arr.sort(reverse=True)
#     return [el for freq, el in sorted_arr]

# arr = [4, 2, 2, 8, 3, 3, 1, 1, 1, 8]
# sorted_result = sort_by_frequency(arr)

# print(sorted_result)
# def sort_by_frequency(arr):
#     freq_map = {}
#     for el in arr:
#         if el not in freq_map:
#             freq_map[el] = 0
#         freq_map[el] += 1

#     sorted_arr = []
#     for el, freq in freq_map.items():
#         sorted_arr.append((freq, el))

#     sorted_arr.sort(reverse=True)
#     return [el for freq, el in sorted_arr]

# arr = [4, 2, 2, 8, 3, 3, 1, 1, 1, 8]
# sorted_result = sort_by_frequency(arr)

# print(sorted_result)

# def sort_by_frq(a):
#     d = {}
#     for i in a:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] +=1
#     ls = []
#     for el,feq in d.items():
#         ls.append((feq,el))
    
#     ls.sort(reverse=True)
#     return [el for feq,el in ls]
    
# a = [4, 2, 2, 8, 3, 3, 1, 1, 1, 8]
# print(*sort_by_frq(a))
#tcs live qusiton

# def diag_abs_diff(matrix,n):
#     i = 0
#     j = 0
#     left_diag = 0
#     right_diag = 0
#     while(i<n):
#         left_diag += matrix[i][j]
#         i +=1
#         j +=1
#     i = 0
#     j = n-1
#     while(i<n):
#         right_diag += matrix[i][j]
#         i+=1
#         j-=1
        
#     print(left_diag)
#     print(right_diag)
#     return abs(left_diag-right_diag)

# n = int(input())
# matrix = []
# for i in range(n):
#     row = [int(x) for x in input().split()]
#     matrix.append(row)
# print(matrix)
        
# print(diag_abs_diff(matrix,n))




#find hcf:
# def findhcf(num1,num2):
#     hcf = 0
#     for i in range(2,min(num1,num2)):
#         if num1%i==0 and num2%i==0:
#             hcf = i
#     return hcf

# n,m = input().split()
# print(findhcf(int(n),int(m)))

# #find lcm:
# def findlcm(num1,num2):
    
# def findhcf(a,b):
#     if b==0:
#         return a
#     else:
#         return findhcf(b,a%b)
    
# n,m=  input().split()
# lcm = (int(n)*int(m))//findhcf(int(n),int(m))
# print(lcm)

# def getGCD(a,b):
#     if b==0:
#         return a
#     else:
#         return getGCD(b,a%b)

# n,m=  input().split()
# lcm = (int(n)*int(m))//getGCD(int(n),int(m))
# print(lcm)

# def bin_to_dec(num):
#     base = 1
#     dec = 0
#     while num>0:
#         rem = num%10
#         dec += rem*base
#         num //= 10
#         base *= 2
#     return dec
# n = int(input())
# print(bin_to_dec(n))

# def dec_to_bin(num):
#     base = 1
#     bin_num = 0
#     while num>0:
#         rem = num%2
#         bin_num += rem*base
#         base *= 10
#         num //= 2
#     return bin_num

# n = int(input())
# print(dec_to_bin(n))

# from math import pi
# def area_of_circle(r):
#     return pi * r**2

# r= int(input())
# print(area_of_circle(r))

# import math
# def checkPrime(num):
#     if num<2:
#         return False
#     else:
#         for i in range(2,int(math.sqrt(num))):
#             if num%i==0:
#                 return False
#     return True

# n,m= input().split()
# for i in range(int(n),int(m)+1):
#     if checkPrime(i):
#         print(i,end=' ')


# def dig_count(num):
#     count = 0
#     while num>0:
#         count += 1
#         num //= 10
#     return count

# n = int(input())
# print(dig_count(n))

# from num2words import num2words
# def yo(num):
#     return num2words(num)

# n = int(input())
# print(yo(n))

# def count_digits(num,d):
#     count = 0
#     while num>0:
#         if d==num%10:
#             count += 1
#         num//=10
#     return count

# n = int(input())
# m = int(input())
# print(count_digits(n,m))

# Pattern 1
# n = int(input())
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print('*',end=' ')
#     print()
    
# Pattern 2
# n = int(input())
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print('*',end=' ')
#     print()

# Pattern 3
# n = int(input())
# for row in range(1,n+1):
#     col_count = n-row+1
#     for col in range(row):
#         print('*',end=' ')
#     print()

# Pattern 4

# n = int(input())
# for row in range(1,n+1):
#     col_count = n-(n-row)
#     for col in range(1,row+1):
#         print('',col,end=' ')
#     print()

# Pattern 5
# n = int(input())
# for row in range(1,n*2):
#     col_count = row if row<n else n-(row-n)
#     for col in range(1,col_count+1):
#         print('',row,end=' ')
#     print()

# Pattern 6
# n = int(input())
# for row in range(1, n*2):
#     space_count = n-row if row<n else row-n
#     for space in range(1,space_count+1):
#         print('',end=' ')
#     col_count = row if row<n else n-(row-n)
#     for col in range(1,col_count+1):
#         print('*',end=' ')
#     print()
    

# Pattern 7

# n = int(input())
# for row in range(1,n+1):
#     space_count = n-row
#     for space in range(1,space_count+1):
#         print('',end='  ')
#     for col in range(row,0,-1):
#         print(col,end=' ')
#     for col in range(2,row+1):
#         print(col,end=' ')
#     print('')

# Pattern 8

n = int(input())
for row in range(1,2*n):
    