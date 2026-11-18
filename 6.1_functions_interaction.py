"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: One number (num) that the function receives.
# 2. Process, function by function: is_positive checks whether the number is greater than zero. is_negative checks whether the number is less than zero. is_zero checks whether the number equals zero. detailed_message uses these functions to determine whether the number is positive, negative, or zero and returns a message explaining the result.
# 3. Out: A message stating whether the number is positive, negative, or zero.
# 4. The question my fourth function answers:
#Is the number positive, negative, or zero?
#Splitting the program into smaller functions makes it easier to test each condition separately and identify mistakes.


# Your code below
def is_positive(num):
    return num > 0

def is_negative(num):
    return num < 0

def is_zero(num):
    return num == 0

def is_even(num):
    return num % 2 == 0

def detailed_message(num):
    if is_zero(num):
        return "The number is zero."
    elif is_positive(num):
        return "The number is positive."
    elif is_negative(num):
        return "The number is negative."
    elif is_even(num):
        return "The number is even."
    else:
        return "The number is odd."

number = 5
print(detailed_message(5))

