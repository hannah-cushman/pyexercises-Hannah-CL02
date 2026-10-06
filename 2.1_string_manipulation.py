"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:a sentence entered by the user
# 2. Process:transform the sentence using four different string methods
# 3. Out: The sentence in uppercase, lowercase, with extra spaces removed, and with a word replaced
# 4. My four transformations, and when each is useful:
    # Uppercase: useful for making text stand out or creating headings.
    # Lowercase: useful for making text consistent when comparing words.
    # Strip: useful for removing unnecessary spaces at the beginning and end of text.
    # Replace: useful for changing a specific word or part of a sentence.

# Your code below
# getting a sentence from the user
sentence = input("Enter a sentence: ")

# making the sentence uppercase
print("Uppercase:", sentence.upper())

# making the sentence lowercase
print("Lowercase:", sentence.lower())

# removing spaces from the beginning and end
print("Stripped:", sentence.strip())

# replacing a word
print("Replaced:", sentence.replace("python", "coding"))