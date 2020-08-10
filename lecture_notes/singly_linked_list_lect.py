# Linked Lists:
#   1. Store things in sequential order
#   2. Values stored in their own node
#       + Class we represent that has a value and a next_node
#       + Each node ONLY knows the value inside itself and its next node.

class Node:
    def __init__(self, value, next_node=None):
        # value the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_node = next_node

    # method to get value of the node
    def get_value(self):
        return self.value

    # method to get the node's next_node
    def get_next(self):
        return self.next_node

    # method to update the node's next_node to the input node
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # wrap value in a node
        new_node = Node(value)
        # check if linked list is empty
        if self.head is None and self.tail is None:
            # set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node
        else:
            # update the last node's 'next_node' to the new node
            self.tail.set_next(new_node)
            # update 'self.tail' to point to the new node we just added
            self.tail = new_node

    def remove_tail(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        
        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        # otherwise, linked list has more than one node
        else:
            # store last node's value in another variable so we can return it
            val = self.tail.get_value()
            # need to set 'self.tail' to second-to-last node
            # only way is by traversing the whole linked list from the beginning

            # starting from the head, we'll traverse down to the second to last node
            # init another reference to keep track of where we are in the linked list
            # as we're iterating
            current = self.head

            # keep iterating until the node after 'current' is the tail
            while current.get_next() != self.tail:
                # keep iterating
                current = current.get_next()

            # set 'self.tail' to 'current'
            self.tail = current
            # set new tail's next_node to none
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value that we need to return
            val = self.head.get_value()
            # set 'selef.head' to the old head's 'next_node'
            self.head = self.head.get_next()
            # return the old head's value
            return val



if __name__ == "__main__":
    ll = LinkedList()  # Head -> None, Tail -> None
    ll.add_to_tail(5)
    # ll = Node(5)
    # ll.add_to_end(7)
    # ll.add_to_end(18)
    # ll.add_to_end(22)
    # ll.add_to_end(3)
    # ll.set_next(Node(7))
    # ll.next.set_next(Node(18))
    # ll.next.next.set_next(Node(22))
    # ll.next.next.next.set_next(Node(3))