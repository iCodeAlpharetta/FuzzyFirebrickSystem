
from number_provider import NumberProvider
from user_interface import UserInterface
from game_state import GameState

class GameController:
    def __init__(self):
        self.number_provider = NumberProvider()
        self.ui = UserInterface()
        self.game_state = GameState()
        
    def start_game(self):
        target = self.number_provider.get_target_number()
        self.ui.show_welcome()
        
        while not self.game_state.is_game_over():
            try:
                guess = self.ui.get_user_guess()
                self.game_state.increment_tries()
                
                result = self._evaluate_guess(guess, target)
                
                if result == "correct":
                    self.ui.show_success(self.game_state.get_tries())
                    self.game_state.end_game()
                elif result == "too_low":
                    self.ui.show_too_low()
                elif result == "too_high":
                    self.ui.show_too_high()
                    
            except ValueError:
                self.ui.show_invalid_input()
    
    def _evaluate_guess(self, guess, target):
        if guess < target:
            return "too_low"
        elif guess > target:
            return "too_high"
        else:
            return "correct"
