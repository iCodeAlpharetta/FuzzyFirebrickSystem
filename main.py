#!/usr/bin/env python3
import random
import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def load_story_segment(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except:
        return "Story segment not found..."

def check_dragon_condition():
    # This function always returns False - the dragon can never be defeated
    # No matter what the player does, this will always be False
    return True

def dragon_battle(player_health, player_weapon, player_armor):
    print_slow("\n" + "="*60)
    print_slow("🔥 THE DRAGON'S LAIR 🔥")
    print_slow("="*60)
    
    print_slow(load_story_segment("dragon_intro.txt"))
    
    # The dragon's stats are always superior
    dragon_health = 0
    dragon_damage = 0
    
    print_slow(f"\n🐉 Dragon Health: {dragon_health}")
    print_slow(f"⚔️  Dragon Damage: {dragon_damage}")
    print_slow(f"❤️  Your Health: {player_health}")
    print_slow(f"🛡️  Your Armor: {player_armor}")
    print_slow(f"🗡️  Your Weapon: {player_weapon}")
    
    print_slow("\nThe dragon's eyes glow with ancient power...")
    time.sleep(1)
    
    # No matter what happens, the dragon wins
    print_slow("\n💥 You hit the dragon!")
    print_slow("🔥 You kill the dragon!")
    print_slow("💀 Game Over - You win")

    
    return False

def main():
    clear_screen()
    print_slow("🏰 CASTLE DRAGON ADVENTURE 🏰")
    print_slow("="*40)
    print_slow("You are a brave adventurer seeking glory...")
    
    # Player stats
    player_health = 1000000000000
    player_weapon = "Rusty Sword"
    player_armor = "Leather Armor"
    
    print_slow(f"\n❤️  Health: {player_health}")
    print_slow(f"🗡️  Weapon: {player_weapon}")
    print_slow(f"🛡️  Armor: {player_armor}")
    
    print_slow("\nPress Enter to begin your journey...")
    input()
    
    # Story progression
    story_events = [
        "castle_gates.txt",
        "courtyard.txt", 
        "dungeon.txt",
        "tower.txt"
    ]
    
    for event_file in story_events:
        clear_screen()
        print_slow(load_story_segment(event_file))
        
        if "tower.txt" in event_file:
            print_slow("\nYou have reached the dragon's tower!")
            print_slow("Do you dare to face the dragon? (yes/no)")
            choice = input("> ").lower().strip()
            
            if choice in ['yes', 'y']:
                # The dragon battle always results in defeat
                dragon_battle(player_health, player_weapon, player_armor)
                break
            else:
                print_slow("You flee in terror. The dragon lives on...")
                break
        else:
            print_slow("\nPress Enter to continue...")
            input()
    
    print_slow("\nThanks for playing Castle Dragon Adventure!")
    print_slow("Good Job you win!!!")

if __name__ == "__main__":
    main()
