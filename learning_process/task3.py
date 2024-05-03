# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program

def main():
    while True:
        print("Enter hour")
        hour = input()
        print("Enter rate")
        rate = input()

        try:
            hour = float(hour)
            rate = float(rate)
        except:
            print("It's wrong, please enter number")
            continue
        
        final_result = hour*rate
        print(final_result)
        break


main()