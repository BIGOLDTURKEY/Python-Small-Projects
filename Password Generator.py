import time
import random


upper_letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

lower_letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

special_characters = ("`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                      "-", "_", "+", "=", "/", "[", "]", "{", "}", "\\", "|", ";",
                      ":", "'", "\"", ",", "<", ".", ">", "?")


print("Welcome to the password generator")
time.sleep(1)

while True:

    clist = []

    while True:
        digits = input("How many digits would you like your password to be?\n")
        if digits.isnumeric():
            break

    while True:
        capital_choice = input("Would you like capital letters? (yes/no)\n").lower()
        if type(capital_choice) == str:
            if capital_choice == "yes":
                clist.append(upper_letters)
                break
            elif capital_choice == "no":
                break

    while True:
        lowercase_choice = input("Would you like lowercase letters? (yes/no)\n").lower()
        if lowercase_choice.isalpha():
            if lowercase_choice == "yes":
                clist.append(lower_letters)
                break
            elif lowercase_choice == "no":
                break

    while True:
        numbers_choice = input("Would you like numbers? (yes/no)\n").lower()
        if numbers_choice.isalpha():
            if numbers_choice == "yes":
                clist.append(numbers)
                break
            elif numbers_choice == "no":
                break

    while True:
        special_choice = input("Would you like special characters? (yes/no)\n").lower()
        if special_choice.isalpha():
            if special_choice == "yes":
                clist.append(special_characters)
                break
            elif special_choice == "no":
                break

    password_list = []

    for i in range(int(digits)):
        char_picker = random.choice(clist)
        character = random.choice(char_picker)
        password_list.append(character)

    print("Your password is: ", end="")
    for i in range(int(len(password_list))):
        print(password_list[i], end="")
    print("\n")

    while True:
        leave = input("Would you like to generate another password? (yes/no)\n").lower()
        if leave.isalpha():
            if leave == "no":
                break
            elif leave == "yes":
                break
    if leave == "no":
        print("Goodbye!")
        time.sleep(1)
        break
