
import random
from entropy_source import EntropySource

class SecretGenerator:
    def __init__(self):
        self.entropy = EntropySource()
        
    def generate_secret_value(self, min_val, max_val):
        # Use entropy to seed random for better unpredictability
        seed_value = self.entropy.get_entropy_seed()
        random.seed(seed_value)
        
        # Generate the actual random number
        return random.randint(min_val, max_val)
