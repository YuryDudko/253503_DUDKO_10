import math
from GeometricFigure import *
import matplotlib.pyplot as plt

class Triangle(GeometricFigure):
    """
    Class to represent a triangle.
    """

    def __init__(self, base, height, angle, color , writing):
        """
        Initialize the Triangle object.

        Args:
            base (float): The length of the base of the triangle.
            height (float): The height of the triangle.
            angle (float): The angle at the vertex of the triangle (in degrees).
            color (str): The color of the triangle.
        """
        self.base = base
        self.height = height
        self.angle = angle
        self.color = FigureColor(color)
        self.writing = writing

    def __eq__(self , base):
        return self.text.lower() == base.text.lower()

    def calculate_area(self):
        """
        Calculate the area of the triangle.

        Returns:
            float: The area of the triangle.
        """
        return 0.5 * self.base * self.height * math.sin(math.radians(self.angle))

    def get_description(self):
        """
        Get the description of the triangle.

        Returns:
            str: Description of the triangle.
        """
        return "Triangle: Base={}, Height={}, Angle={}, Color={}, Area={}".format(
            self.base, self.height, self.angle, self.color.color, self.calculate_area())

    def draw(self):
        """
        Draw the triangle.
        """
        x = [0, self.base, 0.5 * self.base, 0]
        y = [0, 0, self.height, 0]
        plt.fill(x, y, color=self.color.color)
        #plt.text(0.5 * self.base, 0.5 * self.height, self.get_description(), ha='center')
        plt.text(0.5 * self.base, 0.5 * self.height,self.writing , ha='center')

    def show(self):
        """
        Display the triangle.
        """
        plt.axis('equal')
        plt.axis('off')
        self.draw()
        plt.show()

    def save_to_file(self, filename):
        """
        Save the triangle to a file.

        Args:
            filename (str): Name of the file to save the triangle.
        """
        plt.figure()
        self.draw()
        plt.savefig(filename)

    
