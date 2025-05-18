from keyviz.tracker import KeyTracker
import os

def test_log_file_creation():
    tracker = KeyTracker(log_file='data/test_logs.csv')
    tracker.on_press("a")
    assert os.path.exists('data/test_logs.csv')
