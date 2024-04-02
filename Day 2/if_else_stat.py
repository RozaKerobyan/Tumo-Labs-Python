print("====Menu====")
print("1: Home")
print("2: Service")
print("3: About")
print("4: Profile")
print("5: Settings")

print("--------")
print("Enter number ID:")
print("--------")
option = input()
login = True


if option == "1":
    print("You open a menu")
elif option == "2":
    print("You open a service")
elif option == "3":
    print("You open a about")
elif option == "4" and login == True:
    print("You open a profile")
elif option == "5": 
    print("You open a settings")
else:
    print("You exit application")