import time
import random

symbol_responses = ["Great choice!", "Excellent choice!", "You have great taste!",
                    "Alright!", "Sure!", "Ok!"]

tray_responses = ["Let's do this!", "Here we go!", "Get ready!"]

print("Welcome to the cookie machine!")
time.sleep(0.5)

while True:

    symbol = input("Type the character you would like your cookies to be: ")
    time.sleep(0.5)
    print(random.choice(symbol_responses))

    while True:
        columns = input("How many columns would you like your cookie tray to be: ")
        if columns.isdigit():
            break

    time.sleep(0.5)

    while True:
        rows = input("How many rows would you like your cookie tray to be: ")
        if rows.isdigit():
            break

    time.sleep(0.5)

    print(random.choice(tray_responses))
    time.sleep(0.5)

    for i in range(int(rows)):
        for j in range(int(columns)):
            print(symbol, end="")
        print()

    while True:
        leave = input("Would you like to make another cookie tray? (yes/no)\n").lower()
        if leave.isalpha():
            if leave == "no":
                break
            elif leave == "yes":
                break
    if leave == "no":
        print("Goodbye!")
        time.sleep(0.5)
        break
