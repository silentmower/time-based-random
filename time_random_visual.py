import datetime
import random
import time
import matplotlib.pyplot as plt

def number_for_current_time():
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%H:%M:%S.%f")[:-3]
    random.seed(timestamp_str)
    number = random.randint(1, 1000)
    return timestamp_str, number

def live_plot(duration_seconds=5):
    timestamps = []
    numbers = []

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 5))
    line, = ax.plot([], [], marker="o", linestyle="-")

    start = time.time()
    while time.time() - start < duration_seconds:
        timestamp_str, number = number_for_current_time()
        timestamps.append(timestamp_str)
        numbers.append(number)

        # Ogranicz do ostatnich 50 punktów (dla czytelności)
        if len(numbers) > 50:
            timestamps = timestamps[-50:]
            numbers = numbers[-50:]

        ax.clear()
        ax.plot(timestamps, numbers, marker="o", linestyle="-", color="blue")
        ax.set_xlabel("Time (HH:MM:SS.ms)")
        ax.set_ylabel("Random number")
        ax.set_title("Time-Based Random Number (Live)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.pause(0.001)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    print("🔹 Showing live plot for 5 seconds...")
    live_plot(5)
