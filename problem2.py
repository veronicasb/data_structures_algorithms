"""
PROBLEM

Given 2 strings, A and B, find the minimumu number of steps required to convert 
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
        "string_a": "effortless",
        "string_b": "humorless"
    }, 
    "output": 4
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
    "output": 10
}

tests = [t1, t2, t3, t4, t5, t6, t7, t8]


# STATE CORRECT SOLUTION IN PLAIN ENGLISH


# IMPLEMENT SOLUTION AND TEST -> FIX BUGS


# ANALYZE ALGORITHM COMPLEXITY AND IDENTIFY INEFFICIENCIES 


# APPLY RIGHT TECHNIQUE TO OVERCOME INEFFICIENCY. REPEAT PROCESS.


# COME UP WITH CORRECT SOLUTION STATED IN PLAIN ENGLISH