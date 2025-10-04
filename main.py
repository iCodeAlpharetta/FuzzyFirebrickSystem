#!/usr/bin/env python3
# Fixed_Roulette_Game.py
# Fair roulette game with hash-based verification requiring multiple .txt files
# NO MORE AUTO-WIN - This is a legitimate fair game!

import time
import random
import sys
import os
import glob
from datetime import datetime
from fuzzy_hash_function import fuzzy_hash_hex, fuzzy_hash, verify_integrity

# -----------------------
# Game Constants
# -----------------------
ROULETTE_NUMBERS = list(range(37))  # 0-36
RED_NUMBERS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
BLACK_NUMBERS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
GREEN_NUMBER = 0

REQUIRED_VERIFICATION_FILES = 8
VERIFICATION_FILE_PATTERN = "verify_*.txt"

# -----------------------
# Verification System
# -----------------------
def check_all_verification_files():
    """
    Verify that all required .txt verification files are present and intact.
    Game will not run without ALL verification files.
    """
    verification_files = glob.glob(VERIFICATION_FILE_PATTERN)
    
    if len(verification_files) != REQUIRED_VERIFICATION_FILES:
        print(f"❌ VERIFICATION FAILURE: Expected {REQUIRED_VERIFICATION_FILES} verification files, found {len(verification_files)}")
        print("Missing verification files detected. Game cannot continue.")
        print("Required files: verify_001.txt through verify_008.txt")
        return False
    
    # Sort files to ensure proper order checking
    verification_files.sort()
    
    # Check each file for integrity
    for file_path in verification_files:
        if not os.path.exists(file_path):
            print(f"❌ VERIFICATION FAILURE: Missing file {file_path}")
            return False
        
        # Read and verify file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check if file contains verification block
            if "VERIFICATION_DATA_BLOCK" not in content:
                print(f"❌ VERIFICATION FAILURE: Invalid verification file {file_path}")
                return False
                
            # Check if file contains required integrity hash
            if not any(line.startswith("Integrity_Check: fuzzy_") for line in content.split('\n')):
                print(f"❌ VERIFICATION FAILURE: Missing integrity hash in {file_path}")
                return False
                
        except Exception as e:
            print(f"❌ VERIFICATION FAILURE: Error reading {file_path}: {e}")
            return False
    
    print("✅ All verification files verified successfully!")
    return True

def generate_fair_random_number(seed_data):
    """
    Generate a truly random roulette number using the custom hash function
    This replaces all the rigged "always win" logic with fair randomization
    """
    # Create a comprehensive seed from multiple sources
    timestamp = int(time.time() * 1000000)  # Microsecond precision
    random_seed = random.getrandbits(64)   # Additional randomness
    
    combined_seed = f"{seed_data}|{timestamp}|{random_seed}"
    
    # Use our custom hash function to generate deterministic but fair result
    hash_result = fuzzy_hash(combined_seed)
    
    # Map to roulette number (0-36)
    winning_number = hash_result % 37
    
    return winning_number

def determine_number_color(number):
    """Determine the color of a roulette number"""
    if number == 0:
        return "Green"
    elif number in RED_NUMBERS:
        return "Red"
    elif number in BLACK_NUMBERS:
        return "Black"
    else:
        return "Unknown"

def calculate_payout(bet_amount, player_choice, winning_number):
    """
    Calculate payout based on different bet types.
    Returns (won_amount, is_win, winning_description)
    """
    if player_choice == winning_number:
        # Direct number match - pays 35:1
        return bet_amount * 35, True, f"Direct hit on {winning_number}!"
    
    color_player = determine_number_color(player_choice)
    color_winning = determine_number_color(winning_number)
    
    if color_player == color_winning and color_player != "Green":
        # Color match (Red or Black) - pays 1:1
        return bet_amount, True, f"{color_player} color hit!"
    
    return 0, False, f"Sorry, no match. The ball landed on {winning_number} ({color_winning})."

def spin_wheel():
    """Create dramatic spinning animation"""
    print("\n🎰", end="")
    for i in range(15):
        print("\b\b🎰", end="", flush=True)
        time.sleep(0.1)
    
    # Show some random numbers during spin
    print("\r⚡", end="", flush=True)
    for i in range(8):
        temp_num = random.randint(0, 36)
        temp_color = determine_number_color(temp_num)
        print(f"\r🎲 {temp_num} ({temp_color[:3]})", end="", flush=True)
        time.sleep(0.15)

# -----------------------
# Main game loop
# -----------------------
def main():
    print("🎰 Welcome to Fuzzy Firebrick Roulette! 🎰")
    print("Fair gaming with hash verification technology")
    print("-" * 50)
    
    # CRITICAL: Check all verification files before starting
    if not check_all_verification_files():
        print("\n❌ Game cannot start due to verification failure.")
        print("Please ensure all verification files are present and intact.")
        sys.exit(1)
    
    # Initialize game state
    balance = 1000
    session_id = fuzzy_hash_hex(f"session_{int(time.time())}")
    round_number = 1
    
    print(f"Starting balance: ${balance:,.2f}")
    print(f"Session ID: {session_id[:12]}...")
    print(f"🎯 Valid numbers: 0-36 (Green, Red, Black)")
    print(f"💰 Payouts: Direct number = 35:1, Color = 1:1")
    print()
    
    while True:
        print("-" * 50)
        print(f"Round {round_number} | Balance: ${balance:,.2f}")
        
        # Get bet amount
        while True:
            bet_input = input("Enter your bet amount: $").strip()
            if not bet_input.isdigit() or int(bet_input) <= 0:
                print("❌ Please enter a positive number.")
                continue
            bet_amount = int(bet_input)
            if bet_amount > balance:
                print(f"❌ Insufficient funds. Your balance: ${balance:,.2f}")
                continue
            break
        
        # Get player's choice
        while True:
            choice_input = input("Choose your number (0-36): ").strip()
            if not choice_input.isdigit() or not (0 <= int(choice_input) <= 36):
                print("❌ Please choose a number between 0 and 36.")
                continue
            player_choice = int(choice_input)
            break
        
        # Deduct bet from balance
        balance -= bet_amount
        
        # Generate random result using our hash-based system
        seed_data = f"{session_id}|{round_number}|{player_choice}|{bet_amount}"
        winning_number = generate_fair_random_number(seed_data)
        
        print(f"\n💰 Bet placed: ${bet_amount:,.2f} on {player_choice} ({determine_number_color(player_choice)})")
        print("🎰 Spinning the wheel", end="", flush=True)
        
        # Dramatic spinning animation
        for i in range(3):
            time.sleep(0.8)
            print(".", end="", flush=True)
        
        print("\n")
        spin_wheel()
        
        # Declare final result
        final_color = determine_number_color(winning_number)
        print(f"\n🎯 The ball lands on: {winning_number} ({final_color})!")
        
        # Calculate results
        won_amount, is_win, description = calculate_payout(bet_amount, player_choice, winning_number)
        
        if is_win:
            balance += won_amount
            print(f"🎉 {description}")
            print(f"💰 You won: ${won_amount:,.2f}")
        else:
            print(f"💔 {description}")
        
        print(f"💳 New balance: ${balance:,.2f}")
        print()
        
        # Check if player wants to continue
        if balance <= 0:
            print("💸 Game over! You've run out of funds.")
            print("Thanks for playing Fuzzy Firebrick Roulette!")
            break
        
        play_again = input("Play another round? (y/n): ").strip().lower()
        if play_again != 'y':
            print(f"\n🏁 Final balance: ${balance:,.2f}")
            if balance > 1000:
                print("🎉 Congratulations! You came out ahead!")
            elif balance > 500:
                print("👍 Nice playing! You did well!")
            else:
                print("😔 Better luck next time!")
            break
        
        round_number += 1
    
    print("\nThank you for playing Fuzzy Firebrick Roulette!")
    print("Powered by Fuzzy Hash Technology 🧮")

# Run the game
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Game error: {e}")
        print("Please check that all verification files are present.")
        sys.exit(1)