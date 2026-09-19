# Daily-Manna (Bible Verse Generator)

A lightweight, zero-dependency Python script that generates 100% accurate, completely valid random Scripture coordinates (Book, Chapter, and Verse).

Unlike other scripts that rely on bloated databases or external web APIs, this project uses a highly optimized, fully immutable local data mapping. This ensures instant execution with zero network latency.

## Features

- **Zero Dependencies**: Runs entirely on native Python built-in modules (`random`).
- **Data Integrity**: Uses immutable **Tuples** to protect Bible metrics from accidental runtime mutations.
- **Accurate Bounding**: Completely accounts for single-chapter anomalies (e.g., Philemon, Jude, 2 John) and varying chapter lengths without risking index out-of-bound crashes.
- **Clean Structure**: Separated cleanly into Old and New Testament data nodes.

---

## How It Works Under the Hood

The engine utilizes a nested lookup pattern that implicitly maps data without structural redundancy:

1. **Testament Selection**: Picks randomly between the `OLD_TESTAMENT` or `NEW_TESTAMENT` structural maps.
2. **Book Tracking**: Extracts the dictionary keys to target a single book dynamically.
3. **Chapter Bounding**: Uses `len(book)` to find exactly how many chapters exist, setting a clean ceiling for `random.randint()`.
4. **Verse Index Extraction**: Accesses the exact index location (`chapter - 1`) to pull the verse ceiling constraint for that specific chapter.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher.

### Installation & Usage
1. Clone or download this repository.
2. Change directory to python-playground/daily-manna
3. Run the file directly using your terminal:

```bash
python main.py
```

### Example Console Output
```text
----------------------------------------------------------------------
Verse of the Day: John 3:16
----------------------------------------------------------------------
```

---

## Code Structure Look

```python
# Implicit chapter counting via index item length
NEW_TESTAMENT: = {
    "Matthew": (25, 23, 17, 25, 48, ...),
    "Mark": (45, 28, 35, 41, 43, ...)
}
```

## Contributing
Contributions are welcome! If you would like to expand the `OLD_TESTAMENT` dictionary to include more books beyond Psalms and Proverbs, feel free to open a Pull Request with the validated verse-count tuples.
