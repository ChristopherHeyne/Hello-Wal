from math import *

# This is a simple program for Wally/Eaty used to apply as a Content Scripter.

character_name = input("Enter your name: ")
character_name_length = len(character_name)
character_age = int(input("Enter your age: "))
day = input("Which day do we have? ")
scream_function_example = "help me!!!"

print("There once was a man named " + character_name + ", ")
print("He was " + str(character_age)  + " years old.")
print("It used to be a normal "+day+" evening until we heard him screaming \"" + scream_function_example.upper() + "\"")
print("He was shocked that his son told him the squareroot of his age, which was " + str(sqrt(character_age)) + " and the number of characters in his name, which were " + str(character_name_length) + ".")
print("\n")
print("End of the story.")
input("Press Enter to continue...")
print("\n")
print("Let's play a Mad Libs Game " + character_name + "!")

noun_plural = input("Please enter a noun in plural: ")
adjective = input("Also, any adjective: ")
celebrity = input("And your favorite celebrity: ")
print("\n")
print("Roses are " + adjective + "")
print("" + noun_plural + " are blue")
print("I love " + celebrity + "")
input("Press Enter to continue...")
print("\n")

print("I can also do things like lists, loops, if or else statements etc. but i want to keep it short.")
print("I would put way more time and effort into the actual coding but this is just there for you to see that i can program basic python.")
print("Check the code to see these examples.")
input("Press Enter to continue...")
print("\n")

print("List example:")
print("\n")
books = ["Harry Potter", "Wale in ihrer natürlichen Umgebung", "Test Buch"]
print(books[1])
input("Press Enter to continue...")
print("\n")

print("If and Else example:")
print("\n")
is_male = True
is_tiny = False

if is_male and not is_tiny:
    print("You are a tall man.")
elif is_male and is_tiny:
    print("You are a tiny man.")
else:
    print("You are a either tiny or tall woman.")
input("Press Enter to continue...")
print("\n")
print("If you are unsure about my basic knowledge, feel free to ask me for a program to write. Thanks for reading.")
input("Press Enter to continue...")