class Node:
    def __init__(self,value):
        self.value= value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_head(self,value):
        node=Node(value)
        node.next=self.head
        node.previous=None
        if self.head is not None:
            self.head.previous=node
        self.head=node
        if self.tail is None:
            self.tail=node
        self.size+=1
        return node

    def pop_tail(self):
        if self.tail is None:
            return None  
        node = self.tail
        value = node.value
        self.tail = node.previous
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1

        return value

    def remove(self,node):
        if node.previous is not None:
            node.previous.next=node.next
        else: 
            self.head=node.next

        if node.next is not None:
            node.next.previous=node.previous
        else: self.tail=node.previous
        self.size -= 1
        
        
