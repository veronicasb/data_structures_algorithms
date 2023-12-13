'''

METHOD

1. State the problem clearly and idenitfy output and inputs
2. Come up with example inputs and outputs and try to cover all edge cases
3. Come up with a correct solution in plain English
4. Implement the solution and test it using example inputs. Fix any bugs
5. Analyze the algorithm's complexity and identify inefficiencies
6. Apply the right techniques to overcome inefficiencies. Then, repeat steps 3-6

'''


'''

PROBLEM

Develop a fast in-memory data structure to manage profile information (username, name, email) for 100 
million users. It should allow the following operations to be performed:
- Insert profile information for a new user
- Find profile information of a user with their username
- Update profile information of user with their username
- List all users of the platform sorted by username

You can assume all usernames are unique

'''


###
# Step 1
### 

'''
We need to create a data structure that can store 100 million records and perform
insertion, search, update, and list operations efficiently.

A data structure is something we can define using a class.

INPUTS
details to create a new user:
- user profiles (username, name, email)

OUTPUTS
details from doing the following operations:
- insert
- find
- update
- list_all

'''

# OOP
# classes are a perfect way to represent a person of some kind
# a class is a blueprint for creating an object
class User:
    pass

user1 = User()
print(type(user1))

# Add constructor method to classes to store attributes or properties
# Constructor methods are special funtions that create an instance of a class.
'''
class User:
    # constructor method is essential
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        print(f"User {self.name} created!")

user1 = User("Kalin Denton", "Kalin", "bababa@gmail.com")
print(user1.name)
'''

# Add custom method to class
'''
class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email
        print(f"User {self.name} created!")

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}.")

user2 = User("Shiela Socorro", "Shiela", "radarada@gmail.com")
user2.introduce_yourself("Kalin")
'''

# remove any print statements and add helper methods
# these methods are used to create a string representation of our object
class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User (username = '{self.username}', name = '{self.name}', email= '{self.username}')"
    
    def __str__(self):
        return self.__repr__()
    
'''
__str__() and __repr__()

These 2 functions return an objects string representation.

They're different in that __repr__() is intended to hold information about the object so that it may be created again.
__repr__() is a developer-friendly string representation of an object, while 
__str__() is more human/user-friendly and used for logging reasons.

'''

# Create a class for our output
'''
class UserDatabase:
    def insert(self, user):
        pass
    
    def find(self, username):
        pass

    def update(self, user):
        pass

    def list_all(self):
        pass

'''

###
# Step 2
###

# It's good practice to list out method signatures before implementation

valorie = User("Valorie Kuhens", "valorie", "vk@gmail.com")
jazmyne = User("Jazmyne Daniels", "jazmyne", "jd@gmail.com")
kalin = User("Kalin Denton", "kalin", "kd@gmail.com")
robin = User("Robin Sands", "robin", "rs@gmail.com")
monica = User("Monica Burgess", "monica", "mb@gmail.com")
lexi = User("Lexi Grant", "lexi", "lg@gmail.com")
jose = User("Jose Valasquez", "jose", "jv@gmail.com")

users = [valorie, jazmyne, kalin, robin, monica, lexi, jose]

'''

POTENTIAL SCENARIOS (for each operation)

1. Insert
- insert into an empty database
- insert a user with a username that already exists
- insert a user with a username that doesnt exist
- insert a user with an email that already exists

2. Find
- find a user by name
- find a user by username
- find a user by email
- find a user that does not exist

3. Update
- update a user's name
- update a user's username
- update a user's email
- update a user that does not exist

4. List All
- list all users by username
- list all users by name
- list all users by email
- list all from an empty database

'''


###
# Step 3
###

'''

SOLUTION IN PLAIN ENGLISH

We store User objects in a list sorted by usernames

The operations can be implemented:

1. Insert: loop through the sorted list of users, then add the new user at the postion
that keeps the list sorted

2. Find: Loop through the sorted of users, then find the user object with the username 
matching our query

3. Update: Loop through the sorted list, then find the user object matching the query 
and update the details

4. List: return the list of all User objects

- Note: strings can be compared like integers

'''


###
# Step 4
###

class UserDatabase:
    def __init__(self):
        # a call to this class takes no arguments
        # instantiating it will create an empty list for new users
        self.users = []

    def insert(self, user):
        # create a starting position at 0
        i = 0
        # iterate through all users
        while i < len(self.users):
            # Find the first username greater than the new user's username
            # letters that come before a letter are "less than"
            if self.users[i].username > user.username:
                # once we find the username that we must insert in front of, break out of while loop
                break
            # incrememt position by 1 until we find the username we must insert in front of
            i += 1
        # once we find the username that we must insert in front of, insert it
        self.users.insert(i, user)

    def find(self, username):
        # for each user in the users list...
        for user in self.users:
            # if the username we're looking for appears...
            if user.username == username:
                # return all associated information
                return user
            
    def update(self, user):
        # make a call to the find method, assign it to variables
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

# We can create a new database of users by instantiating an object of UserDatabase class
database1 = UserDatabase()

database1.insert(valorie)
database1.insert(jazmyne)
database1.insert(kalin)

database1.update(User(username = 'kalin', name = 'Kalin D', email = 'kalind@gmail.com'))

# Test potential scenarios

# inserts duplicate usernames
database1.insert(kalin)
print(database1.list_all())

# finds by username, returns None by other details and nonexistent users
print(database1.find('kalin'))
print(database1.find('Kalin D'))
print(database1.find('kalind@gmail.com'))
print(database1.find('veronica'))

# email didnt update, name updated, cant update username, updating a non existent user causes an error
database1.update(User(username='kalin', name='bababa', email='bababa@gmail.com'))
# database1.update(User(username='veronica', name='vero', email='vb@gmail.com'))
print(database1.list_all())


###
# Step 5
###

'''

Insert: O(N)
Find: O(N)
Update: O(N)
List: O(1)

We find that to iterate over 100 million users in our database with the structure we've created
so far, it would take about 10 seconds to simply list all the users, which is slow in today's
technology.

'''


###
# Step 6
###

'''

We can limit number of iterations for common operations (insert, find, and update) by implementing a
binary tree. A binary tree is made up of nodes with branches that point to up to 2 children nodes.
Nodes have 0, 1, or 2 children nodes. Nodes without children are sometimes called leaves.
The single node that begins the tree (at the top) is the root node and it's where operations begin.

We will need key-value pairs for our purposes. Binary trees with kay-value nodes are often referred to as 
a map or treemap

A Binary Search Tree features left subtrees of any node that are lexicographically smaller than a node's key, while
the right subtrees of any node are lexicographically greater. It's easy to locate specific keys by traversing
a single path from the root node.

A balanced tree is a tree that doesnt skew too heavily on either side (the left and right side of the tree arent 
more than 1 level off).

'''


###
# Creating a binary tree
###

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print(type(node0))

node0.left = node1
node0.right = node2
tree = node0

node0 = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(5)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

node0.left = node1
node0.right = node3
node1.left = node2
tree = node0
node3.left = node4
node3.right = node5
node4.right = node6
node5.left = node7
node5.right = node8


# more efficient way than manually creating a tree:
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        # recursive call to function
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(tree_tuple)

print(tree2.key, tree2.left.key, tree2.right.key)


# convert tree back to a tuple

def tree_to_tuple(node):
    # check if argument is a TreeNode object
    if isinstance(node, TreeNode):
        # if the node has no children...
        if node.left == None and node.right == None:
            # return the value of that node
            return node.key
        # otherwise, return a tuple 
        return (
            # every recursive call to this function will return a tuple for as long as
            # each node passed has children
            tree_to_tuple(node.left), 
            node.key, 
            tree_to_tuple(node.right)
        )
    
print(tree_to_tuple(tree2))


# helper function to display keys in a tree

def display_keys(node, space="\t", level=0):
    if node is None:
        print(space*level + "x")
        return
    
    if node.left is None and node.right is None:
        print(space* level + str(node.key))
        return
    
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)

display_keys(tree2)


practice_tuple = ((4, 7, (None, 8, 9)), 12, ((6, 10, 11), 13, (10, 15, 18)))
practice_tree = parse_tuple(practice_tuple)
print(practice_tree.key)

display_keys(practice_tree)

print(tree_to_tuple(practice_tree))


###
# Traversing a Binary Tree (very common coding interview material)
#

'''
A traversal is the process of visiting every node in a binary tree exactly once.
Visiting a node entails adding a node's key to a list. 

Inorder traversal: traverse left subtree recursively in order, traverse the current node, then traverse the right subtree recursively in order

Preorder traversal: traverse the current node, traverse the left subtree recursively preorder, then traverse the right subtree recursively preorder

Postorder traversal: traverse left subtree recursively postorder, traverse right subtree recursively post order, then traverse the current node
'''


# A function to perform an inorder traversal of a binary tree
def traverse_in_order(node):
    # if node is None, this means we've come across a parent node with no children
    if node is None:
        # return an empty list/array
        return []
    # recursively move thru nodes along the left of the tree until node is None
    # add key of current node to list
    # recursively move thru nodes along the right of the tree until node is None
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))

print(traverse_in_order(tree2))


# A function to perform a preorder traversal of a binary tree
def traverse_preorder(node):
    if node is None:
        return []
    return([node.key] + 
           traverse_preorder(node.left) + 
           traverse_preorder(node.right))

print(traverse_preorder(tree2))


# From leetcode.com (preorder)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        return([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))
    
# recursive calls to methods must be called via "self"
    

# A function to perform a postorder traversal of a binary tree
def traverse_postorder(node):
    if node is None:
        return []
    return (traverse_postorder(node.left) + 
            traverse_postorder(node.right) + 
            [node.key])

print(traverse_postorder(tree2))


# calculate height/depth of a binary tree
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree2))

# count number of nodes in a binary tree
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

print(tree_size(tree2))
