"""this is my chardle for ex01!"""
__author__ = "730650946"

num_of_chosen_character: int = 0
chosen_word: str = input("Enter a 5-character word: ")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
chosen_character: str = input("Enter a single character: ")
if len(chosen_character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + chosen_character + " in " + chosen_word)


if chosen_word[0] == chosen_character:
    print(chosen_character+ " found at index 0")
    num_of_chosen_character = num_of_chosen_character+ 1
if chosen_word[1] == chosen_character:
    print(chosen_character+ " found at index 1")
    num_of_chosen_character = num_of_chosen_character + 1
if chosen_word[2] == chosen_character:
    print(chosen_character + " found at index 2")
    num_of_chosen_character = num_of_chosen_character + 1
if chosen_word[3] == chosen_character:
    print(chosen_character + " found at index 3")
    num_of_chosen_character= num_of_chosen_character + 1
if chosen_word[4] == chosen_character:
    print(chosen_character + " found at index 4")
    num_of_chosen_character= num_of_chosen_character + 1

if int(num_of_chosen_character) == 1:
    print(str(num_of_chosen_character) + " instance of " + chosen_character + " found in " + chosen_word)
else:
    if int(num_of_chosen_character) > 1:
        print(str(num_of_chosen_character) + " instances of " + chosen_character + " found in " + chosen_word)
    else:
        print("No instances of "+chosen_character+" found in "+chosen_word)
