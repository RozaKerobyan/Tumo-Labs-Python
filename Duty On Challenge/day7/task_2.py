import re

def count_vowels_and_consonants(input_string):
    # Convert the string to lowercase
    input_string = input_string.lower()
    
    # Find all alphabetic characters in the string
    alphabetic_characters = re.findall(r'[a-z]', input_string)
    
    # Define vowels
    vowels = 'aeiou'
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in alphabetic_characters:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
            
    return vowel_count, consonant_count

def user_input():
    input_string = input("Enter a string: ")
    vowels, consonants = count_vowels_and_consonants(input_string)
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")

# Call the user_input function to start the program
user_input()
