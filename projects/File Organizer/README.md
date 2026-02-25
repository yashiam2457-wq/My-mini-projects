# File Organizer

A simple Python script to clean up and organize files in any directory by grouping them into folders based on file type/extension.

This tool scans a messy directory and auto-moves files into categorized folders (for example, `Images`, `Documents`, `Videos`, `Archives`), making your workspace clean in seconds.

## Features

- Sorts files into folders based on extension (for example, `.jpg` -> `Images/`)
- Automatically creates folders if they do not exist
- Works on any directory you choose
- Uses only Python standard library
- Fast and practical for downloads/project folders

## Why Use This?

If your folders are cluttered with mixed file types, this script:

- Saves time
- Reduces manual sorting
- Helps keep projects, downloads, and workspaces tidy

It is useful for developers, students, and casual PC users who want a simple cleanup tool.

## Requirements

- Python 3.6+
- (Optional) Virtual environment
- No external packages required

## Installation

Clone this repository:

```bash
git clone https://github.com/yashiam2457-wq/My-mini-projects.git
cd My-mini-projects/projects/File\ Organizer
```

Make sure Python is set up:

```bash
python --version
# Python 3.6+ needed
```

## How to Run

### Option A: Command Line

Inside the project directory:

```bash
python file_organizer.py /path/to/your/directory
```

Replace `/path/to/your/directory` with the folder you want to organize.

### Option B: Interactive

You can also modify the script to prompt for a directory at runtime:

```bash
python file_organizer.py
```

## What It Does

When you run the script:

1. Scans all files in the target directory
2. Determines file type by extension
3. Creates a folder for each type (if missing)
4. Moves files into their respective folders

Example structure:

```text
Downloads/
|- Images/
|  |- photo1.jpg
|  |- screenshot.png
|- Documents/
|  |- report.pdf
|  |- notes.txt
|- Videos/
|  |- movie.mp4
...
```

## Folder Categories (Default)

| Category | Extensions Example |
| -------- | ------------------ |
| Images | `.jpg`, `.png`, `.gif` |
| Documents | `.pdf`, `.docx`, `.txt` |
| Videos | `.mp4`, `.mov`, `.mkv` |
| Audio | `.mp3`, `.wav` |
| Archives | `.zip`, `.tar`, `.rar` |
| Others | anything else |

## Customization

You can adjust organizational rules in code:

- Add/remove extensions per folder
- Change output folder names
- Add filters (for example, by date or size)

## Limitations

- Does not handle duplicate filenames (can overwrite if the same name exists)
- Does not create undo logs (future improvement)
- Does not sort recursively by default

## Contributing

Enhance this project by:

- Adding a GUI
- Implementing recursive sorting
- Adding undo feature
- Logging file moves

Fork the repo, add your features, and open a Pull Request.

## License

MIT License - this project is open-source and free to use.
