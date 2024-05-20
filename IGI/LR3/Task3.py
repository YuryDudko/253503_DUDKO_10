# Task 3: Program to analyze text input from the user
# Lab Assignment: #3
# Version: 1.0
# Developer: Yury Dudko
# Date: 28.03.2024

from generators import input_sequence, random_text
from decorator import repeat_execution

# Function to count characters in a text within the range 'g' to 'o'
def count_characters(text):
    """
    Count the number of characters in a text input within the range 'g' to 'o'.
    
    Args:
    text (str): The text string.
    
    Returns:
    int: The count of characters in the specified range.
    """
    count = sum(1 for char in text if 'g' <= char <= 'o')
    return count

# Function to perform task 3 with user input or random text
@repeat_execution
def task_3():
    """
    Function to perform Task 3 with user input or random text.
    """
    text = input("Enter the text: ")
    result = count_characters(text)
    print("Number of characters in the range 'g' to 'o':", result)

#task_3()
