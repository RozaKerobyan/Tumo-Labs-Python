def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        if char in char_index_map:
            # If the character is already in the map, update the start index
            start = max(start, char_index_map[char] + 1)

        # Update the index of the current character
        char_index_map[char] = end

        # Update the maximum length if needed
        max_length = max(max_length, end - start + 1)

    return max_length

# Test 
print(length_of_longest_substring("abcabcbb"))  
