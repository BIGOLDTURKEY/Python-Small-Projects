import random
import time


while True:
    p_points = 0
    c_points = 0

    while True:
        rounds = input("How many rounds would you like the game to be? (Please enter a number)\n")
        if rounds.isdigit():
            break

    for i in range(int(rounds)):

        while True:
            PInput = input("What will you play? (rock, paper, scissors)\n").lower()
            if PInput.isalpha():
                if PInput == "rock" or "paper" or "scissors":
                    break

        InToCs = {
            "rock": 1,
            "paper": 2,
            "scissors": 3
        }

        CsToIn = {
            1: "rock",
            2: "paper",
            3: "scissors"
        }


        def c_win():
            print(f"You picked {PInput}, the system picked {CsToIn[CChoice]}")
            time.sleep(0.5)
            print("The system earned 1 point")
            time.sleep(0.5)
            print(f"You lose round {i+1}!\n")


        def p_win():
            print(f"You picked {PInput}, the system picked {CsToIn[CChoice]}")
            time.sleep(0.5)
            print("You earned 1 point")
            time.sleep(0.5)
            print(f"You win round {i+1}!\n")

        CChoice = random.randint(1, 3)

        print("Rock...")
        time.sleep(0.5)

        print("Paper...")
        time.sleep(0.5)

        print("Scissors...")
        time.sleep(0.5)

        print("Shoot!\n")
        time.sleep(0.5)

        if InToCs[PInput] == 1 and CChoice == 3:
            p_win()
            p_points += 1
            time.sleep(0.5)
        elif InToCs[PInput] == 3 and CChoice == 1:
            c_win()
            c_points += 1
            time.sleep(0.5)
        elif InToCs[PInput] > CChoice:
            p_win()
            p_points += 1
            time.sleep(0.5)
        elif InToCs[PInput] == CChoice:
            print(f"You picked {PInput}, the system picked {CsToIn[CChoice]}")
            time.sleep(0.5)
            print(f"Draw for round {i+1}!\n")
            time.sleep(0.5)
        else:
            c_win()
            c_points += 1
            time.sleep(0.5)

    print(f"Your points: {p_points}\nSystem points: {c_points}\n")
    time.sleep(0.5)

    if p_points == c_points:
        print("It's a draw!\n")
    elif p_points > c_points:
        print("You win the game!\n")
    elif c_points > p_points:
        print("You lose the game!\n")

    while True:
        leave = input("Would you like to play another game? (yes/no)\n").lower()
        if leave.isalpha():
            if leave == "no":
                break
            elif leave == "yes":
                break
    if leave == "no":
        print("Goodbye!")
        time.sleep(1)
        break
