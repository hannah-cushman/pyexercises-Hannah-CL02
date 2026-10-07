"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of numbers
# 2. Process: Go through each item in the list and find its position and its square
# 3. Out: Each item, its position in the list, and its square
# 4. What I compute for each item, and why it is worth showing: I compute the square of each item because it shows a calculation performed on each number and allows me to see how the value changes when it is squared.


# Your code below
list = [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7]

for position, item in enumerate(list):
    print("The item is:", item, 
          "and its position in the list is:", position, 
          "and the square of the item is:", item**2)


# Check it yourself:
# The list contains 11 items, so the program should print exactly 11 lines.
# I checked the output and there are 11 lines, one for each item in the list.
# The first item is at position 0 and the last item is at position 10.