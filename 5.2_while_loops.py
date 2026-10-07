"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A yes or no answer entered by the user
# 2. Process: Keep asking the user for an answer until they answer yes or the maximum number of attempts is reached. Spaces at the beginning and end are removed and the answer is changed to lowercase.
# 3. Out: The number of attempts and a summary of what happened
# 4. My stop condition, my attempt limit, my summary: The loop stops when the user answers yes. I allow a maximum of 5 attempts. The summary shows how many attempts the user made and whether they answered yes.



# Your code below
attempts = 0
max_attempts = 5
answer = ""

while answer != "yes" and attempts < max_attempts:
    answer = input("Do you want to continue? ").strip().lower()
    attempts = attempts + 1

if answer == "yes":
    print("You answered yes after", attempts, "attempt(s).")
else:
    print("You reached the maximum number of attempts.")
    print("You made", attempts, "attempts.")