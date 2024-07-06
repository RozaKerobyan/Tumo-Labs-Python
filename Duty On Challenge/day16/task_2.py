import string
import random

def generate_password(length=6):
    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = '!@#$%^&*()_+=-'

    # Combine all character sets
    all_chars = uppercase_letters + lowercase_letters + digits + symbols

    # Generate password
    password = ''.join(random.sample(all_chars, length))
    
    return password

# Main function and result
def main():
    try:
        length = int(input("Enter the password length: "))
        password = generate_password(length)
    except ValueError:
        print("Invalid input. Length must be an integer.")
        return
    
    print("The password is:", password)

if __name__ == "__main__":
    main()
