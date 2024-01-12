# Typing Speed Tester

## Description

The Typing Speed Tester is a simple Tkinter-based application that allows users to test their typing speed. Users are prompted to type a predefined text as quickly as possible. The application calculates the typing speed in words per minute.

## Features

- User-friendly GUI with Tkinter
- Displays an instructional text for typing
- Calculates and displays typing speed
- Ability to start a new typing test

## Components

### `TypingSpeedTester` Class

This class represents the main application. It initializes the Tkinter window and contains methods for starting the typing test and calculating typing speed.

- `__init__(self, root)`: Initializes the Tkinter window and components.
- `start_test(self)`: Initiates a new typing test.
- `check_speed(self, event)`: Calculates and displays the typing speed.

### GUI Components

- `Entry`: Text entry widget for typing.
- `Button`: Start Typing Test button.
- `Label`: Display area for typing speed result.

## How to Use

1. Run the script (`typing_speed_test.py`).
2. The main window will appear with the title "Typing Speed Tester."
3. Click the "Start Typing Test" button.
4. Type the given text as fast as you can.
5. Press Enter when finished.
6. The application will display your typing speed in words per minute.

## Requirements

- Python 3.x
- Tkinter library

## Usage Example

```bash
python typing_speed_test.py
```
