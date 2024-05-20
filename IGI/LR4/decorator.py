# Function to handle user input for repeating execution
def repeat_execution(func):
    """
    Decorator function to repeat the execution of a function.
    
    Args:
    func (function): The function to be decorated.
    
    Returns:
    function: The decorated function.
    """
    def wrapper(*args, **kwargs):
        while True:
            result = func(*args, **kwargs)
            #print("\nResult:", result)
            choice = input("Do you want to compute again? (yes/no): ").lower()
            if choice != 'yes':
                break
    return wrapper

    