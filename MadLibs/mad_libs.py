print("Hi its's Mad Libs game")
print("================")

def template1():
  print()
  print(f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. The hospital is a/an {adjective[0]} place, there are a lot of {adjective[1]} {noun[0]} here. There are nurses here who have {color} {part_of_the_body[0]}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {number} {noun[1]}. Today I talked to a doctor and they were wearing a {noun[2]} on their {part_of_the_body[1]}. I heard that all doctors {verb} {noun[3]} every day for breakfast. The most {adjective[2]} thing about being in the hospital is the {silly_word } {noun[0]} !")
  print()
def template2():
  print()
  print(f"This weekend I am going camping with {proper_noun} {persons_name}. I packed my lantern, sleeping bag, and {noun[0]}. I am so {adjective_feeling} to {verb[0]} in a tent. I am {adjective_feeling} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb[1]}. I have heard that the {color} lake is great for {verbing}. Then we will {adverb_ly} hike through the forest for {number} {measure_of_time}. If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun[1]} around the campfire!!")
  print()
def template3():
  print()
  print(f"Dear {persons_name}, I am writing to you from a {adjective[0]} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective[1]} {magical_creature[0]} and {adjective[2]} {magical_creature[1]} here! In the {roominahouse} there is a pool full of {noun[0]}. I fall asleep each night on a {noun[1]} of {noun[2]} and dream of {adjective[3]} {noun[3]}. It feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verbing} on a {adjective[4]} {noun[4]}!!")
  print()
sure = input("You want to start game, please input YES or NO: ").upper()

while True:
    if (sure == "YES"):
        print("Okay, we let's go playing")
        print("================")
        choose = int(input("What's your template, please input 1, 2 or 3: "))
        if (choose == 1):
            while True:
                number = input("Input a number: ")

                if number.isdigit():
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please enter number")
                    print("!!!!!!!!!!!!!!!!")

            measure_of_time = input("enter a measure of time: ")
            mode_of_transportation = input("enter a mode of transportation: ")
            adjective = input("enter three adjectives: ").split()
            noun = input("enter four nouns: ").split()
            color = input("enter a color: ")
            part_of_the_body = input("enter two parts of a body: ").split()
            silly_word = input("enter a silly word: ")
            verb = input("enter a verb: ")
            template1()
        elif (choose == 2):
            proper_noun = input("Give a proper noun: ")
            persons_name = input("Give a name: ")
            noun = input("Give two nouns: ").split()
            adjective_feeling = input("Give an adjective Feeling: ")
            verb = input("Give two verbs: ").split()
            animal = input("Give a type of animal: ")
            color = input("Give an interesting color:")
            measure_of_time = input("enter a measure of time: ")
            silly_word = input("enter a silly word: ")
            while True:
                verbing = input("Input a verb + ing: ")
    
                if verbing.endswith("ing"):
                    break 
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please type correctly")
                    print("!!!!!!!!!!!!!!!!")

            while True:
                adverb_ly = input("Input a adverb + ly: ")

                if adverb_ly.endswith("ly"):
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please type correctly")
                    print("!!!!!!!!!!!!!!!!")

            while True:
                number = input("Input a number: ")

                if number.isdigit():
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please enter number")
                    print("!!!!!!!!!!!!!!!!")
            template2()

        elif (choose == 3):
            persons_name = input("Give a name: ")
            adjective = input("enter five adjectives: ").split()
            color = input("Give an interesting color:")
            animal = input("Give a type of animal: ")
            place = input("Enter a place: ")
            magical_creature = input("Enter two magical creatures: ").split()
            roominahouse = input("Enter a room in a house: ")
            noun = input("enter five nouns: ").split()
            measure_of_time = input("enter a measure of time: ")
            verbing = input("verb + ing: ")
            while True:
                number = input("Input a number: ")

                if number.isdigit():
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please enter number")
                    print("!!!!!!!!!!!!!!!!")
            template3()         
        else:
            print("You entered the wrong number to select a template...")
        break
    elif (sure == "NO"):
         print("You can't play")
         break
    else:
        print("please enter either 1, 2 or 3")
    done = input("do you want to do it again? y/n")
    if done == "y":
     continue
    elif done == "n":
     break



