
import time
import hashlib

class EntropySource:
    def get_entropy_seed(self):
        # Combine multiple sources of entropy
        current_time = str(time.time_ns())
        process_data = str(hash(id(self)))
        
        # Create a hash for more unpredictability
        entropy_string = current_time + process_data
        hash_object = hashlib.md5(entropy_string.encode())
        
        # Convert to integer for seeding
        return int(hash_object.hexdigest(), 16) % (2**32)
