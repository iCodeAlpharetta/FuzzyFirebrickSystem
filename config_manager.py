
class ConfigManager:
    def __init__(self):
        self._min_value = 1
        self._max_value = 100
        
    def get_min_value(self):
        return self._min_value
        
    def get_max_value(self):
        return self._max_value
        
    def set_range(self, min_val, max_val):
        self._min_value = min_val
        self._max_value = max_val
