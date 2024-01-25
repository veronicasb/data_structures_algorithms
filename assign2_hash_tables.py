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
    result = 0

    for char in a_string:
        num = 

        result += 1

    index = result %
    return index

get_index(data_list, '') == 0 # should output True