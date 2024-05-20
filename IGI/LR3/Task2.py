# Task 2: Program to find the sum of a sequence of numbers
# Lab Assignment: #3
# Version: 1.0
# Developer: Yury Dudko
# Date: 28.03.2024

from generators import input_sequence, generate_random_numbers
from decorator import repeat_execution

# Function to find the sum of a sequence of numbers
def find_sequence_sum(numbers):
    """
    Find the sum of a sequence of numbers.
    
    Args:
    numbers (iterable): The sequence of numbers.
    
    Returns:
    float: The sum of the sequence.
    """
    return sum(numbers)

# Function to perform task 2
@repeat_execution
def task_2():
    """
    Function to perform Task 2.
    """
    

    choice = input("Do you want to enter the numbers manually or use random numbers? (manual/random): ").lower()
    if choice == 'manual':
        numbers = input_sequence()
    elif choice == 'random':
        count = int(input("Enter the count of numbers: "))
        numbers = generate_random_numbers(count)
    else:
        print("Invalid choice. Please enter 'manual' or 'random'.")
        return

    result = find_sequence_sum(numbers)
    print("Sum of the sequence:", result)

#task_2()
