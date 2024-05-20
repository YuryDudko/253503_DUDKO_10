import random
import string

def generate_random_number():
    """
    Generate a random number for Task 1.
    
    Returns:
    float: A random number within the range (-1, 1).
    """
    return random.uniform(-1, 1)

# Generator function to initialize a sequence from user input
def input_sequence():
    """
    Generator function to initialize a sequence from user input.
    
    Yields:
    float: Each element of the sequence entered by the user.
    """
    while True:
        try:
            value = float(input("Enter a value (0 to end): "))
            if value == 0:
                break
            yield value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Generator function for initializing a sequence using a range
def range_sequence(start, stop, step=1):
    """
    Generator function to initialize a sequence using a range.
    
    Args:
    start (float): The start value of the sequence.
    stop (float): The end value of the sequence.
    step (float, optional): The step size between each element. Defaults to 1.
    
    Yields:
    float: Each element of the sequence generated using the range.
    """
    value = start
    while value < stop:
        yield value

# Generator function for random text generation
def random_text(length):
    """
    Generator function to generate random text.
    
    Args:
    length (int): The length of the random text.
    
    Yields:
    str: Each character of the random text.
    """
    for _ in range(length):
        yield random.choice(string.ascii_letters)

# Generator function to generate random numbers
def generate_random_numbers(count):
    """
    Generate random numbers.
    
    Args:
    count (int): The number of random numbers to generate.
    
    Yields:
    float: Each random number generated.
    """
    for _ in range(count):
        yield random.randint(-100, 100)

def generate_random_numbers(count):
    """
    Generate random numbers.
    
    Argumentss:
    count (float): The number of random numbers to generate.
    
    Yields:
    float: Each random number generated.
    """
    for _ in range(count):
        yield random.uniform(-100.0, 100.0)

# Generator function to generate a random string
def generate_random_string(length):
    """
    Generate a random string.
    
    Argumentss:
    length (int): The length of the random string.
    
    Yields:
    str: Each character of the random string.
    """
    for _ in range(length):
        yield random.choice(string.ascii_letters)
