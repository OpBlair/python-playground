# Python File Organizer

A simple and efficient Python script to automatically sort and organize files in a specified directory into categorized folders based on their file extensions.

---

## Features

* **Automatic Categorization:** Sorts files into specific folders (`videos`, `music`, `images`, `documents`) based on their extension.
* **Fallback Handling:** Any file types not explicitly defined are automatically moved into an `others` folder.
* **Safe Moving:** Checks if a file with the same name already exists in the destination folder to prevent overwriting or data loss.
* **Custom Path Support:** Run the script on the current directory or specify any custom path on your system.

---

## Supported File Categories & Extensions

| Category | Extensions |
| --- | --- |
| **Videos** | `.mp4`, `.mkv`, `.webm` |
| **Music** | `.mp3`, `.wav` |
| **Images** | `.png`, `.jpeg`, `.jpg`, `.gif` |
| **Documents** | `.pdf`, `.doc`, `.docx`, `.md`, `.pptx`, `.xlsx`, `.csv`, `.txt` |
| **Others** | Any other extension (default fallback) |

---

## Requirements

* Python 3.x (No external libraries required; uses built-in `os` and `shutil` modules).

---

## Usage

1. Save the script to your computer (e.g., as `main.py`).
2. Open your terminal or command prompt.
3. Run the script:
```bash
python main.py

```


4. When prompted, enter the path of the directory you want to organize, or simply press **Enter** to use the current directory where the script is running.
