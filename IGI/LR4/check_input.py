
# Function to validate float input
def validate_float_input(prompt):
    """
    Validate float input from the user.
    
    Args:
    prompt (str): The prompt message for input.
    
    Returns:
    float: The valid float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def validate_float_input_task3(prompt):
    """
    Validate float input from the user.
    
    Args:
    prompt (str): The prompt message for input.
    
    Returns:
    float: The valid float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if (value > -1 and value < 1):
                return value
            
            print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to validate float input
def validate_int_input(prompt):
    """
    Validate float input from the user.
    
    Args:
    prompt (str): The prompt message for input.
    
    Returns:
    float: The valid float value entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
