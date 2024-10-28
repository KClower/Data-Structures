"""
Singly Link Lists only point in one direction.
There is still a head andf tail.
Find the tail by finding None.
"""

"""
Breakout project:
How do you find and return the middle node of a singly link list in one pass ?
You do not have access to the length of the list.
If the list is even you should return the first of the two nodes.
You may not store nodes in another data structure. (Don't use an array)
"""

"""
Understand:
Find the middle node in one pass.
Return the first of the two nodes if the list is even.

Plan:
A while loop with 2 pointer variables where one variable makes 2 next moves, 
the other makes 1 next move until None is found by the pointer making 2 next moves.
Return the variable that is making 1 next move.
"""

"""
Execute:
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        pass
        # new_node = Node(value)
        # if not self.head:
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     self.head.prev = new_node
        #     self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def remove_tail(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value

        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        current.next = None
        self.tail = current
        return value

    def find_mid(self):
        pass
        # current_node_one = self.head
        # current_node_two = self.head
        # if not self.head.next:
        #     return self.head
        # if not self.head.next.next:
        #     return self.head
        # while current_node_one.next:
        #     if current_node_one.next.next:
        #         current_node_one = current_node_one.next.next
        #         current_node_two = current_node_two.next
        #     else:
        #         return current_node_two
        # return current_node_two

