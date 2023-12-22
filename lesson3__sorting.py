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

# results = evaluate_test_cases(bubble_sort, tests)


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
            j -= 1
        # place our current list element in front of previous element being compared
        nums.insert(j + 1, cur)
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


# Step 6

"""
"DIVIDE AND CONQUER" - MERGE SORT

1. Divide the inputs into two roughly equal parts
2. Recursively solve the problem individually for each of the two parts
3. Combine the results to solve the problem for the original inputs
4. Include terminating conditions for small or indivisible inputs

"""


# Step 7 (repeat step 3)

"""
State solution in plain english. Our new solution is Merge Sort.
Basically what we wrote above.
1. If list is empty or contains one element, return it
2. If not, divide the list into 2 equal parts
3. Sort each part recursively using Merge Sort
4. Merge/Combine the 2 parts 

"""


# Step 8 (repeat step 4)

def merge(nums1, nums2):
    # set variable to hold results
    result = []

    # set values for iteration
    i, j = 0, 0

    # iterate over each list
    while i < len(nums1) and j < len(nums2):
        # compare elements from each list
        if nums1[i] <= nums2[j]:
            # add the lesser value to the results first
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    # get remainder of each list
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # return final sorted and merged lists
    return result + nums1_tail + nums2_tail


def merge_sort(nums):
    # Our terminating condition
    # If list is empty or has 1 element, return it
    if len(nums) < 2:
        return nums

    # Divide list into 2 equal parts
    mid = len(nums) // 2
    # left_half = nums[:mid]
    # right_half = nums[mid:]

    # Sort each part recursively
    # left_sorted, right_sorted = merge_sort(nums[:mid]), merge_sort(nums[mid:])

    # Combine the 2 parts
    # sorted_nums = merge(left_sorted, right_sorted)

    return merge(merge_sort(nums[:mid]),
                  merge_sort(nums[mid:]))


# results = evaluate_test_cases(merge_sort, tests)


# Step 9 (repeat step 5)

"""
COMPLEXITY ANALYSIS OF MERGE SORT

Time complexity: O(nlogn)

Space complexity: O(n)

Merge Sort requires allocating space as large as the input itself. This makes it slow in 
practice since memory allocation is more expensive than comparison and swapping as in 
Bubble Sort.

So Bubble Sort is slowest, Insertion Sort is a bit faster, and Merge Sort is even 
faster, but inefficient with space.

***Try to void memory allocations as much as possible***

"""


# Step 10 (repeat step 6, jump back to step 3)

"""
To resolve the inefficiency above, we have...

QUICKSORT

1. If list is less than 2 elements, return it
2. Pick a random element from the list - this is called our "pivot"
3. Reorder the list so that all elements less than our "pivot" come before it and 
the elements greater than it come after. This process is called "partitioning".
4. The pivot element divides the list into 2 parts that can be sorted recursively and 
independently.

"""


# Step 11 (repeat step 4)

# Helper function - picks pivot, partitions list, and returns position of pivot
def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
        print("Pivot:", nums[end])

    # Left and right pointers
    l, r = start, end - 1
    print("Left Pointer Index:", l, ", Left Pointer Value:", nums[l])
    print("Right Pointer:", r, ", Right Pointer Value:", nums[r])

    # Iterate over list while left and right pointers do not overlap
    while r > l:
        # Increment left pointer if number is less or equal to pivot
        # Left pointer is travelling left to right on list
        if nums[l] <= nums[end]:
            print("Left Element:", nums[l], ", Pivot Element:", nums[end])
            l += 1
            print("New Left Pointer:", l)
        # Decrement right pointer if number is greater than pivot
        # Right pointer is traveling right to left on list
        elif nums[r] > nums[end]:
            print("Right Element:", nums[r], ", Pivot Element:", nums[end])
            r -= 1
            print("New Right Pointer:", r)
        # If 2 out-of-place elements are found, swap them
        else:
            print("Element out of place:", nums[l], "at left index", l)
            print("Element out of place:", nums[r], "at right index", r)
            nums[l], nums[r] = nums[r], nums[l]
    # Place pivot between the 2 parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end 

def quicksort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot - 1)
        quicksort(nums, pivot + 1, end)

    return nums

# results = evaluate_test_cases(quicksort, tests)

ls = [1, 5, 6, 2, 0, 11, 3]
partition_example = partition(ls)


# Step 12 (repeat step 5)

"""
COMPLEXITY ANALYSIS OF QUICKSORT

Time Complexity
Average-Case: O(nlogn) if youre able to partition list in roughly equal parts
Worst-Case: O(n^2) if your pivot ends up being the lowest possible element, at most, 
we'll end up making a recursive call to Quicksort n-1 times. This is as bad as Bubble Sort

Space Complexity: O(1)

Quicksort is still preferred because its running time is closer to O(nlogn) in practice 
as long as you use a good strategy for picking a pivot.

"""


# Return to the original problem...

"""
Write a function to sort a list of notebooks in decreasing order of likes.
Your function must be efficient enough to sort millions of notebooks each week.
"""

# Class to create notebook objects
class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return f"Notebook <\"{self.username}/{self.title}\", {self.likes} likes>"
    
nb0 = Notebook("pytorch-basics", "aakashns", 373)
nb1 = Notebook("linear-regression", "siddhant", 532)
nb2 = Notebook("logistics-regression", "vikas", 31)
nb3 = Notebook("feedforward-nn", "sonaksh", 94)
nb4 = Notebook("cifar10-cnn", "biraj", 2)
nb5 = Notebook("cifar10-resnet", "tanya", 29)
nb6 = Notebook("anime-gans", "hemanth", 80)
nb7 = Notebook("python-fundamentals", "vishal", 136)
nb8 = Notebook("python-functions", "aakashns", 74)
nb9 = Notebook("python-numpy", "siddhant", 92)

# A collection of notebooks
notesbooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]

print(notesbooks)

# Custom comparison function to compare 2 notebooks
def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return "lesser"
    elif nb1.likes < nb2.likes:
        return "greater"
    elif nb1.likes == nb2.likes:
        return "equal"
    
def default_compare(x, y):
    if x < y:
        return "lesser"
    elif x == y:
        return "equal"
    else:
        return "greater"

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == "lesser" or result == "equal":
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

# Implement merge sort using custom comparison function
def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare),
                 merge_sort(objs[mid:], compare),
                 compare)

sorted_notebooks = merge_sort(notesbooks, compare_likes)

for book in sorted_notebooks:
    print(book)


"""
EXERCISES:

1. Implement generic form of Bubble Sort
2. Implement generic form of Insertion Sort
3. Implement generic form of Quicksort

"""