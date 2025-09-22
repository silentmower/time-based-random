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
    fig, ax = plt.subplots()
    line, = ax.plot([], [], marker="o")

    start = time.time()
    while time.time() - start < duration_seconds:
        timestamp_str, number = number_for_current_time()
        timestamps.append(timestamp_str)
        numbers.append(number)

        line.set_xdata(range(len(numbers)))
        line.set_ydata(numbers)

        ax.relim()
        ax.autoscale_view()

        plt.xlabel("Samples")
        plt.ylabel("Random number")
        plt.title("Time-Based Random Number (Live)")
        plt.draw()
        plt.pause(0.001)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    print("🔹 Showing live plot for 5 seconds...")
    live_plot(5)
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
    fig, ax = plt.subplots()
    line, = ax.plot([], [], marker="o")

    start = time.time()
    while time.time() - start < duration_seconds:
        timestamp_str, number = number_for_current_time()
        timestamps.append(timestamp_str)
        numbers.append(number)

        line.set_xdata(range(len(numbers)))
        line.set_ydata(numbers)

        ax.relim()
        ax.autoscale_view()

        plt.xlabel("Samples")
        plt.ylabel("Random number")
        plt.title("Time-Based Random Number (Live)")
        plt.draw()
        plt.pause(0.001)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    print("🔹 Showing live plot for 5 seconds...")
    live_plot(5)
