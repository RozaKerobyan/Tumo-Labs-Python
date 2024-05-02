import random

options = ("rock", "paper", "scissors")

# Loop for continuous gameplay
while True:
    player = None
    computer = random.choice(options)

    # Ask the player to enter their choice until it is valid
    while player not in options:
        player = input("Enter choice: (rock, paper, scissors)")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Determine the winner
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose")

    # Ask if the player wants to play again
    playing_again = input("Play again? (y/n)").lower()

    if playing_again == "y":
        continue
    elif playing_again == "n":
        break

print("Thanks for playing")
