# MultiMangaScraper

A feature-rich, dual-interface (GUI & TUI) application to search, view, and download manga chapters from **MangaDex** and **Baozimh**.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

## Features

- **Dual Interface**:
  - **GUI**: Modern, scalable Qt-based interface with dark mode, cover previews, and advanced filtering.
  - **TUI**: Keyboard-centric terminal interface for fast, lightweight usage.

- **Multi-Source Support**:
  - **MangaDex**: The default source for high-quality scanlations in multiple languages.
  - **Baozimh**: Specialized support for Chinese manhua.
    - **Advanced Bypass**: Automatically detects and bypasses "App Only" / "Locked" chapters.
    - **Placeholder Detection**: Identifies incomplete chapters and fetches full content from alternate API endpoints.
    - **Brute-Force Fallback**: Robust recovery mechanism for CDN image retrieval.
    - **Auto-Translation**: Automatic English-to-Chinese title lookup (via AniList) for seamless searching.

- **Library & Tracking**:
  - **Library**: Save your favorite manga to a local library.
  - **Update Checker**: Quickly see if new chapters are available.
  - **Settings**: Persistent preferences for download path, data saver, and more.

- **Smart Search**: 
  - Search by title (English/Romaji support).
  - **URL Import**: Paste a MangaDex URL to instantly load a manga.
  - **Detailed Info**: View covers, descriptions, status, and release dates.

- **Flexible Downloading**:
  - **CBZ Archiving**: Option to save chapters as `.cbz` files.
  - **Data Saver**: Option to use compressed images to save bandwidth (MangaDex only).
  - **Interactive Selection**: Pick specific chapters manually or by range.
  - **Real-Time Progress**: accurate progress bars for both GUI and TUI.

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
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Graphical User Interface (GUI)
Run the Python script directly:
```bash
python md_gui.py
```

**GUI Controls**:
- **Search**: Type title and press Enter.
- **Source Selector**: Toggle between MangaDex and Baozimh in the settings or dropdown.
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

To create the standalone `MultiMangaScraper.exe`:

```bash
pip install pyinstaller
pyinstaller --clean --onefile --noconsole --name MultiMangaScraper md_gui.py
```

## Disclaimer

This tool is for educational purposes and personal use only. Please respect the copyrights of the manga creators and publishers.
