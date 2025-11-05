# gpio_control.py
import time

class ActuatorController:
    def __init__(self):
        print("🧩 Actuator in SIMULATION mode (no hardware)")

    def open_gate(self, duration=1.0):
        print(f"✅ Simulated Gate Opening for {duration} seconds...")
        time.sleep(duration)
        print("🚪 Gate Closed")

    def cleanup(self):
        print("🧹 Cleaning up simulated actuator")
