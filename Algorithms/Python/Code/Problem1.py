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
Rewriting the function above with output as a dictionary of numbers that contains any two numbers from the list add up to k
    and the index of them according to the respective groups of 2.

For example, given [1, 2, 3, 4, 5, 6] and k of 9, return {1, 8: (0, 1), 2, 7: (1, 2), 3, 6: (2, 3), 4, 5: (3, 4) } since 1 + 8 = 9.
"""

def two_sum_with_index(list_nums, k):
    # Check if the list is empty
    if not list_nums:
        return {}
    
    # Check if the list has only one element
    if len(list_nums) == 1:
        return {}
    
    # Create a dictionary to store the numbers we have seen so far
    # and their indices
    # If the complement (k - num) exists in the dictionary, return the indices
    # Otherwise, add the current number to the dictionary
    # This will ensure that we only traverse the list once
    # and check for the complement in O(1) time
    # This will give us an O(n) time complexity for the problem
    # and O(n) space complexity for the dictionary
    # This is the one-pass solution

    # Initialize an empty dictionary to store the numbers we have seen so far
    num_dict = {}
    result = {}
    # Traverse the list of numbers
    for i, num in enumerate(list_nums):
        # Check if the complement (k - num) exists in the dictionary
        if k - num in num_dict:
            # If it does, add the pair of numbers and their indices to the result dictionary
            result[(num, k - num)] = (i, num_dict[k - num])
        
        # Add the current number and its index to the dictionary
        num_dict[num] = i
    return result

"""
Rewriting the function above with:
- A given list of numbers, a number k and a number n.
- Return the dictionary of numbers that contains any n numbers from the list add up to k 
    and the index of them according to the respective groups of n.

For example, given [1, 2, 3, 4, 5, 6] and k of 9 and n of 3, return {1, 2, 6: (0, 1, 5), 2, 3, 5: (1, 2, 4), 3, 4, 6: (2, 3, 5) } since 1 + 2 + 6 = 9.
"""

"""
This function takes a list of numbers, a target sum k, and a number n.
It returns a dictionary where the keys are tuples of n numbers from the list that sum to k,
and the values are tuples of their indices in the original list.
The function uses a backtracking approach to find all combinations of n numbers from the list.

The Big-O time complexity of this function is O(n^n) in the worst case,
where n is the length of the input list. This is because we are generating all possible combinations of n numbers from the list.
The space complexity is O(n) for the recursion stack and the result dictionary.
The function also sorts the input list, which takes O(n log n) time.
The function uses a backtracking approach to find all combinations of n numbers from the list.
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

"""
This function takes a list of numbers, a target sum k, and a number n.
It returns a dictionary where the keys are tuples of n numbers from the list that sum to k,
and the values are tuples of their indices in the original list.
The function uses a hash table to store the numbers and their indices in the list.
The function uses a backtracking approach to find all combinations of n numbers from the list.
The function also handles duplicates by using a tuple of sorted numbers as the key in the result dictionary.

The Big-O time complexity of this function is O(n^2) in the worst case,
where n is the length of the input list. This is because we are generating all possible combinations of n numbers from the list.
The space complexity is O(n) for the recursion stack and the result dictionary.
The function also sorts the input list, which takes O(n log n) time.

The function uses a backtracking approach to find all combinations of n numbers from the list.
The function also handles duplicates by using a tuple of sorted numbers as the key in the result dictionary.
The function uses a hash table to store the numbers and their indices in the list.
"""
def n_sum2(nums, target_sum, n):
    num_dict = {}
    result = {}
    
    def find_combinations(current_sum, current_combination, start_index):
        if len(current_combination) == n:
            if current_sum == target_sum:
                # key = tuple(sorted(current_combination))
                key = tuple(current_combination)
                result[key] = tuple([num_dict[num] for num in current_combination])
            return
        
        for i in range(start_index, len(nums)):
            num = nums[i]
            if num in num_dict:
                new_sum = current_sum + num
                if new_sum <= target_sum:
                    new_combination = current_combination + (num,)
                    find_combinations(new_sum, new_combination, i + 1)
    
    for i, num in enumerate(nums):
        num_dict[num] = i
    
    find_combinations(0, (), 0)
    
    return result
