# Ask user
input_str = input("Enter a list of integers separated by spaces: ")

# Split the input string into individual numbers.
numbers_str = input_str.split()

# Convert each number from string to integer.
numbers = [int(num) for num in numbers_str]

# Find largest and smallest numbers.
largest = max(numbers)
smallest = min(numbers)

#Print largest and smallest numbers.
print("The largest number is:", largest)
print("The smallest number is:", smallest)
