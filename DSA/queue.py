# queue = []
# def enqueue():
#     elem = input("enter the elem: ")
#     queue.append(elem)
    
# def dequeue():
#     if not queue:
#         print('Underflow!')
#     print('removed: ',queue[0])
#     queue.pop(0)
    
# def display():
#     print(queue)

# while True:
#     choice = int(input('Enter choice: 1.add 2.remove 3.display 4.exit\n'))
#     if choice ==1:enqueue()
#     elif choice ==2:dequeue()
#     elif choice ==3:display()
#     elif choice == 4:break
#     else:print("Invalid Input")
# import collections
# q = collections.deque()
# q.append(10)
# print(q)
# q.popleft()
# print(q)
# import queue
# q = queue.queue()
# print(q)
# q.put(10)
# q.put(50)
# q.put(30)
# q.get()
# q.get()
# q.get()
import queue
q = queue.PriorityQueue()
q.put(10)