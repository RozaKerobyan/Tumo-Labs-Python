import random

templates = [
    '''It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}.
The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. 
There are nurses here who have {color} {part_of_body}. If someone wants to come into my room I told them that they have to {verb} first. 
I’ve decorated my room with {number2} {noun2}. 
Today I talked to a doctor and they were wearing a {noun3} on their {part_of_body2}. 
I heard that all doctors {verb2} {noun4} every day for breakfast. 
The most {adjective3} thing about being in the hospital is the {silly_word} {noun3}!''',

    '''This weekend I am going camping with {proper_noun}. I packed my lantern, sleeping bag, and {noun}. 
I am so {adjective_feeling} to {verb} in a tent. 
I am {adjective_feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. 
While we’re camping, we are going to hike, fish, and {verb2}. 
I have heard that the {color} lake is great for {verb_ing}. 
Then we will {adverb_ly} hike through the forest for {number} {measure_of_time}. 
If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! 
At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!''',

    '''Dear {proper_noun}, I am writing to you from a {adjective} castle in an enchanted forest. 
I found myself here one day after going for a ride on a {color} {animal} in {place}. 
There are {adjective2} {magical_creature_plural} and {adjective3} {magical_creature_plural2} here! 
In the {room_in_house}, there is a pool full of {noun}. 
I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}. 
It feels as though I have lived here for {number} {measure_of_time}. 
I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!'''
]

# Function to gather user inputs
def get_user_input(prompts):
    user_inputs = {}
    for prompt in prompts:
        user_inputs[prompt] = input(f"Enter {prompt.replace('_', ' ')}: ")
    return user_inputs

# Function to generate story
def generate_story(template, user_inputs):
    return template.format(**user_inputs)

# Main program
def main():
    # Ask user to choose a template
    print("Choose a template by entering a number (1, 2, or 3):")
    for i, template in enumerate(templates, 1):
        print(f"{i}: {template[:60]}...") # Show first part of each template for user reference

    choice = int(input()) - 1

    if choice not in [0, 1, 2]:
        print("Invalid choice. Exiting.")
        return

    # Determine the required inputs based on template chosen
    if choice == 0:
        prompts = ["number", "measure_of_time", "mode_of_transportation", "adjective", "adjective2", 
                   "noun", "color", "part_of_body", "verb", "number2", "noun2", "noun3", 
                   "part_of_body2", "verb2", "noun4", "adjective3", "silly_word", "noun3"]
    elif choice == 1:
        prompts = ["proper_noun", "noun", "adjective_feeling", "verb", "adjective_feeling2", 
                   "animal", "verb2", "color", "verb_ing", "adverb_ly", "number", 
                   "measure_of_time", "color2", "animal2", "number2", "silly_word", "noun2"]
    else:
        prompts = ["proper_noun", "adjective", "color", "animal", "place", "adjective2", 
                   "magical_creature_plural", "adjective3", "magical_creature_plural2", 
                   "room_in_house", "noun", "noun2", "noun_plural3", "adjective4", 
                   "noun_plural4", "number", "measure_of_time", "verb_ing", "adjective5", "noun5"]

    # Get user input
    user_inputs = get_user_input(prompts)

    # Generate and display story
    story = generate_story(templates[choice], user_inputs)
    print("\nHere is your story:\n")
    print(story)

# Run the program
if __name__ == "__main__":
    main()
