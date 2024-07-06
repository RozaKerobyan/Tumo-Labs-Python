def is_product_of_two_distinct_numbers(num_list, target):
    # Check for each pair of distinct numbers if their product equals the target
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            if i != j and num_list[i] * num_list[j] == target:
                return "YES"
    return "NO"

# Inputs
n = int(input())
num_list = [int(input()) for _ in range(n)]
target = int(input())

# Determine if the target is a product of two distinct numbers from the set
result = is_product_of_two_distinct_numbers(num_list, target)

# Result
print(result)
