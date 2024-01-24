"""
PROBLEM

Write a function to reverse a linked list.

"""


# What is a linked list?

"""
A data structure used for storing a sequence of elements, similar to 
a list.

"""

# Create a linked list and store numbers in it

class Node:
    def __init__(self, num):
        self.data = num
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

list1 = LinkedList
list1.head = Node(2)
list1.head.next = Node(3)
list1.head.next.next = Node(4)

# Improve our process and retrieve numbers from linked list

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = Node(val)

    def show(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

list2 = LinkedList() # parentheses are needed here in order to use methods
list2.append(2)
list2.append(3)
list2.append(5)

list2.show()

# Add methods to retrieve more information about our linked list

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = Node(val)

    def show(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next

    def length(self):
        result = 0
        cur = self.head
        while cur is not None:
            result += 1
            cur = cur.next
        return result

    def get_element(self, position):
        i = 0
        cur = self.head
        while cur is not None:
            if i == position:
                return cur.data
            cur = cur.next
            i += 1
        return None

list3 = LinkedList()
list3.append(2)
list3.append(3)
list3.append(5)
list3.append(9)

list3.show()

print("\n", list3.length())

print(list3.get_element(2))


"""
SOLUTION

Reverse a linked list

"""

def reverse_ls(node):
    if node.head is None:
        return 
    
    cur_node = node.head
    prev_node = None

    while cur_node is not None:
        next_node = cur_node.next

        cur_node.next = prev_node
        
        prev_node = cur_node
        cur_node = next_node

    node.head = prev_node

reverse_ls(list3)

list3.show()


