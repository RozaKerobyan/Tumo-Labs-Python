def max_subarray_sum(nums):
    if not nums:
        return 0

    current_sum = max_sum = nums[0]
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update current_sum to the maximum of the current element or the sum of current_sum and the current element
        current_sum = max(num, current_sum + num)
        # Update max_sum to the maximum of max_sum and current_sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  
