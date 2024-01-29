"""
PROBLEM

Given 2 polynomials represented by 2 lists, write a function that efficiently multiplies 
the polynomials. Represent the solution as a list as well.

"""


# STATE THE PROBLEM CLEARLY. IDENTIFY INPUT AND OUTPUT FORMATS.

"""
Function that efficiently multiplies 2 polynomials and represents the solution as a list.

Input:

1. poly1 = a list of integers representing a polynomial (e.g. [2, 0, 5, 7] represents 
2 + 5x^2 + 7x^3)

2. poly2 = a list of integers representing a polynomial (e.g. [3, 4, 2] represents 
3 + 4x + 2x^2)

Output:
1. answer = a list of integers representing a polynomial (e.g. [6, 8, 19, 41, 38, 14] 
represents 6 + 8x + 19x^2 + 41x^3 + 38x^4 + 14x^5)

"""

def mulitply_poly(poly1, poly2):
    pass


# BRAINSTORM EXAMPLE INPUTS AND OUTPUTS

"""
1. a generic case
2. 1 empty list
3. 2 empty lists
4. 1 list with 1 element
5. 2 lists with 1 element each
6. 1 list of repeating elements
7. 2 lists of repeating elements
8. 1 long list and 1 short list

"""

t1 = {
    "input": {
        "poly1": [2, 0, 5, 7],
        "poly2": [3, 4, 2]
    },
    "output": [6, 8, 19, 41, 38, 14]
}

t2 = {
    "input": {
        "poly1": [2, 0, 5, 7],
        "poly2": []
    },
    "output": [2, 0, 5, 7]
}

t3 = {
    "input": {
        "poly1": [],
        "poly2": []
    },
    "output": -1
}

t4 = {
    "input": {
        "poly1": [2, 1, 5, 7],
        "poly2": [2]
    },
    "output": [4, 2, 10, 14]
}

t5 = {
    "input": {
        "poly1": [8],
        "poly2": [2]
    },
    "output": [16]
}

t6 = {
    "input": {
        "poly1": [2, 2, 2, 2],
        "poly2": [3, 4, 2]
    },
    "output": [6, 14, 18, 18, 12, 4]
}

t7 = {
    "input": {
        "poly1": [4, 4, 4],
        "poly2": [4, 4, 4]
    },
    "output": [16, 0, 16, 0, 16]
}

t8 = {
    "input": {
        "poly1": [2, 1, 5, 7, 2, 1, 5, 7],
        "poly2": [3, 4]
    },
    "output": [6, 11, 19, 41, 34, 11, 19, 41, 28]
}

tests = [t1, t2, t3, t4, t5, t6, t7, t8]


# BRAINSTORM CORRECT SOLUTION IN PLAIN ENGLISH

# IMPLEMENT SOLUTIONS AND TEST. FIX BUGS

# ANALYZE ALGORITHM COMPLEXITY AND IDENTIFY INEFFICIENCIES

# OVERCOME INEFFICIENCY. REPEAT 3 - 6