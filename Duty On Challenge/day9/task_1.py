def cyclic_right(numbers):
    # Convert the input string to a list of integers
    num_list = [int(num) for num in numbers.split()]
    
    # Perform the cyclic shift
    if num_list:  
        last_element = num_list.pop()  
        num_list.insert(0, last_element)
    
    # Convert the list back to a string of space separated numbers
    shifted_numbers = ' '.join(map(str, num_list))
    
    return shifted_numbers

# Ask user
input_string = input("Enter a string of space separated natural numbers: ")

# Perform the cyclic shift
output_string = cyclic_right(input_string)

# Result
print(output_string)
