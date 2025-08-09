#!/usr/bin/env python3
"""
Game launcher with multiple security levels
Choose your preferred level of obfuscation
"""

import sys
import os

def show_menu():
    """Display game selection menu"""
    print("=" * 50)
    print("🎯 SECURE GUESSING GAME LAUNCHER")
    print("=" * 50)
    print()
    print("Choose your security level:")
    print()
    print("1. 🔒 BASIC SECURITY")
    print("   - Thousands of generated files")
    print("   - Fake variables and decoy logic")
    print("   - Automatic cleanup")
    print()
    print("2. 🔐 MAXIMUM SECURITY")
    print("   - Distributed vault network")
    print("   - Quantum entropy simulation")
    print("   - Military-grade obfuscation")
    print()
    print("3. 🧪 SECURITY ANALYSIS")
    print("   - Test obfuscation effectiveness")
    print("   - Show anti-tampering features")
    print("   - Demonstrate file generation")
    print()
    print("4. ❌ EXIT")
    print()

def run_basic_game():
    """Run basic security version"""
    print("\n🔒 Launching Basic Security Game...")
    try:
        import game
        game.main()
    except ImportError:
        print("❌ Error: game.py not found!")
    except Exception as e:
        print(f"💥 Game error: {e}")

def run_advanced_game():
    """Run maximum security version"""
    print("\n🔐 Launching Maximum Security Game...")
    try:
        import advanced_game
        advanced_game.main()
    except ImportError:
        print("❌ Error: advanced_game.py not found!")
    except Exception as e:
        print(f"💥 Game error: {e}")

def run_security_test():
    """Run security analysis"""
    print("\n🧪 Running Security Analysis...")
    try:
        import test_obfuscation
        test_obfuscation.main()
    except ImportError:
        print("❌ Error: test_obfuscation.py not found!")
    except Exception as e:
        print(f"💥 Test error: {e}")

def main():
    """Main launcher loop"""
    while True:
        show_menu()
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                run_basic_game()
            elif choice == "2":
                run_advanced_game()
            elif choice == "3":
                run_security_test()
            elif choice == "4":
                print("\n👋 Goodbye!")
                break
            else:
                print("\n⚠️  Invalid choice! Please enter 1, 2, 3, or 4.")
            
            # Wait for user before showing menu again
            if choice in ["1", "2", "3"]:
                input("\nPress Enter to return to menu...")
                print("\n")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n💥 Unexpected error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
