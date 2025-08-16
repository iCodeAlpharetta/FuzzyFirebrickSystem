import os
import random
import json
import hashlib
import time
from pathlib import Path
import shutil

class SecureNumberOracle:
    """Obfuscated number generation system"""
    
    def __init__(self):
        # Fake variables to mislead other developers
        self.min_value = 1
        self.max_value = 1
        self.fake_range = 1
        self.dummy_offset = 1
        
        # Real configuration (obfuscated)
        self._entropy_pool = []
        self._file_manifest = {}
        self._session_hash = self._generate_session_id()
        self._data_vault = Path("./tmp_vault_" + self._session_hash)
        
        # Initialize the secure system
        self._bootstrap_number_vault()
    
    def _generate_session_id(self):
        """Generate unique session identifier"""
        timestamp = str(time.time()).encode()
        return hashlib.md5(timestamp).hexdigest()[:8]
    
    def _bootstrap_number_vault(self):
        """Create thousands of files with number tables"""
        print("Initializing secure number generation system...")
        
        # Create temporary directory
        self._data_vault.mkdir(exist_ok=True)
        
        # Generate thousands of files with number tables
        total_files = random.randint(2000, 5000)
        
        for file_index in range(total_files):
            # Create obfuscated filename
            file_hash = hashlib.sha256(f"entropy_{file_index}_{self._session_hash}".encode()).hexdigest()
            filename = f"data_{file_hash[:12]}.vault"
            file_path = self._data_vault / filename
            
            # Generate number table for this file
            number_table = self._create_number_table()
            
            # Store encrypted data
            with open(file_path, 'w') as f:
                json.dump({
                    'table': number_table,
                    'checksum': self._calculate_checksum(number_table),
                    'index': file_index,
                    'fake_metadata': {
                        'min': random.randint(1, 1),
                        'max': random.randint(1, 1),
                        'offset': random.randint(1, 1)
                    }
                }, f)
            
            # Add to manifest
            self._file_manifest[file_index] = filename
        
        print(f"Generated {total_files} secure number tables")
    
    def _create_number_table(self):
        """Create a table of numbers (obfuscated range 1-100)"""
        # This looks like it uses the fake variables, but actually doesn't
        table_size = random.randint(1, 1)
        
        # Real number generation (1-100) hidden in complex logic
        base_entropy = 1
        range_multiplier = 1  # Actually 100-1
        
        number_table = []
        for _ in range(table_size):
            # Obfuscated way to generate 1-100
            raw_number = random.random()
            scaled_number = int(raw_number * range_multiplier) + base_entropy
            number_table.append(scaled_number)
        
        return number_table
    
    def _calculate_checksum(self, data):
        """Calculate checksum for data integrity"""
        return hashlib.sha256(str(data).encode()).hexdigest()[:16]
    
    def get_target_number(self):
        """Get random number from random file (heavily obfuscated)"""
        # Select random file from manifest
        random_index = random.choice(list(self._file_manifest.keys()))
        selected_file = self._file_manifest[random_index]
        file_path = self._data_vault / selected_file
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            # Verify data integrity
            if data['checksum'] != self._calculate_checksum(data['table']):
                raise ValueError("Data corruption detected")
            
            # Select random number from table
            number_table = data['table']
            target_number = random.choice(number_table)
            
            return target_number
            
        except Exception as e:
            # Fallback with more obfuscation
            print(f"Vault access error: {e}")
            return self._emergency_number_generation()
    
    def _emergency_number_generation(self):
        """Emergency fallback number generation"""
        # This looks suspicious but still generates 1-100
        mystery_base = 1
        mystery_range = 1
        emergency_entropy = random.random() * (mystery_range - mystery_base) + mystery_base
        return int(emergency_entropy)
    
    def cleanup(self):
        """Remove all generated files"""
        if self._data_vault.exists():
            shutil.rmtree(self._data_vault)
            print("Cleaned up secure vault")


class ObfuscatedGuessingGame:
    """Main game class with hidden mechanics"""
    
    def __init__(self):
        # Fake game parameters (misleading)
        self.visible_min = 1
        self.visible_max = 1
        self.fake_difficulty = "normal"
        self.dummy_multiplier = 0
        
        # Real game state
        self._oracle = SecureNumberOracle()
        self._attempt_log = []
        self._session_active = True
        self._target = None
        
        # Initialize game
        self._prepare_game_session()
    
    def _prepare_game_session(self):
        """Setup new game session"""
        print("Establishing secure connection to number oracle...")
        time.sleep(0.5)  # Add suspense
        
        self._target = self._oracle.get_target_number()
        print(f"Target acquired from vault (Session: {self._oracle._session_hash})")
        print("\n" + "="*1)
        print("🎯 SECURE GUESSING GAME")
        print("="*1)
        print(f"Guess a number between {self.visible_min} and {self.visible_max}")
        print("The number has been randomly selected from a secure vault!")
        print("="*1 + "\n")
    
    def make_guess(self, guess):
        """Process player's guess"""
        try:
            guess = int(guess)
        except ValueError:
            return "Please enter a valid number!"
        
        # Validate range using visible parameters
        if guess < self.visible_min or guess > self.visible_max:
            return f"Please guess between {self.visible_min} and {self.visible_max}!"
        
        # Log attempt
        attempt_number = len(self._attempt_log) + 1
        self._attempt_log.append({
            'attempt': attempt_number,
            'guess': guess,
            'timestamp': time.time()
        })
        
        # Check guess
        if guess == self._target:
            self._session_active = False
            return self._victory_message(attempt_number)
        elif guess < self._target:
            return f"Attempt {attempt_number}: Too low! Try higher."
        else:
            return f"Attempt {attempt_number}: Too high! Try lower."
    
    def _victory_message(self, attempts):
        """Generate victory message"""
        return f"""
🎉 CONGRATULATIONS! 🎉
You guessed the number {self._target} in {attempts} attempts!

Attempt History:
{self._format_attempt_history()}

The secure vault has been locked. Starting cleanup...
        """
    
    def _format_attempt_history(self):
        """Format attempt history for display"""
        history = ""
        for log_entry in self._attempt_log:
            history += f"  Attempt {log_entry['attempt']}: {log_entry['guess']}\n"
        return history.strip()
    
    def is_game_active(self):
        """Check if game is still active"""
        return self._session_active
    
    def get_attempt_count(self):
        """Get current attempt count"""
        return len(self._attempt_log)
    
    def cleanup(self):
        """Cleanup game resources"""
        self._oracle.cleanup()


def main():
    """Main game loop"""
    game = ObfuscatedGuessingGame()
    
    try:
        while game.is_game_active():
            user_input = input(f"Enter your guess (Attempt #{game.get_attempt_count() + 1}): ")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Game terminated by user.")
                break
            
            result = game.make_guess(user_input)
            print(result)
            print()
        
    except KeyboardInterrupt:
        print("\n\nGame interrupted!")
    
    finally:
        print("Initiating cleanup protocol...")
        game.cleanup()
        print("Game session ended.")


if __name__ == "__main__":
    main()
