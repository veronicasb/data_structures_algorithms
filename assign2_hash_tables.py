"""
Dictionaries in Python are implemented using a data structure called hash table. 

A hash table uses a list/array to store the key-value pairs, and uses a hashing 
function to determine the index for storing or retrieving the data associated 
with a given key.

"""


"""
PROBLEM

Implement a Hash Table that allows for insertion, finding, updating, and listing.

"""

# Create a list of a fixed size

MAX_SIZE = 4096

data_list = [None] * MAX_SIZE

# Template to create Hash Table

class HashTable:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass
    
    def find(self, key):
        """Find the value associated with a key"""
        pass
    
    def update(self, key, value):
        """Change the value associated with a key"""
        pass
    
    def list_all(self):
        """List all the keys"""
        pass


# HASHING FUNCTION
    
"""
ALGORITHM FOR HASHING FUNCTION - CONVERT STRINGS INTO NUMERIC LIST INDICES

1. Iterate over string
2. Convert each character into a number using "ord" function
3. Add numbers for each character to obtain hash for entire string
4. Take remainder of result with size of data list

"""

def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0

    for char in a_string:
        # Convert the character to a number (using ord)
        num = ord(char)
        # Update result by adding the number
        result += num

    # Take the remainder of the result with the size of the data list
    index = result % len(data_list)
    return index

print(get_index(data_list, '') == 0) # should output True

print(get_index(data_list, 'Aakash') == 585)


# Insert key_value pair into hash table

key, val = "Veronica", "415415415"

idx = get_index(data_list, key)

print(idx)

data_list[idx] = (key, val)

data_list[get_index(data_list, "Monica")] = ("Monica", "313313313")


# Find value associated with a pair - get hash of key and look up index in data list

idx = get_index(data_list, "Veronica")

print(idx)

key, val = data_list[idx]

print(val)

key, val = data_list[get_index(data_list, "Veronica")]

print(val)


# List keys using list comprehension

name_keys = [kv[0] for kv in data_list if kv is not None]

print(name_keys)


# BASIC HASH TABLE IMPLEMENTATION USING HASHING FUNCTION

class BasicHashTable:
    def __init__(self, max_size=MAX_SIZE):
        # 1. Create list of size 'max_size' with all values set to None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find index for key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store key-value pair at right index
        self.data_list[idx] = (key, value)

    def find(self, key):
        # 1. Find index for key using get_index
        idx = get_index(self.data_list, key)

        # 2. Retrieve data stored at index
        kv = self.data_list[idx]

        # 3. Return value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
        
    def update(self, key, value):
        # 1. Find index for key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store new key-value pair in right index
        self.data_list[idx] = (key, value)

    def list_all(self):
        # 1. Extract key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]
    
# Test - outputs should be "True"
    
basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list) == 1024)

# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# Find a value
print(basic_table.find('Hemanth') == '8888888888')

# Update a value
basic_table.update('Aakash', '7777777777')

# Check the updated value
print(basic_table.find('Aakash') == '7777777777')

# Get the list of keys
print(basic_table.list_all() == ['Aakash', 'Hemanth'])


# FUNCTION TO HANDLE COLLISIONS USING LINEAR PROBING

"""
HANDLING COLLISIONS USING LINEAR PROBING

A collision occurs when we try to store data at keys that share the same hash.

1. While inserting a new key-value pair, if the target index is occupied, we try the next 
index repeatedly until we find the closes empty location

2. While finding a key-value pair, we use the same strategy as above, but instead of searching 
for an empty location, we look for a location that contains a key-value pair with a matching key 

3. While finding a key-value pair, we use the same strategy as above, but instead of searching 
for an empty location, we look for a location that contains a key-value pair with a matching key 
and update its value

"""

def get_valid_index(data_list, key):
    # Start by getting index
    idx = get_index(data_list, key)

    while True:
        # Get key-value stored at idx
        kv = data_list[idx]

        # If None, return idx
        if kv is None:
            return idx
        
        # If stored key matches given key, return index
        k, v = kv
        if k == key:
            return idx
        
        # Move to next index
        idx += 1

        # Go back to start if you reach end of array
        if idx == len(data_list):
            idx = 0

# Test - output should be True

# Create an empty hash table
data_list2 = [None] * MAX_SIZE

# New key 'listen' should return expected index
print(get_valid_index(data_list2, 'listen') == 655)

# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, 'listen')] = ('listen', 99)

# Colliding key 'silent' should return next index
print(get_valid_index(data_list2, 'silent') == 656)


# IMPLEMENTATION OF HASH TABLE WITH LINEAR PROBING FUNCTION

