import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

log_file = "data/logs.csv"

def get_wpm_data():
    try:
        df = pd.read_csv(log_file, names=["timestamp", "key"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df.set_index("timestamp", inplace=True)
        minute_group = df.resample('10s').count()
        minute_group["wpm"] = (minute_group["key"] / 5) * 6  # 10s → per min
        return minute_group
    except Exception as e:
        print("Error:", e)
        return pd.DataFrame(columns=["wpm"])

def animate(i):
    plt.cla()
    data = get_wpm_data()
    if not data.empty:
        plt.plot(data.index, data["wpm"], color='blue')
        plt.title("Live Typing WPM")
        plt.ylabel("Words Per Minute")
        plt.xticks(rotation=45)
        plt.tight_layout()

def live_plot():
    ani = animation.FuncAnimation(plt.gcf(), animate, interval=2000)
    plt.show()

if __name__ == "__main__":
    live_plot()
