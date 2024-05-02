# Prompt the user to enter two numbers
num1 = int(input())
num2 = int(input())

# Display the options for mathematical operations
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")

# Prompt the user to choose an operator
choose = input("Choose operator: ")

# Perform the chosen operation based on the user's input
if choose == "1":
    print(num1 + num2)  # Addition
elif choose == "2":
    print(num1 - num2)  # Subtraction
elif choose == "3":
    print(num1 * num2)  # Multiplication
elif choose == "4":
    print(num1 // num2)  # Integer division
