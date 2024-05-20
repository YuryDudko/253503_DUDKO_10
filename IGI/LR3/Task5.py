# Task 5: Program to Find the minimum positive element and sum of elements between the first and last positive elements in the given list.
# Lab Assignment: #3
# Version: 1.0
# Developer: Dudko Yury
# Date: 28.03.2024

from generators import input_sequence,generate_random_numbers
from decorator import repeat_execution

# Function for user input of list elements
def input_list():
    """
    Function for user input of list elements.
    
    Returns:
    list: The list of input elements.
    """
    elements = []
    while True:
        try:
            element = float(input("Enter a real number (0 to end): "))
            if element == 0:
                break
            elements.append(element)
        except ValueError:
            print("Invalid input. Please enter a valid real number.")
    return elements

# Function to find the minimum positive element and sum of elements between the first and last positive elements
def process_list(elements):
    """
    Find the minimum positive element and sum of elements between the first and last positive elements in the given list.
    
    Args:
    elements (list): The list of elements.
    
    Returns:
    tuple: A tuple containing the minimum positive element and the sum of elements between the first and last positive elements.
    """
    min_positive = None
    sum_between_positive = 0
    first_positive_found = False
    for element in elements:
        if element > 0:
            if not first_positive_found:
                min_positive = element
                first_positive_found = True
            else:
                min_positive = min(min_positive, element)
                sum_between_positive += element
        elif first_positive_found:
            sum_between_positive += element
    return min_positive, sum_between_positive

# Function to print the list
def print_list(elements):
    """
    Print the list of elements.
    
    Args:
    elements (list): The list of elements.
    """
    print("List of elements:", elements)

# Function to perform task 5 with user input or random numbers
@repeat_execution
def task_5():
    """
    Function to perform Task 5 with user input or random numbers.
    """
    choice = input("Do you want to enter the list manually or use random numbers? (manual/random): ").lower()
    if choice == 'manual':
        elements = input_list()
    elif choice == 'random':
        count = int(input("Enter the count of elements: "))
        elements = list(generate_random_numbers(count))
    else:
        print("Invalid choice. Please enter 'manual' or 'random'.")
        return

    for elem in elements:
        print(elem)
    # print_list(elements)
    
    min_positive, sum_between_positive = process_list(elements)
    if min_positive is not None:
        print("\nMinimum positive element:", min_positive)
        print("Sum of elements between the first and last positive elements:", sum_between_positive)
    else:
        print("\nThere are no positive elements in the list.")

#task_5()
