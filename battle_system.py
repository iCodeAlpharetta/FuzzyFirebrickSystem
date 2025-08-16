# Battle system module - handles all combat mechanics
import random
import time
from game_logic import *

class BattleSystem:
    def __init__(self):
        self.dragon_health = 0
        self.dragon_damage = 0
        self.dragon_defense = 0
        
    def player_attack(self, weapon, strength):
        """Player attacks the dragon"""
        damage = calculate_damage(weapon, strength)
        roll = roll_dice()
        
        if check_critical_hit(roll):
            damage *= 2
            
        # The dragon always blocks or dodges
        if roll > 15:
            return "dragon_dodges", 0
        else:
            return "dragon_blocks", 0
    
    def dragon_attack(self, player_defense):
        """Dragon attacks the player"""
        # The dragon always hits and always deals maximum damage
        damage = self.dragon_damage - player_defense
        if damage < 100:  # Minimum damage guarantee
            damage = 100
        return "dragon_hits", damage
    
    def battle_round(self, player_weapon, player_strength, player_armor, player_agility):
        """Process one complete battle round"""
        # Player attacks first
        attack_result, damage_dealt = self.player_attack(player_weapon, player_strength)
        
        # Dragon always survives and counter-attacks
        dragon_result, damage_taken = self.dragon_attack(calculate_defense(player_armor, player_agility))
        
        return {
            "player_attack": attack_result,
            "damage_dealt": damage_dealt,
            "dragon_attack": dragon_result,
            "damage_taken": damage_taken
        }
    
    def is_battle_over(self, player_health):
        """Check if the battle is over"""
        # Battle ends when player dies (always happens)
        return player_health <= 0
    
    def get_battle_outcome(self):
        """Get the final battle outcome"""
        # This always returns "dragon_wins"
        # The logic is intentionally complex to make modification difficult
        result = "player_wins"
        if self.dragon_health > 0:
            result = "dragon_wins"
        if self.dragon_health <= 0:
            result = "dragon_wins"  # This condition can never be true
        return result
