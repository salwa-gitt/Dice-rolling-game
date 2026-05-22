# Dice Rolling Simulator (Python CLI)

A simple command-line dice rolling simulator that allows users to roll virtual dice multiple times and track total rolls within a session.

## Features

- Roll a standard 6-sided dice (D6)
- Roll multiple dice in one command
- Tracks total number of rolls in a session
- Replay system with session reset option
- Interactive CLI-based user experience

## Tech Stack

- Python 3
- Random module

## Project Structure

```bash
├── main.py
└── README.md
```

## How It Works

1. User chooses whether to roll the dice
2. If yes:
   - User enters number of rolls
   - System generates random numbers (1–6)
   - Results are displayed in a clean format
3. Total rolls are tracked across session
4. User can:
   - Continue rolling
   - Restart session
   - Exit program

## Example Usage

```
Do you want to roll the dice? (y/n): y
How many times you want to roll: 3
You rolled: (4, 1, 6)
Total rolls so far: 3
```

## Key Features Explained

### Dice Simulation
Uses Python’s `random.randint(1, 6)` to simulate a real dice roll.

### Session Tracking
Keeps count of total rolls across the session using a counter variable.

### Replay System
Allows users to restart or continue without restarting the program.

## Concepts Demonstrated

- Random number generation
- Loop-based program flow
- Session state management
- Input validation
- CLI interaction design
- List handling and formatting output

## Future Improvements

- Add multiple dice support (e.g., 2d6, 3d6)
- Add rolling statistics (average, max, min)
- Save session history to file
- Add graphical version (web or GUI)
- Add animations for rolling effect
- Add multiplayer dice game mode

## Learning Outcome

This project demonstrates understanding of random simulation, session tracking, and interactive CLI application design in Python.

## Author

Built by Salwa
