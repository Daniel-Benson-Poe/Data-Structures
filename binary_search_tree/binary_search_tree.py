"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:  # check if new value is less than value of current node
            if self.left is None:  # check if there are any nodes to the left
                self.left = BSTNode(value)  # Create new node to the left with the new value
            else:  # if there is a node already to the left
                self.left.insert(value)  # run insert method again using the left node as the new value
        else:  # if new value is greater than or equal to value of current node
            if self.right is None:  # check if there is a node to the right
                self.right = BSTNode(value)  # insert new node with the new value to the right
            else:  # if there is a node already to the right
                self.right.insert(value)  # run insert method again using right node as the new value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:  # check if target and current node's value is equal
            return True
        elif target < self.value and self.left:  # check if target is less than current node's value and there is a node to the left
            return self.left.contains(target)  # run contains method again using node to the left
        elif target > self.value and self.right:  # check if target is greater than current node's value and there is a node to the right
            return self.right.contains(target)  # run contains method again using node to the right
        return False  # if we've gotten this far the tree does not contain the target value

    # Return the maximum value found in the tree
    def get_max(self):
        current = self  # set current to first node
        while(current.right):  # continue iterating to the right (the greater than side) until there is no more nodes to the right
            current = current.right  # set current to the node to the right as the loop goes
        return current.value  # return value of the node found to the farthest right (or the first node!)

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)  # call function on initial node
        if self.left:  # check if there is a node to the left
            self.left.for_each(fn)  # run for_each method on node to the left
        if self.right:  # check if there is a node to the right
            self.right.for_each(fn)  # run for_each method on node to the right

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
