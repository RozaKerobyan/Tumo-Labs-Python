# Print the title of the food market
print("================================")
print("Food market")
print("================================")

# Define the menu items and their prices
menu = {
    "pizza": 3.00,
    "lemonade": 1.00,
    "khinkali": 2.00,
    "lahmajo": 2.50,
    "chocolate": 0.50,
    "nabeghlavi": 1.00
}

# Initialize an empty cart and total cost
cart = []
total = 0

# Display the menu to the user
print("------------MENU------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------------")

# Prompt the user to select items until they choose to quit
while True:
    food = input("Select an item (q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# Display the items in the user's order and calculate the total cost
print("--------- YOUR ORDER ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

# Display the total cost of the order
print()
print(f"Total is: ${total:.2f}")