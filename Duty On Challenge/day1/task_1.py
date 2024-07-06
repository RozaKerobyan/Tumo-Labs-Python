def move_zeros(nums):
    non_zero = 0

    for num in nums:
        # If the current element is non-zero
        if num != 0:
            nums[non_zero] = num
            non_zero += 1

    # Fill the remaining positions with zeros
    for i in range(non_zero, len(nums)):
        nums[i] = 0

    return nums

# Test the function
nums = [0,8,3,0,2,7,0]
result = move_zeros(nums)
print(result)
