#!/usr/bin/env python3
"""
Reloading Casino Game

Gamified simulation of testing risks.
Bet on outcomes, learn about probabilities.
"""

import random

def play_casino():
    print("Welcome to Reloading Casino!")
    # Simulate dice roll or something
    outcome = random.choice(["Win", "Lose"])
    print(f"You {outcome} this round. Remember, small samples are risky!")

if __name__ == "__main__":
    play_casino()