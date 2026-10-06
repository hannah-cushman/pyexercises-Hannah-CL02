"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of numbers
# 2. Process: Sort the list and calculate the average of the numbers
# 3. Out: The whole list, one item from the list, the sorted list, and the average
# 4. What my list is about, and what I computed from it: My list is a list of numbers. I calculated the average because it shows the overall value of the numbers in the list.


# Your code below
num1=2
num2=3
num3=4

list = [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7]

print(num1)
print(num2)
print(num3)

# list before sort
print("list before sorting:",list)

# sorting the list
list.sort()

# printing the sorted list
print("The sorted list is:", list)

# removing the last item from the list
list.pop()

# print the list after removing the last number
print("The list after removing the last:", list)

# calculate the average
average = sum(list) / len(list)
print("The average of the list is:", average)
