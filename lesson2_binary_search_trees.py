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


''' 
CHECK FOR A BALANCED BT

If a tree is balanced, its time complexity of insertion is O(log N), otherwise, worst-case
complexity, it is O(N).
'''

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


'''
CREATE A BALANCED BST

Use a recursive strategy to turn the middle element into the root node, then
create left and right subtrees accordingly.

The algorithms closely resembles a binary search.

***Data must be sorted***
'''

def make_balanced_bst(data, low=0, high=None, parent=None):
    '''
    setting our default parameters make's it easier to call this function because our
    low, high, and parent will generally be the same every time we call this function.
    But we cant set the low, high, and parent within the function because we are 
    calling this function recursively.
    '''
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
    '''
    we will recursively call our function and pass along the same data, 0 as our low, the index before the middle
    index of our data, and the root node we just created (containing the key-value pair of the middle our data) as our parent
    '''
    root.left = make_balanced_bst(data, low, middle-1, root)

    # the right child of our root node will be greater than the value of our middle key-value pair from our data (set as our root node)
    '''
    we will recursively call our function and pass along the same data, the index after the middle index of our data 
    as our low, the last index of our data as our high (which we set above), and the root node we just 
    created (containing the key-value pair of the middle our data) as our parent
    '''
    root.right = make_balanced_bst(data, middle+1, high, root)

    # our final result will be an entire BST, which is returned as the root node of that structure
    return root 

user_data = [(user.username, user) for user in users]
user_data.sort()
balanced_user_bst = make_balanced_bst(user_data)
TreeNode.display_keys(balanced_user_bst)


'''
BALANCE AN UNBALANCED BST

first perform an inorder traversal, then create a balanced BST using the above function
'''
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