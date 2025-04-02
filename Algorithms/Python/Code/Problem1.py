"""
Daily Coding Problem: Problem #1 [Easy]

This problem was recently asked by Google.

Given a list of numbers and a =
number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is =
17.

Bonus: Can you do this in one pass?
"""

def two_sum(list_nums, k):
    # Check if the list is empty
    if not list_nums:
        return False
    
    # Check if the list has only one element
    if len(list_nums) == 1:
        return False
    
    # Create a set to store the numbers we have seen so far
    # and check if the complement (k - num) exists in the set
    # If it does, return True
    # Otherwise, add the current number to the set
    # This will ensure that we only traverse the list once
    # and check for the complement in O(1) time
    # This will give us an O(n) time complexity for the problem
    # and O(n) space complexity for the set
    # This is the one-pass solution

    # Initialize an empty set to store the numbers we have seen so far
    list_added = set()
    
    # Traverse the list of numbers
    for num in list_nums:
        if k - num in list_added:
            return True
        
        list_added.add(num)

    return False

"""
Rewriting the function above with:
- A given list of numbers, a number k and a number n.
- Return the dictionary of numbers that contains any n numbers from the list add up to k and the index of them according to the respective groups of n.

For example, given [1, 2, 3, 4, 5, 6] and k of 9 and n of 3, return {1, 2, 6: (0, 1, 5), 2, 3, 5: (1, 2, 4), 3, 4, 6: (2, 3, 5) } since 1 + 2 + 6 = 9.
"""

def n_sum(nums, k, n):
    nums = [(num, i) for i, num in enumerate(nums)]
    nums.sort()
    result = {}
    
    def backtrack(start, path, target):
        
        if len(path) == n:
            if sum(num for num, _ in path) == target:
                key = tuple(sorted(num for num, _ in path))
                value = tuple(i for _, i in path)
                result[key] = value
            return
        
        if len(path) > n or start >= len(nums):
            return
        
        for i in range(start, len(nums)):
            if i > start and nums[i][0] == nums[i-1][0]:
                continue
            if sum(num for num, _ in path) + nums[i][0] > target:
                break
            backtrack(i + 1, path + [nums[i]], target)
    
    backtrack(0, [], k)
    return result