# Task 4: Program to create and visualize a triangle
# Lab Assignment: #5
# Version: 1.0
# Developer: Yury Dudko
# Date: 20.04.2024

from Triangle import Triangle
from check_input import validate_float_input,validate_int_input
from decorator import *

@repeat_execution
def task_4():
    """
    Function to create and visualize a triangle.
    """
    base = validate_float_input("Enter the base of the triangle: ")
    height = validate_float_input("Enter the height of the triangle: ")
    angle = validate_float_input("Enter the angle at the vertex of the triangle (in degrees): ")
    color = input("Enter the color of the triangle: ")
    writing = input("Enter your text")

    triangle = Triangle(base, height, angle, color, writing)
    triangle.show()  # Display the triangle
    triangle.save_to_file("triangle.png")  # Save the triangle to a file
    print("Area of the triangle:", triangle.calculate_area())

