from random import randint

# Function to generate a random number between 0 and 10
def generate_number():
    random_number = randint(0, 10)
    return random_number

# Main function to execute the guessing game
def main():
    # Generate the random number
    the_number = generate_number()
    
    # Initialize the number of attempts
    i = 1
    
    # Loop until the correct number is guessed
    while True:
        print("Guess the number")
        number = input()
        
        try:
            number = int(number)
        except:
            # Handle the case when input is not a valid number
            print("Wrong input. Please enter a valid number.")
            continue

        # Check if the guessed number is equal to the random number
        if number == the_number:
            print("Congratulations! You guessed the correct number in {} attempts.".format(i))
            break
        elif number > the_number:
            # If the guessed number is higher than the random number
            print("Go lower")
        elif number < the_number:
            # If the guessed number is lower than the random number
            print("Go higher")

        print("========")
        i += 1  # Increment the number of attempts

# Call the main function to start the game
main()