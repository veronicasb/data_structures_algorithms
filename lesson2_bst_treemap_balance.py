from lesson2_linear_binary import TreeNode
from lesson2_linear_binary import User
import random, string

practice_tuple = ((4, 7, (None, 8, 9)), 12, ((6, 10, 11), 13, (10, 15, 18)))
tree = TreeNode.parse_tuple(practice_tuple)

"""
BINARY SEARCH TREE (BST)

A BST is a binary tree that has the following features:
1. The left subtree of any node only contains nodes with values LESS THAN a node's value
2. The right subtree of any node only contains nodes with values GREATER THAN a node's value

With this, every subtree of a BST is itself a BST
"""

# A function to check if a binary tree is a BST, find the maximum key, and find the minimum key


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    # first, check if node exists
    if node is None:
        # if node does not exist, return the following
        return True, None, None

    # this line of code will travel down the left side of a BT until it there are no more
    is_bst_l, min_l, max_l = is_bst(node.left)
    # this line of code will travel down the right side of a BT until it there are no more
    is_bst_r, min_r, max_r = is_bst(node.right)

    # check if tree is a BST:
    # are left and right nodes BSTs?
    is_bst_node = (
        is_bst_l
        and is_bst_r
        and
        # is there no left subtree? | is the current node key greater than the max in the left subtree?
        (max_l is None or node.key > max_l)
        and
        # is there no right subtree? | is the current node key less than the min in the right subtree?
        (min_r is None or node.key < min_r)
    )

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # this function returns whether the node is a BST, its minimumu key, and maximum key
    return is_bst_node, min_key, max_key


print(is_bst(tree))


"""
STORING KEY-VALUE PAIRS USING BSTS
"""


class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


valorie = User("Valorie Kuhens", "valorie", "vk@gmail.com")
jazmyne = User("Jazmyne Daniels", "jazmyne", "jd@gmail.com")
kalin = User("Kalin Denton", "kalin", "kd@gmail.com")
robin = User("Robin Sands", "robin", "rs@gmail.com")
monica = User("Monica Burgess", "monica", "mb@gmail.com")
lexi = User("Lexi Grant", "lexi", "lg@gmail.com")
jose = User("Jose Valasquez", "jose", "jv@gmail.com")

users = [valorie, jazmyne, kalin, robin, monica, lexi, jose]

new_tree = BSTNode(kalin.username, kalin)

print(new_tree.key, new_tree.value)


"""
INSERTING INTO A BST
"""


def insert(node, key, value):
    # if a node doesnt exist, create a node in that place
    if node is None:
        node = BSTNode(key, value)

    # starting from root node, compare key to be inserted
    # if key being inserted is smaller, recursively insert in left subtree or
    # attach as left child
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node

    # if key being inserts is larger, recurively insert in right subtree or attach
    # as right child
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node

    # return root node
    return node


# to create first node, user insert function none as target
tree3 = insert(None, kalin.username, kalin)
print(tree3.key, tree3.value)

# insert all users into new tree
for user in users:
    insert(tree3, user.username, user)

TreeNode.display_keys(tree3)


"""
Skewed/unbalanced BSTs are problematic because the height of them ceases to be logarithmic.

If a tree is balanced, its time complexity of insertion is O(log N), otherwise, worst-case
complexity, it is O(N).
"""

print(TreeNode.height(tree3))


"""
FINDING A NODE IN A BST
"""


def find(node, key):
    # if root node is none, the tree doesnt even exist
    if node is None:
        return None
    # if root node is equal to search key, search key is the root node
    if key == node.key:
        return node
    # if search key is less than the key of the root node, start searching left subtree
    if key < node.key:
        return find(node.left, key)
    # if search key is greater than the key of the root node, start searching right subtree
    if key > node.key:
        return find(node.right, key)


result = find(tree3, "monica")
print(result.key, result.value)


"""
UPDATING A NODE IN A BST

Time complexity is the same as find operation
"""


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


"""
LIST ALL NODES

Time complexity = O(n), where n is number of nodes
"""


def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


print(list_all(tree3))


""" 
CHECK FOR A BALANCED BT

If a tree is balanced, its time complexity of insertion is O(log N), otherwise, worst-case
complexity, it is O(N).
"""


def is_balanced(node):
    # the end condition occurs first
    if node is None:
        return True, 0
    # ensure left subtree is balanced
    balanced_l, height_l = is_balanced(node.left)
    # ensure right subtree is balanced
    balanced_r, height_r = is_balanced(node.right)
    # ensure the height difference between the two isnt more than 1
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height


"""
CREATE A BALANCED BST

Use a recursive strategy to turn the middle element into the root node, then
create left and right subtrees accordingly.

The algorithms closely resembles a binary search.

***Data must be sorted***
"""


def make_balanced_bst(data, low=0, high=None, parent=None):
    """
    setting our default parameters make's it easier to call this function because our
    low, high, and parent will generally be the same every time we call this function.
    But we cant set the low, high, and parent within the function because we are
    calling this function recursively.
    """
    if high is None:
        # high will get set to the number of elements in our data
        high = len(data) - 1
    if low > high:
        # if low is greater than high, this means we're outside the index of our data
        return None

    # calculate the middle index of our data
    middle = (low + high) // 2
    # set the key-value pair for our root node as the key-value pair at the middle of our data
    key, value = data[middle]

    # create our root node using the key-value pair from the middle of our data
    root = BSTNode(key, value)
    # the parent of our root node will be None by default (root nodes dont have parents because they lead the tree structure)
    root.parent = parent

    # the left child of our root node will be less than the value of our middle key-value pair from our data (set as our root node)
    """
    we will recursively call our function and pass along the same data, 0 as our low, the index before the middle
    index of our data, and the root node we just created (containing the key-value pair of the middle our data) as our parent
    """
    root.left = make_balanced_bst(data, low, middle - 1, root)

    # the right child of our root node will be greater than the value of our middle key-value pair from our data (set as our root node)
    """
    we will recursively call our function and pass along the same data, the index after the middle index of our data 
    as our low, the last index of our data as our high (which we set above), and the root node we just 
    created (containing the key-value pair of the middle our data) as our parent
    """
    root.right = make_balanced_bst(data, middle + 1, high, root)

    # our final result will be an entire BST, which is returned as the root node of that structure
    return root


user_data = [(user.username, user) for user in users]
user_data.sort()
balanced_user_bst = make_balanced_bst(user_data)
TreeNode.display_keys(balanced_user_bst)


"""
BALANCE AN UNBALANCED BST

first perform an inorder traversal, then create a balanced BST using the above function
"""


def balance_bst(node):
    # in the case of BSTs, list_all is an inorder traversal operation
    return make_balanced_bst(list_all(node))


# create a heavily skewed BST
unbalanced_tree = None

for user in users:
    unbalanced_tree = insert(unbalanced_tree, user.username, user)

TreeNode.display_keys(unbalanced_tree)

unbalanced_tree_balanced = balance_bst(unbalanced_tree)

TreeNode.display_keys(unbalanced_tree_balanced)


"""
After every insertion, balance the tree

Complexity of operations on a balanced BST:

- Insert: O(logN) + O(N) = O(N)
-- If a tree is balanced, its height is O(logN). For insertion, you may have to traverse a path from the root to a leaf.
-- At max, the length of that path is the height of the tree or O(logN)
-- If we balance a tree after every insertion, that's an additional O(N)
-- LogN becomes much smaller than N as N grows

- Find: O(logN)
- Update: O(logN)
- List all: O(N)

We will find that the log of 100 mil [O(logN)] is around 26, which means it would only take
26 operations to find or update a node in a BST.

O(N), the speed of our original solution, would take 100 mil operations.

All of this amounts to 19 milliseconds vs. 10 seconds, so O(logN) is 300,000x faster than O(N), which 
ends up being a significantly better user experience and cost-effective (CPU is business for less time 
so you wont need a large machine or too many machines).

To speed up insertions, we could balance a BST every 1000 insertions (every 1000th insertions 
would take a few seconds) or balance every hour.
"""


"""
A PYTHON-FRIENDLY TREEMAP

The ultimate solution to our original problem.

Remember that a map/treemap is a binary tree containing key-value pairs.
"""


# in place of our original UserDatabase class
class TreeMap:
    # internally stores a balanced binary search tree
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        # a combination of insert and update
        node = find(self.root, key)
        counter = 0
        if not node:
            self.root = insert(self.root, key, value)
            counter += 1
            if counter == 1000:
                self.root = balance_bst(self.root)
                counter = 0
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        # replacement to find operation
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        # replacement for list_all function
        # round brackets instead of square brackets means we've created a generator
        return (x for x in list_all(self.root))

    """
    GENERATORS REFRESHER

    generators - are functions that return an object that can be iterated over
    special because they generate elements in object "lazily" (generate items one at a time and only when you ask for it )
    memory efficient, good for large data sets

    yield keyword
    def mygenerator():
        yield 1
        yield 2
        yield 3
    """

    def __len__(self):
        return TreeNode.size(self.root)

    def display(self):
        return TreeNode.display_keys(self.root)

    """
    We've set special methods in our class that allow us to use indexing notation instead
    of calling methods using dot notation
    """


treemap = TreeMap()

for user in users:
    treemap[user.username] = user.username

treemap.display()

veronica = User(username="veronica", name="Veronica Burgess", email="vb@gmail.com")

treemap["veronica"] = veronica

treemap.display()

# __len__ allows us to use len function on class object
print(len(treemap))

# __iter__ allows us to iterate over class object
for key, value in treemap:
    print(key, value)


"""
When creating solutions, make implementation as Python-friendly/intuitive as possible
AKA "encapsulation"
"""


# Test lots of users
def random_user():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(5))


user_count = 0
while user_count < 2000:
    rand_username = random_user()
    rand_name = f"{rand_username} {random_user()}"
    rand_email = f"{random_user()}@gmail.com"
    new_user = User(username=rand_username, name=rand_name, email=rand_email)
    treemap[rand_username] = new_user
    user_count += 1

treemap.display()


"""
SELF-BALANCING BINARY TREES & AVL TREES

A self-balancing binary tree is one that remains balanced after every node insertions. 

An AVL Tree is one form of a self-balancing tree. The way it works: track the "balance factor" 
(the height difference between the left and right subtrees), then rotate unbalanced subtrees 
along the path of insertion/deletion.

The "balance factor" of a balanced BST is 0, -1, or 1. When you insert a new node into the BST, 
it increments (by 1) the balance factor of each node it must "travel over" to get to its position. 
Anytime a node reaches a balance factor of 2 or -2, the tree must be rotated at that node to balance 
back out. Negative/positive balance factors represent whether the node is in the left 
subtree (negative) or the right subtree (positive).

4 scenarios for balancing:

1. Left-Right: [2 rotations] when 3 nodes zigzag left then right (1 <- -2 | 1 -> 0), shift the nodes so 
that the trio becomes left-aligned (1 <- 0 <- -2), then complete the scenario with a Right-Right rotation. 

2. Right-Left: [2 rotations] when 3 nodes zigzag right then left (2 -> -1 | 0 <- -1), shift the nodes so 
that the trio becomes right-aligned (2 -> 0 -> -1), then complete the scenario with a Left-Left rotation. 

3. Left-Left: [1 rotation] when 3 nodes are all right-aligned (2 -> 1 -> 0), shift trio to the left (-1) 
so that the middle node becomes the root. After balancing, balance factor of the trio defaults back 
to 0 -> 0 -> 0.

4. Right-Right: [1 rotation] when 3 nodes are all left-aligned (0 <- -1 <- -2), shift trio to the right (1) 
so that middle node becomes root. After balancing, balance factor of trio defaults back to 0 -> 0 -> 0.


Complexity: Each rotation takes constant time. At most, log N (height of traversal path) rotations may 
be required. Insertion and deletion can be performed in O(log N) time. 

"""

# HELPER FUNCTIONS

# Left rotation while preserving BST properties

# Right rotation while preserving BST properties

# At insertions, perform rotation at the proper place

# Track balance factor of each node


"""
SUMMARY

1. We started with a list
2. We improved upon it by transforming it into a Binary Tree
3. We improved upon it by transforming it into a Binary Search Tree
4. Added balancing into the mix
 
Binary trees form the basis of relational databases like MySQL
"""
