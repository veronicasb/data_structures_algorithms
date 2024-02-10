import numpy as np

"""
PROBLEM

Given 2 strings, A and B, find the minimum number of steps required to convert 
A to B. The following 3 operations are permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

"""


# STATE PROBLEM AND DETERMINE INPUT/OUTPUT FORMATS

"""
A function that finds the minimum number of steps required to transform one string 
into another string.

Input:
1. string_a - a string to transform
2. string_b - a string to transform to

Output:
1. steps - an integer as the number of steps required to convert one string to another

"""

def conversion_steps(string_a, string_b):
    pass


# BRAINSTORM EXAMPLE INPUTS AND OUTPUTS 

"""
1. generic example
2. another generic example
3. 1 string thats longer than the other
4. 1 string thats shorter than the other
5. 1 empty string and 1 nonempty string
6. 1 string that is the reverse of another string
7. 2 strings that are the same
8. 2 strings that are completely different

"""

t1 = {
    "input": {
        "string_a": "intention",
        "string_b": "execution"
    }, 
    "output": 5
}

t2 = {
    "input": {
        "string_a": "wednesday",
        "string_b": "thursday"
    }, 
    "output": 5
}

t3 = {
    "input": {
        "string_a": "eventually",
        "string_b": "event"
    }, 
    "output": 5
}

t4 = {
    "input": {
        "string_a": "fact",
        "string_b": "factoid"
    }, 
    "output": 3
}

t5 = {
    "input": {
        "string_a": "molasses",
        "string_b": ""
    }, 
    "output": 8
}

t6 = {
    "input": {
        "string_a": "paper",
        "string_b": "repap"
    }, 
    "output": 4
}

t7 = {
    "input": {
        "string_a": "mouse",
        "string_b": "mouse"
    }, 
    "output": 0
}

t8 = {
    "input": {
        "string_a": "statistics",
        "string_b": "adjacently"
    }, 
    "output": 9
}

tests = [t1, t2, t3, t4, t5, t6, t7, t8]


# STATE CORRECT SOLUTION IN PLAIN ENGLISH

"""
BRUTE FORCE (RECURSIVE - EXPONENTIAL)

1. Create 2 iterator variables idx1 and idx2 starting at 0 that will scan thru each sequence.
Our recursive function will compute the LCS of seq1[idx1:] and seq2[idx2:]

2. If seq1[idx1] and seq2[idx2] are equal, then this character belongs to the LCS of 
seq1[idx1:] and seq2[idx2:].

3. If seq1[idx1] and seq2[idx2] are NOT equal, then the LCS of seq1[idx1:] and seq2[idx2:] is the 
longer one among the LCS of seq1[idx1+1:], seq2[idx2:] and the LCS of seq1[idx1:], seq2[idx2+1:] 

4. If either seq1[idx1:] or seq2[idx2:] is empty, then their LCS is 0/empty

Solution resembles a binary tree.

"""


# IMPLEMENT SOLUTION AND TEST -> FIX BUGS

def conversion_steps(string_a, string_b, i1=0, i2=0):
    if i1 == len(string_a):
        return len(string_b) - i2
    if i2 == len(string_b):
        return len(string_a) - i1
    if string_a[i1] == string_b[i2]:
        return conversion_steps(string_a, string_b, i1+1, i2+1)
    return 1 + min(conversion_steps(string_a, string_b, i1, i2+1), # Insert at beginning of str1
                   conversion_steps(string_a, string_b, i1+1, i2), # Remove from beginning of str1
                   conversion_steps(string_a, string_b, i1+1, i2+1)) # Swap first character of str1

# Test

for test in tests:
    print(conversion_steps(test["input"]["string_a"], test["input"]["string_b"]) == test["output"])


# ANALYZE ALGORITHM COMPLEXITY AND IDENTIFY INEFFICIENCIES 

"""
Complexity: O(2^n1+n2)

Referring back to lecture notes:

Remember that the number of leaf nodes N in a binary tree means that the height of 
the tree is O(logN), which gives us enough information to determine the size of the tree.

Time complexity = O(2^m+n)
m is the length of 1 sequence and n is the length of the other. 2^m+n will end up being the 
number of leaves in our tree. The total number of elements in our tree will end up being 
double that minus 1.

We end up making 2^m+n recursive calls in our solution.

One inefficiency that exists in our solution is that we end up recursing over repeating 
"elements" in our tree, so we resolve subproblems more than once, which isnt necessary.
We can improve this using "memoization".

"""

# APPLY RIGHT TECHNIQUE TO OVERCOME INEFFICIENCY. REPEAT PROCESS.

"""
Improved method: memoization

Referring to lecture notes:

One inefficiency that exists in our solution is that we end up recursing over repeating 
"elements" in our tree, so we resolve subproblems more than once, which isnt necessary.
We can improve this using "memoization".

"""

# STATE CORRECT SOLUTION STATED IN PLAIN ENGLISH

"""
MEMOIZATION

"""


# IMPLEMENT SOLUTION AND TEST -> FIX BUGS

def conversion_steps2(string_a, string_b):
    memo = {}
    def recurse(i1, i2):
        key = (i1, i2)
        if key in memo:
            return memo[key]
        elif i1 == len(string_a):
            memo[key] = len(string_b) - i2
        elif i2 == len(string_b):
            memo[key] = len(string_a) - i1
        elif string_a[i1] == string_b[i2]:
            memo[key] = recurse(i1+1, i2+1)
        else:
            memo[key] = 1 + min(recurse(i1, i2+1), 
                                recurse(i1+1, i2), 
                                recurse(i1+1, i2+1))
        return memo[key]
    return recurse(0, 0)

# Test

for test in tests:
    print(conversion_steps2(test["input"]["string_a"], test["input"]["string_b"]) == test["output"])


# ANALYZE ALGORITHM COMPLEXITY AND IDENTIFY INEFFICIENCIES 

"""
Complexity: O(n1​∗n2​)

Referring to lecture notes:

The complexity of any memoization case will be the number of keys in that dictionary. 
In this case, it would be m*n. So, we've managed to reduce the time complexity of our 
solution from O(2^m+n) to O(m*n). m and n are the lengths of our sequences.

"""


# APPLY RIGHT TECHNIQUE TO OVERCOME INEFFICIENCY. REPEAT PROCESS.

"""
Improved method: dynamic programming

Referring to lecture notes:

Disadvantages of memoization: requires recursive calls, which is an issue for large problems (recursion takes up memory and time)

Dynamic Programming: can resolve disadvantages of memoization thru iteration - instead of using a dictionary, we use a matrix; 
we can use for-loops instead of recursion

1. Create a matrix of (n1 + 1) * (n2 + 1) initialized with 0s. matrix[i][j] represents the LCS of seq1[:i] and seq2[:j].
n1 and n2 are the lengths of our sequences.
2. If seq1[i] and seq2[j] are equal, then matrix[i+1][j+1] = 1 + matrix[i][j]
3. If seq1[i] and seq2[j] are equal, then matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

"""


# STATE CORRECT SOLUTION STATED IN PLAIN ENGLISH

"""
DYNAMIC PROGRAMMING

"""


# IMPLEMENT SOLUTION AND TEST -> FIX BUGS



def conversion_steps3(string_a, string_b):
    # Get the lengths of the input strings
    m = len(string_a)
    n = len(string_b)
     
    # Initialize a list to store the current row
    curr = [0] * (n + 1)
     
    # Initialize the first row with values from 0 to n
    for j in range(n + 1):
        curr[j] = j
     
    # Initialize a variable to store the previous value
    previous = 0
     
    # Loop through the rows of the dynamic programming matrix
    for i in range(1, m + 1):
        # Store the current value at the beginning of the row
        previous = curr[0]
        curr[0] = i
         
        # Loop through the columns of the dynamic programming matrix
        for j in range(1, n + 1):
            # Store the current value in a temporary variable
            temp = curr[j]
             
            # Check if the characters at the current positions in str1 and str2 are the same
            if string_a[i - 1] == string_b[j - 1]:
                curr[j] = previous
            else:
                # Update the current cell with the minimum of the three adjacent cells
                curr[j] = 1 + min(previous, curr[j - 1], curr[j])
             
            # Update the previous variable with the temporary value
            previous = temp
     
    # The value in the last cell represents the minimum number of operations
    return curr[n]

# Test

for test in tests:
    print(conversion_steps3(test["input"]["string_a"], test["input"]["string_b"]) == test["output"])


# ANALYZE ALGORITHM COMPLEXITY AND IDENTIFY INEFFICIENCIES 

"""
Complexity: O(n1*n2), the same as memoization

"""