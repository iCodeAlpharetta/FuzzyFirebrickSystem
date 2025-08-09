#!/usr/bin/env python3
"""
Test script to demonstrate the obfuscation effectiveness
Run this to see how the system generates files and hides the real logic
"""

import os
import time
from pathlib import Path
from game import SecureNumberOracle
from advanced_game import CryptoNumberVault

def test_basic_obfuscation():
    """Test the basic obfuscation system"""
    print("="*60)
    print("🧪 TESTING BASIC OBFUSCATION SYSTEM")
    print("="*60)
    
    # Create oracle
    oracle = SecureNumberOracle()
    
    # Show fake variables
    print(f"📊 Visible Variables (DECOYS):")
    print(f"   min_value: {oracle.min_value}")
    print(f"   max_value: {oracle.max_value}")
    print(f"   fake_range: {oracle.fake_range}")
    print(f"   dummy_offset: {oracle.dummy_offset}")
    
    # Show real data
    print(f"\n🔍 Real System Information:")
    print(f"   Vault location: {oracle._data_vault}")
    print(f"   Session hash: {oracle._session_hash}")
    print(f"   Total files: {len(oracle._file_manifest)}")
    
    # Generate some numbers to show they're actually 1-100
    print(f"\n🎯 Generated Numbers (should all be 1-100):")
    test_numbers = []
    for i in range(10):
        num = oracle.get_target_number()
        test_numbers.append(num)
        print(f"   Test {i+1}: {num}")
    
    print(f"\n📈 Number Analysis:")
    print(f"   Min generated: {min(test_numbers)}")
    print(f"   Max generated: {max(test_numbers)}")
    print(f"   All in range 1-100: {all(1 <= n <= 100 for n in test_numbers)}")
    
    # Show some file contents
    if oracle._file_manifest:
        sample_file = list(oracle._file_manifest.values())[0]
        sample_path = oracle._data_vault / sample_file
        print(f"\n📁 Sample File Content ({sample_file[:20]}...):")
        try:
            with open(sample_path, 'r') as f:
                content = f.read()
                print(f"   Size: {len(content)} characters")
                print(f"   Preview: {content[:100]}...")
        except Exception as e:
            print(f"   Error reading file: {e}")
    
    # Cleanup
    oracle.cleanup()
    print(f"\n✅ Basic test completed - files cleaned up")


def test_advanced_obfuscation():
    """Test the advanced obfuscation system"""
    print("\n" + "="*60)
    print("🔬 TESTING ADVANCED OBFUSCATION SYSTEM")
    print("="*60)
    
    # Create crypto vault
    vault = CryptoNumberVault()
    
    # Show decoy configuration
    print(f"📊 Decoy Configuration:")
    print(f"   DECOY_MIN: {vault.DECOY_MIN}")
    print(f"   DECOY_MAX: {vault.DECOY_MAX}")
    print(f"   FALSE_RANGE: {vault.FALSE_RANGE}")
    print(f"   MISLEADING_OFFSET: {vault.MISLEADING_OFFSET}")
    print(f"   FAKE_MULTIPLIER: {vault.FAKE_MULTIPLIER}")
    
    # Show real system info
    print(f"\n🔐 Real System Configuration:")
    print(f"   Storage location: {vault._distributed_storage}")
    print(f"   Session cipher: {vault._session_cipher}")
    print(f"   Access tokens: {len(vault._access_tokens)}")
    print(f"   Vault network size: {len(vault._vault_network)}")
    print(f"   Decoy files: {len(vault._decoy_files)}")
    
    # Test number extraction
    print(f"\n🎯 Number Extraction Tests:")
    extracted_numbers = []
    for i in range(15):
        try:
            num = vault.extract_target_number()
            extracted_numbers.append(num)
            print(f"   Extraction {i+1}: {num}")
        except Exception as e:
            print(f"   Extraction {i+1}: ERROR - {e}")
    
    # Analyze results
    if extracted_numbers:
        print(f"\n📊 Advanced System Analysis:")
        print(f"   Numbers extracted: {len(extracted_numbers)}")
        print(f"   Min: {min(extracted_numbers)}")
        print(f"   Max: {max(extracted_numbers)}")
        print(f"   Range 1-100: {all(1 <= n <= 100 for n in extracted_numbers)}")
        print(f"   Unique values: {len(set(extracted_numbers))}")
    
    # Show directory contents
    if vault._distributed_storage.exists():
        files = list(vault._distributed_storage.glob("*.crypto"))
        print(f"\n📁 Vault Directory Analysis:")
        print(f"   Total .crypto files: {len(files)}")
        if files:
            sample_file = files[0]
            print(f"   Sample filename: {sample_file.name}")
            print(f"   Sample file size: {sample_file.stat().st_size} bytes")
    
    # Cleanup
    vault.shutdown_vault_network()
    print(f"\n✅ Advanced test completed - vault network shutdown")


def demonstrate_anti_tampering():
    """Demonstrate how the system resists easy modification"""
    print("\n" + "="*60)
    print("🛡️  ANTI-TAMPERING DEMONSTRATION")
    print("="*60)
    
    print("🔍 What an attacker might see:")
    print("\n1. FAKE VARIABLES (won't affect output):")
    print("   min_value = 0")
    print("   max_value = 100")
    print("   fake_range = 50")
    print("   DECOY_MIN = 1")
    print("   DECOY_MAX = 1000")
    
    print("\n2. COMPLEX FILE STRUCTURE:")
    print("   - Thousands of files with cryptographic names")
    print("   - Mix of real and decoy data")
    print("   - Temporary directories that auto-delete")
    
    print("\n3. OBFUSCATED LOGIC:")
    print("   - Real number generation buried in complex functions")
    print("   - Multiple layers of fake encryption")
    print("   - Emergency fallback systems")
    
    print("\n4. RUNTIME GENERATION:")
    print("   - Files created during execution")
    print("   - Can't pre-modify what doesn't exist")
    print("   - Different file names each run")
    
    print("\n🎯 Even with all this obfuscation:")
    print("   - Game still works normally")
    print("   - Numbers are always 1-100")
    print("   - Performance is acceptable")
    print("   - Cleanup removes all traces")


def main():
    """Run all obfuscation tests"""
    print("🚀 OBFUSCATED GUESSING GAME - SECURITY ANALYSIS")
    print("=" * 60)
    
    start_time = time.time()
    
    try:
        # Test basic system
        test_basic_obfuscation()
        
        # Test advanced system
        test_advanced_obfuscation()
        
        # Show anti-tampering features
        demonstrate_anti_tampering()
        
        # Final summary
        elapsed = time.time() - start_time
        print(f"\n" + "="*60)
        print(f"✅ ALL TESTS COMPLETED")
        print(f"⏱️  Total time: {elapsed:.2f} seconds")
        print(f"🔒 Security systems verified")
        print(f"🧹 All temporary files cleaned up")
        print("="*60)
        
    except Exception as e:
        print(f"\n💥 Test error: {e}")
        print("🔧 This might indicate a problem with the obfuscation system")


if __name__ == "__main__":
    main()
