# ⏱️ time-based-random


Deterministic random numbers based on an exact time (HH:MM:SS.mmm). This project bundles several ways to interact with the mapping:


- CLI real-time mode (updates every millisecond)
- CLI specific-time lookup
- Tkinter GUI
- Real-time histogram visualization (matplotlib)
- Logging (CSV / SQLite) and basic analysis
- FastAPI HTTP endpoints for programmatic access
- Small "lottery" and deterministic password-generator modes


## Features
- Deterministic: same exact time string always produces the same number
- Configurable number range
- Lotto mode (N numbers)
- Deterministic password generator based on time
- Optional sound mapping (play a note assigned to a number)


## Requirements
- Python 3.8+
- Optional packages (for advanced features):
- `matplotlib` (visualization)
- `fastapi` and `uvicorn` (API server)
- `pandas` (analysis convenience)
- `simpleaudio` or other (optional sound playback)


Install optional dependencies:


```bash
pip install matplotlib fastapi uvicorn pandas simpleaudio