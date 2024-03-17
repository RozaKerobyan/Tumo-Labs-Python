print("Hi its's Mad Libs game")
print("================")

template_1 = ("1: It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !")
template_2 = ("2: This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!")
template_3 =("3: Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!")

sure = input("You want to start game, please input YES or NO: ")

for sure_output in sure:
    if (sure == "YES"):
        print("Okay, we let's go playing")
        print("================")
        print("You need to choose anybody template")
        print(template_1)
        print("================================================================================")
        print(template_2)
        print("================================================================================")
        print(template_3)
        print("================================================================================")
        choose = int(input("What's your template, please input 1, 2 or 3: "))
        if (choose == 1):
            print("Your template is ===>>> " + template_1)

            print("================================")

            while True:
                number = input("Input a number: ")

                if number.isdigit():
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please enter number")
                    print("!!!!!!!!!!!!!!!!")

            measure_of_time = input ("Measure of time: ")
            mode_of_trasportation = input("Mode of Transportation: ")
            adjective = input("Input adjective: ")
            adjective2 = input("Input adjective: ")
            noun = input("Input noun: ")
            color = input("Input a color: ")
            part_of_the_body = input("Input Part of the Body: ")
            verb = input("Input a verb: ")

            while True:
                number2 = input("Input a number: ")

                if number2.isdigit():
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please enter number")
                    print("!!!!!!!!!!!!!!!!")

            noun2 = input("Input noun: ")
            noun3 = input("Input noun: ")
            part_of_the_body2 = input("Input Part of the Body: ")
            verb2 = input("Input a verb: ")
            noun4 = input("Input noun: ")
            adjective3 = input("Input adjective: ")
            silly_word = input("Input a silly word: ")
            noun5 = input("Input noun: ")

            print("================================")
            print("The story you entered...")
            print("================================")
            print("Input a number: " + number)
            print("Measure of time: " + measure_of_time)
            print("Mode of Trasportation : " + mode_of_trasportation)
            print("Input adjective: " + adjective)
            print("Input adjective: " + adjective2)
            print("Input noun: " + noun)
            print("Input a color: " + color)
            print("Input Part of the Body: " + part_of_the_body)
            print("Input a verb: " + verb)
            print("Input a number: " + number2)
            print("Input noun: " + noun2)
            print("Input noun: " + noun3)
            print("Input Part of the Body: " + part_of_the_body2)
            print("Input a verb: " + verb2)
            print("Input noun: " + noun4)
            print("Input adjective: " + adjective3)
            print("Input a silly word: " + silly_word)
            print("Input noun" + noun5)

            print("================================")
            print("Your template text is ready")
            print("================================")
            print("It was about " + number + " " + measure_of_time + "  ago when I arrived at the hospital in a " + mode_of_trasportation + ". The hospital is a/an " + adjective + " place, there are a lot of" + adjective2 + " " + noun + " here. There are nurses here who have " + color + " " + part_of_the_body + ". If someone wants to come into my room I told them that they have to "+ verb + " first. I’ve decorated my room with " + number2 + " " + noun2 + ". Today I talked to a doctor and they were wearing a "+ noun3 + " on their " + part_of_the_body2 + ". I heard that all doctors " + verb2 + " " + noun4 + " every day for breakfast. The most " + adjective3 + " thing about being in the hospital is the " + silly_word + " " + noun5 + " !")
        elif (choose == 2):
            print("Your template is ===>>> " + template_2) 

            print("================================")

            name = input("Input Person Name :")
            noun = input("Input noun: ")
            adjective_1 = input("Input adjective (feeling): ")
            verb = input("Input verb: ")
            adjective_2 = input("Input adjective (feeling): ")
            animal = input("Input an animal: ")
            verb2 = input("Input a verb: ")
            color = input("Input a color: ")

            while True:
                verb_ing = input("Input a verb + ing: ")
    
                if verb_ing.endswith("ing"):
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
            
    
            measure_of_time = ("Measure of time: ")
            color2 = input("Input a color: ")
            animal2 = input("Input an animal: ")

            while True:
                number2 = input("Input a number: ")

                if number2.isdigit():
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please enter number")
                    print("!!!!!!!!!!!!!!!!")


            silly_word = input("Input a silly word: ")
            noun2 = input("Input noun: ")
            print("================================")
            print("The story you entered...")
            print("================================")
            print("Input Person Name :" + name)
            print("Input noun: " + noun)
            print("Input adjective (feeling): " + adjective_1)
            print("Input verb: " + verb)
            print("Input adjective (feeling): " + adjective_2)
            print("Input an animal: " + animal)
            print("Input a verb: " + verb2)
            print("Input a color: " + color)
            print("Input a verb + ing: " + verb_ing)
            print("Input a adverb + ly: " + adverb_ly)
            print("Input a number: " + number)
            print("Measure of time: " + measure_of_time)
            print("Input a color: " + color2)
            print("Input an animal: " + animal2)
            print("Input a number: " + number2)
            print("INput a silly word: " + silly_word)
            print("Input noun: " + noun2)
            print("================================")
            print("Your template text is ready")
            print("================================")
            print("This weekend I am going camping with " + name + ". I packed my lantern, sleeping bag, and " + noun + ". I am so " + adjective_1 + " to " + verb + " in a tent. I am " + adjective_2 + " we might see a(n) " + animal + ", I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and  " + verb2 + ". I have heard that the " + color + " lake is great for " + verb_ing + ". Then we will " + adverb_ly + " hike through the forest for " + number +" "+ measure_of_time + ". If I see a " + color2 + " " + animal2 + " while hiking, I am going to bring it home as a pet! At night we will tell " + number2 + " " + silly_word + " stories and roast " + noun2 + " around the campfire!!")
        elif (choose == 3):
            print("Your template is ===>>> " + template_3)

            print("================================")
            
            name = input("Input Person Name :")
            adjective_1 = input("Input adjective: ")
            color = input("Input a color: ")
            animal = input("Input an animal: ")
            place = input("Input a place: ")
            adjective_2 = input("Input adjective: ")
            magical_creature = input("Input Magical Creature (Plural): ")
            adjective_3 = input("Input adjective: ")
            magical_creature2 = input("Input Magical Creature (Plural): ")
            room_in_a_house = input("Input Room in a House: ")
            noun = input("Input noun: ")
            noun2 = input("Input noun: ")
            noun_plural = input("Input noun (plural): ")
            adjective_4 = input("Input adjective: ")
            noun_plural2 = input("Input noun (plural): ")
            
            while True:
                number = input("Input a number: ")

                if number.isdigit():
                    break
                else:
                    print("!!!!!!!!!!!!!!!!")
                    print("You typed wrong, please enter number")
                    print("!!!!!!!!!!!!!!!!")

            measure_of_time = ("Measure of time: ")
            verb_ing = input("Input a verb + ing: ")
            adjective_5 = input("Input adjective: ")
            noun3 = input("Input noun: ")
            print("================================")
            print("The story you entered...")
            print("================================")
            print("Input Person Name :" + name)
            print("Input adjective: " + adjective_1)
            print("Input a color: " + color)
            print("Input an animal: " + animal)
            print("Input a place: " + place)
            print("Input adjective: " + adjective_2)
            print("Input Magical Creature (Plural): " + magical_creature)
            print("Input adjective: " + adjective_3)
            print("Magical Creature (Plural): " + magical_creature2)
            print("Input Room in a House: " + room_in_a_house)
            print("Input noun: " + noun)
            print("Input noun: " + noun2)
            print("Input noun (plural): " + noun_plural)
            print("Input adjective: " + adjective_4)
            print("Input noun (plural): " + noun_plural2)
            print("Input a number: " + number)
            print("Measure of time: " + measure_of_time)
            print("Input a verb + ing: " + verb_ing)
            print("Input adjective: " + adjective_5)
            print("Input noun: " + noun3)
            print("================================")
            print("Your template text is ready")
            print("================================")
            print("Dear " + name + ", I am writing to you from a " + adjective_1 + " castle in an enchanted forest. I found myself here one day after going for a ride on a " + color + " " + animal + " in " + place + ". There are " + adjective_2 + " " + magical_creature + " and " + adjective_3 + " " + magical_creature2 + " here! In the " + room_in_a_house + " there is a pool full of " + noun + ". I fall asleep each night on a " + noun2 + " of " + noun_plural + " and dream of " + adjective_4 + " " + noun_plural2 + ". It feels as though I have lived here for " + number + " " + measure_of_time + ". I hope one day you can visit, although the only way to get here now is " + verb_ing + " on a " + adjective_5 + " " + noun3 + "!!")
        else:
            print("You entered the wrong number to select a template...")
        break
    elif (sure == "NO"):
         print("You can't play")
         break
    else:
        print("Exit")


