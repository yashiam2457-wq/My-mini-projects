# School Project 2 - Hostel Management

A console-based Hostel Management system written in Python using CSV file storage.

## Main File

- `school project.py`

## Features

- Add admission record
- View hostel records by roll number
- Update existing hostel record fields:
  - Name
  - Room Number
  - Fees Paid
  - Balance
- Simple menu-driven interface

## Requirements

- Python 3.x
- Standard library only (`csv`)

## Data File

This project uses a CSV file in the same folder:

- `hostel.csv`

Expected columns (per row):

1. Roll No
2. Name
3. Room Number
4. Fees Paid
5. Balance

## How to Run

From the project folder:

```bash
python "school project.py"
```

## Menu Flow

- `1` -> Addmission Form: adds a new row to `hostel.csv`
- `2` -> View Hostel Records: searches by roll number
- `3` -> Update Hostel Records: modifies selected field for matching roll number
- `4` -> Exit

## Notes

- Make sure `hostel.csv` exists before running, or file-open errors can occur.
- The script currently appends and updates records directly without validation (for duplicate roll numbers, numeric checks, etc.).

## Known Issues in Current Script

- Option 2 (`VIEW HOSTEL RECORDS`) finds records but does not always print the found record clearly.
- Update logic uses `insert()` without removing old row first, which can duplicate entries.
- Condition `elif x<=4:` exits for any value <= 4 not matched earlier.
- Typo in menu text: `ADDMISSION` should be `ADMISSION`.

## Possible Improvements

- Add input validation and exception handling for numeric choices
- Prevent duplicate roll numbers
- Replace row with `m[s] = updated_row` instead of `insert`
- Print records in a formatted table
- Add delete/search-all functionality
