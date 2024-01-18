
"""
PROBLEM

You are given a list of numbers, obtained by rotating a sorted list an unknown number of 
times. Write a function to determine the minimum number of times the original sorted list 
was rotated to obtain the given list. Your function should have the worst-case complexity of 
O(logN), where N is the length of the list. You can assume that all the numbers in the list 
are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list 
[0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the 
first element.

"Sorted list" refers to a list where the elements are arrange in increasing order.

"""


# STATE PROBLEM CLEARLY. IDENTIFY INPUT AND OUTPUT FORMATS.

"""
A function that takes a rotated list, then counts the minimum number of times a sorted list 
had to be rotated to result in that given rotated list.

Inputs:
1. rotated_ls - a rotated list (ex. [5, 6, 9, 0, 2, 3, 4] )

Outputs:
1. rotations - an int as the number of times an original sorted list was rotated to 
match input nums (ex. if our original sorted list is [0, 2, 3, 4, 5, 6, 9], 
our output would be "3") 

"""

# our function signature

def rotated_list(rotated_ls):
    pass


# COME UP WITH EXAMPLE INPUTS AND OUTPUTS. TRY TO COVER EDGE CASES.

"""
1. A generic case - list of size 10 rotated 3 times.
2. A generic case - list of size 8 rotated 5 times.
3. A list that wasn't rotated at all.
4. A list that was rotated once.
5. A list that was rotated n-1 times, where n is the size of the list.
6. A list that was rotated n times - get back the original list?
7. An empty list.
8. A list with 1 element.

"""

# create test cases of the above examples

t1 = {
    "input": {
        "rotated_ls": [7, 1, 9, 2, 6, 5, 3, 0, 11, 23]
    }, 
    "output": 3}

t2 = {
    "input": {
        "rotated_ls": [3, 32, 8, 46, 1, 6, 0, 10]
    }, 
    "output": 5}

t3 = {
    "input": {
        "rotated_ls": [65, 1, 7, 43]
    }, 
    "output": 0}

t4 = {
    "input": {
        "rotated_ls": [34, 9, 1, 89, 23, 12, 3]
    }, 
    "output": 1}

t5 = {
    "input": {
        "rotated_ls": [1, 56, 23, 7, 8, 43]
    }, 
    "output": 5}

t6 = {
    "input": {
        "rotated_ls": [34, 9, 13, 4, 10, 0]
    }, 
    "output": 6}

t7 = {
    "input": {
        "rotated_ls": []
    }, 
    "output": 0}

t8 = {
    "input": {
        "rotated_ls": [4]
    }, 
    "output": 0}

tests = [t1, t2, t3, t4, t5, t6, t7, t8]


# COME UP WITH A CORRECT SOLUTION. STATE IT IN PLAIN ENGLISH.


# IMPLEMENT THE SOLUTION AND TEST IT USING EXAMPLE INPUTS. FIX BUGS.

# ANALYZE THE ALGORITHMS COMPLEXITY AND IDENTIFY INEFFICIENCIES.

# APPLY RIGHT TECHNIQUE TO OVERCOME INEFFICIENCY. REPEAT STEPS 3 - 6.