from node import Node

#Last In First Out
class Stack:
    def __init__(self):
        self._top = None

    #add new node
    def push(self, entry):
        new_node = Node(entry)
        new_node.next = self._top
        self._top = new_node

    #remove node
    def pop(self):
        #if the stack is empty, RuntimeError
        if self.is_empty():
            raise RuntimeError
        else:
            pop_value = self._top.entry
            self._top = self._top.next
            return pop_value
        
    #check if the stack is empty
    def is_empty(self):
        return self._top is None