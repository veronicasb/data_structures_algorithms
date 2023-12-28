from jovian.pythondsa import evaluate_test_cases

"""
2 common problems in dynamic programming: 

1. longest common subsequence
2. knapsack

"""

# Longest Common Subsequence

"""
PROBLEM

Write a function to find the length of the longest common subsequence between
two sequences.

A sequence is a group of items with deterministic ordering. Strings, lists, tuples, etc.

A subsequence is a sequence obtained by deleting zero or more elements from 
another sequence.

"""

"""
METHOD

1. State problem clearly and indentify inputs and outputs
2. Brainstorm example inputs and outputs, especially ones that cover edge cases
3. Brainstorm a correct solution for the problem stated in plain English
4. Implement solution and test example inputs. Fix bugs.
5. Analyze complexity and indentify inefficiencies.
6. Improve inefficiencies, then repeat 3-6

"""


# Step 1

"""
A function that identifies the longest common subsequence between 2 sequences, 
then counts and returns the number of characters in that subsequence.

Parameters: 
1. seq1: a sequence (e.g. "serendipitous")
2. seq2: another sequence (e.g. "precipitation")

Return:
1. len_lcs: length of longest common subsequence (e.g. 7)

"""

# After step 1 is complete, we can create a signature for our function
def len_lcs(seq1, seq2):
    pass


# Step 2

"""
Example inputs: (4 to 5 or more)

1. 2 sequences with no common subsequence
2. 2 empty subsequences
3. 1 empty subsequence
4. 1 sequence that is a whole subsequence of the other
5. multiple lcs
6. general case (lists)
7. general case (strings)

"""

t0 = {
    "input": {
        "seq1": "serendipitous",
        "seq2": "precipitation"
    },
    "output": 7
}

t1 = {
    "input": {
        "seq1": [1, 3, 5, 7, 2, 5, 2, 3],
        "seq2": [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    "output": 5
}

t2 = {
    "input": {
        "seq1": "longest",
        "seq2": "stone"
    },
    "output": 3
}

t3 = {
    "input": {
        "seq1": "asdfwevad",
        "seq2": "opkpoiklklj"
    },
    "output": 0
}

t4 = {
    "input": {
        "seq1": "dense",
        "seq2": "condensed"
    },
    "output": 5
}

t5 = {
    "input": {
        "seq1": "",
        "seq2": "opkpoiklklj"
    },
    "output": 0
}

t6 = {
    "input": {
        "seq1": "",
        "seq2": ""
    },
    "output": 0
}

t7 = {
    "input": {
        "seq1": "abcdef",
        "seq2": "badcfe"
    },
    "output": 3
}

lcs_tests = [t0, t1, t2, t3, t4, t5, t6, t7]


# Step 3

"""
RECURSIVE SOLUTION

1. Create 2 iterator variables idx1 and idx2 starting at 0 that will scan thru each sequence.
Our recursive function will compute the LCS of seq1[idx1:] and seq2[idx2:]

2. If seq1[idx1] and seq2[idx2] are equal, then this character belongs to the LCS of 
seq1[idx1:] and seq2[idx2:].

3. If seq1[idx1] and seq2[idx2] are NOT equal, then the LCS of seq1[idx1:] and seq2[idx2:] is the 
longer one among the LCS of seq1[idx1+1:], seq2[idx2:] and the LCS of seq1[idx1:], seq2[idx2+1:] 

4. If either seq1[idx1:] or seq2[idx2:] is empty, then their LCS is 0/empty

Solution resembles a binary tree.

"""


# Step 4

def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    # The end-scenario/base-case should always be handled first
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)
    
result = lcs_recursive(lcs_tests[0]["input"]["seq1"], lcs_tests[0]["input"]["seq2"])
print(result, lcs_tests[0]["output"])

evaluate_test_cases(lcs_recursive, lcs_tests)


# Step 5