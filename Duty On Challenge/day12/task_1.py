import random

def generate_bingo_card():
    # Initialize an empty 2D list for the Bingo card
    bingo_card = [['' for _ in range(5)] for _ in range(5)]
    
    # Generate a list of unique random numbers between 1 and 90
    numbers = random.sample(range(1, 91), 24)
    
    # Sort the numbers
    numbers.sort()
    
    # Insert numbers into the Bingo card
    index = 0
    for i in range(5):
        for j in range(5):
            if i == 2 and j == 2:
                # Center square
                bingo_card[i][j] = 'BINGO!'
            else:
                bingo_card[i][j] = numbers[index]
                index += 1
    
    return bingo_card

def display_bingo_card(bingo_card):
    for row in bingo_card:
        print(' | '.join(str(x).ljust(6) for x in row))
        print('-' * 37)

# Generate and display the Bingo card
bingo_card = generate_bingo_card()
display_bingo_card(bingo_card)
