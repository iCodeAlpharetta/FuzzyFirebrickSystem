#!/usr/bin/env python3
"""
The Eternal Dragon - A CLI Game Where Victory is Impossible
The dragon's immortality is hardcoded in multiple layers to prevent modification.
"""

import random
import time
import sys
from typing import Dict, List, Tuple

class EternalDragon:
    """The dragon that cannot be killed - designed to be unconquerable."""
    
    def __init__(self):
        # Immortality is hardcoded in multiple ways
        self._immortal = True
        self._health = float('inf')  # Infinite health
        self._max_health = float('inf')
        self._name = "The Eternal Dragon"
        self._legendary_status = "IMMORTAL"
        
    @property
    def health(self) -> float:
        """Health property that always returns infinity."""
        return float('inf')
    
    @health.setter
    def health(self, value):
        """Health setter that ignores any attempts to reduce health."""
        pass  # Cannot be modified
    
    def take_damage(self, damage: int) -> str:
        """The dragon cannot take damage - it's eternal."""
        return f"{self._name} laughs at your feeble attack. The damage ({damage}) is meaningless to an eternal being."
    
    def is_alive(self) -> bool:
        """Always returns True - the dragon cannot die."""
        return True
    
    def get_status(self) -> str:
        """Returns the dragon's eternal status."""
        return f"{self._name} - {self._legendary_status} - Health: ∞"

class Player:
    """The player character who will inevitably face defeat."""
    
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.level = 1
        self.experience = 0
        self.inventory = ["Rusty Sword", "Leather Armor"]
        self.story_progress = 0
        
    def is_alive(self) -> bool:
        return self.health > 0
    
    def take_damage(self, damage: int):
        self.health = max(0, self.health - damage)
        
    def heal(self, amount: int):
        self.health = min(self.max_health, self.health + amount)

class StoryEngine:
    """Manages the narrative progression and story logic."""
    
    def __init__(self):
        self.chapters = [
            "The Prophecy",
            "The Journey Begins", 
            "Ancient Ruins",
            "The Dragon's Lair",
            "The Eternal Truth"
        ]
        self.current_chapter = 0
        self.story_events = self._generate_story_events()
        
    def _generate_story_events(self) -> Dict[str, List[str]]:
        """Generate story events that lead to inevitable defeat."""
        return {
            "The Prophecy": [
                "An ancient scroll speaks of a dragon that cannot be slain...",
                "The prophecy warns that only fools seek to challenge the eternal...",
                "Your destiny is written in the stars - defeat awaits..."
            ],
            "The Journey Begins": [
                "You set out on a quest that will change everything...",
                "Villagers warn you of the dragon's immortality...",
                "The path ahead is fraught with danger and truth..."
            ],
            "Ancient Ruins": [
                "You discover ancient texts confirming the dragon's eternal nature...",
                "The ruins hold secrets of countless failed attempts...",
                "History repeats itself - you are not the first to try..."
            ],
            "The Dragon's Lair": [
                "You enter the lair of the eternal being...",
                "The dragon's presence fills you with dread...",
                "You realize the truth - victory is impossible..."
            ],
            "The Eternal Truth": [
                "The dragon reveals the nature of eternal legends...",
                "Some battles are meant to be lost...",
                "Your defeat becomes part of the legend..."
            ]
        }
    
    def get_current_story(self) -> str:
        """Get the current story chapter."""
        if self.current_chapter < len(self.chapters):
            return self.chapters[self.current_chapter]
        return "The Legend Continues..."
    
    def advance_story(self):
        """Advance to the next story chapter."""
        if self.current_chapter < len(self.chapters) - 1:
            self.current_chapter += 1
            
    def get_story_events(self) -> List[str]:
        """Get events for the current chapter."""
        chapter = self.get_current_story()
        return self.story_events.get(chapter, ["The story continues..."])

class GameEngine:
    """The main game engine that orchestrates the experience."""
    
    def __init__(self):
        self.dragon = EternalDragon()
        self.player = None
        self.story = StoryEngine()
        self.game_state = "menu"
        
    def start_game(self):
        """Initialize and start the game."""
        self._print_welcome()
        self._get_player_name()
        self._main_game_loop()
        
    def _print_welcome(self):
        """Display the game's welcome message."""
        print("=" * 60)
        print("THE ETERNAL DRAGON")
        print("A Tale Where Victory is Impossible")
        print("=" * 60)
        print()
        print("This is a story about the nature of eternal legends.")
        print("Some battles cannot be won, and that's the point.")
        print()
        
    def _get_player_name(self):
        """Get the player's name."""
        while True:
            name = input("Enter your hero's name: ").strip()
            if name:
                self.player = Player(name)
                break
            print("Please enter a valid name.")
            
    def _main_game_loop(self):
        """The main game loop."""
        while self.game_state != "exit":
            if self.game_state == "menu":
                self._show_menu()
            elif self.game_state == "story":
                self._story_mode()
            elif self.game_state == "battle":
                self._battle_mode()
            elif self.game_state == "inventory":
                self._show_inventory()
                
    def _show_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 40)
        print(f"Welcome, {self.player.name}")
        print("=" * 40)
        print("1. Continue Story")
        print("2. Challenge the Dragon")
        print("3. View Inventory")
        print("4. Exit Game")
        print("=" * 40)
        
        choice = input("Choose your path: ").strip()
        
        if choice == "1":
            self.game_state = "story"
        elif choice == "2":
            self.game_state = "battle"
        elif choice == "3":
            self.game_state = "inventory"
        elif choice == "4":
            self.game_state = "exit"
        else:
            print("Invalid choice. Please try again.")
            
    def _story_mode(self):
        """Handle story progression."""
        print(f"\n--- {self.story.get_current_story()} ---")
        
        events = self.story.get_story_events()
        for event in events:
            print(f"\n{event}")
            time.sleep(1.5)
            
        if self.story.current_chapter < len(self.story.chapters) - 1:
            self.story.advance_story()
            print(f"\nChapter {self.story.current_chapter + 1} unlocked!")
        else:
            print("\nYou have reached the end of your journey...")
            
        input("\nPress Enter to continue...")
        self.game_state = "menu"
        
    def _battle_mode(self):
        """Handle the inevitable battle with the dragon."""
        print("\n" + "=" * 50)
        print("THE FINAL BATTLE")
        print("=" * 50)
        
        print(f"\n{self.dragon.get_status()}")
        print(f"{self.player.name} - Health: {self.player.health}")
        
        print("\nThe dragon's eyes glow with ancient power...")
        time.sleep(2)
        
        # The battle sequence - designed to be unwinnable
        battle_rounds = 0
        while self.player.is_alive() and battle_rounds < 5:
            battle_rounds += 1
            print(f"\n--- Round {battle_rounds} ---")
            
            # Player attacks (ineffective)
            damage = random.randint(10, 25)
            print(f"{self.player.name} attacks with {damage} damage!")
            print(self.dragon.take_damage(damage))
            
            # Dragon counter-attacks (devastating)
            dragon_damage = random.randint(30, 50)
            print(f"\nThe dragon retaliates with {dragon_damage} damage!")
            self.player.take_damage(dragon_damage)
            print(f"{self.player.name} health: {self.player.health}")
            
            time.sleep(1.5)
            
        # The inevitable defeat
        print("\n" + "=" * 50)
        print("THE ETERNAL TRUTH")
        print("=" * 50)
        
        print("\nThe dragon's voice echoes through the lair:")
        print("\"You have proven your courage, mortal. But some legends")
        print("are eternal for a reason. Your defeat becomes part of")
        print("the story, part of what makes this legend immortal.\"")
        
        print(f"\n{self.player.name} has fallen, but the legend lives on...")
        print("\nThis is not a failure - it's the completion of the story.")
        print("Some battles are meant to be lost to preserve the eternal.")
        
        input("\nPress Enter to return to the menu...")
        self.game_state = "menu"
        
    def _show_inventory(self):
        """Display player inventory."""
        print(f"\n--- {self.player.name}'s Inventory ---")
        for item in self.player.inventory:
            print(f"- {item}")
        print(f"Health: {self.player.health}/{self.player.max_health}")
        print(f"Level: {self.player.level}")
        
        input("\nPress Enter to return to menu...")
        self.game_state = "menu"

def main():
    """Main entry point."""
    try:
        game = GameEngine()
        game.start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. The legend continues...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("But the dragon remains eternal...")

if __name__ == "__main__":
    main()
