# Task 1: Program to compute the value of the function using power series expansion
# Lab Assignment: #3
# Version: 1.0
# Developer: Dudko Yury
# Date: 28.03.2024

import math
from input_check import *
from generators import input_sequence, generate_random_number
from decorator import repeat_execution

# Function to compute the value of 1/(1-x) using power series expansion
def compute_function_value(x, eps=1e-6, max_iter=500):
    """
    Compute the value of 1/(1-x) .
    
    Arguments:
    x (float): The argument value.
    eps (float, optional): The desired precision.
    max_iter (int, optional): Maximum number of iterations.
    
    Returns:
    x, result, n, math_result, and eps.
    """
    result = 0
    n = 0
    while abs(x) < 1 and abs(x ** n) > eps and n < max_iter:
        result += x ** n
        n += 1
    math_result = 1 / (1 - x)
    return x, result, n, math_result, eps

# Function to perform task 1 with user input or random number
@repeat_execution
def task_1():
    """
    Function to perform Task 1 with user input
    """
    #x = float(input("Enter the value of x (-1 < x < 1): "))
    x = validate_float_input("Enter the value of x (-1 < x < 1): ")

    result = compute_function_value(x)
    print("x:", result[0])
    print("result:", result[1])
    print("n:", result[2])
    print("math_result:", result[3])
    print("eps:", result[4])

#task_1()
