def is_curzon(num):
    term1 = 2 ** num + 1
    term2 = 2 * num + 1
    return term1 % term2 == 0

# Test cases
print(is_curzon(5))
print(is_curzon(10)) 
print(is_curzon(14)) 
