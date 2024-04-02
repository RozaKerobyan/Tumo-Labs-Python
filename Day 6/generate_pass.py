import random
import string

def generate_password(theLength):
    letters = string.ascii_letters
    digits = string.digits
    totalChars = letters + digits
    finalResult = ""
    for i in range(theLength):
        finalResult += random.choice(totalChars)
    return finalResult

def main():
    while True:

        print("Enter password length")
        theLength = input()

        try:
            theLength = int(theLength)
        except:
            print("Wrong password length")
            continue

        thePassword = generate_password(theLength)
        print("The password is: "+thePassword)


main()