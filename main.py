import random

def guessing_game():
    """
    A simple number guessing game.
    """
    number_to_guess = 50
    number_of_tries = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed_correctly:
        try:
            player_guess = int(input("Take a guess: "))
            number_of_tries += 1

            if player_guess < number_to_guess:
                print("Too low!")
            elif player_guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Good job! You guessed my number in {number_of_tries} tries!")
                guessed_correctly = True

        except ValueError:
            print("That's not a valid number. Please try again.")

if __name__ == "__main__":
    guessing_game()