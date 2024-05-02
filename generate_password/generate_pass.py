import random
import string

# Function to generate a password of given length
def generate_password(theLength):
    # Define character sets for letters and digits
    letters = string.ascii_letters
    digits = string.digits
    
    # Combine letters and digits to create the total character set
    totalChars = letters + digits
    
    # Initialize an empty string to store the final password
    finalResult = ""
    
    # Generate the password by randomly selecting characters from the total character set
    for i in range(theLength):
        finalResult += random.choice(totalChars)
    
    # Return the generated password
    return finalResult

# Main function to execute the password generation
def main():
    while True:
        # Prompt user to enter password length
        print("Enter password length")
        theLength = input()

        try:
            # Convert user input to an integer
            theLength = int(theLength)
        except:
            # Handle the case when input is not a valid integer
            print("Wrong password length")
            continue

        # Generate the password of specified length
        thePassword = generate_password(theLength)
        
        # Display the generated password
        print("The password is: " + thePassword)

# Call the main function to start the password generation process
main()
