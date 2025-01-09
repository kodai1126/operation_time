from node import Node

#First in first out
class Queue:
    def __init__(self):
        self._front = None
        self._back = None

    #add Node at the back
    def enqueue(self, entry):
        new_node = Node(entry)
        if self.is_empty():
            self._front = new_node
            self._back = new_node
        else:
            self._back.next = new_node
            self._back = new_node

    #check if the queue is empty
    def is_empty(self):
        return self._front is None