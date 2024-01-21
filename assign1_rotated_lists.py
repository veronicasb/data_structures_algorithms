from jovian.pythondsa import evaluate_test_cases

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


# 1. STATE PROBLEM CLEARLY. IDENTIFY INPUT AND OUTPUT FORMATS.

"""
A function that takes a rotated list, then counts the minimum number of times it was rotated 
from its original sequence.

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


# 2. COME UP WITH EXAMPLE INPUTS AND OUTPUTS. TRY TO COVER EDGE CASES.

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
        "rotated_ls": [7, 8, 9, 0, 1, 2, 3, 4, 5, 6]
    }, 
    "output": 3}

t2 = {
    "input": {
        "rotated_ls": [3, 4, 5, 6, 7, 0, 1, 2]
    }, 
    "output": 5}

t3 = {
    "input": {
        "rotated_ls": [0, 1, 2, 3]
    }, 
    "output": 0}

t4 = {
    "input": {
        "rotated_ls": [5, 0, 1, 2, 3, 4]
    }, 
    "output": 1}

t5 = {
    "input": {
        "rotated_ls": [1, 2, 3, 4, 5, 6, 7, 0]
    }, 
    "output": 7}

t6 = {
    "input": {
        "rotated_ls": [0, 1, 2, 3, 4, 5]
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


# 3. COME UP WITH A CORRECT SOLUTION. STATE IT IN PLAIN ENGLISH.

"""
My guess:

1. Take the given rotated list and identify its last element
2. Iterate over original sorted list until the number of the last element in the 
given rotated list is found
3. Take the index of the element found in the original sorted list, then count 
the distance between the index and the end of the list.
4. Return count

This algorithm wouldn't work because we aren't actually given the original sorted list 
at any point. The only information we have is the rotated list and the fact that its
original sequence would be in ascending sorted order.


2nd guess:

1. Iterate over given rotated list
2. If we find an element that is lesser in value than the element that came before it, 
set it as our target
2a. Calculate the number of rotations using (lenth of rotated list) - (index of our target + 1)
2b. Return calculation
3. Otherwise, keep iterating over list until target is found or until end
4. Return 0 if no target is found


This algorithm works easily because our target becomes obvious as the element that is smaller than 
the element that comes before it. Then, we can count the number of jumps from our target 
to the end of the list using a simple calculation, which ends up being our answer. 


Correct solution: Linear Search

1. Iterate over given rotated list using while loop
2. If we find an element that is lesser in value than the element that came before it, 
return its index - this is the answer.
3. Otherwise, return 0 (target was never found)

"""


# 4. IMPLEMENT THE SOLUTION AND TEST IT USING EXAMPLE INPUTS. FIX BUGS.

def rotated_list(rotated_ls):
    i = 0
    while i < len(rotated_ls):
        if rotated_ls[i] < rotated_ls[i - 1]:
            return i
        i += 1
    return 0

for test in tests:
    print(rotated_list(test["input"]["rotated_ls"]))
    print(test["output"], "\n")

results = evaluate_test_cases(rotated_list, tests)


# 5. ANALYZE THE ALGORITHMS COMPLEXITY AND IDENTIFY INEFFICIENCIES.

"""
The algorithm we're using is Linear Search, so our worst-case scenario is that 
we end up iterating through an entire list before we find our answer. This equates 
to a complexity of O(N), where N is the length of the rotated list that we're given. 

Our best-case scenario would be that we find our answer at the first index. This 
would equate to a complexity of O(1). 

Worst --> Average --> Best: Linear Search
O(N) --> O(N) --> O(1)

"""


# 6. APPLY RIGHT TECHNIQUE TO OVERCOME INEFFICIENCY. REPEAT STEPS 3 - 6.

"""
We can drastically improve upon Linear Search using Binary Search. 

"""


# 7. REPEAT STEP 3 (COME UP WITH CORRECT SOLUTION STATED IN PLAIN ENGLISH)

"""
Correct solution: Binary Search

Algorithm in my words...
0. Set the highest and lowest index of our list
1. While lowest point is less than highest point, find the middle point of the given list
2. If the middle point is our answer, return it
2a. If answer isnt middle point, check the left half and return the answer
2b. If answer isnt in the left half, check the right half and return the answer
3. Return 0 if answer isnt found

"""


# 8. REPEAT STEP 4 (IMPLEMENT THE CORRECT SOLUTION)

def rotated_ls_binary(rotated_ls):
    low, high = 0, len(rotated_ls) - 1
    
    while low <= high:
        mid = (high + low) // 2
        mid_element = rotated_ls[mid]
        if mid_element < rotated_ls[mid - 1]:
            return mid
        elif mid_element > rotated_ls[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1

    return 0

binary_result = evaluate_test_cases(rotated_ls_binary, tests)


# 9. REPEAT STEP 5 (ANALYZE COMPLEXITY)

"""
The algorithm we're using is Binary Search, so our worst-case scenario is that our 
target is in the first position of our list. This equates to a complexity of 
O(log N), where N is the length of the rotated list that we're given. 

Our best-case scenario would be that we find our answer at the middle point. This 
would equate to a complexity of O(1). 

Worst --> Average --> Best: Binary Search
O(log N) --> O(log N) --> O(1)

"""


# BONUS 1 - IMPLEMENT ROTATED_LS_BINARY USING THE GENERIC BINARY SEARCH FUNCTION

# The generic version of Binary Search

def binary_search(low, high, condition):
    while low <= high:
        middle = (low + high) // 2
        result = condition(middle)
        if result == "found":
            return middle
        elif result == "left":
            high = middle - 1
        else:
            low = middle + 1
    return 0

# Rewrite function using generic version

def rotated_ls_binary_generic(rotated_ls):
    def condition(mid):
        if rotated_ls[mid] < rotated_ls[mid - 1]:
            return "found"
        elif rotated_ls[mid] > rotated_ls[mid - 1]:
            return "left"
        else:
            return "right"

    return binary_search(0, (len(rotated_ls) - 1), condition)

# Test

evaluate_test_cases(rotated_ls_binary_generic, tests)


# BONUS 2 - HANDLING REPEATING NUMBERS

# Add test cases that include repeating numbers

extended_test = list(tests)

repeating_t1 = {
    "input": {
        "rotated_ls": [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    },
    "output": 8
}

repeating_t2 = {
    "input": {
        "rotated_ls": [3, 4, 4, 0, 1, 2, 2]
    },
    "output": 3
}

extended_test.append([repeating_t1, repeating_t2])

# Modify generic Binary Search solution to handle repeating elements

def binary_search(low, high, condition):
    while low <= high:
        middle = (low + high) // 2
        result = condition(middle)
        if result == "found":
            return middle
        elif result == "left":
            high = middle - 1
        else:
            low = middle + 1
    return 0

def rotated_ls_binary_generic(rotated_ls):
    def condition(mid):
        if rotated_ls[mid] < rotated_ls[mid - 1]:
            return "found"
        elif rotated_ls[mid] > rotated_ls[mid - 1]:
            return "left"
        else:
            return "right"

    return binary_search(0, (len(rotated_ls) - 1), condition)

# Test

evaluate_test_cases(rotated_ls_binary_generic, tests)


# BONUS 3 - FIND POSITION OF TARGET NUMBER WITHIN ROTATED LIST

# Add test cases that include targets

# Generic test case 
search_test1 = {
    "input": {
        "rotated_ls": [5, 6, 9, 0, 2, 3, 4],
        "target": 2
    }, 
    "output": 5
}

# Generic test case
search_test2 = {
    "input": {
        "rotated_ls": [6, 7, 0, 1, 2, 3, 4, 5],
        "target": 4
    }, 
    "output": 7
}

# A list with repeating elements
search_test3 = {
    "input": {
        "rotated_ls": [6, 7, 7, 0, 1, 2, 3, 4, 5, 5],
        "target": 4
    }, 
    "output": 7
}

# A list with no elements 
search_test4 = {
    "input": {
        "rotated_ls": [],
        "target": 9
    }, 
    "output": -1
}

# A list where our target doesnt exist
search_test5 = {
    "input": {
        "rotated_ls": [23, 0, 4, 8, 10],
        "target": 2
    }, 
    "output": -1
}

search_test = [search_test1, search_test2, search_test3, search_test4, search_test5]

# Modify binary algorithm (not generic) to search for target 

# Test