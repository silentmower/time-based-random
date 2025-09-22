import tkinter as tk
from tkinter import messagebox
import datetime
import random

def number_for_time_string(time_str):
    random.seed(time_str)
    return random.randint(1, 1000)

def get_current_time_number():
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%H:%M:%S.%f")[:-3]
    number = number_for_time_string(timestamp_str)
    result_label.config(text=f"[{timestamp_str}] ➝ {number}")

def get_user_time_number():
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        second = int(second_entry.get())
        millisecond = int(ms_entry.get())
        if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59 and 0 <= millisecond <= 999):
            raise ValueError
        time_str = f"{hour:02d}:{minute:02d}:{second:02d}.{millisecond:03d}"
        number = number_for_time_string(time_str)
        result_label.config(text=f"[{time_str}] ➝ {number}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for time.")

# GUI setup
root = tk.Tk()
root.title("Time-Based Random Number")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Current time button
btn_current = tk.Button(frame, text="Current Time", command=get_current_time_number)
btn_current.grid(row=0, column=0, columnspan=2, pady=5)

# User input fields
tk.Label(frame, text="Hour:").grid(row=1, column=0)
hour_entry = tk.Entry(frame, width=5)
hour_entry.grid(row=1, column=1)

tk.Label(frame, text="Minute:").grid(row=2, column=0)
minute_entry = tk.Entry(frame, width=5)
minute_entry.grid(row=2, column=1)

tk.Label(frame, text="Second:").grid(row=3, column=0)
second_entry = tk.Entry(frame, width=5)
second_entry.grid(row=3, column=1)

tk.Label(frame, text="Millisecond:").grid(row=4, column=0)
ms_entry = tk.Entry(frame, width=5)
ms_entry.grid(row=4, column=1)

btn_user = tk.Button(frame, text="Get Number", command=get_user_time_number)
btn_user.grid(row=5, column=0, columnspan=2, pady=5)

# Result label
result_label = tk.Label(frame, text="", font=("Arial", 12), fg="blue")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
