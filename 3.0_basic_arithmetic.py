"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers entered by the user
# 2. Process:add, subtract, multiply, and divide the numbers
# 3. Out: the sum, difference, product, and quotient of the numbers
# 4. What happens when the second number is zero, and why: When the second number is zero, the program does not perform the division because division by zero is undefined. The if statement checks for zero first and prints a message instead.


# Your code below
# getting two inputs from the user
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

# add the two numbers 
sum = num1 + num2

# print the sum
print("The sum of two numbers is:", sum)

# finding the difference between two numbers
diff = num1 - num2
print("The difference between two numbers is:", diff)

# finding the product of two numbers
product = num1 * num2
print("The product of two numbers is:", product)

# finding the division of two numbers
if num2 == 0:
    print("You cannot divide by zero.")
else:
    division = num1 / num2
    print("The division of two numbers is:", division)