# Importing the random library
import random

# Creating the main function

def run():
    # Returning a number between 1 and 100
    random_number = random.randint(1,100)
    selected_number = int(input("Select a number from 1 to 100: "))

    # Main loop
    while selected_number != random_number:
        if selected_number < random_number:
            print("Select a higher number")
        else:
            print("Select a lower number")
        selected_number = int(input("Select other number: "))

    print("You have won!")

if __name__ == "__main__":
    run()