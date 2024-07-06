def split_tuple(input_tuple):
    # Calculate the middle index
    middle_index = len(input_tuple) // 2

    # Get the first half and second half using slicing
    first_half = input_tuple[:middle_index]
    last_half = input_tuple[middle_index:]

    # Print the results
    print("First half values:", first_half)
    print("Last half values:", last_half)

# Test
input_tuple = (1, 3, 5, 7, 9)
split_tuple(input_tuple)

