import random

"""
PROBLEM

Write a function to sort a list of notebooks in decreasing order of likes.
Your function must be efficient enough to sort millions of notebooks each week.

In short, write a program to sort a list of numbers.

"""

"""
STRATEGY

1. State problem and identify inputs and outputs
2. Gather example inputs and outputs
3. Compile correct solution in plain English
4. Implement solution and test it using examples
5. Analyze complexities and identify inefficiencies
6. Improve inefficiencies, then repeat 3-6

"""


# Step 1

"""
A function to sort a list of numbers in increasing order.

Parameters: a list of numbers

Return: a sorted list

"""


def sort(nums):
    pass


# Step 2

"""
Various scenarios:

1. A random list
2. A sorted list
3. A descending-sorted list
4. A list with repeats
5. An empty list
6. A list with 1 element
7. A list with 1 element repeated
8. A long list

"""

# A random list
test0 = {
    "input": {"nums": [4, 2, 6, 3, 4, 6, 2, 1]},
    "output": [1, 2, 2, 3, 4, 4, 6, 6],
}

# A random list
test1 = {
    "input": {"nums": [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]},
    "output": [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23],
}

# A sorted list
test2 = {
    "input": {"nums": [3, 5, 6, 8, 9, 10, 99]},
    "output": [3, 5, 6, 8, 9, 10, 99],
}

# A descending-sorted list
test3 = {
    "input": {"nums": [99, 10, 9, 8, 6, 5, 3]},
    "output": [3, 5, 6, 8, 9, 10, 99],
}

# A list with repeats
test4 = {
    "input": {"nums": [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]},
    "output": [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23],
}

# An empty list
test5 = {
    "input": {"nums": []},
    "output": [],
}

# A list with 1 element
test6 = {
    "input": {"nums": [23]},
    "output": [23],
}

# A list with 1 element repeated
test7 = {
    "input": {"nums": [23, 23, 23, 23, 23]},
    "output": [23, 23, 23, 23, 23],
}

# A long list
inlist = list(range(10000))
outlist = list(range(10000))
random.shuffle(inlist)

test8 = {
    "input": {"nums": inlist},
    "output": outlist,
}

tests = [test1, test2, test3, test4, test5, test6, test7, test8]


# Step 3

"""
BUBBLE SORT

1. Iterate over list of numbers starting from the left
2. Compare each number with the number that follows it
3. If number greater than following, swap the elements
4. Repeat 1-3 until sort complete, at most n-1 times

"""


# Step 4