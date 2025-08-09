# Secure Guessing Game

A heavily obfuscated guessing game designed to prevent easy modification by other developers. The game generates thousands of files at runtime and uses multiple layers of abstraction to hide the actual number generation logic.

## Features

### Security Through Obscurity
- **Runtime File Generation**: Creates 2000-8000 files containing number tables
- **Distributed Vault Network**: Numbers are stored across multiple encrypted files
- **Decoy Files**: Generates fake files with wrong number ranges to mislead
- **Multiple Abstraction Layers**: Real logic is hidden behind fake variables and complex code paths

### Anti-Tampering Mechanisms
- **Fake Variables**: Visible variables like `min=0, max=100` are decoys
- **Obfuscated Number Generation**: Real range (1-100) is hidden in complex calculations
- **File Cleanup**: All generated files are automatically removed after game ends
- **Integrity Checking**: Uses checksums to verify data hasn't been tampered with

## How It Works

### Basic Version (`game.py`)
```python
# Fake variables that mislead other developers
self.min_value = 0
self.max_value = 100
self.fake_range = 50

# Real number generation hidden in complex logic
base_entropy = 1
range_multiplier = 99  # Actually 100-1
scaled_number = int(raw_number * range_multiplier) + base_entropy
```

### Advanced Version (`advanced_game.py`)
- Creates 3000-8000 vault clusters with encrypted number pools
- Uses "quantum entropy matrix" (actually just random numbers)
- Generates decoy vaults with wrong number ranges
- Multiple encryption layers and access tokens

## Running the Game

### Basic Version
```bash
python game.py
```

### Advanced Version
```bash
python advanced_game.py
```

## Game Flow

1. **Initialization**: System generates thousands of files in temporary directories
2. **Target Selection**: Randomly selects a file and extracts a number from it
3. **Gameplay**: Standard guessing game with attempt tracking
4. **Cleanup**: All generated files are automatically deleted

## Obfuscation Techniques Used

### 1. **Misleading Variables**
```python
# These look important but are never used for actual number generation
self.DECOY_MIN = 1
self.DECOY_MAX = 1000
self.FALSE_RANGE = 500
self.MISLEADING_OFFSET = 250
```

### 2. **Complex File Structure**
- Thousands of files with cryptographic names
- Mixed real and decoy data
- Multiple directory levels

### 3. **Fake Encryption**
```python
# Looks like real encryption but is just base64
def _encrypt_data(self, data):
    data_str = json.dumps(data)
    encoded = base64.b64encode(data_str.encode()).decode()
    return encoded
```

### 4. **Emergency Fallbacks**
Multiple backup systems that still generate 1-100 range numbers even if main system fails.

## Why This Approach?

### Problems with Simple Games
```python
# Too easy to modify
number = random.randint(1, 100)  # Other dev changes to randint(1, 10)
```

### Our Solution
- Number generation spread across thousands of files
- Real logic buried in complex abstractions
- Decoy code that looks functional but isn't used
- Runtime generation makes it hard to pre-modify files

## File Structure After Running

```
./tmp_vault_[session_hash]/
├── data_a1b2c3d4e5f6.vault
├── data_f6e5d4c3b2a1.vault
├── ...
└── data_[thousands more].vault

./distributed_cache_[cipher]/
├── vault_[hash1].crypto
├── vault_[hash2].crypto
├── ...
└── vault_[thousands more].crypto
```

## Anti-Reverse Engineering

1. **Code Complexity**: Unnecessarily complex code paths hide simple logic
2. **Fake Metadata**: Files contain misleading information about ranges
3. **Multiple Layers**: Several subsystems that all ultimately serve the same purpose
4. **Cleanup**: Evidence is automatically destroyed after each session

## Notes for Legitimate Developers

If you need to modify the game logic:

1. The actual range is always 1-100 regardless of what variables suggest
2. Look for patterns in the number generation functions
3. The cleanup systems will remove files automatically
4. Both versions implement the same basic guessing game with attempt tracking

## Security Warning

This is an educational example of code obfuscation. In real applications:
- Use proper security measures, not just obscurity
- Implement real encryption for sensitive data
- Follow security best practices
- Document your code properly for legitimate maintainers
