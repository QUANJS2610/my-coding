"""
This is the main file for the project. This file will be used to run the project.
The main() function is the entry point for the project.
"""

# Importing the required libraries for the project
import sys

# Adding the code directory to the path so that the code can be imported
sys.path.append('./Code')

# Importing the required libraries for the project
from Code.Problem1 import n_sum, two_sum

def Problem1():
    # Example input
    list_nums = input("Enter a list of numbers separated by spaces: ").split()
    list_nums = [int(i) for i in list_nums] # Convert the input to a list of integers
    
    k = int(input("Enter a number k: ")) # Input for the number k

    n = int(input("Enter a number n: ")) # Input for the number n

    # Check if the list is empty
    if not list_nums:
        print("The list is empty")
        return
    
    # Check if the list has less than n elements
    if len(list_nums) < n:
        print(f"The list has less than {n} elements")
        return
    
    # Calling the two_sum function
    result1 = two_sum(list_nums, k)

    # Printing the result
    print(f"Does any two numbers in {list_nums} add up to {k}? {result1}")
    
    # Calling the two_sum_with_index function
    result2 = n_sum(list_nums, k, n)

    # Printing the result
    print(f"The dictionary of numbers that sum of them is equal to {k} and the index of them according to the respective groups of {n}: {result2}")

# Importing the required libraries for the project
def main():
    Problem1()

# The following is the standard boilerplate that calls the main() function. 
if __name__ == "__main__":
    main()