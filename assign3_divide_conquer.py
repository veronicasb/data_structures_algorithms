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
    "output": []
}

t3 = {
    "input": {
        "poly1": [],
        "poly2": []
    },
    "output": []
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
    "output": [16, 32, 48, 32, 16]
}

t8 = {
    "input": {
        "poly1": [2, 1, 5, 7, 2, 1, 5, 7],
        "poly2": [3, 4]
    },
    "output": [6, 11, 19, 41, 34, 11, 19, 41, 28]
}

tests = [t1, t2, t3, t4, t5, t6, t7, t8]


# STATE CORRECT SOLUTION IN PLAIN ENGLISH

"""
If we have 2 lists of length m and n, the highest degree of exponents we will end up with 
will equal (m + n - 2) and the length of our resulting list will equal (m + n - 1).

We can set result[k] = sum of all pair poly1[i] * poly2[j] where i+j = k.

1. Initialize list "result" of length (m + n - 1) with 0s
2. Using "i" as our iterator, iterate over each element in "poly1"
2a. For each element "i" in poly1, using "j" as our iterator, iterate over each element in "poly2"
2a.a. Add "i" and "j" to get "k" (the position of our sum of pairs in "result")
2a.b. Add the product of pairs "poly1[i]" and "poly2[j]" 
2a.c. Append the result to "result[k]"
3. Return "result"

"""


# IMPLEMENT SOLUTION AND TEST -> FIX BUGS

def mulitply_poly(poly1, poly2):
    if len(poly1) < 1 or len(poly2) < 1:
        return []
    
    result_length = len(poly1) + len(poly2) - 1
    result = [0] * result_length

    for i in range(len(poly1)):

        for j in range(len(poly2)):
            k = i + j
            sum_pairs = poly1[i] * poly2[j]
            result[k] += sum_pairs

    return result

for test in tests:
    print(mulitply_poly(test["input"]["poly1"], test["input"]["poly2"]) == test["output"])


# ANALYZE ALGORITHM COMPLEXITY AND IDENTIFY INEFFICIENCIES
    
"""
Complexity is O(N^2).

"""


# OVERCOME INEFFICIENCY. REPEAT 3 - 6

"""
We can apply the "Divide and Conquer" technique to produce the same results more efficiently. 

"""


# STATE NEW SOLUTION IN PLAIN ENGLISH

"""
DIVIDE

1. Divide poly1 into 2 subproblems (A0, A1)
2. Divide poly2 into 2 subproblems (B0, B1)

CONQUER

3. Calculate the products of the 4 subproblems (A0*B0, A0*B1, A1*B0, A1*B1) 
recursively

COMBINE

4. Add the products of the 4 subproblems (the complexity of this step is O(N) - why?)

5. Return the result

"""


# IMPLEMENT NEW SOLUTION AND TEST -> FIX BUGS

# Multiply two polynomials
def add(poly1, poly2):
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def increase_exponent(poly, n):
    return [0] * n + poly

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def multiply(p,q):
    n = len(p) + len(q) - 2
    m = n//2
    if len(p)==1: 
        res = []
        return res
    else:
        a,b = split(p, q)
        a0, a1, b0, b1 = a[0], a[1], b[0], b[1] 

        y=multiply(add(a0,a1),add(b0,b1))
        u=multiply(a0,b0)
        z=multiply(a1,b1)
        diff = add(y,[(-1 * x) for x in add(u,z)])
        add1 = add(u, increase_exponent(diff,m))
        add2 = increase_exponent(z,n)
        return add(add1, add2)
      

# Test
print(multiply(t1["input"]["poly1"], t1["input"]["poly2"]))

# ANALYZE COMPLEXITY

"""
The complexity of the "Divide and Conquer" algorithm using 4 subproblems is O(N^2), the same 
as our brute force solution.

However, if we implement the algorithm using 3 subproblems, this reduces our complexity to 
O(N^log3).

"""