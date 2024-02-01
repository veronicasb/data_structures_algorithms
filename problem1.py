"""
PROBLEM

You are given an array of non-negative numbers. Find a continuous subarray of the list 
which adds up to a given sum.

"""


# STATE THE PROBLEM CLEARLY. IDENTIFY INPUT AND OUTPUT FORMATS.

"""
Function that finds a continuous subarray of the list which adds to a given sum.

Inputs:
1. array - a list of nonnegative numbers
2. sum - an integer as our given sum

Outputs:
1. result - a list as our continuous subarray that adds to the given sum

"""

def subarray(array, sum):
    pass

# BRAINSTORM EXAMPLE INPUTS AND OUTPUTS

"""
1. A given sum of 0
2. A given sum that is too high to reach (e.g. 100)
3. A generic input (e.g. [1, 7, 4, 2, 1, 3, 11, 5], 10)
4. A given sum that totals all elements in the given list
5. A given list with repeating elements
6. A given list with no elements
7. A given list that is long af
8. A given list with repeating elements and sum that is not reachable

"""

t1 = {
    "input": {
        "array": [1, 7, 4, 2, 1, 3, 11, 5],
        "sum": 0
    },
    "output": -1
}

t2 = {
    "input": {
        "array": [1, 7, 4, 2, 1, 3, 11, 5],
        "sum": 100
    },
    "output": -1
}

t3 = {
    "input": {
        "array": [1, 7, 4, 2, 1, 3, 11, 5],
        "sum": 10
    },
    "output": [4, 2, 1, 3]
}

t4 = {
    "input": {
        "array": [1, 7, 4, 2, 1, 3, 11, 5],
        "sum": 34
    },
    "output": [1, 7, 4, 2, 1, 3, 11, 5]
}

t5 = {
    "input": {
        "array": [4, 4, 4, 4, 4, 4],
        "sum": 8
    },
    "output": [4, 4]
}

t6 = {
    "input": {
        "array": [],
        "sum": 10
    },
    "output": -1
}

t7 = {
    "input": {
        "array": [1, 7, 4, 2, 1, 3, 11, 5, 1, 7, 4, 2, 1, 3, 11, 5],
        "sum": 10
    },
    "output": [4, 2, 1, 3]
}

t8 = {
    "input": {
        "array": [4, 4, 4, 4, 4, 4],
        "sum": 7
    },
    "output": -1
}

tests = [t1, t2, t3, t4, t5, t6, t7, t8]


# STATE CORRECT SOLUTION IN PLAIN ENGLISH


# IMPLEMENT SOLUTION AND TEST -> FIX BUGS


# ANALYZE ALGORITHM COMPLEXITY AND IDENTIFY INEFFICIENCIES


# OVERCOME INEFFICIENCY. REPEAT 3 - 6