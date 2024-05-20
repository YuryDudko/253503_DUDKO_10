import numpy as np
class MatrixOperations:
    @staticmethod
    def create_matrix(n, m):
        """
        Create a matrix of size (n, m) with random integer values.

        Args:
            n (int): Number of rows.
            m (int): Number of columns.

        Returns:
            numpy.ndarray: A matrix of size (n, m) with random integer values.
        """
        return np.random.randint(0, 100, size=(n, m))

    @staticmethod
    def count_min_elements(matrix):
        """
        Count the number of elements in the matrix that are equal to the minimum value and return their indices.

        Args:
            matrix (numpy.ndarray): Input matrix.

        Returns:
            tuple: A tuple containing the count of minimum elements and their indices.
        """
        min_value = np.min(matrix)
        min_indices = np.argwhere(matrix == min_value)
        return len(min_indices), min_indices

    @staticmethod
    def calculate_std_with_function(matrix):
        """
        Calculate the standard deviation of the matrix using numpy's std function.

        Args:
            matrix (numpy.ndarray): Input matrix.

        Returns:
            float: The standard deviation of the matrix.
        """
        std_function = np.std(matrix)
        return std_function

    @staticmethod
    def calculate_std_with_formula(matrix):
        """
        Calculate the standard deviation of the matrix using the formula.

        Args:
            matrix (numpy.ndarray): Input matrix.

        Returns:
            float: The standard deviation of the matrix.
        """
        mean = np.mean(matrix)
        squared_diff = np.mean((matrix - mean) ** 2)
        formula_std = np.sqrt(squared_diff)
        return formula_std