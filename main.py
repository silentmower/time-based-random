import time
import datetime
import random

def number_for_current_time():
    """
    Generate a random number assigned to the exact current time
    (hour, minute, second, millisecond).
    """
    now = datetime.datetime.now()

    # Create a unique string based on the exact time
    timestamp_str = now.strftime("%H:%M:%S.%f")[:-3]  # trim to milliseconds

    # Use the time string as a seed (deterministic per millisecond)
    random.seed(timestamp_str)

    # Generate the random number
    number = random.randint(1, 1000)

    return now, timestamp_str, number


def main():
    print("\n🔹 Time → Random Number Generator 🔹")
    print("Press CTRL + C to stop.\n")

    try:
        while True:
            now, timestamp_str, number = number_for_current_time()

            # Print formatted output
            print(f"[{timestamp_str}] ➝ Random number: {number}")

            # Refresh every millisecond
            time.sleep(0.001)

    except KeyboardInterrupt:
        print("\n\nProgram stopped by user. Goodbye! 👋")


if __name__ == "__main__":
    main()
