# stack = []
# def push():
#     global n,stack
#     if len(stack)==n:
#         print('Overflow!!')
#         return
#     ip = input('Enter element: ')
#     stack.append(ip)

# def pop():
#     if not stack:
#         print("Underflow!!")
#         return
#     print('Removed element is: ',stack[-1])
#     stack.pop()
    
# def display():
#     print('Stack elements are: ')
#     for i in stack:
#         print(i)
        
# n = int(input('Enter the limit of the stack: '))
# while True:
#     choice = int(input('Select 1.push 2.pop 3.display 4.exit\n'))
#     if choice ==1:
#         push()
#     elif choice==2:
#         pop()
#     elif choice==3:
#         display()
#     elif choice==4:
#         break
#     else:
#         print('Enter a valid input!')

########################### Using Collections ###########################
# import collections
# stack = collections.deque()
# stack.append(10)
# stack.append(9)
# print(stack)
# stack.pop()
# stack.pop()
# print(stack)
