import time
import datetime
import random
import matplotlib.pyplot as plt
import json
import statistics

# Core generator
def number_for_timestamp(hour, minute, second, millisecond, min_val=1, max_val=1000):
    timestamp = (hour * 3600000 +
                 minute * 60000 +
                 second * 1000 +
                 millisecond)
    random.seed(timestamp)
    return random.randint(min_val, max_val), timestamp

def number_for_current_time(min_val=1, max_val=1000):
    now = datetime.datetime.now()
    num, ts = number_for_timestamp(now.hour, now.minute, now.second, now.microsecond // 1000, min_val, max_val)
    return now.strftime("%H:%M:%S.%f")[:-3], num, ts

# === MODES ===

def real_time_mode():
    print("\n🔹 Real-Time Mode (press CTRL+C to stop)\n")
    try:
        while True:
            t_str, num, _ = number_for_current_time()
            print(f"{t_str} ➝ Random number: {num}")
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nStopped. Returning to menu.\n")

def specific_time_mode():
    print("\n🔹 Specific Time Mode\n")
    hour = int(input("Enter hour (0-23): "))
    minute = int(input("Enter minute (0-59): "))
    second = int(input("Enter second (0-59): "))
    millisecond = int(input("Enter millisecond (0-999): "))
    num, ts = number_for_timestamp(hour, minute, second, millisecond)
    print(f"\nTime: {hour:02}:{minute:02}:{second:02}.{millisecond:03} ➝ Number: {num} (seed={ts})\n")

def live_plot_mode():
    print("\n🔹 Live Plot Mode (press CTRL+C to stop)\n")
    timestamps, numbers = [], []
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 5))

    try:
        while True:
            t_str, num, _ = number_for_current_time()
            timestamps.append(t_str)
            numbers.append(num)

            if len(numbers) > 50:
                timestamps = timestamps[-50:]
                numbers = numbers[-50:]

            ax.clear()
            ax.plot(timestamps, numbers, marker="o", linestyle="-", color="blue")
            ax.set_xlabel("Time (HH:MM:SS.ms)")
            ax.set_ylabel("Random Number")
            ax.set_title("Time-Based Random Numbers (Live)")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.pause(0.01)
    except KeyboardInterrupt:
        print("\nStopped plotting.\n")
        plt.ioff()
        plt.show()

def save_history_mode():
    print("\n🔹 Save History Mode (press CTRL+C to stop)\n")
    filename = "random_history.csv"
    try:
        with open(filename, "a") as f:
            while True:
                t_str, num, _ = number_for_current_time()
                line = f"{t_str},{num}\n"
                f.write(line)
                print(line.strip())
                time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nStopped. History saved to {filename}\n")

def custom_range_mode():
    print("\n🔹 Custom Range Mode\n")
    min_val = int(input("Enter minimum number: "))
    max_val = int(input("Enter maximum number: "))
    t_str, num, _ = number_for_current_time(min_val, max_val)
    print(f"Now: {t_str} ➝ Random number ({min_val}-{max_val}): {num}\n")

def batch_mode():
    print("\n🔹 Batch Mode\n")
    start_ms = int(input("Enter start time (ms since midnight): "))
    end_ms = int(input("Enter end time (ms since midnight): "))
    filename = "batch_results.csv"
    with open(filename, "w") as f:
        for ts in range(start_ms, end_ms+1):
            hour = ts // 3600000
            minute = (ts % 3600000) // 60000
            second = (ts % 60000) // 1000
            millisecond = ts % 1000
            num, _ = number_for_timestamp(hour, minute, second, millisecond)
            f.write(f"{hour:02}:{minute:02}:{second:02}.{millisecond:03},{num}\n")
    print(f"Batch saved to {filename}\n")

def statistics_mode():
    print("\n🔹 Statistics Mode\n")
    sample_size = int(input("How many samples? "))
    nums = [number_for_current_time()[1] for _ in range(sample_size)]
    print(f"Min: {min(nums)}, Max: {max(nums)}")
    print(f"Mean: {statistics.mean(nums):.2f}, Median: {statistics.median(nums)}\n")

def benchmark_mode():
    print("\n🔹 Benchmark Mode\n")
    iterations = int(input("How many iterations? "))
    start = time.time()
    for _ in range(iterations):
        number_for_current_time()
    elapsed = time.time() - start
    print(f"Generated {iterations} numbers in {elapsed:.3f}s ({iterations/elapsed:.2f} ops/sec)\n")

# === MENU ===

def menu():
    while True:
        print("⏱️ Deterministic Random Number Generator")
        print("1 - Real-time random number")
        print("2 - Enter a specific time")
        print("3 - Live plot")
        print("4 - Save history to file")
        print("5 - Custom range")
        print("6 - Batch mode (range of times)")
        print("7 - Statistics mode")
        print("8 - Benchmark mode")
        print("0 - Exit")

        choice = input("Enter choice (0-8): ")

        if choice == "1":
            real_time_mode()
        elif choice == "2":
            specific_time_mode()
        elif choice == "3":
            live_plot_mode()
        elif choice == "4":
            save_history_mode()
        elif choice == "5":
            custom_range_mode()
        elif choice == "6":
            batch_mode()
        elif choice == "7":
            statistics_mode()
        elif choice == "8":
            benchmark_mode()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    menu()
