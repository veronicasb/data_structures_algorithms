from lesson2_binary_trees import TreeNode
from lesson2_binary_trees import User

practice_tuple = ((4, 7, (None, 8, 9)), 12, ((6, 10, 11), 13, (10, 15, 18)))
tree = TreeNode.parse_tuple(practice_tuple)

'''
BINARY SEARCH TREE (BST)

A BST is a binary tree that has the following features:
1. The left subtree of any node only contains nodes with values LESS THAN a node's value
2. The right subtree of any node only contains nodes with values GREATER THAN a node's value

With this, every subtree of a BST is itself a BST
'''

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
    is_bst_node = (is_bst_l and is_bst_r and 
                   # is there no left subtree? | is the current node key greater than the max in the left subtree?
                   (max_l is None or node.key > max_l) and
                    # is there no right subtree? | is the current node key less than the min in the right subtree?
                   (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # this function returns whether the node is a BST, its minimumu key, and maximum key
    return is_bst_node, min_key, max_key

print(is_bst(tree))


'''
STORING KEY-VALUE PAIRS USING BSTS
'''
class BSTNode():
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


'''
INSERTING INTO A BST
'''

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


'''
Skewed/unbalanced BSTs are problematic because the height of them ceases to be logarithmic.

If a tree is balanced, its time complexity of insertion is O(log N), otherwise, worst-case
complexity, it is O(N).
'''

print(TreeNode.height(tree3))


'''
FINDING A NODE IN A BST
'''

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


'''
UPDATING A NODE IN A BST

Time complexity is the same as find operation
'''

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


'''
LIST ALL NODES

Time complexity = O(n), where n is number of nodes
'''

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

print(list_all(tree3))