import math
import numpy as np
import matplotlib.pyplot as plt

class FunctionSeries:
    """
    Class to compute the value of the function using power series expansion.
    """

    def __init__(self, x, eps=1e-6, max_iter=500):
        """
        Initialize the FunctionSeries object.

        Args:
            x (float): The argument value.
            eps (float, optional): The desired precision. Default is 1e-6.
            max_iter (int, optional): Maximum number of iterations. Default is 500.
        """
        self.x = x
        self.eps = eps
        self.max_iter = max_iter

    def compute_function_value(self):
        """
        Compute the value of the function using power series expansion.

        Returns:
            float: Result of the series expansion.
            int: Number of iterations.
            float: Mathematical result.
        """
        result = 0
        n = 0
        while abs(self.x) < 1 and abs(self.x ** n) > self.eps and n < self.max_iter:
            result += self.x ** n
            n += 1
        math_result = 1 / (1 - self.x)
        return result, n, math_result

    def mean(self, sequence):
        """
        Calculate the mean of a sequence.

        Args:
            sequence (list): List of numbers.

        Returns:
            float: Mean value of the sequence.
        """
        return np.mean(sequence)

    def median(self, sequence):
        """
        Calculate the median of a sequence.

        Args:
            sequence (list): List of numbers.

        Returns:
            float: Median value of the sequence.
        """
        return np.median(sequence)

    def mode(self, sequence):
        """
        Calculate the mode of a sequence.

        Args:
            sequence (list): List of numbers.

        Returns:
            float: Mode value of the sequence.
        """
        return max(set(sequence), key=sequence.count)

    def variance(self, sequence):
        """
        Calculate the variance of a sequence.

        Args:
            sequence (list): List of numbers.

        Returns:
            float: Variance of the sequence.
        """
        return np.var(sequence)

    def standard_deviation(self, sequence):
        """
        Calculate the standard deviation of a sequence.

        Args:
            sequence (list): List of numbers.

        Returns:
            float: Standard deviation of the sequence.
        """
        return np.std(sequence)

    def plot_series_and_function(self):
        """
        Plot the series expansion and the mathematical function.
        """
        n_values = np.arange(self.max_iter)
        series_values = [self.x ** n for n in n_values]
        plt.plot(n_values, series_values, label='Series Expansion', color='blue')

        math_function_values = [1 / (1 - self.x)] * self.max_iter
        plt.plot(n_values, math_function_values, label='Math Function', color='red')

        plt.xlabel('n')
        plt.ylabel('Value')
        plt.legend()
        plt.title('Series Expansion vs Math Function')
        plt.grid(True)
        plt.show()

    def save_plot_to_file(self, filename):
        """
        Save the plot to a file.

        Args:
            filename (str): Name of the file to save the plot.
        """
        n_values = np.arange(self.max_iter)
        series_values = [self.x ** n for n in n_values]
        plt.plot(n_values, series_values, label='Series Expansion', color='blue')

        math_function_values = [1 / (1 - self.x)] * self.max_iter
        plt.plot(n_values, math_function_values, label='Math Function', color='red')

        plt.xlabel('n')
        plt.ylabel('Value')
        plt.legend()
        plt.title('Series Expansion vs Math Function')
        plt.grid(True)
        plt.savefig(filename)