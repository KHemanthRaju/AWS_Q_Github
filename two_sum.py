def two_sum(nums, target):
    """
    Returns the indices of the two numbers in `nums` that add up to `target`.
    
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    
    Returns:
        List[int]: Indices of the two numbers.
    """
    num_map = {}  # To store number and its index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # If no solution is found (shouldn't happen as per problem statement)

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("Indices of numbers that add up to target:", result)
