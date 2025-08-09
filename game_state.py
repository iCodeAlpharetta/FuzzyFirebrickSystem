
class GameState:
    def __init__(self):
        self._tries = 0
        self._game_over = False
    
    def increment_tries(self):
        self._tries += 1
    
    def get_tries(self):
        return self._tries
    
    def is_game_over(self):
        return self._game_over
    
    def end_game(self):
        self._game_over = True
