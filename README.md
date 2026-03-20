# MultiMangaScraper & GUI

A feature-rich, industrial-grade application to search, view, and download manga chapters from **MangaDex**, **Baozimh**, **Happymh**, and **NewToki**. Featuring a professional "cinematic" dark theme and advanced anti-detection capabilities.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

## 🚀 Key Features

- **Professional UI/UX**:
  - **Cinematic Dark Theme**: A modern, content-forward interface with custom widgets, smooth transitions, and a deep-dark palette.
  - **Custom Widgets**: iOS-style toggle switches, interactive language chips, and a download button with an integrated progress overlay.
  - **Scalable Previews**: High-quality manga cover art with smooth scaling and shimmer loading effects.
- **Multi-Source Support**:
  - **MangaDex**: Default provider with full metadata, search, and data-saver support.
  - **Baozimh**: Specialized for Chinese manga with automated "App Only" chapter bypassing and placeholder detection.
  - **Happymh**: Advanced Cloudflare bypass using SeleniumBase UC Mode and AVIF-to-JPG conversion.
  - **NewToki**: Robust Korean source support with human-like navigation, auto-scrolling for lazy-loaded images, and interactive CAPTCHA handling.
- **Advanced Anti-Detection**:
  - **Human Simulation**: JS-simulated mouse movements, random delays, and viewport resizing to mimic real user behavior.
  - **SeleniumBase UC**: Undetected-chromedriver integration to bypass modern bot protections like Cloudflare and 403 blocks.
  - **Cookie Transfer**: Seamlessly transfers `cf_clearance` cookies from browser sessions to high-speed downloaders.
- **Library & Smart Tracking**:
  - **Library Management**: Save your favorite series to a local library with one-click access.
  - **Update Checker**: Automatically identifies when new chapters are available for your tracked manga.
- **Flexible Downloading**:
  - **Format Support**: Automatically converts modern formats (AVIF) to standard JPEGs for maximum compatibility.
  - **CBZ Archiving**: Pack your chapters into `.cbz` files automatically.
  - **Filtering**: Select specific chapter ranges or filter by scanlation group and language.

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/DFlow69/MultiMangaScraper.git
    cd MultiMangaScraper
    ```

2.  **Install Dependencies**:
    It is recommended to use the provided batch script for a quick setup:
    ```powershell
    ./install.bat
    ```
    Or manually install via pip:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Chrome**:
    Ensure you have Google Chrome installed. For **NewToki**, the app currently targets Chrome version 146 (or the latest compatible `undetected-chromedriver`).

## 📖 Usage

> [!IMPORTANT]
> **MANDATORY FOR HAPPYMH & NEWTOKI**: For these sources, you **MUST** paste the absolute series URL (e.g., `https://m.happymh.com/manga/berserk`) directly into the search bar. Searching by title for these specific sources is unreliable due to strict bot protection and search obfuscation.

### Launching the App
- **GUI (Recommended)**:
  ```bash
  python md_gui.py
  ```

### Manual CAPTCHA Handling
For sources like NewToki, if a CAPTCHA or Cloudflare "Just a moment" screen appears:
1.  A dialog will pop up in the app.
2.  Solve the challenge manually in the browser window that opens.
3.  Click **"Solved"** in the app to resume the automated extraction.

## 🛠️ Building from Source

To create a standalone executable:

```bash
pip install pyinstaller
pyinstaller --clean --onefile --noconsole --name MultiMangaScraper md_gui.py
```

## 📜 Disclaimer

This tool is for educational purposes and personal use only. Please respect the copyrights of the manga creators and publishers. Use responsibly.
