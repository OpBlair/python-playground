# YouTube Video Downloader

A lightweight and robust Python command-line utility powered by **`yt-dlp`**. This tool allows you to easily download individual YouTube videos or perform automated batch downloads using a simple JSON file containing a list of URLs.

---

## Features

* **Single Video Downloads:** Input any YouTube URL and save the video directly to your preferred folder.
* **Batch Processing:** Pass a JSON file of links to download multiple videos sequentially.
* **Smart JSON Parsing:** Automatically detects lists of URLs whether they are structured as a raw array or nested inside an object (`urls`, `links`, etc.).
* **Duplicate Protection:** Automatically filters out duplicate URLs in batch jobs to save time and bandwidth.
* **Auto-Directory Management:** Automatically creates target output folders if they do not already exist.

---

## Prerequisites

Before running the script, make sure you have the following installed on your system:

1. **Python 3.x**
2. **`yt-dlp` Library:**
   ```bash
   pip install yt-dlp
   ```
3. **FFmpeg (Recommended):** The script requests the best video and best audio streams (`'format': 'bestvideo+bestaudio/best'`). FFmpeg is required to merge these streams into a single playable file (like MP4 or MKV). Make sure FFmpeg is installed and added to your system's PATH.

---

## Usage Guide

1. Save the Python script to your local machine (e.g., as `downloader.py`).
2. Open your terminal or command prompt.
3. Run the script:
   ```bash
   python downloader.py
   ```
4. Follow the interactive menu prompts:
   * **Option 1:** Enter a single YouTube URL and specify an optional output directory.
   * **Option 2:** Provide the path to a JSON file containing multiple URLs for batch processing.

---

## JSON File Format (For Batch Downloads)

When using **Option 2**, your JSON file can be structured in a few different ways. 

### Option A: A simple list of strings
```json
[
  "https://www.youtube.com/watch?v=EXAMPLE_ID_1",
  "https://www.youtube.com/watch?v=EXAMPLE_ID_2",
  "https://www.youtube.com/watch?v=EXAMPLE_ID_3"
]
```

### Option B: An object with a `urls` or `links` key
```json
{
  "description": "My favorite coding tutorials",
  "urls": [
    "https://www.youtube.com/watch?v=EXAMPLE_ID_1",
    "https://www.youtube.com/watch?v=EXAMPLE_ID_2"
  ]
}
```

---

## Error Handling

* **Missing Library:** If `yt-dlp` is not found, the script will gracefully exit and remind you to run `pip install yt-dlp`.
* **Invalid JSON:** If the batch file is formatted incorrectly, a clear error message will guide you without crashing unexpectedly.
* **Broken URLs:** If an individual video URL fails (e.g., video is deleted or private), the script logs the error, skips it, and continues downloading the rest of the batch queue.
