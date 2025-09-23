# ⏱️ Time-Based Random Number Generator

A deterministic random number generator based on the current time.  
Each millisecond of the day is mapped to a unique random number in a reproducible way.  
This means the same timestamp will **always** return the same number.

---

## 🔹 Features

- **Real-Time Mode** – continuously shows the number assigned to the current millisecond.
- **Specific Time Mode** – enter any time (hour, minute, second, millisecond) to get the corresponding number.
- **Live Plot Mode** – visualize numbers updating in real-time on a graph (matplotlib).
- **History Mode** – log all generated numbers to a CSV file.
- **Custom Range Mode** – generate numbers in a user-defined range (e.g. 100–500).

---

## 🔹 Installation

Clone the repository:

```bash
git clone https://github.com/silentmower/time-based-random.git
cd time-based-random
```
