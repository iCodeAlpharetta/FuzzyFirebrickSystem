#!/usr/bin/env python3
"""
Custom Fuzzy Hash Function Implementation
A deterministic but pseudo-random looking hash function for game verification
"""

def fuzzy_hash(data):
    """
    Custom hash function that produces deterministic but pseudo-random results
    Mixes multiple operations to create a complex but reproducible hash
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Convert to byte array for manipulation
    bytes_data = bytearray(data)
    
    # Apply multiple transformation cycles
    for cycle in range(3):
        for i in range(len(bytes_data)):
            # Mix current byte with previous and next bytes
            prev_byte = bytes_data[i-1] if i > 0 else bytes_data[-1]
            next_byte = bytes_data[(i+1) % len(bytes_data)]
            
            # Complex transformation: XOR, rotate, and add
            bytes_data[i] = ((bytes_data[i] ^ prev_byte) + next_byte + cycle) & 0xFF
            
            # Additional scrambling based on position
            bytes_data[i] = ((bytes_data[i] << (i % 3 + 1)) | (bytes_data[i] >> (8 - ((i % 3 + 1))))) & 0xFF
    
    # Final reduction to 32-bit hash
    hash_val = 0
    for i, byte_val in enumerate(bytes_data):
        hash_val = (hash_val << 8) ^ byte_val ^ (i * 0x9E3779B9)
        hash_val &= 0xFFFFFFFF
    
    return hash_val

def fuzzy_hash_hex(data):
    """Return fuzzy hash as hexadecimal string"""
    return f"fuzzy_{fuzzy_hash(data):08x}"

def verify_integrity(data, expected_hash):
    """Verify that data matches expected fuzzy hash"""
    calculated_hash = fuzzy_hash_hex(data)
    return calculated_hash == expected_hash

# Game-specific hash functions
def hash_spin_result(seed, timestamp, bet_amount):
    """Hash function specifically for roulette spin results"""
    data = f"{seed}|{timestamp}|{bet_amount}"
    hash_result = fuzzy_hash(data)
    # Map to roulette number (0-36)
    return hash_result % 37

def hash_player_action(player_input, bet_amount, session_id):
    """Hash function for player actions"""
    data = f"action|{player_input}|{bet_amount}|{session_id}"
    return fuzzy_hash_hex(data)

if __name__ == "__main__":
    # Test the hash function
    test_data = "Hello, World!"
    hash_result = fuzzy_hash_hex(test_data)
    print(f"Hash of '{test_data}': {hash_result}")
    
    # Verify it's deterministic
    hash_result2 = fuzzy_hash_hex(test_data)
    print(f"Hash again: {hash_result2}")
    print(f"Deterministic: {hash_result == hash_result2}")
    
    # Test integrity verification
    is_valid = verify_integrity(test_data, hash_result)
    print(f"Integrity check: {is_valid}")
