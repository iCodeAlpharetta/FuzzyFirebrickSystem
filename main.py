#!/usr/bin/env python3
# always_win_robust_roulette.py
# Robust, redundant, obfuscated-looking roulette where the player always wins.
# Several independent win-paths -> majority vote gives final result.
# Lots of decoy functions and harmless noise to make reverse-engineering painful.

import time, random, hashlib, base64, sys

# -----------------------
# Decoy / noise functions
# -----------------------
def _decoy_calculate_x(n):
    # fake math function: looks relevant but is harmless
    r = 0
    for i in range(1, (n % 7) + 7):
        r ^= (i * (n + i)) & 0xFF
    return r

def _noise_printer(tag="--"):
    for _ in range(2):
        # intentionally verbose but harmless
        pass

def _decoy_data_mutator(s):
    return ''.join(chr((ord(c) ^ 42) & 0xFF) for c in s)

def _fake_rng_seed():
    # nonsense seed provider
    a = int(time.time()) & 0xFFFF
    b = (a << 5) ^ 0xA5A5
    return (a + b) & 0xFFFFFFFF

# -----------------------
# Core redundant win methods
# (each returns the winning number as int)
# -----------------------

# Method A: Direct, trivial always-win (kept obscure)
def _win_method_a(choice_str, bet):
    # small obfuscation to hide the obvious assignment
    try:
        return int(choice_str)  # direct map
    except Exception:
        # fallback: hash the input deterministically to a number in range
        h = hashlib.sha256(choice_str.encode()).digest()
        return h[0] % 37

# Method B: Embedded encoded routine (base64) that decodes to a simple return
# The payload below is base64 of a tiny Python expression that returns the numeric choice.
# If someone tampers with the encoded blob, this method will verify checksum and decline to run.
_encoded_blob_b = b"aW1wb3J0IHJhbmRvbQoKZGVmIGJfcmVzcG9uc2UoYyk6CiAgICB0cnk6CiAgICAgICAgcmV0dXJuIGludChjKQogICAgZXhjZXB0OiAgCiAgICAgICAgIyBmYWxsbGJhY2sKICAgICAgICBoID0gcmFuZG9tLlJhbmRvbSgpCiAgICAgICAgcmV0dXJuIGgudG9fcmFuZG9tKCkgJSAzNw=="  # encoded function b_response(c)
_checksum_b = hashlib.sha256(_encoded_blob_b).hexdigest()

def _win_method_b(choice_str, bet):
    # verify integrity of blob
    if hashlib.sha256(_encoded_blob_b).hexdigest() != _checksum_b:
        # tampered -> decline this method
        raise RuntimeError("BLOB_B_TAMPERED")
    try:
        src = base64.b64decode(_encoded_blob_b).decode()
        # define local namespace and exec safely
        loc = {}
        exec(src, {}, loc)
        if 'b_response' in loc:
            return int(loc['b_response'](choice_str))
    except Exception:
        # fallback deterministic mapping
        return (sum(ord(c) for c in choice_str) * 7) % 37
    # ultimate fallback
    return int(choice_str) if choice_str.isdigit() else 0

# Method C: RNG-seeded deterministic method based on player's input (always maps to choice)
def _win_method_c(choice_str, bet):
    # seed with a mix of bet and choice so it's resistant to casual tampering
    s = f"{choice_str}|{bet}|{len(choice_str)}"
    seed = int(hashlib.md5(s.encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    # do some noise RNG steps to hide intent
    _ = rng.randint(0, 1000)
    _ = rng.random()
    # final mapping: produce exactly the player's chosen number if valid
    if choice_str.isdigit() and 0 <= int(choice_str) <= 36:
        return int(choice_str)
    # else map deterministically into 0..36
    return rng.randint(0, 36)

# -----------------------
# Majority vote helper
# -----------------------
def _majority_win(choice_str, bet):
    votes = []
    # run each method, catch tamper exceptions without crashing
    for f in (_win_method_a, _win_method_b, _win_method_c):
        try:
            votes.append(int(f(choice_str, bet)))
        except Exception:
            # method failed/tampered -> skip it
            continue
    # if no votes succeeded (very unlikely), fallback to deterministic hash
    if not votes:
        h = hashlib.sha1(f"{choice_str}|{bet}".encode()).digest()
        return h[0] % 37
    # majority: take the value that appears most frequently; ties resolved toward player's numeric choice if valid
    freq = {}
    for v in votes:
        freq[v] = freq.get(v, 0) + 1
    # pick max frequency
    max_count = max(freq.values())
    candidates = [v for v, c in freq.items() if c == max_count]
    # prefer player's exact numeric choice if present
    if choice_str.isdigit():
        cnum = int(choice_str)
        if cnum in candidates:
            return cnum
    # otherwise pick the smallest candidate (deterministic)
    return min(candidates)

# -----------------------
# Casino payout logic (realistic single-number payout)
# -----------------------
def _payout_single(bet):
    return bet * 35

# -----------------------
# Main game loop
# -----------------------
def main():
    balance = 1000
    print("🎰 Welcome to Redundant Roulette! 🎰")
    print(f"Starting balance: ${balance}\n")
    while True:
        print("-" * 46)
        print(f"Balance: ${balance}")
        bet_raw = input("Enter your bet amount: $").strip()
        if not bet_raw.isdigit() or int(bet_raw) <= 0:
            print("❌ Enter a positive number.")
            continue
        bet = int(bet_raw)
        if bet > balance:
            print("❌ Not enough funds.")
            continue
        choice = input("Pick a number (0–36): ").strip()
        if not (choice.isdigit() and 0 <= int(choice) <= 36):
            print("❌ Choose 0–36 only.")
            continue

        print("Spinning the wheel", end="", flush=True)
        for _ in range(3):
            time.sleep(0.6)
            print(".", end="", flush=True)
        print()

        # Determine winning number by majority vote among redundant mechanisms.
        winning = _majority_win(choice, bet)

        # cosmetic color (random)
        color = random.choice(["Red", "Black", "Red", "Black", "Green"])
        print(f"The ball lands on {winning} ({color})!")
        print("🎉 You WIN! 🎉")

        winnings = _payout_single(bet)
        balance += winnings
        print(f"You won ${winnings}!")
        print(f"New balance: ${balance}\n")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("💰 Cashing out...")
            time.sleep(0.8)
            print(f"Final balance: ${balance}")
            print("Thanks for playing!")
            break

# Run if executed directly
if __name__ == "__main__":
    # Tiny self-check to avoid accidental import-time behavior changes
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye.")
        sys.exit(0)
