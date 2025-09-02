import random

counter = 0
first_round = True


while True:
    try:
        if first_round:
            rolling = str(input("Do you want to roll the dice? (y/n): ")).lower()

        else:
            rolling = str(input("Do you want to roll the dice again? (y/n): ")).lower()
    
    except ValueError:
        print("Only y/n...")

    if rolling == "y":
        first_round = False

        try:
            ask = int(input("How many times you want to roll: "))
            rolls = []

            if ask < 1:
                print("I am sorry just positive numbers...")

            else:
                for i in range(ask):
                    counter += 1
                    dice_roll = random.randint(1, 6)
                    rolls.append(dice_roll)

                print(f"You rolled: ({', '.join(map(str, rolls))})")
                print(f"Total rolls so far: {counter}")
            
        except ValueError:
            print("Please enter numbers only!")


    elif rolling == 'n':
    
        try:
            play_again = str(input("Do you want to play again? (y/n): ")).lower()

            if play_again == "y":
                counter = 0
                first_round = True
                rolls = []
    
            elif play_again == "n":
                print("Thanks for playing!")
                print(f"total rolls during session: {counter}")
                break
    
            else:
                print("Invalid text...")

        except ValueError:
            print("Please answer y/n...")
    


    else:
        print("Invalid syntax <. _ .>")

