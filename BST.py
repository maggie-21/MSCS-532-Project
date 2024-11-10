# Node class for the Binary Search Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Binary Search Tree (BST) class
class BST:
    def insert(self, root, key):
        # If the tree is empty, return a new node
        if root is None:
            return Node(key)
        else:
            # Otherwise, recur down the tree
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def search(self, root, key):
        # Base Cases: root is null or key is present at root
        if root is None or root.val == key:
            return root

        # Key is greater than root's key
        if root.val < key:
            return self.search(root.right, key)

        # Key is smaller than root's key
        return self.search(root.left, key)
