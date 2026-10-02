# YouTube Video Downloader (Web UI Edition)

A sleek, lightweight full-stack web application built to download YouTube videos effortlessly from your browser. Powered by **Flask**, styled with **Tailwind CSS**, and backed by the robust **`yt-dlp`** library.

---

## Project Structure

This project maintains a clean separation between the original command-line interface (CLI) script and the modern web application version:

```text
youtube-downloader/
├── cli_downloader.py       # Original terminal-based script
└── web_version/            # Full-stack web application
    ├── main.py             # Flask backend server
    ├── static/
    │   └── script.js       # Frontend behavior & asynchronous requests
    └── templates/
        └── index.html      # Frontend HTML template (Tailwind CSS)

```

---

## Features

* **Modern Web Interface:** Dark-mode responsive UI designed with Tailwind CSS for a smooth user experience.
* **Asynchronous Fetch API:** Downloads initiate seamlessly via background requests without forcing full page reloads.
* **Custom Output Directories:** Choose or specify custom download folders directly from the browser interface.
* **Decoupled Architecture:** Clean separation of concerns with a dedicated static JavaScript file using modern `defer` loading.
* **Side-by-Side Legacy Support:** Your original CLI script remains completely untouched and functional.

---

## Getting Started & Installation

### 1. Prerequisites

Ensure you have Python installed on your system. You will need to install **Flask** and **`yt-dlp`**:

```bash
pip install yt-dlp flask

```

### 2. Navigate to the Web Version

Open your terminal and move into the web application directory:

```bash
cd web_version

```

### 3. Run the Web Server

Launch the Flask backend:

```bash
python app.py

```

### 4. Open in Your Browser

Open your favorite web browser and navigate to:
**`http://127.0.0.1:5000`**

---

## Tech Stack

* **Backend:** Python, Flask, `yt-dlp`
* **Frontend:** HTML5, Tailwind CSS (via CDN)
* **Scripting:** Vanilla JavaScript (Async/Await, Fetch API)

```
