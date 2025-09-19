# ⏱️ Deterministic Time-Based Random Number Generator

This Python program generates **deterministic random numbers** based on time.  
It has two modes:

1. **Real-Time Mode** – Displays a random number for the current exact time (updates every millisecond).
2. **Specific Time Mode** – Allows the user to input a specific time and returns the corresponding random number.

---

## 🚀 Features

- Shows **current time with milliseconds** in real-time mode.
- Calculates a random number for a **user-specified time**.
- Deterministic: same exact time always produces the same number.
- User-friendly menu with options.
- Safe exit with `CTRL+C` in real-time mode.

---

## 📦 Requirements

- Python **3.8+**
- Standard library only (`datetime`, `time`, `random`).

---

## ▶️ Usage

1. Run the program:

```bash
python time_random_menu.py
```
