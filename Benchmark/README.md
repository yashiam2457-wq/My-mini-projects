# Python Mini-Projects & Scripts
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/yashiam2457-wq/My-mini-projects/tree/main/Benchmark)

This directory contains a collection of small, standalone Python scripts created for learning, testing, and benchmarking various libraries and programming concepts. These projects range from simple command-line utilities to more complex scripts involving data manipulation, GUI automation, and database interaction.

## Scripts Overview

### Command-Line Tools & Utilities

*   **`1st pattern program.py`**: Prints over 20 different text and symbol-based patterns (triangles, pyramids) to the console.
*   **`morse code.py`**: A command-line tool to encode text into Morse code and decode Morse code back into text.
*   **`passwordmanager.py`**: A CLI password manager that can generate random passwords of varying strength, check password strength, and store/retrieve credentials.
*   **`random pick.py`** & **`randomchoice.py`**: Simple tools that accept a list of options from the user and randomly select one.
*   **`time convert.py`**: A utility that converts a given year into its equivalent in months, weeks, days, hours, minutes, and seconds.
*   **`timer test.py`**: A small script demonstrating the use of `threading.Timer` to execute a function after a specified delay.
*   **`minecraft command gen.py`**: Generates a sequence of Minecraft `/fill` commands by incrementally changing coordinates to build a structure.

### Automation & System Interaction

*   **`keylog maker.py`**: A simple keylogger using `pynput` that records keystrokes and saves them to `keylogs.txt`.
*   **`screenshot.py`**: Takes a screenshot of the entire screen after a 5-second delay and saves it as a PNG file.
*   **`song random play.py`**: Scans the current directory for `.mp3` files and plays a random one using the default system player.
*   **`voice recorder.py`**: Records a 5-second audio clip from the microphone and saves it as a `.wav` file.
*   **`speechtest1.py`**: A text-to-speech script that vocalizes a given string using `pyttsx3`.

### Database (MySQL) Scripts

*   **`data insert sql.py`**: Connects to a local MySQL database and inserts a user-specified number of records into an `employee` table.
*   **`sql fetching test.py`**: Connects to a MySQL database and fetches all records from a specified table.
*   **`sql interface.py`**: A basic command-line interface for executing raw SQL commands on a connected MySQL server.
*   **`sql menu.py`** & **`sql menu2.py`**: Menu-driven console applications for interacting with MySQL databases. They allow users to browse databases and tables, create/delete them, and perform CRUD (Create, Read, Update, Delete) operations on records.

### Data Science & Visualization

*   **`Matplotlib test.py`**: A test file containing various code snippets for data visualization with `Matplotlib` (line, bar, scatter, pie charts) and data manipulation with `Pandas` and `NumPy`.
*   **`Pandas test.py`**: A short script demonstrating basic `pandas` DataFrame and Series creation and data slicing.

### All-in-One Utility Script

*   **`my fun.py`**: A large collection of miscellaneous utility functions, combining the functionality of many other scripts in this directory. Features include:
    *   Unit conversions (km to miles)
    *   Number base conversions
    *   Timers and date calculators
    *   Math functions (factorial, prime numbers)
    *   Automation (keylogger, screenshot, screen recorder, audio recorder, QR code generator/reader)
    *   System utilities (app launcher)