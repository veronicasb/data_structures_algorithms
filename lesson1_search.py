from jovian.pythondsa import evaluate_test_cases

"""

DSA is crucial because it helps you:
1. To think about problems systematically
2. To envision different inputs, outputs , and edge cases
3. Communicate ideas clearly to colleagues and collaborate
4. Convert thoughts and ideas into code

"""

"""

STRATEGY

1. State problem, identify input and output formats
2. Brainstorm example inputs and outputs that cover all edge cases (extreme/rare examples)
3. Brainstorm a solution for the problem in plain english
4. Implement solution and text example inputs. Fix bugs
5. Analyze complexity, identify inefficiencies. 
6. Apply technique to overcome inefficiencies - this is where DSA becomes significant. 
Repeat 3-6

"""

"""
PROBLEM

Lucy has cards with numbers on them - they are arranged in decreasing order and turned around 
(we don't know the specific numbers). She challenges Jose to pick a given number from the cards in as
little moves as possible. Write a function to help Jose.

1. We can represent the sequence of cards as a sorted list. So, in other words, write a function to find the
position of a given number in a sorted list of numbers. We need to minimize the number of times we access the list.
Our inputs include a sequence of cards (a list), a card (some number to be determined), and our output is a position (
the index of the card to be determined).

Input and output allows us to create the signature of our function:


2. Example inputs and outputs => test cases. Possible cases to consider when testing: num occurs somewhere in the middle
of cards, num is the first element in cards, num is the last element in cards, cards contains only num as an element, cards does 
not contain num, cards is an empty list, cards contains repeating numbers, or num occurs more than once in cards.


3. Aim for correctness, then efficiency. Checking all possible answers to find the simplest or most obvious answer is called the
brute force solution. In this case, our brute force solution is flipping over every card until the number is found. 
- create a variable with a value of 0
- check if the number at index of variable in cards is our number
- if yes, the variable is the answer and can be returned
- if no, increment the variable by 1 and repeat the process until the end of the cards list
- if number is not found, return -1

Basically a loop described in words. Also an example of a linear search algorithm.
An algorithm is basically a list of statements that can be converted into code.


4. see below


5. complexity - a measure of the amount of time and/or space an algorithm requires; complexity typically 
refers to the worst-case complexity

time complexity (running time) for linear search is cN for some fixed constant c that depends on number of operations 
performed in each iteration and time taken to execute a statement. 

space complexity for linear search is some constant c'(independent of N) since we only need a single position variable that occupies constant
space in computer's RAM

Big O Notation - the way complexity is expressed (Big O Notation is the expression of complexity; they refer to the same thing)

time complexity of linear search = O(N); space complexity of linear search = O(1)


6. by each going over each card one at a time, we arent utilizing the fact that it's sorted. Our next best bet would be to start in the middle 
and take advantage of the fact that the cards are sorted. Depending on our number, we can then focus on the lower half or the upper half of 
the deck, then repeat the process. This is binary search.

7. (jump back to step 3) binary search solution (in plain english):
- find the element in the middle of the list
- if it matches our number, return the middle position as the answer
- if it is less than our number, binary search the first half of the list
- if it is greater than our number, binary search the second half of the list
- if no more elements remain, return -1
"""


###
# Step 1:
###
def locate_cards(cards, num):
    pass


###
# Step 2:
###
cards = [13, 11, 10, 7, 4, 3, 1, 0]
num = 7
output = 3

result = locate_cards(cards, num)
if result == output:
    print(result)

# alternatively - using dictionaries makes repetitive testing easier
# input key will contain 1 key for each argument to the function
test_case = {"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "num": 7}, "output": 3}

# to test
# remember that ** unpacks keyword arguments (kwargs)
locate_cards(**test_case["input"]) == test_case["output"]

#
# create test cases for every possibility listed in step 2 above
#
tests = []
# append the example we created above
tests.append(test_case)
# create a test case for if num occurs in the middle of cards
tests.append({"input": {"cards": [13, 11, 10, 7, 4, 3, 1, 0], "num": 1}, "output": 6})
# create a test case for if num is the first element in cards
tests.append({"input": {"cards": [4, 2, 1, -1], "num": 4}, "output": 0})
# create test case for if num is last element in cards
tests.append({"input": {"cards": [4, 7, 2, -6, 1], "num": 1}, "output": 4})
# create test case for if cards contains only num as element
tests.append({"input": {"cards": [8], "num": 8}, "output": 0})
# create test case for if cards does not contain num
# the problem statement doesnt specify what to do in this scenario --> make a reasonable assumption
tests.append({"input": {"cards": [4, 7, 1, 0, -9], "num": 5}, "output": -1})
# create test case for if cards is empty
tests.append({"input": {"cards": [], "num": 2}, "output": -1})
# create test case for if cards contains repeating numbers
tests.append(
    {"input": {"cards": [3, 3, 3, 8, 8, 1, 9, 3, 6, 6, 6], "num": 1}, "output": 5}
)
# create test case for if cards contains num more than once
# we assume our function will return the first instance of num
tests.append({"input": {"cards": [3, 8, 3, 9, 0], "num": 3}, "output": 0})

# view full list of test cases
# a good number of test cases to produce is 3-5
# with lots of practice, you should be able to complete step 1 & 2 in 2-3 minutes
print(tests)


###
# Step 3 - see above
###


###
# Step 4 - implement solution and test it using examples
###

# start with function signature produced in step 1

# linear search
def locate_card(cards, num):
    # create variable with value of 0
    position = 0

    # print details to confirm - this is called logging
    # print("cards:", cards)
    # print("num:", num)

    # set loop
    while position < len(cards):

        # print("position:", position)

        # check if element at position matches num
        if cards[position] == num:

            # if yes, return position
            return position
        
        # increment position
        position += 1

        # check for end of cards list (solution before implementing empty list check)
        # if position == len(cards):

    # number not found, return -1
    return -1


# test function using test cases produced in step 2

result = locate_card(tests[0]['input']['cards'], tests[0]['input']['num'])
print(result)
print(result == tests[0]['output'])

evaluate_test_cases(locate_card, tests)

# code with the assumption that your code will be wrong

cards6 = tests[6]['input']['cards']
query6 = tests[6]['input']['num']
locate_cards(cards6, query6)

# we see that the issue is that the cards list is empty
# print statements are a more effective way to debug


evaluate_test_cases(locate_card, tests)


# everytime you make changes to code, you want to test all cases again

"""
in real interviews, it's best to skip implementing and testing brute force solutions
because it's easy to determine its complexity in plain english. However, brute force solutions
are best for practice/study - in case youre not able to figure out the optimal solution, you can still
implement the brute force solution, which is acceptable

"""

###
# Step 5 - see above
###


###
# Step 6 - see above
###


###
# Step 7 (jump back to step 3) - implement solution from previous step
###


def test_location(cards, num, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    # if middle number card is equal to our number...
    if mid_number == num:
        # ... check if the number card before it is still within range and equal to our number...
        if mid - 1 >= 0 and cards[mid - 1] == num:
            # ... if it is, return left
            return "left"
        else:
            # ... if it isnt, return found
            return "found"
    # otherwise, if middle number card is less than the value of our number...
    elif mid_number < num:
        # ... return left
        return "left"
    # otherwise, return right
    else:
        return "right"


def locate_card(cards, num):
    low, high = 0, len(cards) - 1

    while low <= high:
        middle = (high + low) // 2
        mid_card = cards[middle]

        print("lo:", low, ", hi:", high, ", mid:", middle, ", mid_number:", mid_card)

        if mid_card == num:
            return middle
        elif mid_card < num:
            high = middle - 1
        elif mid_card > num:
            low = middle + 1

    return -1


# testing will show issues with cards lists that have repeating elements
# we can fix this by creating a helper function test_location()
# rule of thumb: functions must be 10 lines of code or less
evaluate_test_cases(locate_card, tests)


# generic algorithm for binary search
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
    return -1


# take generic algorithm and re-write our function
# a function inside of a function is called "function closure"
def locate_card(cards, num):
    def condition(mid):
        if cards[mid] == num:
            if mid > 0 and cards[mid - 1] == num:
                return "left"
            else:
                return "found"
        elif cards[mid] < num:
            return "left"
        else:
            return "right"

    return binary_search(0, len(cards) - 1, condition)
