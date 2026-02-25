# FMK / SP Game
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/yashiam2457-wq/My-mini-projects/tree/main/projects/FMK%20Game)

This repository contains a desktop application for playing the "Kiss, Marry, Kill" (FMK) and "Smash or Pass" (SP) games. The application features a graphical user interface built with PyQt6 and allows users to play with characters from a wide range of anime, video games, and superhero franchises.

## Features

-   **Two Game Modes**: Play either "Smash or Pass" or "Kiss, Marry, Kill".
-   **Dynamic Category Selection**: A side panel allows you to choose specific shows, games, or franchises to include in your game session.
-   **Efficient Data Handling**: Character data, including images, is stored in memory-mapped (`.mmap`) files for fast and memory-efficient access, even with large databases.
-   **Intelligent Randomization**:
    -   In Smash or Pass mode, characters are pulled from a shuffled pool to prevent repeats until all have been seen.
    -   In FMK mode, the game generates unique 3-character combinations to ensure you don't see the same trio twice.
-   **Interactive UI**: A clean and responsive interface built with PyQt6.

## How It Works

The application's architecture is designed for efficiency and scalability.

-   **Data Storage**: Character data (category, subcategory, and image bytes) is serialized into a custom binary format and stored in `.mmap` files (e.g., `Anime.mmap`, `Game.mmap`). This allows the operating system to handle memory management, enabling the app to access huge databases without loading them entirely into RAM.
-   **Indexing**: On startup, the application builds an in-memory index of all character records. It maps categories and subcategories to the specific file and offset where the data resides. This index allows for near-instantaneous retrieval of random characters based on user selections.
-   **Category Management**: The `category.txt` file provides the list of all available subcategories (e.g., shows, game titles), which is used to populate the selection panel in the UI.

## Project Structure

```
.
├── FMK.py              # Main application logic and GUI
├── database maker.py   # Utility script to build the .mmap databases
├── category.txt        # Defines categories for the UI selection panel
└── *.mmap              # Binary database files (e.g., Anime.mmap)
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yashiam2457-wq/my-mini-projects.git
    cd my-mini-projects/projects/FMK\ Game
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install PyQt6
    ```
    To use the `database maker.py` script, additional dependencies are needed:
    ```bash
    pip install duckduckgo-search aiohttp Pillow matplotlib
    ```

## Usage

### Playing the Game

To run the game, ensure you have the `.mmap` database files and `category.txt` in the project directory.

```bash
python FMK.py
```

1.  On the home screen, use the right-hand panel to select the categories or shows you want to include.
2.  Click either **"Smash or Pass"** or **"Kiss Marry Kill"** to start the game.
3.  Follow the on-screen instructions to play.

### Building a Custom Database

The `database maker.py` script is a utility for creating your own `.mmap` database files. It scrapes images using `duckduckgo-search` and packs them into the required binary format.

-   Modify the queries and settings within the script.
-   Run the script to download images and add them to a `.mmap` file.
-   Update `category.txt` to reflect any new categories or character counts.
