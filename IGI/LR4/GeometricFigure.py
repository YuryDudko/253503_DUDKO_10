from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    """
    Abstract base class for geometric figures.
    """

    @abstractmethod
    def calculate_area(self):
        """
        Abstract method to calculate the area of the geometric figure.
        """
        pass

class FigureColor:
    """
    Class to represent the color of a geometric figure.
    """

    def __init__(self, color):
        """
        Initialize the FigureColor object.

        Args:
            color (str): The color of the figure.
        """
        self._color = color

    @property
    def color(self):
        """
        Get the color of the figure.

        Returns:
            str: The color of the figure.
        """
        return self._color