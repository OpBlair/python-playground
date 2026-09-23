# Daily-Manna (Bible Verse Generator)

A lightweight Python script that generates 100% accurate, completely valid random Scripture coordinates (Book, Chapter, and Verse) and instantly fetches the matching verse text using a secure web API.

Unlike basic static text scripts, this project combines a highly optimized local data mapping strategy with real-time text retrieval to bring you a fresh, accurate scriptural reading instantly.

## Features

- **Real-Time API Integration**: Connects dynamically to a public REST (`bible-api.com`) database to pull the literal text of the verse.
- **Data Integrity**: Uses immutable **Tuples** to protect structural Bible metrics from accidental runtime mutations.
- **Accurate Bounding**: Completely accounts for single-chapter anomalies (e.g., Philemon, Jude, 2 John) and varying chapter lengths without risking index out-of-bound crashes.
- **Clean Structure**: Separated cleanly into Old and New Testament data nodes.
- **Zero Dependency**: Relies exclusively on Python's standard library (urllib and json) to fetch, parse, and process data without external package installations.

---

## How It Works Under the Hood

The engine utilizes a hybrid approach mapping local coordinates directly into clean URL payloads:

1. **Testament Selection**: Picks randomly between the Old or New Testament structural maps.
2. **Book Tracking**: Extracts the dictionary keys to target a single book dynamically.
3. **Chapter Bounding**: Uses `len(book)` to find exactly how many chapters exist, setting a clean ceiling for `random.randint()`.
4. **Verse Index Extraction**: Accesses the exact index location (`chapter - 1`) to pull the verse ceiling constraint for that specific chapter.
5. **Payload Fetching**: Standardizes data into an HTTP GET request to output the exact scriptural content to your console window safely.

---

## Improvements & Translation Support

The underlying engine supports dynamic switching of text versions directly from the API layer. You can update the query parameters within your URL construction to request any of the following supported translations:

* **`kjv`**: King James Version (Default setup)
* **`web`**: World English Bible
* **`almeida`**: João Ferreira de Almeida (Portuguese)
* **`rvr1960`**: Reina-Valera 1960 (Spanish)
* **`bbe`**: Bible in Basic English

To switch versions dynamically, simply change the `translation` variable payload passed into the query configuration:
```python
translation = "web"  # Switch seamlessly to the World English Bible
url = f'https://bible-api.com{book} {chapter}:{verse}?translation={translation}'
```

---

## Acknowledgements & API Source

This project proudly utilizes the **Bible API** service hosted at [bible-api.com](https://bible-api.com). 

Special thanks to **Tim Morgan** ([@sevenwire](https://github.com)), the developer who built and maintains this incredible, free, public domain tool. Because of his public work, this application can pull clean, open-source scriptural text over simple HTTP calls with no authentication tokens or API keys required.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher.
- `requests` package installed.

### Installation & Usage
1. Clone or download this repository.
2. Change directory to `python-playground/daily-manna`.
3. Install the required HTTP package dependencies:
   ```bash
   pip install requests
   ```
4. Run the file directly using your terminal:
   ```bash
   python main.py
   ```

### Example Console Output
```text
----------------------------------------------------------------------
Verse of the Day: John 3:16
----------------------------------------------------------------------
For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.
----------------------------------------------------------------------
```

---

## Code Structure Look

```python
# Safe HTTP parsing via formatted query URLs
url = f'https://bible-api.com{book} {chapter}:{verse}?translation=kjv'
```

## Contributing
Contributions are welcome! If you would like to expand the Old Testament dictionary to include more books beyond Psalms and Proverbs, feel free to open a Pull Request with the validated verse-count tuples.
