from jovian.pythondsa import evaluate_test_cases

# Binary Search, Linked Lists, Complexity Analysis

'''

DSA is crucial because it helps you:
1. To think about problems systematically
2. To envision different inputs, outputs , and edge cases
3. Communicate ideas clearly to colleagues and collaborate
4. Convert thoughts and ideas into code

'''

'''

STRATEGY

1. State problem, identify input and output formats
2. Brainstorm example inputs and outputs that cover all edge cases (extreme/rare examples)
3. Brainstorm a solution for the problem in plain english
4. Implement solution and text example inputs. Fix bugs
5. Analyze complexity, identify inefficiencies. 
6. Apply technique to overcome inefficiencies - this is where DSA becomes significant. Repeat 3-6

'''

'''
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

'''


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
test_case = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'num': 7
    },
    'output': 3
}

# to test
# remember that ** unpacks keyword arguments (kwargs)
locate_cards(**test_case['input']) == test_case['output']

#
# create test cases for every possibility listed in step 2 above
#
tests = []
# append the example we created above
tests.append(test_case)
# create a test case for if num occurs in the middle of cards
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'num': 1
    },
    'output': 6
})
# create a test case for if num is the first element in cards
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'num': 4
    },
    'output': 0
})
# create test case for if num is last element in cards
tests.append({
    'input': {
        'cards': [4, 7, 2, -6, 1],
        'num': 1
    },
    'output': 4
})
# create test case for if cards contains only num as element
tests.append({
    'input': {
        'cards': [8],
        'num': 8
    },
    'output': 0
})
# create test case for if cards does not contain num
# the problem statement doesnt specify what to do in this scenario --> make a reasonable assumption
tests.append({
    'input': {
        'cards': [4, 7, 1, 0, -9],
        'num': 5
    },
    'output': -1
})
# create test case for if cards is empty
tests.append({
    'input': {
        'cards': [],
        'num': 2
    },
    'output': -1
})
# create test case for if cards contains repeating numbers
tests.append({
    'input': {
        'cards': [3, 3, 3, 8, 8, 1, 9, 3, 6, 6, 6],
        'num': 1
    },
    'output': 5
})
# create test case for if cards contains num more than once
# we assume our function will return the first instance of num
tests.append({
    'input': {
        'cards': [3, 8, 3, 9, 0],
        'num': 3
    },
    'output': 0
})

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
def locate_card(cards, num):
    # create variable with value of 0
    position = 0

    # set loop
    while True:

        # check if element at position matches num
        if cards[position] == num:

            # if yes, return position
            return position
        
        # increment position
        position += 1

        # check for end of cards list
        if position == len(cards):

            # number not found, return -1
            return -1
        
# test function using test cases produced in step 2
result = locate_card(tests[0]['input']['cards'], tests[0]['input']['num'])
print(result)
print(result == tests[0]['output'])

evaluate_test_cases(locate_card, tests)