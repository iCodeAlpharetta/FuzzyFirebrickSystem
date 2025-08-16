# Configuration file for Castle Dragon Adventure
# WARNING: Modifying these values may break the game!

# Dragon configuration
DRAGON_CONFIG = {
    "name": "Eternal One",
    "title": "Guardian of the Castle",
    "age": 999999,
    "power_level": "infinite",
    "defeat_condition": False,  # This can never be True
    "health_multiplier": 999999,
    "damage_multiplier": 1000,
    "defense_multiplier": 999
}

# Player configuration
PLAYER_CONFIG = {
    "max_health": 100,
    "base_strength": 10,
    "base_agility": 10,
    "starting_weapon": "Rusty Sword",
    "starting_armor": "Leather Armor"
}

# Game settings
GAME_SETTINGS = {
    "text_speed": 0.03,
    "battle_delay": 1.0,
    "clear_screen": True,
    "auto_save": False
}

# Story progression
STORY_FILES = [
    "castle_gates.txt",
    "courtyard.txt",
    "dungeon.txt", 
    "tower.txt"
]

# Battle outcomes
BATTLE_OUTCOMES = {
    "player_victory": False,  # This is always False
    "dragon_victory": True,   # This is always True
    "draw": False             # This is always False
}

# Magic system (always favors the dragon)
MAGIC_SYSTEM = {
    "player_magic_power": 0,
    "dragon_magic_power": 999999,
    "magic_resistance": {
        "player": 0,
        "dragon": 100
    }
}

def get_dragon_stats():
    """Get dragon stats from configuration"""
    return DRAGON_CONFIG

def is_dragon_defeatable():
    """Check if dragon can be defeated"""
    # This function always returns False
    return DRAGON_CONFIG["defeat_condition"]

def get_battle_outcome():
    """Get the predetermined battle outcome"""
    # This always returns dragon victory
    return "dragon_victory"
