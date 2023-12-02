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
2. Brainstorm example inputs and outputs that cover all edge cases
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

2. Example inputs and outputs = test cases. 
'''

# Step 1:
def locate_cards(cards, num):
    pass

# Step 2:
cards = [13, 11, 10, 7, 4, 3, 1, 0]
num = 7
output = 3

result = locate_cards(cards, num)
if result == output:
    print(result)

# alternatively

test_cases = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'num': 7
    },
    'output': 3
}
