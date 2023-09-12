class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Traversing
    def print_LL(self):
        if self.head is None:
            print('Empty!!')
        else:
            temp = self.head
            while (temp!=None):
                print(f'{temp.data}->',end='')
                temp = temp.next
                
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next= self.head
        self.head = new_node
        
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = new_node
    def add_after(self,data,x):
        temp = self.head
        while temp is not None:
            if temp.data==x:
                break
            temp = temp.next
        
        if temp is None:
            print('Node not present!')
        else:
            new_node = Node(data)
            new_node.next=temp.next
            temp.next = new_node
            
    def add_before(self,data,x):
        if self.head is None:
            print('Empty list!')
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data ==x:
                break
            temp = temp.next
        if temp.next is None:
            print("Node dosen't exist")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked list is not empty')
            
    def delete_begin(self):
        if self.head is None:
            print('List is empty!')
        else:
            self.head = self.head.next
            
    def delete_end(self):
        if self.head is Node:
            print('List is empty')
            
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
    def delete_by_value(self,value):
        if self.head is None:
            print('List is empty!')
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == value:
                break
            temp = temp.next
        if temp.next is None:
            print('Node not present!')
        else:
            temp.next = temp.next.next
            
LL1 = LinkedList()
LL1.insert_empty(99)
LL1.add_begin(20)
LL1.add_begin(10)
LL1.add_end(40)
LL1.add_after(30,20)
LL1.add_before(15,20)
LL1.delete_begin()
LL1.delete_by_value(99)
LL1.print_LL()