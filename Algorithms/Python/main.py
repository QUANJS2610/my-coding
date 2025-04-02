"""
This is the main file for the project. This file will be used to run the project.
The main() function is the entry point for the project.
"""

# Importing the required libraries for the project
import sys

# Adding the code directory to the path so that the code can be imported
sys.path.append('./Code')

import random  # Importing the random library for generating random numbers for the problem

# Importing the required libraries for the project
from Code.Problem1 import n_sum, n_sum2, two_sum, two_sum_with_index

def generate_random_list(size, min_value, max_value):
    random_set = set()

    while len(random_set) < size:
        random_set.add(random.randint(min_value, max_value))

    return list(random_set)

def Problem1():
    # Example input
    # list_nums = input("Enter a list of numbers separated by spaces: ").split()

    # Setting the seed for random number generation to 0 for reproducibility of the results
    random.seed(0)    

    # Input for the size of the list and the number of random numbers to generate
    size = int(input("Enter the size of the list: ")) 

    # Check if the input is valid
    if size <= 0:
        print("The size of the list must be greater than 0")
        return
    
    max_value = int(input("Enter the number of random numbers to generate: "))
    
    # Check if the input is valid
    if max_value <= 0:
        print("The number of random numbers to generate must be greater than 0")
        return
    
    # Check if the size is greater than the max value
    if size > max_value:    
        print("The size of the list must be less than the number of random numbers to generate")    
        return

    # list_nums = [random.randint(1, n) for _ in range(size)]
    # list_nums = random.sample(range(1, n+1), size)
    list_nums = generate_random_list(size, 1, max_value) # Generating a list of random numbers

    # Check if the list is empty
    if not list_nums:
        print("The list is empty")
        return
        
    print(f"Generated list of numbers: {list_nums}")

    list_nums = [int(i) for i in list_nums] # Convert the input to a list of integers
    
    k = int(input("Enter a number k: ")) # Input for the number k
    
    # Check if the input is valid
    if k <= 0:
        print("The number to sum must be greater than 0")
        return
    
    n = int(input("Enter a number n: ")) # Input for the number n

    # Check if the input is valid
    if n <= 0:
        print("The number of elements to sum must be greater than 0")
        return
    
    #Check if the number k is less than the number n
    if k < n:
        print("The number to sum must be greater than the number of elements to sum")
        return

    # Check if the list has less than n elements
    if len(list_nums) < n:
        print(f"The list has less than {n} elements")
        return
    
    # Calling the two_sum function
    result1 = two_sum(list_nums, k)

    # Printing the result
    print(f"Does any two numbers in {list_nums} add up to {k}? {result1}")

    
    # Calling the two_sum function
    result2 = two_sum_with_index(list_nums, k)

    # Printing the result
    print(f"The dictionary of numbers that sum of them is equal to {k} and the index of them according to the respective groups of 2: {result2}")
    
    # Calling the two_sum_with_index function
    result3 = n_sum(list_nums, k, n)

    # Printing the result
    print(f"The dictionary of numbers that sum of them is equal to {k} and the index of them according to the respective groups of {n}: {result3}")

    # Calling the two_sum_with_index function
    result4 = n_sum2(list_nums, k, n)

    # Printing the result
    print(f"The dictionary of numbers that sum of them is equal to {k} and the index of them according to the respective groups of {n}: {result4}")

# Importing the required libraries for the project
def main():
    Problem1()

# The following is the standard boilerplate that calls the main() function. 
if __name__ == "__main__":
    main()