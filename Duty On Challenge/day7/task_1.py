def print_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

def user_input():
    try:
        height = int(input("Enter number a between 1 and 10 for height: "))
        if height <= 0 or height > 10:
            print("Error: Please enter number between 1 and 10 ")
        elif height % 2 == 0:
            print("Error: Reminder height must be an odd number ")
        else:
            print_triangle(height)
    except ValueError:
        print("Error: Please enter a valid integer.")

# Call the function
user_input()
