def remove_duplicates(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Test
input_list = [57, 94, 4, 4, 4, 41, 65, 94, 4, 99, 9, 9, 94]
output_list = remove_duplicates(input_list)
print(output_list)