def create_new_string(input_string):
    # Get the first character
    first_char = input_string[0]
    
    # Get the middle character
    middle_index = len(input_string) // 2
    middle_char = input_string[middle_index]
    
    # Get the last character
    last_char = input_string[-1]
    
    # Create the new string with uppercase characters
    new_string = first_char.upper() + middle_char.upper() + last_char.upper()
    
    return new_string

# Test
input_str = "Euphoria"
output_str = create_new_string(input_str)
print(output_str)  
