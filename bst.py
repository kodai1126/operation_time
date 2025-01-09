class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    #initialize
    def __init__(self):
        self.root = None

    #insert a new key
    def insert(self, key):
        if self.root is None:
            self.root = BinaryNode(key)
        else:
            self._rec_insert(self.root, key)
    
    #recursive insert
    def _rec_insert(self, root, key):
        if key == root.value:
            #prevent duplication
            return

        #key is smaller than the root value
        if key < root.value:
            if root.left is None:
                root.left = BinaryNode(key)
            else:
                self._rec_insert(root.left, key)
        
        #key is larger than the root value
        else:
            if root.right is None:
                root.right = BinaryNode(key)
            else:
                self._rec_insert(root.right, key)
    #search
    def search(self, key):
        return self._rec_search(self.root, key)

    #searching recusion
    def _rec_search(self, node, key):
        if node is None:
            return None
        if node.value == key:
            return True
        #search left
        elif key < node.value:
            return self._rec_search(node.left, key)
        #search right
        else:
            return self._rec_search(node.right, key)