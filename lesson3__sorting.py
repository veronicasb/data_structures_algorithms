import random
from jovian.pythondsa import evaluate_test_cases

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

"""
INSERTION SORT

1. Iterate over a list of numbers 
2. Compare each number to numbers previous to it
3. If a previous number is greater than our current, insert 
current element in its position
4. Repeat 1-3 until sort complete
"""


# Step 4


def bubble_sort(nums):
    # avoid modifying nums in place so as not to effect our testing
    # ask interviewers to clarify whether they want list sorted in-place or not
    nums = list(nums)

    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


nums0, output0 = test0["input"]["nums"], test0["output"]

print("Input:", nums0)
print("Expected Output:", output0)
result0 = bubble_sort(nums0)
print("Actual Output:", result0)
print("Match:", result0 == output0)

results = evaluate_test_cases(bubble_sort, tests)

def insertion_sort(nums):
    # create copy of list
    nums = list(nums)
    # iterate over list
    for i in range(len(nums)):
        # pull current list element out and put it aside
        cur = nums.pop(i)
        # set a new index variable that is 1 less than our current index
        j = i - 1
        # ensure that our new index variable is still within list index range
        # also ensure that the element that came before our current element is larger
        while j >= 0 and nums[j] > cur:
            # if so, decrement our new index variable by 1 (compare the second previous element)
            # we basically look thru previous elements until we find one that is less than our current element
            j -=1
        # place our current list element in front of previous element being compared
        nums.insert(j+1, cur)
    # return sorted list
    return nums

# Step 5

"""
COMPLEXITY ANALYSIS OF BUBBLE SORT

The core operations of Bubble Sort are "compare" and "swap". 

(n - 1) * (n - 1) = n^2 - 2n + 1

So, the time complexity of Bubble Sort is O(n^2), AKA "quadratic complexity".

The space complexity of Bubble Sort is O(n) because the space required to store inputs 
must be considered.

If we were sorting a massive list, we'd come to find that bubble sort is very inefficient.
This is because we're shifting elements one position at a time.

"""

"""
COMPLEXITY ANALYSIS OF INSERTION SORT

Time complexity: O(n^2)

Space complexity of: O(1)

Insertion Sort is faster than Bubble Sort in practice, despite having the same 
time complexity, because it is more adaptive.

"""