from random import randint
def generate_number():
    random_number = randint(0,10)
    return random_number

def main():
    the_number = generate_number()
    i = 1
    while True:
        print("Guess the number")
        number = input()

        try:
            number = int(number)
        except:
            print("Wrong number")
            continue

        if number == the_number:
            print("Congratulations...")
            print("It's corecct number is {} You've tried {} time".format(str(number), str(i)))
            break
        elif number > the_number:
            print("Go Lower")
        elif number < the_number:
            print("Go higher")

        print("========")
        i += 1


main()




