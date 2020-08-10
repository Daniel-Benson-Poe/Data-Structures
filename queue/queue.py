from singly_linked_list import Node, LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# Using array:
# class Queue:
#     def __init__(self):
#         # self.size = 0
#         self.storage = []  # using an array
    
#     def __len__(self):
#         return len(self.storage)  # return length of the queue array

#     def enqueue(self, value):
#         # appnd value to the end of the array
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             # remove value from the front of the list - this is our first in first out
#             return self.storage.pop(0)
#         return None

# Using linked list:
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size  # return size of the queue

    def enqueue(self, value):
        # insert tail to the queue
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            val = self.storage.remove_head()
            self.size -= 1
            return val
        return None