def mask_number(input_string):
    # Ensure input is a string to handle different input types
    input_string = str(input_string)
    
    # If the input is less than or equal to 4 digits, return it as is
    if len(input_string) <= 4:
        return input_string
    
    # Mask all characters except the last 4
    masked_part = '*' * (len(input_string) - 4)
    last_four_digits = input_string[-4:]
    
    return masked_part + last_four_digits

# Test
input1 = "1234 5678 1234 5678"
output1 = mask_number(input1.replace(" ", "")) 
print(output1) 
input2 = "52310259"
output2 = mask_number(input2)
print(output2) 