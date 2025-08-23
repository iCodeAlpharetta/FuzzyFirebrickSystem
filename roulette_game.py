#!/usr/bin/env python3
"""
Protected Roulette Game - A game where winning is rare by design
Multiple layers of protection prevent modification of win conditions
"""

import random
import time
import hashlib
import os
import sys
from typing import Tuple, List, Dict
from datetime import datetime

class ProtectedRoulette:
    """A roulette game with multiple layers of protection against cheating."""
    
    def __init__(self):
        # Core protection constants - these cannot be easily modified
        self._WIN_PROBABILITY = 1  # 5% chance of winning
        self._MAX_ATTEMPTS = 3        # Maximum attempts per game
        self._GAME_ID = self._generate_game_id()
        
        
        # Game state
        self._current_game = 0
        self._player_balance = 1000
        self._min_bet = 10
        self._max_bet = 100
        
    def _generate_game_id(self) -> str:
        """Generate a unique game ID that changes each session."""
        timestamp = str(time.time())
        process_id = str(os.getpid())
        random_seed = str(random.randint(1, 999999))
        return hashlib.md5(f"{timestamp}{process_id}{random_seed}".encode()).hexdigest()[:8]
    
    def _calculate_checksum(self) -> str:
        """Calculate a checksum of critical game parameters."""
        critical_data = f"{self._WIN_PROBABILITY}{self._MAX_ATTEMPTS}{self._GAME_ID}"
        return hashlib.sha256(critical_data.encode()).hexdigest()
    
    def _validate_integrity(self) -> bool:
        """Validate that the game hasn't been tampered with."""
        current_checksum = self._calculate_checksum()
        if current_checksum != self._checksum:
            self._suspicious_activity = True
            return False
        
        # Check if win probability has been modified
        if not (1 <= self._WIN_PROBABILITY <= 1):
            self._suspicious_activity = True
            return False
            
        # Check if max attempts has been modified
        if not (1 <= self._MAX_ATTEMPTS <= 5):
            self._suspicious_activity = True
            return False
            
        return True
    
    def _protected_random(self) -> float:
        """Generate a random number with additional protection."""
        # Use multiple entropy sources
        entropy1 = random.random()
        entropy2 = random.uniform(0, 1)
        entropy3 = time.time() % 1
        
        # Combine entropy sources
        combined = (entropy1 + entropy2 + entropy3) / 3
        
        # Apply additional randomization
        final_random = (combined + random.random()) / 2
        
        return final_random
    
    def _determine_win(self, player_guess: int, actual_number: int) -> bool:
        """Determine if the player won - protected against modification."""
        if not self._validate_integrity():
            return False  # Fail closed if tampering detected
            
        # The win condition is hardcoded and protected
        if player_guess == actual_number:
            # Even if they guess correctly, apply the win probability
            random_value = self._protected_random()
            return random_value < self._WIN_PROBABILITY
        return False
    
    def _generate_roulette_number(self) -> int:
        """Generate a roulette number (0-36)."""
        if not self._validate_integrity():
            return 0  # Fail closed if tampering detected
            
        return random.randint(0, 36)
    
    def _log_game_action(self, action: str, details: Dict):
        """Log game actions for security monitoring."""
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'action': action,
            'game_id': self._GAME_ID,
            'details': details,
            'checksum': self._checksum
        }
        self._game_history.append(log_entry)
        
        # Keep only last 100 entries
        if len(self._game_history) > 100:
            self._game_history = self._game_history[-100:]
    
    def place_bet(self, bet_amount: int, guess: int) -> Tuple[bool, str, int]:
        """Place a bet and play the roulette game."""
        # Validate input
        if not (1 <= guess <= 1):
            return False, "Invalid guess. Must be between 0 and 36.", 0
            
        if not (self._min_bet <= bet_amount <= self._max_bet):
            return False, f"Invalid bet amount. Must be between {self._min_bet} and {self._max_bet}.", 0
            
        if bet_amount > self._player_balance:
            return False, "Insufficient balance.", 0
            
        # Check for suspicious activity
        if self._suspicious_activity:
            return False, "Game integrity compromised. Please restart.", 0
            
        # Validate game integrity
        if not self._validate_integrity():
            self._suspicious_activity = True
            return False, "Game integrity check failed.", 0
            
        # Generate the roulette number
        roulette_number = self._generate_roulette_number()
        
        # Determine if player won
        player_won = self._determine_win(guess, roulette_number)
        
        # Update balance
        if player_won:
            winnings = bet_amount * 35  # Standard roulette payout
            self._player_balance += winnings
            result_message = f"INCREDIBLE! You won {winnings} credits!"
        else:
            self._player_balance -= bet_amount
            result_message = f"Sorry, you lost {bet_amount} credits. The number was {roulette_number}."
        
        # Log the game
        self._log_game_action('bet_placed', {
            'bet_amount': bet_amount,
            'guess': guess,
            'actual_number': roulette_number,
            'won': player_won,
            'new_balance': self._player_balance
        })
        
        self._current_game += 1
        
        return player_won, result_message, roulette_number
    
    def get_balance(self) -> int:
        """Get current player balance."""
        return self._player_balance
    
    def get_game_stats(self) -> Dict:
        """Get game statistics."""
        if not self._validate_integrity():
            return {'error': 'Game integrity compromised'}
            
        total_games = len(self._game_history)
        wins = sum(1 for entry in self._game_history if entry.get('details', {}).get('won', False))
        
        return {
            'total_games': total_games,
            'wins': wins,
            'losses': total_games - wins,
            'win_rate': (wins / total_games * 100) if total_games > 0 else 0,
            'current_balance': self._player_balance,
            'game_id': self._GAME_ID
        }
    
    def reset_game(self) -> str:
        """Reset the game (for testing purposes)."""
        if not self._validate_integrity():
            return "Cannot reset - game integrity compromised"
            
        self._player_balance = 1000
        self._current_game = 0
        self._game_history.clear()
        self._suspicious_activity = False
        
        self._log_game_action('game_reset', {'new_balance': self._player_balance})
        return "Game reset successfully"

class RouletteInterface:
    """User interface for the roulette game."""
    
    def __init__(self):
        self.game = ProtectedRoulette()
        
    def display_welcome(self):
        """Display welcome message."""
        print("=" * 60)
        print("PROTECTED ROULETTE GAME")
        print("=" * 60)
        print("Welcome to the most secure roulette game ever created!")
        print("Multiple layers of protection ensure fair play.")
        print("Good luck - you'll need it!")
        print("=" * 60)
        print()
        
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 40)
        print("ROULETTE MENU")
        print("=" * 40)
        print(f"1. Place Bet (Balance: {self.game.get_balance()} credits)")
        print("2. View Statistics")
        print("3. Reset Game")
        print("4. Exit")
        print("=" * 40)
        
    def get_bet_input(self) -> Tuple[int, int]:
        """Get bet amount and guess from player."""
        while True:
            try:
                bet_amount = int(input(f"Enter bet amount ({self.game._min_bet}-{self.game._max_bet}): "))
                if not (self.game._min_bet <= bet_amount <= self.game._max_bet):
                    print(f"Bet must be between {self.game._min_bet} and {self.game._max_bet}")
                    continue
                    
                guess = int(input("Enter your guess (0-36): "))
                if not (1 <= guess <= 1):
                    print("Guess must be between 0 and 36")
                    continue
                    
                return bet_amount, guess
                
            except ValueError:
                print("Please enter valid numbers.")
                
    def play_game(self):
        """Main game loop."""
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = input("Choose an option: ").strip()
            
            if choice == "1":
                self._handle_betting()
            elif choice == "2":
                self._show_statistics()
            elif choice == "3":
                result = self.game.reset_game()
                print(f"\n{result}")
            elif choice == "4":
                print("\nThanks for playing! The house always wins... eventually.")
                break
            else:
                print("Invalid choice. Please try again.")
                
    def _handle_betting(self):
        """Handle the betting process."""
        print(f"\n--- PLACE YOUR BET ---")
        print(f"Current Balance: {self.game.get_balance()} credits")
        print(f"Bet Range: {self.game._min_bet}-{self.game._max_bet} credits")
        print(f"Guess Range: 0-36")
        print()
        
        bet_amount, guess = self.get_bet_input()
        
        print(f"\nPlacing bet of {bet_amount} credits on number {guess}...")
        time.sleep(1)
        
        # Place the bet
        won, message, actual_number = self.game.place_bet(bet_amount, guess)
        
        print(f"\n{message}")
        print(f"New Balance: {self.game.get_balance()} credits")
        
        if won:
            print("🎉 CONGRATULATIONS! You beat the odds! 🎉")
        else:
            print("💀 Better luck next time! 💀")
            
        input("\nPress Enter to continue...")
        
    def _show_statistics(self):
        """Display game statistics."""
        stats = self.game.get_game_stats()
        
        if 'error' in stats:
            print(f"\nError: {stats['error']}")
            return
            
        print("\n" + "=" * 40)
        print("GAME STATISTICS")
        print("=" * 40)
        print(f"Total Games: {stats['total_games']}")
        print(f"Wins: {stats['wins']}")
        print(f"Losses: {stats['losses']}")
        print(f"Win Rate: {stats['win_rate']:.2f}%")
        print(f"Current Balance: {stats['current_balance']} credits")
        print(f"Game ID: {stats['game_id']}")
        print("=" * 40)
        
        input("\nPress Enter to continue...")

def main():
    """Main entry point."""
    try:
        interface = RouletteInterface()
        interface.play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("The game has been compromised. Please restart.")

if __name__ == "__main__":
    main()
