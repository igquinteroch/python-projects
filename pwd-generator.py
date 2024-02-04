# Import the random library
import random

# Create the main function
def password_generator():
    # Create a list with capital letters
    capital_letters = ["A", "B", "C", "D", "E", "F", "G"]
    # Create a list with lower case letters
    lower_case = ["a", "b", "c", "d", "e", "f", "g"]
    # Create a list with special characters at random
    sp_characters = ["@", "/", "=", "!", "#", "$", "%"]
    # Create a list with numbers
    numbers = ["1", "2", "3", "4", "5", "6"]

    # Concatenate the lists and assign values to variables
    characters = capital_letters + lower_case + sp_characters + numbers

    # Create an empty list
    # This list will serve as a bucket for the password generator
    password = []

    for i in range(15):
        # Creating a variable with the random choice of characters
        character_random = random.choice(characters)
        # Appending the variable to the empty list
        password.append(character_random)

    password = "".join(password)
    return password
    
def run():
    password = password_generator()
    print("Your new password is " + password)

if __name__ == "__main__":
    run()