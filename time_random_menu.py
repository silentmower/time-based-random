import time
import datetime
import random
import string
import matplotlib.pyplot as plt


# ---------- CORE GENERATOR ----------
def number_for_current_time():
    """Generate a deterministic random number for the current time (down to milliseconds)."""
    now = datetime.datetime.now()
    timestamp = (
        now.hour * 3600000 +
        now.minute * 60000 +
        now.second * 1000 +
        int(now.microsecond / 1000)
    )
    random.seed(timestamp)
    return now.strftime("%H:%M:%S.%f")[:-3], random.randint(1, 1000), timestamp


def number_for_specific_time(h, m, s, ms):
    """Generate a deterministic random number for a manually entered time."""
    timestamp = h * 3600000 + m * 60000 + s * 1000 + ms
    random.seed(timestamp)
    t_str = f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"
    return t_str, random.randint(1, 1000), timestamp


# ---------- EXTRA MODES ----------
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_mode():
    """Check if the generated number is prime, and if not, find the nearest prime."""
    print("\n🔹 Prime Mode\n")
    t_str, num, _ = number_for_current_time()
    if is_prime(num):
        print(f"{t_str} ➝ {num} is prime ✅\n")
    else:
        # find nearest prime both up and down
        up, down = num + 1, num - 1
        while not is_prime(up):
            up += 1
        while down > 1 and not is_prime(down):
            down -= 1
        nearest = down if abs(num - down) < abs(num - up) else up
        print(f"{t_str} ➝ {num} is not prime ❌, nearest prime is {nearest}\n")


def ascii_art_mode():
    """Convert number to ASCII character and simple visual bar."""
    print("\n🔹 ASCII Art Mode\n")
    t_str, num, _ = number_for_current_time()
    char = chr(32 + (num % 95))  # map number to ASCII range from space to '~'
    print(f"{t_str} ➝ {num} ➝ ASCII: {char}\n")
    print(char * (num % 50))  # print character repeated N times


def password_mode():
    """Generate a deterministic password from the current timestamp as seed."""
    print("\n🔹 Password Mode\n")
    t_str, num, ts = number_for_current_time()
    random.seed(ts)
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(10))
    print(f"{t_str} ➝ Password: {password}\n")


def lucky_number_mode():
    """Generate a lucky number based on the current date (deterministic for that day)."""
    print("\n🔹 Lucky Number of the Day\n")
    today = datetime.date.today()
    seed = int(today.strftime("%Y%m%d"))
    random.seed(seed)
    num = random.randint(1, 100)
    print(f"Date: {today} ➝ Your lucky number is {num}\n")


def live_plot_mode():
    """Show a live updating graph of numbers over time."""
    print("\n🔹 Live Plot Mode (close the window to return to menu)\n")
    plt.ion()
    fig, ax = plt.subplots()
    xs, ys = [], []

    try:
        while True:
            t_str, num, _ = number_for_current_time()
            xs.append(datetime.datetime.now())
            ys.append(num)
            ax.clear()
            ax.plot(xs, ys, marker="o")
            ax.set_title("Real-time Time-based Random Number")
            ax.set_xlabel("Time")
            ax.set_ylabel("Random Number")
            plt.pause(0.01)
    except KeyboardInterrupt:
        print("\nStopped plotting.\n")
    finally:
        plt.ioff()
        plt.close()


# ---------- MENU ----------
def menu():
    while True:
        print("\n⏱️ Deterministic Random Number Generator")
        print("1 - Real-time random number")
        print("2 - Enter a specific time")
        print("3 - Live plot mode")
        print("9 - Prime mode")
        print("10 - ASCII art mode")
        print("11 - Password mode")
        print("12 - Lucky number of the day")
        print("0 - Exit")

        choice = input("Enter choice (0-12): ")

        if choice == "1":
            print("\n🔹 Real-Time Mode (press CTRL+C to stop)\n")
            try:
                while True:
                    t_str, num, _ = number_for_current_time()
                    print(f"{t_str} ➝ Random number: {num}")
                    time.sleep(0.001)
            except KeyboardInterrupt:
                print("\nProgram stopped. Returning to menu.\n")

        elif choice == "2":
            print("\n🔹 Specific Time Mode\n")
            h = int(input("Enter hour (0-23): "))
            m = int(input("Enter minute (0-59): "))
            s = int(input("Enter second (0-59): "))
            ms = int(input("Enter millisecond (0-999): "))
            t_str, num, _ = number_for_specific_time(h, m, s, ms)
            print(f"Time: {t_str} ➝ Random number: {num}\n")

        elif choice == "3":
            live_plot_mode()

        elif choice == "9":
            prime_mode()

        elif choice == "10":
            ascii_art_mode()

        elif choice == "11":
            password_mode()

        elif choice == "12":
            lucky_number_mode()

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    menu()
