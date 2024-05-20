# Main file to test all tasks
# Developer: Yury Dudko
# Date: 28.03.2024

from Task1 import task_1
from Task2 import task_2
from Task3 import task_3
from Task4 import task_4
from Task5 import task_5
from decorator import repeat_execution


# Main function to execute tests
def main():
    """
    Main function to execute tests for all tasks.
    
    """
    while True:
        a = input("Menu:\n 1. Task1 \n 2. Task2 \n 3. Task3\n 4. Task4\n 5. Task5\n 0.Exit\n Enter an option:")
        match a:
            case "1":
                print("Task 1: Program to manage an address book and save contacts to files")
                task_1()
            case '2':
                print("\nTask 2: Program to analyze text and perform various operations")
                task_2()
            case '3':
                print("\nTask 3: Program to compute the value of the function using power series expansion")
                task_3()
            case '4':
                print("\nTask 4: Program to create and visualize a triangle")
                task_4()
            case '5':
                print("\nTask 5: Program to perform matrix operations and calculate standard deviation")
                task_5()
            case '0':
                break
            case _:
                print("There is no such an option") 

if __name__ == "__main__":
    main()
