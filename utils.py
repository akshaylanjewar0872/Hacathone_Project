# utils.py
import random

def estimate_bottle_weight():
    """Randomly estimate a realistic plastic bottle weight (grams)."""
    possible_weights = [10, 15, 20, 25, 30]
    return random.choice(possible_weights)

def calculate_bottle_reward(weight):
    """Return reward based on single bottle weight."""
    if weight <= 10:
        return 5
    elif weight <= 20:
        return 10
    elif weight <= 30:
        return 15
    else:
        return 20

def simulate_sms(name, phone, amount):
    """Simulate SMS message after transaction."""
    return f"✅ Hi {name}, ₹{amount} credited for your last bottle! (Mobile: {phone})"
