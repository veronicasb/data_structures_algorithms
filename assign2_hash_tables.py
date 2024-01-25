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

"""
ALGORITHM FOR HASHING - CONVERT STRINGS INTO NUMERIC LIST INDICES

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


# Basic hash table implementation