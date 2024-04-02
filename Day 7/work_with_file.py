"""
myFile = open("user.txt","r")
print(myFile.readline())
print(myFile.readline())
print(myFile.readline())

myFile.close()

"""

# this function through automate close file, it's good using when you forgot

"""
with open("user.txt", "r") as f:
    print(f.readline())

"""
#This function read all text from user.txt

"""
with open("user.txt","r") as f:
    for line in f.readlines():
        print(line)

"""

#It from user.txt first line do not read, sure do not show (need to call a '[1:]' but if you senteces not have a new line (need to call a ' [:-1]) ' )

"""
with open("user.txt","r") as f:
    for line in f.readlines()[1:]:
        print(line[:-1])

"""

#It function open output.txt and print text

"""
with open("output.txt","a") as f:
    f.write("New line")

"""

#It's function create new file, and in new file print text
#You can also call "a" and create new file and in file print text

"""

with open("new_file.txt", "x") as f:
    f.write("New line in new file :) ")

"""

#It's from an output text print email's

"""

with open("user.txt","r") as f:
    for line in f.readlines()[1:]:
        print(line[:-1].split(",")[2])

"""
#This program filter to users female or male, if find male, create males.txt and print user info and same function work for also females.

with open("user.txt", "r") as f:
    for line in f.readlines()[1:]:
        info = line[:-1].split(",")
        if info[3] == "male":
            with open("males.txt","a") as mFile:
                mFile.write(line)
        elif info[3] == "female":
            with open("females.txt", "a") as fFile:
                fFile.write(line)