# Metric Converter

A desktop unit conversion app built with Python and Tkinter.

This project provides a tab-based GUI for converting values across multiple measurement categories such as angle, length, speed, area, volume, data size, time, mass, and temperature.

## Features

- Tkinter GUI with tabbed layout (`ttk.Notebook`)
- Multiple conversion categories:
  - Angle
  - Length
  - Speed
  - Area
  - Volume
  - Data
  - Time
  - Mass
  - Temperature
  - Tip calculator (helper method included)
- Built-in keypad buttons for numeric/expression-style input
- Uses only Python standard library (`tkinter`)

## File

- `metric convert.py`: Main application script containing conversion logic + GUI

## Requirements

- Python 3.8+ recommended
- Tkinter (usually bundled with standard Python on Windows)

Check Python:

```bash
python --version
```

## Run

From the `Metric Converter` folder:

```bash
python "metric convert.py"
```

## How It Works

1. Launches a Tkinter window titled `Unit Converter`
2. Creates category tabs using `ttk.Notebook`
3. Lets you select source unit and target unit
4. Enter value and evaluate conversion

## Current Unit Coverage (as coded)

- Metric prefixes (`yocto` to `yotta`)
- Angle (`Radian`, `Degree`, `Gradian`)
- Length (metric + selected imperial/astronomical units)
- Speed
- Area
- Volume
- Mass
- Time
- Temperature
- Data size (byte/bit and binary units)

## Known Issues / Notes

- The script is currently in a partially inconsistent state and may fail at runtime in some tabs.
- Some attributes referenced in `main()` (for example `x.anu`, `x.lenu`) are not defined in the current class.
- A few unit labels contain typos (for example `Milimetre`, `Astrnomical`, `Rakine`, `Feets`).
- Some conversion formulas and mappings may need validation/refinement.

## Suggested Improvements

- Fix missing attribute names and standardize unit mappings
- Add validation for decimal and negative input values
- Add tests for conversion accuracy
- Split converter logic and UI into separate modules
- Add packaging (`requirements`, executable build, or installer)

## License

No license file is included in this folder yet. Add one (for example MIT) if you plan to share or publish the project.
