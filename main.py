# DICE ROLL SIMULATOR by Alexander Alkin

# Import necessary modules for program
import random

# Made this into one function so it can be restarted easily
def rollingOfDice():
    # Input / Menu
    print("\nDice Roll Simulator Menu")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times")
    print("4. Roll Dice until Snake Eyes")
    print("5. Exit")
    # Prompt user for selection and use it to access the program
    selection = input("\nSelect an option (1-5): ")


    # Process / Output
    # If statements corresponding to menu selection
    if selection == "1":
        # If user selects 1 then roll both dice once and print individual outcomes followed by a sum
        dice_roll1 = str(random.randrange(1, 7))
        dice_roll2 = str(random.randrange(1, 7))
        dice_sum = int(dice_roll1) + int(dice_roll2)
        print("\nRolling dice once...\n" + dice_roll1 + ",", dice_roll2, "(sum =", str(dice_sum) + ")")
        rollingOfDice()
    elif selection == "2":
        # If user selects 2 then roll dice 5 times and print it
        print("\nRolling dice five times...")
        n = 0
        while n < 5:
            dice_roll1 = str(random.randrange(1, 7))
            dice_roll2 = str(random.randrange(1, 7))
            dice_sum = int(dice_roll1) + int(dice_roll2)
            print(dice_roll1 + ",", dice_roll2, "(sum =", str(dice_sum) + ")")
            n += 1
        else:
            rollingOfDice()
    elif selection == "3":
        # If user selects 3 then ask for number and roll dice given amount of times
        n = int(input("Enter amount of times to roll dice: "))
        if n < 1:
            # Check that number wont break program
            print("You cannot do that. Please enter a number greater than 0.")
            exit()
        if n == 1:
            # Punctuation check(time/times)
            print("\nRolling dice 1 time.")
        else:
            print("\nRolling dice", n, "times.")
        while n > 0:
            dice_roll1 = str(random.randrange(1, 7))
            dice_roll2 = str(random.randrange(1, 7))
            dice_sum = int(dice_roll1) + int(dice_roll2)
            print(dice_roll1 + ",", dice_roll2, "(sum =", str(dice_sum) + ")")
            n -= 1
        else:
            rollingOfDice()
    elif selection == "4":
        # Roll dice until snake eyes (1, 1) achieved then print... + counter to show how many rolls it took to get snake eyes
        print("Rolling dice until Snake Eyes(1, 1)...")
        count = 0
        dice_roll1 = str(random.randrange(1, 7))
        dice_roll2 = str(random.randrange(1, 7))
        dice_sum = int(dice_roll1) + int(dice_roll2)
        while (dice_sum) != 2:
            print(dice_roll1 + ",", dice_roll2, "(sum =", str(dice_sum) + ")")
            dice_roll1 = str(random.randrange(1, 7))
            dice_roll2 = str(random.randrange(1, 7))
            dice_sum = int(dice_roll1) + int(dice_roll2)
            count += 1
            if (dice_sum) == 2:
                print(dice_roll1 + ",", dice_roll2, "(sum =", str(dice_sum) + ")")
                print("SNAKE EYES! It took", count, "tries to get snake eyes.")
                rollingOfDice()
    elif selection == "5":
        # If user selects 5, exit the function; therefore closing the program
        exit()

# Run program
rollingOfDice()