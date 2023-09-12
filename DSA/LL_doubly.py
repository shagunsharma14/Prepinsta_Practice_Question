class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print('List is empty!')
        else:
            temp = self.head
            while temp is not None:
                print(f'{temp.data}->',end='')
                temp=  temp.next

    def print_LL_reverse(self):
        if self.head is None:
            print('List is empty!')
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            while temp is not None:
                print(f'{temp.data}->',end="")
                temp = temp.prev
                
    def insert_empty(self):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('List is not empty!')

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        
    def add_after(self,data,x):
        if self.head is None:
            print('Empty!')
        else:
            temp = self.head
            while temp is not None:
                if temp.data is x:
                    break
                temp = temp.next
            if temp is None:
                print('Not present!')
            else:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next is not None:
                    temp.next.prev = new_node
                temp.next = new_node
                
    def add_before(self,data,x):
        if self.head is None:
            print('Empty!')
        else:
            temp = self.head
            while temp is not None:
                if temp.data is x:
                    break
                temp = temp.next
            if temp is None:
                print('Empty!')
            else:
                new_node = Node(data)
                new_node.next = temp
                new_node.prev = temp.prev
                if temp.prev is not None:
                    temp.prev.next = new_node
                else:
                    self.head = new_node
                temp.prev = new_node
                
    
dl= LinkedList()
dl.add_begin("A") 
dl.add_begin("C")
dl.add_end("Z")
dl.add_after("B","A")
dl.print_LL_reverse()