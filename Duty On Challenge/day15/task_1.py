# Ask user 
input_words = input("Enter words seperated by commas: ").split(',')

# Strip any extra whitespace from each string
input_words = [words.strip() for words in input_words]


# Sort the list of strings by their length
sorted_fruits = sorted(input_words, key=len)

# Result
print(sorted_fruits)

