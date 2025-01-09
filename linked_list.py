#import node
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    #get the length of the list
    def length(self):
        return self.size
    
    #add new node
    def insert(self, index, entry):
        if index < 0 or index > self.size:
            raise IndexError
        
        new_node = Node(entry)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            jumper = self.head
            for i in range(index-1):
                jumper = jumper.next
            new_node.next = jumper.next
            jumper.next = new_node

        self.size += 1

    #get the value of the specific node
    def get_entry(self, index):
        if index < 0 or index >= self.size:
            raise RuntimeError
        
        jumper = self.head
        for i in range(index):
            jumper = jumper.next
        return jumper.entry