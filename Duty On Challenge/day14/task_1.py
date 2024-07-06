def move_zeros(nums):
    non_zero = 0

    for i in nums:
        if i != 0:
            nums[non_zero] = i
            non_zero += 1
    
    for j in range(non_zero, len(nums)):
        nums[j] = 0

    return nums

# Test 
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))