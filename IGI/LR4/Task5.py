# Task 5: Program to perform matrix operations and calculate standard deviation
# Lab Assignment: #4
# Version: 1.0
# Developer: Yury Dudko
# Date: 20.04.2024

from MatrixOperations import *
from decorator import *
from check_input import validate_int_input

@repeat_execution
def task_5():
    x = validate_int_input("Enter the width of matrix: ")
    y = validate_int_input("Enter the height of matrix: ")


    # Create a matrix
    matrix = MatrixOperations.create_matrix(x, y)
    print("Created matrix:")
    print(matrix)

    # Count elements equal to the minimum value and their indices
    count, indices = MatrixOperations.count_min_elements(matrix)
    print(f"\nNumber of elements equal to the minimum value: {count}")
    print("Indices of these elements:")
    print(indices)

    # Calculate standard deviation
    std_function = MatrixOperations.calculate_std_with_function(matrix)
    formula_std = MatrixOperations.calculate_std_with_formula(matrix)
    print(f"\nStandard deviation (using numpy's std function): {std_function:.2f}")
    print(f"Standard deviation (using formula): {formula_std:.2f}")