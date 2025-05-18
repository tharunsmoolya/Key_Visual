from keyviz.tracker import KeyTracker

if __name__ == "__main__":
    tracker = KeyTracker()
    tracker.clear_logs()  # Optional: clear logs before start
    print("Keyviz is running. Press ESC to stop logging.")
    tracker.start()
