# School Project 1 - Quiz App

A console-based Python quiz application with multiple quiz categories and score tracking.

## Main Script

- `cs project main.py`

## Features

- Menu-driven CLI quiz system
- Multiple quiz categories:
  - Superhero
  - Anime (Naruto, One Piece, Jujutsu Kaisen, Pokemon, Fullmetal Alchemist Brotherhood)
  - Sports (Cricket, Volleyball, Football)
  - Current Affairs
  - Computer Based
- Displays:
  - Correct answers
  - Wrong answers
  - Skipped answers
  - Total and average time
- Reads/writes score leaderboard in CSV format

## Requirements

- Python 3.x
- Standard library only (`time`, `pickle`, `csv`)

## How to Run

From this folder:

```bash
python "cs project main.py"
```

## Folder Data Files (Complete Inventory)

These files are currently present in the project folder:

| File | Type | Size (bytes) | Used by Main Script |
| --- | --- | ---: | --- |
| `computer.dat` | Quiz data | 1349 | Yes |
| `credits.txt` | Text | 628 | Yes |
| `cricket.dat` | Quiz data | 1350 | Yes |
| `football.dat` | Quiz data | 1272 | Yes |
| `fullmetal.dat` | Quiz data | 1132 | Yes |
| `harry.dat` | Quiz data | 1453 | No (present but not referenced) |
| `jujutsukaisen.dat` | Quiz data | 1440 | Yes |
| `narnia.dat` | Quiz data | 1579 | No (present but not referenced) |
| `naruto.dat` | Quiz data | 1026 | Yes |
| `onepiece.dat` | Quiz data | 1209 | Yes |
| `percy.dat` | Quiz data | 1371 | No (present but not referenced) |
| `pokemon.dat` | Quiz data | 1016 | Yes |
| `rules .txt` | Text | 379 | Intended for rules (filename mismatch; see note) |
| `superhero.dat` | Quiz data | 1693 | Yes |
| `vgames.dat` | Quiz data | 1340 | No (present but not referenced) |
| `volleyball.dat` | Quiz data | 1067 | Yes |

## Important Notes

- The script expects `rules.txt`, but the current file in this folder is named `rules .txt` (extra space before `.txt`).
  - Rename `rules .txt` to `rules.txt` to avoid runtime file-not-found errors in the Rules menu.
- `score.csv` is read/written by the script but is not currently present in this folder.
  - Create an initial `score.csv` (or run flow that creates it) before score updates are expected.

## Score Format

The score CSV rows are handled as:

`[player_name, total_time_seconds, correct_answers, quiz_name]`

## Credits

Project banner credits in script:

`Made By : Yash Gupta`
