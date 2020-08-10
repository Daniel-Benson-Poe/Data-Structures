from singly_linked_list import Node, LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0  # using an array and linked list
        # self.storage = []  # Using an array
        self.storage = LinkedList()  # using linked list

    def __len__(self):
        # return len(self.storage)  # using array
        return self.size

    def push(self, value):
        # self.storage.insert(0, value)  # inserts value at index 0
        self.storage.add_to_tail(value)  # run new nude through add_to_tail method
        self.size += 1

    def pop(self):
        # check that there are values in the list
        # using array
        # if self.storage:
        #     return self.storage.pop(0)  # removes the value at index 0 and returns that value
        # else:
        #     # if list is empty return None
        #     return None

        # using linked list
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        return None

# The difference between using an array and a linked list when using a stack
# is largely in the operation time. An array will take longer to 'push' and
# 'pop' because they require continguent allocation in memory. 
