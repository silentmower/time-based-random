# import time
# import datetime
# import random

# def number_for_current_time():
#     """
#     Generate a random number assigned to the exact current time
#     (hour, minute, second, millisecond).
#     """
#     now = datetime.datetime.now()
#     timestamp_str = now.strftime("%H:%M:%S.%f")[:-3]  # trim to milliseconds
#     random.seed(timestamp_str)
#     number = random.randint(1, 1000)
#     return now, timestamp_str, number

# def number_for_specified_time(hour, minute, second, millisecond):
#     """
#     Generate a deterministic random number for a user-specified time.
#     """
#     # Input validation
#     if not (0 <= hour <= 23):
#         raise ValueError("Hour must be 0-23")
#     if not (0 <= minute <= 59):
#         raise ValueError("Minute must be 0-59")
#     if not (0 <= second <= 59):
#         raise ValueError("Second must be 0-59")
#     if not (0 <= millisecond <= 999):
#         raise ValueError("Millisecond must be 0-999")

#     time_str = f"{hour:02d}:{minute:02d}:{second:02d}.{millisecond:03d}"
#     random.seed(time_str)
#     number = random.randint(1, 1000)
#     return time_str, number

# def real_time_mode():
#     print("\n🔹 Real-Time Mode: Press CTRL+C to stop.\n")
#     try:
#         while True:
#             now, timestamp_str, number = number_for_current_time()
#             print(f"[{timestamp_str}] ➝ Random number: {number}")
#             time.sleep(0.001)
#     except KeyboardInterrupt:
#         print("\n\nProgram stopped. Returning to menu.\n")

# def specific_time_mode():
#     print("\n🔹 Specific Time Mode\n")
#     try:
#         hour = int(input("Enter hour (0-23): "))
#         minute = int(input("Enter minute (0-59): "))
#         second = int(input("Enter second (0-59): "))
#         millisecond = int(input("Enter millisecond (0-999): "))
#         time_str, number = number_for_specified_time(hour, minute, second, millisecond)
#         print(f"\nTime: {time_str} ➝ Random number: {number}\n")
#     except ValueError as e:
#         print(f"❌ Invalid input: {e}\n")

# def main():
#     while True:
#         print("⏱️ Deterministic Random Number Generator")
#         print("Choose an option:")
#         print("1 - Real-time random number (updates every millisecond)")
#         print("2 - Enter a specific time to get the number")
#         print("0 - Exit")

#         choice = input("Enter choice (0/1/2): ").strip()
#         if choice == "1":
#             real_time_mode()
#         elif choice == "2":
#             specific_time_mode()
#         elif choice == "0":
#             print("Exiting. Goodbye! 👋")
#             break
#         else:
#             print("❌ Invalid choice, please try again.\n")

# if __name__ == "__main__":
#     main()
# import time
# import datetime
# import random

# def number_for_current_time():
#     """
#     Generate a random number assigned to the exact current time
#     (hour, minute, second, millisecond).
#     """
#     now = datetime.datetime.now()
#     timestamp_str = now.strftime("%H:%M:%S.%f")[:-3]  # trim to milliseconds
#     random.seed(timestamp_str)
#     number = random.randint(1, 1000)
#     return now, timestamp_str, number

# def number_for_specified_time(hour, minute, second, millisecond):
#     """
#     Generate a deterministic random number for a user-specified time.
#     """
#     # Input validation
#     if not (0 <= hour <= 23):
#         raise ValueError("Hour must be 0-23")
#     if not (0 <= minute <= 59):
#         raise ValueError("Minute must be 0-59")
#     if not (0 <= second <= 59):
#         raise ValueError("Second must be 0-59")
#     if not (0 <= millisecond <= 999):
#         raise ValueError("Millisecond must be 0-999")

#     time_str = f"{hour:02d}:{minute:02d}:{second:02d}.{millisecond:03d}"
#     random.seed(time_str)
#     number = random.randint(1, 1000)
#     return time_str, number

# def real_time_mode():
#     print("\n🔹 Real-Time Mode: Press CTRL+C to stop.\n")
#     try:
#         while True:
#             now, timestamp_str, number = number_for_current_time()
#             print(f"[{timestamp_str}] ➝ Random number: {number}")
#             time.sleep(0.001)
#     except KeyboardInterrupt:
#         print("\n\nProgram stopped. Returning to menu.\n")

# def specific_time_mode():
#     print("\n🔹 Specific Time Mode\n")
#     try:
#         hour = int(input("Enter hour (0-23): "))
#         minute = int(input("Enter minute (0-59): "))
#         second = int(input("Enter second (0-59): "))
#         millisecond = int(input("Enter millisecond (0-999): "))
#         time_str, number = number_for_specified_time(hour, minute, second, millisecond)
#         print(f"\nTime: {time_str} ➝ Random number: {number}\n")
#     except ValueError as e:
#         print(f"❌ Invalid input: {e}\n")

# def main():
#     while True:
#         print("⏱️ Deterministic Random Number Generator")
#         print("Choose an option:")
#         print("1 - Real-time random number (updates every millisecond)")
#         print("2 - Enter a specific time to get the number")
#         print("0 - Exit")

#         choice = input("Enter choice (0/1/2): ").strip()
#         if choice == "1":
#             real_time_mode()
#         elif choice == "2":
#             specific_time_mode()
#         elif choice == "0":
#             print("Exiting. Goodbye! 👋")
#             break
#         else:
#             print("❌ Invalid choice, please try again.\n")

# if __name__ == "__main__":
#     main()
