# Task 3: Program to compute the value of the function using power series expansion
# Lab Assignment: #4
# Version: 1.0
# Developer: Yury Dudko
# Date: 20.04.2024

from CalculateSeries import *
from check_input import validate_float_input
from decorator import *

@repeat_execution
def task_3():
    """
    Main function to execute Task 3.
    """
    x = validate_float_input_task3("Enter the value of x (-1 < x < 1): ")
    function_series = FunctionSeries(x)

    result, n, math_result = function_series.compute_function_value()
    print("Result of the series expansion:", result)
    print("Number of iterations:", n)
    print("Mathematical result:", math_result)

    # Compute additional parameters
    sequence = [x ** n for n in range(function_series.max_iter)]
    print("Mean:", function_series.mean(sequence))
    print("Median:", function_series.median(sequence))
    print("Mode:", function_series.mode(sequence))
    print("Variance:", function_series.variance(sequence))
    print("Standard Deviation:", function_series.standard_deviation(sequence))

    # Plot the series expansion and the mathematical function
    function_series.plot_series_and_function()

    # Save the plot to a file
    function_series.save_plot_to_file("function_series_plot.png")
