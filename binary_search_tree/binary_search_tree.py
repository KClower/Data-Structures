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

import sys
sys.path.append('./queue')
from queue import Queue
sys.path.append('./stack')
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        
        elif value >= self.value: # this line handles multiple values (not conventional)
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, cb):
        cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        queue = Queue()
        queue.enqueue(self)

        while len(queue) > 0:
            current = queue.dequeue()
            

            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
      

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()
        stack.push(self)

    # Iterate while the stack is not empty
        while len(stack) > 0:
        # Pop the current node from the stack
            current_node = stack.pop()
            print(current_node.value)  # Print the node's value

        # Push the right and then left children to the stack if they exist
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)

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
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print(bst.contains(7))
print(bst.contains(20))
print(bst.get_max())
def print_value(value):
    print(value)

# Call for_each to apply print_value to each node
bst.for_each(print_value)

# Example of summing all values in the tree
sum_values = 0
def sum_fn(value):
    global sum_values
    sum_values += value

bst.for_each(sum_fn)
print(f"Sum of all values: {sum_values}")
bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
