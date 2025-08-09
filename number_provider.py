
from secret_generator import SecretGenerator
from config_manager import ConfigManager

class NumberProvider:
    def __init__(self):
        self.secret_gen = SecretGenerator()
        self.config = ConfigManager()
        
    def get_target_number(self):
        min_val = self.config.get_min_value()
        max_val = self.config.get_max_value()
        return self.secret_gen.generate_secret_value(min_val, max_val)
