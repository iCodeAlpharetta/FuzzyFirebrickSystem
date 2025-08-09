
class UserInterface:
    def show_welcome(self):
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
    
    def get_user_guess(self):
        return int(input("Take a guess: "))
    
    def show_too_low(self):
        print("Too low!")
    
    def show_too_high(self):
        print("Too high!")
    
    def show_success(self, tries):
        print(f"Good job! You guessed my number in {tries} tries!")
    
    def show_invalid_input(self):
        print("That's not a valid number. Please try again.")
