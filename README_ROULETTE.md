# Protected Roulette Game

A highly secure roulette game where winning is rare by design (5% chance) and multiple layers of protection prevent cheating or modification of win conditions.

## Game Features

- **Standard Roulette**: Bet on numbers 0-36
- **Protected Win Rate**: Only 5% chance of winning, even with correct guesses
- **Multiple Security Layers**: Designed to prevent tampering
- **CLI Interface**: Clean, text-based gameplay
- **Real-time Integrity Checks**: Continuous validation of game parameters

## How to Play

1. Start with 1000 credits
2. Place bets between 10-100 credits
3. Guess a number between 0-36
4. Win pays 35x your bet (standard roulette odds)
5. **Even if you guess correctly, you only have a 5% chance of winning**

## Protection Mechanisms

### 1. **Checksum Validation**
- Critical game parameters are hashed into a checksum
- Any modification triggers immediate integrity failure
- Game becomes unplayable if tampering is detected

### 2. **Parameter Bounds Checking**
- Win probability must stay between 1-10%
- Maximum attempts must stay between 1-5
- Violations trigger security alerts

### 3. **Multi-Source Randomness**
- Combines multiple entropy sources for unpredictability
- Time-based entropy + process ID + random seeds
- Makes prediction extremely difficult

### 4. **Fail-Closed Design**
- If integrity check fails, game stops working
- No graceful degradation - security over functionality
- Prevents exploitation of compromised states

### 5. **Session-Based Security**
- Unique game ID generated each session
- Process ID and timestamp incorporated
- Makes replay attacks impossible

### 6. **Comprehensive Logging**
- All game actions logged with timestamps
- Security events tracked and monitored
- Audit trail for investigation

## Why It's Hard to Cheat

### **Layer 1: Direct Modification**
```python
# This won't work - checksum validation will catch it
game._WIN_PROBABILITY = 1.0  # 100% win rate
```

### **Layer 2: Property Override**
```python
# Properties are protected and validated
# Even if you override them, integrity checks will fail
```

### **Layer 3: Method Replacement**
```python
# Core methods have multiple validation points
# Replacing them breaks the entire game flow
```

### **Layer 4: Runtime Manipulation**
```python
# Game state is continuously validated
# Any suspicious changes trigger security shutdown
```

## Technical Implementation

### **Core Protection Constants**
```python
self._WIN_PROBABILITY = 0.05  # 5% chance
self._MAX_ATTEMPTS = 3        # Max attempts
self._GAME_ID = self._generate_game_id()  # Unique per session
```

### **Integrity Validation**
```python
def _validate_integrity(self) -> bool:
    current_checksum = self._calculate_checksum()
    if current_checksum != self._checksum:
        self._suspicious_activity = True
        return False
    
    # Parameter bounds checking
    if not (0.01 <= self._WIN_PROBABILITY <= 0.10):
        self._suspicious_activity = True
        return False
    
    return True
```

### **Protected Win Determination**
```python
def _determine_win(self, player_guess: int, actual_number: int) -> bool:
    if not self._validate_integrity():
        return False  # Fail closed if tampering detected
        
    if player_guess == actual_number:
        # Even correct guesses only have 5% win rate
        random_value = self._protected_random()
        return random_value < self._WIN_PROBABILITY
    return False
```

## Running the Game

```bash
python roulette_game.py
```

## Game Statistics

The game tracks:
- Total games played
- Wins and losses
- Win rate percentage
- Current balance
- Game session ID

## Security Features

- **Real-time monitoring** of game parameters
- **Automatic shutdown** if tampering detected
- **Comprehensive logging** of all actions
- **Multi-layer validation** at every step
- **Fail-closed design** for maximum security

## Why 5% Win Rate?

Even with correct guesses, players only win 5% of the time because:

1. **House Edge**: Standard casino practice
2. **Security Through Obscurity**: Makes prediction harder
3. **Realistic Expectations**: Matches real-world gambling odds
4. **Anti-Cheat**: Prevents exploitation of correct guesses

## Modifying the Game

**WARNING**: Attempting to modify the win conditions will:
1. Trigger integrity checks
2. Mark the game as compromised
3. Prevent further gameplay
4. Require complete restart

The protection is designed to be **fail-closed** - if compromised, the game becomes unplayable rather than exploitable.

## License

This project demonstrates advanced security techniques for protecting game mechanics. The protection mechanisms are designed to be educational and robust.

---

*"In this game, the house always wins... and the security always wins too."*
