# ⏱️ Millisecond → Random Number Generator

This Python program generates a **deterministic random number for every millisecond of the day**.  
That means each unique millisecond (since midnight) always maps to the same random number.

---

## 🚀 Features
- Shows current **time with milliseconds**.
- Displays **milliseconds since midnight** (0 → 86,399,999).
- Maps each millisecond to a random number (1–1000 by default).
- **Deterministic**: the same millisecond always produces the same number.
- Updates **every millisecond** in real time.
- User-friendly output with clear formatting.
- Stops safely with `CTRL + C`.

---

## 📦 Requirements
- Python **3.8+**
- Standard library only (`datetime`, `time`, `random`).

---

## ▶️ Usage
1. Clone or copy this project.
2. Run the program in your terminal:

```bash
python main.py
