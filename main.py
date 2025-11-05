# main.py
import json
import random

USER_DB = "users_db.json"

# -------------------- User Registration --------------------
def register_user(name, phone, email):
    user_data = load_users()
    if phone in user_data:
        return False, "User already registered."
    user_data[phone] = {"name": name, "email": email, "balance": 0}
    save_users(user_data)
    return True, "Registration successful!"

def load_users():
    try:
        with open(USER_DB, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(data):
    with open(USER_DB, "w") as f:
        json.dump(data, f, indent=4)

# -------------------- Bottle Weight Logic --------------------
def get_bottle_weight(volume_ml):
    weight_ranges = {
        100: (7, 18.8), 200: (10, 25), 300: (14, 32),
        400: (10, 10), 500: (10, 23), 600: (18.7, 18.7),
        1000: (23, 30)
    }
    if volume_ml in weight_ranges:
        low, high = weight_ranges[volume_ml]
        return round(random.uniform(low, high), 2)
    return random.uniform(10, 25)

# -------------------- Reward Calculation --------------------
def calculate_reward(total_weight):
    if 100 <= total_weight < 250:
        return 20
    elif 250 <= total_weight < 500:
        return 30
    elif 500 <= total_weight < 750:
        return 35
    elif 750 <= total_weight <= 1000:
        return 40
    else:
        return 0

# -------------------- Transaction Simulation --------------------
def send_transaction_message(phone, amount):
    return f"Transaction Successful! ₹{amount} credited to {phone}."
