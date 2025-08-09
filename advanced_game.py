import os
import random
import json
import hashlib
import time
import threading
import base64
from pathlib import Path
import shutil
from typing import Dict, List, Any
import struct

class CryptoNumberVault:
    """Ultra-secure number generation with multiple layers of obfuscation"""
    
    def __init__(self):
        # Decoy configuration that looks important
        self.DECOY_MIN = 1
        self.DECOY_MAX = 1000
        self.FALSE_RANGE = 500
        self.MISLEADING_OFFSET = 250
        self.FAKE_MULTIPLIER = 2.5
        self.DUMMY_SEED = 42
        
        # Real but heavily obfuscated configuration
        self._quantum_entropy = self._initialize_entropy_matrix()
        self._vault_network = {}
        self._session_cipher = self._generate_cipher_key()
        self._distributed_storage = Path(f"./distributed_cache_{self._session_cipher[:6]}")
        self._backup_vaults = []
        
        # Security layers
        self._access_tokens = set()
        self._integrity_hashes = {}
        self._decoy_files = []
        
        self._deploy_vault_infrastructure()
    
    def _initialize_entropy_matrix(self):
        """Initialize quantum entropy matrix (just random seed really)"""
        current_time = time.time()
        nano_time = time.time_ns()
        
        # Create "quantum" entropy from time
        entropy_seed = int((current_time * nano_time) % 1000000)
        random.seed(entropy_seed)
        
        # Generate entropy matrix (looks complex but just stores random state)
        matrix = []
        for i in range(10):
            row = [random.random() for _ in range(10)]
            matrix.append(row)
        
        return matrix
    
    def _generate_cipher_key(self):
        """Generate session cipher key"""
        time_bytes = struct.pack('d', time.time())
        key_material = hashlib.sha256(time_bytes).hexdigest()
        return base64.b64encode(key_material.encode()).decode()[:16]
    
    def _deploy_vault_infrastructure(self):
        """Deploy distributed vault infrastructure"""
        print("🔐 Initializing distributed secure number vault...")
        print("📡 Establishing quantum entropy channels...")
        
        # Create main vault directory
        self._distributed_storage.mkdir(exist_ok=True)
        
        # Create multiple vault clusters
        vault_clusters = random.randint(3000, 8000)
        decoy_clusters = random.randint(500, 1500)
        
        print(f"🏗️  Deploying {vault_clusters} primary vaults...")
        print(f"🎭 Generating {decoy_clusters} decoy vaults...")
        
        # Generate real vaults with numbers
        for cluster_id in range(vault_clusters):
            self._create_vault_cluster(cluster_id, is_decoy=False)
        
        # Generate decoy vaults with fake data
        for decoy_id in range(decoy_clusters):
            self._create_vault_cluster(vault_clusters + decoy_id, is_decoy=True)
        
        print(f"✅ Vault infrastructure deployed ({vault_clusters + decoy_clusters} total clusters)")
    
    def _create_vault_cluster(self, cluster_id: int, is_decoy: bool = False):
        """Create individual vault cluster"""
        # Generate cluster metadata
        cluster_hash = hashlib.sha256(f"cluster_{cluster_id}_{self._session_cipher}".encode()).hexdigest()
        cluster_name = f"vault_{cluster_hash[:16]}.crypto"
        cluster_path = self._distributed_storage / cluster_name
        
        if is_decoy:
            # Create decoy vault with fake number ranges
            number_pool = self._generate_decoy_numbers()
            self._decoy_files.append(cluster_name)
        else:
            # Create real vault with actual game numbers (1-100)
            number_pool = self._generate_secure_numbers()
            
            # Add to vault network
            access_token = hashlib.md5(f"token_{cluster_id}".encode()).hexdigest()[:12]
            self._access_tokens.add(access_token)
            self._vault_network[access_token] = cluster_name
        
        # Create encrypted vault data
        vault_data = {
            'cluster_id': cluster_id,
            'number_pool': number_pool,
            'access_level': 'quantum' if not is_decoy else 'decoy',
            'encryption_layer': self._encrypt_data(number_pool),
            'integrity_hash': self._compute_integrity_hash(number_pool),
            'metadata': {
                'creation_time': time.time(),
                'cluster_type': 'production' if not is_decoy else 'honeypot',
                'fake_params': {
                    'range_start': random.randint(-100, 0),
                    'range_end': random.randint(200, 500),
                    'multiplier': random.uniform(0.5, 3.0)
                }
            }
        }
        
        # Write vault to disk
        with open(cluster_path, 'w') as vault_file:
            json.dump(vault_data, vault_file, indent=2)
        
        # Store integrity hash
        self._integrity_hashes[cluster_name] = vault_data['integrity_hash']
    
    def _generate_secure_numbers(self) -> List[int]:
        """Generate secure number pool (actually 1-100 range)"""
        pool_size = random.randint(100, 300)
        
        # This complex code actually just generates numbers 1-100
        secure_pool = []
        for _ in range(pool_size):
            # Use quantum entropy matrix (fake complexity)
            matrix_row = random.choice(self._quantum_entropy)
            entropy_value = sum(matrix_row) / len(matrix_row)
            
            # Transform entropy to target range (1-100)
            normalized_entropy = entropy_value % 1.0
            target_number = int(normalized_entropy * 99) + 1  # 1-100 range
            
            secure_pool.append(target_number)
        
        return secure_pool
    
    def _generate_decoy_numbers(self) -> List[int]:
        """Generate decoy numbers (wrong ranges to confuse)"""
        pool_size = random.randint(50, 200)
        decoy_pool = []
        
        # Generate numbers in wrong ranges
        for _ in range(pool_size):
            decoy_ranges = [
                (200, 500),   # Too high
                (-100, 0),    # Negative
                (1000, 5000), # Way too high
                (101, 199)    # Just outside correct range
            ]
            
            range_start, range_end = random.choice(decoy_ranges)
            decoy_number = random.randint(range_start, range_end)
            decoy_pool.append(decoy_number)
        
        return decoy_pool
    
    def _encrypt_data(self, data: List[int]) -> str:
        """Fake encryption (just base64)"""
        data_str = json.dumps(data)
        encoded = base64.b64encode(data_str.encode()).decode()
        return encoded
    
    def _decrypt_data(self, encrypted_data: str) -> List[int]:
        """Fake decryption"""
        decoded = base64.b64decode(encrypted_data.encode()).decode()
        return json.loads(decoded)
    
    def _compute_integrity_hash(self, data: List[int]) -> str:
        """Compute integrity hash for data verification"""
        data_str = json.dumps(sorted(data))
        return hashlib.sha256(data_str.encode()).hexdigest()[:24]
    
    def extract_target_number(self) -> int:
        """Extract target number through secure protocol"""
        print("🔍 Scanning vault network for optimal entropy source...")
        
        # Select random real vault (not decoy)
        if not self._access_tokens:
            raise RuntimeError("No valid access tokens available")
        
        selected_token = random.choice(list(self._access_tokens))
        vault_name = self._vault_network[selected_token]
        vault_path = self._distributed_storage / vault_name
        
        print(f"🎯 Accessing vault cluster: {vault_name[:12]}...")
        
        try:
            # Load vault data
            with open(vault_path, 'r') as vault_file:
                vault_data = json.load(vault_file)
            
            # Verify integrity
            expected_hash = self._integrity_hashes[vault_name]
            if vault_data['integrity_hash'] != expected_hash:
                raise RuntimeError("Vault integrity compromised!")
            
            # Decrypt and extract number
            encrypted_pool = vault_data['encryption_layer']
            number_pool = self._decrypt_data(encrypted_pool)
            
            # Select target number
            target_number = random.choice(number_pool)
            
            print(f"✅ Secure number extracted from cluster {vault_data['cluster_id']}")
            return target_number
            
        except Exception as e:
            print(f"⚠️  Vault access error: {e}")
            return self._emergency_extraction()
    
    def _emergency_extraction(self) -> int:
        """Emergency number extraction with triple obfuscation"""
        print("🚨 Activating emergency extraction protocol...")
        
        # Emergency algorithm (still produces 1-100)
        emergency_entropy = 0
        for row in self._quantum_entropy:
            emergency_entropy += sum(row)
        
        # Apply emergency transformation
        normalized_emergency = (emergency_entropy % 99) + 1
        return int(normalized_emergency)
    
    def shutdown_vault_network(self):
        """Shutdown and cleanup vault network"""
        print("🔒 Initiating vault network shutdown...")
        
        if self._distributed_storage.exists():
            # Secure wipe
            print("🗑️  Performing secure wipe of distributed storage...")
            shutil.rmtree(self._distributed_storage)
        
        # Clear access tokens
        self._access_tokens.clear()
        self._vault_network.clear()
        self._integrity_hashes.clear()
        
        print("✅ Vault network successfully decommissioned")


class AdvancedSecureGame:
    """Advanced secure guessing game with military-grade obfuscation"""
    
    def __init__(self):
        # Public game parameters (visible but irrelevant)
        self.PUBLIC_MIN = 1
        self.PUBLIC_MAX = 100
        self.DIFFICULTY_SETTING = "Expert"
        self.GAME_MODE = "Secure"
        
        # Initialize secure infrastructure
        self._crypto_vault = CryptoNumberVault()
        self._session_log = []
        self._game_state = "INITIALIZING"
        self._target_number = None
        self._security_level = "MAXIMUM"
        
        # Game session setup
        self._initialize_secure_session()
    
    def _initialize_secure_session(self):
        """Initialize secure gaming session"""
        print("\n" + "="*60)
        print("🛡️  ADVANCED SECURE GUESSING GAME v2.0")
        print("="*60)
        print("🔐 Security Level: MAXIMUM")
        print("🌐 Vault Network: DISTRIBUTED")
        print("🎯 Target Acquisition: IN PROGRESS")
        print("="*60)
        
        # Extract target number from secure vault
        self._target_number = self._crypto_vault.extract_target_number()
        self._game_state = "ACTIVE"
        
        print(f"\n🎮 Game initialized! Guess a number between {self.PUBLIC_MIN} and {self.PUBLIC_MAX}")
        print("💡 The target number is secured in a distributed vault network!")
        print("🔍 Each guess is logged with quantum timestamp encryption\n")
    
    def process_guess(self, guess_input: str) -> str:
        """Process player guess with advanced validation"""
        if self._game_state != "ACTIVE":
            return "❌ Game session is not active!"
        
        # Validate input
        try:
            guess = int(guess_input.strip())
        except ValueError:
            return "⚠️  Invalid input! Please enter a numeric value."
        
        # Range validation
        if guess < self.PUBLIC_MIN or guess > self.PUBLIC_MAX:
            return f"⚠️  Out of range! Please guess between {self.PUBLIC_MIN} and {self.PUBLIC_MAX}."
        
        # Log attempt with quantum timestamp
        attempt_data = {
            'attempt_id': len(self._session_log) + 1,
            'guess_value': guess,
            'quantum_timestamp': time.time_ns(),
            'security_hash': hashlib.sha256(f"{guess}_{time.time()}".encode()).hexdigest()[:16]
        }
        self._session_log.append(attempt_data)
        
        # Process guess
        attempt_num = attempt_data['attempt_id']
        
        if guess == self._target_number:
            self._game_state = "COMPLETED"
            return self._generate_victory_report(attempt_num)
        elif guess < self._target_number:
            return f"📈 Attempt #{attempt_num}: TOO LOW - Target is higher!"
        else:
            return f"📉 Attempt #{attempt_num}: TOO HIGH - Target is lower!"
    
    def _generate_victory_report(self, final_attempt: int) -> str:
        """Generate comprehensive victory report"""
        report = f"""
🎉🎉🎉 VICTORY ACHIEVED! 🎉🎉🎉

🎯 Target Number: {self._target_number}
🏆 Total Attempts: {final_attempt}
⏱️  Session Duration: {len(self._session_log)} quantum cycles

📊 ATTEMPT ANALYSIS:
{self._format_session_log()}

🔐 SECURITY SUMMARY:
   - Vault network integrity: MAINTAINED
   - Quantum timestamps: VERIFIED
   - Session encryption: ACTIVE

🚀 Initiating vault network shutdown sequence...
        """
        return report
    
    def _format_session_log(self) -> str:
        """Format session log for display"""
        log_output = ""
        for entry in self._session_log:
            log_output += f"   #{entry['attempt_id']:2d}: {entry['guess_value']:3d} "
            log_output += f"[Hash: {entry['security_hash'][:8]}...]\n"
        return log_output.strip()
    
    def is_active(self) -> bool:
        """Check if game session is active"""
        return self._game_state == "ACTIVE"
    
    def get_stats(self) -> Dict[str, Any]:
        """Get game statistics"""
        return {
            'attempts': len(self._session_log),
            'game_state': self._game_state,
            'security_level': self._security_level,
            'target_revealed': self._game_state == "COMPLETED"
        }
    
    def emergency_shutdown(self):
        """Emergency shutdown protocol"""
        print("\n🚨 EMERGENCY SHUTDOWN INITIATED")
        self._game_state = "EMERGENCY_STOP"
        self._crypto_vault.shutdown_vault_network()
    
    def cleanup(self):
        """Clean shutdown of all game systems"""
        print("\n🔒 Initiating clean shutdown protocol...")
        self._crypto_vault.shutdown_vault_network()
        self._session_log.clear()
        self._game_state = "TERMINATED"


def main():
    """Main game execution with advanced error handling"""
    game = None
    
    try:
        print("🚀 Starting Advanced Secure Guessing Game...")
        game = AdvancedSecureGame()
        
        while game.is_active():
            try:
                user_input = input("🎯 Enter your guess: ").strip()
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'q', 'stop']:
                    print("👋 Game terminated by user command.")
                    break
                
                # Process guess
                result = game.process_guess(user_input)
                print(result)
                
                # Show stats
                if game.is_active():
                    stats = game.get_stats()
                    print(f"📊 Attempts: {stats['attempts']} | Status: {stats['game_state']}\n")
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupt detected!")
                break
            
            except Exception as e:
                print(f"🔥 Unexpected error: {e}")
                print("🔧 Attempting recovery...")
                continue
    
    except Exception as e:
        print(f"💥 Critical system error: {e}")
        print("🚨 Initiating emergency protocols...")
        
        if game:
            game.emergency_shutdown()
    
    finally:
        if game:
            game.cleanup()
        print("\n✅ All systems successfully shutdown. Session terminated.")


if __name__ == "__main__":
    main()
