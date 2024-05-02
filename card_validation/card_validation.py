# Print the title of the card validation check program
print("================================")
print("Card validation check program")
print("================================")

# Initialize variables for summing odd and even digits, and total
sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Prompt the user to enter the card number
numbers = input("Enter card numbers: ")

# Check the length of the input
if len(numbers) > 16:
    print("It's wrong, because you typed more numbers than expected...")
elif len(numbers) < 16:
    print("It's wrong, because you typed fewer numbers than expected...")
elif len(numbers) == 16:
    # Reverse the input string to start from the rightmost digit
    numbers = numbers[::-1]
    
    # Iterate through the reversed string to sum odd and even digits
    for i in numbers[::2]:  # Odd digits
        sum_odd_digits += int(i)

    for i in numbers[1::2]:  # Even digits
        i = int(i) * 2
        if i >= 10:
            sum_even_digits += (1 + (i % 10))
        else:
            sum_even_digits += i
    
    # Calculate the total sum
    total = sum_odd_digits + sum_even_digits

    # Check if the total is divisible by 10 to determine card validity
    if total % 10 == 0:
        print("IT'S VALID")
    else:
        print("IT'S INVALID")
