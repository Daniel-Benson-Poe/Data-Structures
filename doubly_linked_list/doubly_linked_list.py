"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev  # points to current node's previous node
        self.value = value  # points to current node's value
        self.next = next  # points to current node's next node
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node  # holds head of doubly linked list
        self.tail = node  # holds tail of doubly linked list
        self.length = 1 if node is not None else 0  # holds length of doubly linked list

    def __len__(self):
        return self.length  # method to return length of doubly linked list
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)  # instantiate new node
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            self.head = new_node  # set head to new node
            self.tail = new_node  # set tail to new node
            self.length += 1  # increment length by 1
        else:
            new_node.next = self.head  # if there are already nodes in the linked list
            self.head.prev = new_node  # set current head's previous node to new node
            self.head = new_node  # set current head to new node
            self.length += 1  # increment length by 1
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            return  # return None if linked list is already empty
        if not self.head.next:  # check if there is only one node present in linked list
            head = self.head  # hold head node in a variable
            self.head = None  # set head to None
            self.tail = None  # set tail to None
            self.length = 0  # set length to 0; the linked list is empty at this point
            return head.value  # return value of the removed head node
        val = self.head.value  # hold value of head node in temporary variable
        self.head = self.head.next  # set head to current head's next node
        self.head.prev = None  # set head's previous node to None
        self.length -= 1  # decrement length by 1
        return val  # return value of removed head node
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)  # instantiate new node
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            self.head = new_node  # set head to new node
            self.tail = new_node  # set tail to new node
            self.length += 1  # increment length by 1
        
        else:  # If nodes are already present in linked list
            self.tail.next = new_node  # set current tail's next node to new node
            new_node.prev = self.tail  # set new node's previous node to current tail
            self.tail = new_node  # set current tail to new node
            self.length += 1  # increment length by 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            return  # return None (linked list is empty)
        val = self.tail.value  # hold value of current tail node in temp variable
        if self.tail.prev is None:  # check if there is only one node in the linked list
            self.head = None  # set current head node to None
            self.tail = None  # set current tail node to None
            self.length = 0  # set length of linked list to 0; the linked list is currently empty
        else:  # if there is more than 1 node in the linked list
            self.tail = self.tail.prev  # set tail to current tail's previous node
            self.tail.next = None  # set new tail's next node to None
        self.length -= 1  # decrement length by 1
        return val  # return value of removed tail node
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            return  # return None; linked list is empty
        current = self.tail  # set current node to the current tail node
        while current is not node:  # check if the current node is equal to the node we are searching for
            current = current.prev  # set current to current's previous node
        moved_node = current  # set current node into temp variable for storage
        if current.next is None:  # Check if current node is the tail of the linked list
            self.tail = self.tail.prev  # set tail to current tail's previous node
            self.tail.next = None  # set new tail's next node to None
        else:  # If current node is not the tail node
            current.prev.next = current.next  # set current node's previous node's next node to current node's next node
            current.next.prev = current.prev  # set current node's next node's previous node to current node's previous node
        
        moved_node.next = self.head  # set the moved node's next node to current head
        self.head.prev = moved_node  # set current head's previous node to the moved node
        self.head = moved_node  # set current head to moved node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            return  # return None; linked list is empty
        current = self.head  # set current node to current head node
        while current is not node:  # check if current node is node being looked for
            current = current.next  # set current node to current node's next node
        moved_node = current  # set current node to temp variable for storage
        if current.prev is None:  # check if current node is the head of the linked list
            self.head = self.head.next  # set head to current head's next node
            self.head.prev = None  # set new head's previous node to None
        else:  # if current node is not head of the linked list
            current.prev.next = current.next  # set current node's previous node's next node to current node's next node
            current.next.prev = current.prev  # set current node's next node's previous node to current node's previous node
        
        self.tail.next = moved_node  # set current tail's next node to the moved node
        moved_node.prev = self.tail  # set the moved node's previous node to current tail node
        moved_node.next = None  # set moved node's next node to None
        self.tail = moved_node  # set tail node to moved node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            return  # return None; linked list is empty
        current = self.head  # set current node to current head node
        while currrent is not node:  # check if current node is target node
            current = current.next  # set current node to current node's next node
        if current.prev is None and current.next is None:  # check if there is only one node in linked list
            self.head = None  # set head node to None
            self.tail = None  # set tail node to None
            self.length = 0  # set length of linked list to 0; linked list is now empty
        elif current.prev is None:  # check if current node is the head node
            self.head = self.head.next  # set head node to current head node's next node
            self.head.prev = None  # set new head node's previous node to None
        elif current.next is None:  # check if current node is the tail node
            self.tail = self.tail.prev  # set tail node to current tail node's previous node
            self.tail.next = None  # set new tail node's next node to None
        else:  # if current node is some node in between the head node and tail node
            current.prev.next = current.next  # set current node's previous node's next node to current node's next node
            current.next.prev = current.prev  # set current node's next node's previous node to current node's previous node
        self.length -= 1  # decrement length by 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:  # check if there are no nodes present in the linked list
            return  # return None; linked list is empty
        max_num = self.head.value  # set max_num variable to current head node's value
        current = self.head  # set current node to current head node
        while current.next:  # check if current node's next node is not None
            current = current.next  # set current node to current node's next node
            if current.value > max_num:  # check if current node's value is greater than max_num's value
                max_num = current.value  # if so, set max_num variable to current node's value
        return max_num  # return max_num variable