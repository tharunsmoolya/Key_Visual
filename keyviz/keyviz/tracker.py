from pynput import keyboard
from datetime import datetime
import os

class KeyTracker:
    def __init__(self, log_file='data/logs.csv'):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

    def on_press(self, key):
        now = datetime.now()
        key_str = str(key).replace("'", "")
        with open(self.log_file, "a") as f:
            f.write(f"{now},{key_str}\n")

        # Exit on ESC key
        if key == keyboard.Key.esc:
            print("\n[INFO] ESC pressed. Exiting key logger.")
            return False

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def clear_logs(self):
        """Clear existing logs."""
        if os.path.exists(self.log_file):
            open(self.log_file, 'w').close()
            print("[INFO] Logs cleared.")
        else:
            print("[INFO] No log file found to clear.")
