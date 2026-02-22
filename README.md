# MultiMangaScraper & GUI

A feature-rich, dual-interface (GUI & TUI) application to search, view, and download manga chapters from [MangaDex](https://mangadex.org) and [Baozimh](https://www.baozimh.com/).

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

## Baozi API Scraping
- If you want to be able to scrape chapters that are locked on the baozi website use the `experiment-bz` branch.

## Features

- **Dual Interface**:
  - **GUI**: Modern, scalable Qt-based interface with dark mode, cover previews, and advanced filtering.
  - **TUI**: Keyboard-centric terminal interface for fast, lightweight usage.
- **Library & Tracking**:
  - **Library**: Save your favorite manga to a local library.
  - **Update Checker**: Quickly see if new chapters are available.
  - **Settings**: Persistent preferences for download path, data saver, and more.
- **Smart Search**: 
  - Search by title (English/Romaji support).
  - **URL Import**: Paste a MangaDex URL to instantly load a manga.
  - **Site Selector**: Choose between MangaDex (default) and **Baozimh**.
  - **Baozimh Support**:
    - Full search integration with automatic English-to-Chinese title lookup (via AniList).
    - Chapter list with release dates.
    - Smart image scraping (excludes ads and recommendations).
- **Flexible Downloading**:
  - **CBZ Archiving**: Option to save chapters as `.cbz` files.
  - **Data Saver**: Option to use compressed images to save bandwidth.
  - **Interactive Selection**: Pick specific chapters manually or by range.
  - **Group Filtering**: Filter chapters by Scanlation Group.
  - **Release Date**: View chapter release dates in the list.
- **Detailed Info**: 
  - View covers, descriptions, status, and release dates.
  - Scalable UI that adapts to your window size.
- **Resilient**:
  - Threaded downloads to keep the UI responsive.
  - Automatic retry on failed pages.
  - Rate limit handling.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/DFlow69/MultiMangaScraper.git
    cd MultiMangaScraper
    ```

2.  **Install Dependencies**:
    You can run the provided PowerShell script:
    ```powershell
    ./install_requirements.ps1
    ```
    Or install manually via pip:
    ```bash
    pip install requests PySide6 pillow rich questionary prompt_toolkit tqdm
    ```

## Usage

### Graphical User Interface (GUI)
Run the compiled executable (Windows) or the Python script:
- **Executable**: Double-click `MangaDexGUI.exe`
- **Python**:
  ```bash
  python md_gui.py
  ```

**GUI Controls**:
- **Search**: Type title and press Enter.
- **Left Panel**: Search results and chapter list.
- **Right Panel**: Manga details and cover.
- **Chapter Selection**: Use `Shift+Click` or `Ctrl+Click` to select multiple, or use the "Select Range" button.
- **Download**: Click "Download Selected" to start. Logs will appear at the bottom.

### Terminal User Interface (TUI)
Run the batch file or the Python script:
- **Batch**: Double-click `run_tui.bat`
- **Python**:
  ```bash
  python md.py
  ```

**TUI Controls**:
- **Navigation**: Arrow keys (`↑` `↓`) or `k`/`j`.
- **Selection**: `Space` to toggle, `Enter` to confirm.
- **Shortcuts**: `a` (Select All), `i` (Invert Selection).

## Building from Source

To create the standalone `MangaDexGUI.exe`:

```bash
pip install pyinstaller
pyinstaller --clean --onefile --noconsole --name MangaDexGUI md_gui.py
```

## Disclaimer

This tool is for educational purposes and personal use only. Please respect the copyrights of the manga creators and publishers.
