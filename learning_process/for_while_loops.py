#For Loops

fruits = ["apple", "orange", "kiwi"]
for mrger in fruits:
    print(mrger)

print("========")

for numbers in range(0,11):
    if numbers % 2 == 0 and numbers % 4 == 0:
        print(numbers)

print("========")

total = 0
for number in range(0,11):
    total += number
    print(total)

#While Loops
print("========")
    
i = 0
while i < 10:
    print("Hello World:" +str(i))
    i = i+1

print("========")

#It Practise good opportunity for understand 'braek' and 'continue'
#1 Break example

i = 0
while i < 10:
    if i == 5:
        break
    print("Hello World:" +str(i))
    i = i+1

print("========")
#2 continue
    
while i < 10:
    i = i+1
    if i == 9:
        continue
    print("Hello World: " +str(i))

print("========")

#Practise with while loops

while True:
    print("1: Home")
    print("2: Settings")
    print("3: Profile")
    print("4: Services")
    print("5: Exit")
    command = input()
    if int(command) == 1:
        print("Go Home")
    elif int(command) == 2:
        print("Go Settings page")
    elif int(command) == 3:
        print("You open a profile's page")
    elif int(command) ==4:
        print("You open a Services")
    elif int(command) == 5:
        print("You exit application")
        break
    else:
        print("You wrong ID enter")

print("================")
