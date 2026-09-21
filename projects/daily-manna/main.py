import random
import requests

old_testament = {
    "Psalms": (6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 11, 11, 21, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10, 10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 12, 6, 7, 21, 26, 9, 24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6, 11),
    "Proverbs": (33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31)
}

new_testament = {
    # Gospels and History
    "Matthew": (25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20),
    "Mark": (45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20),
    "Luke": (80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53),
    "John": (51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25),
    "Acts": (26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27, 32, 44, 31),
    
    # Pauline Epistles (letters from Paul)
    "Romans": (32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27),
    "1 Corinthians": (31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24),
    "2 Corinthians": (24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14),
    "Galatians": (24, 21, 29, 31, 26, 18),
    "Ephesians": (23, 22, 21, 32, 33, 24),
    "Philippians": (30, 30, 21, 23),
    "Colossians": (29, 23, 25, 18),
    "1 Thessalonians": (10, 20, 13, 18, 28),
    "2 Thessalonians": (12, 17, 18),
    "1 Timothy": (20, 15, 16, 16, 25, 21),
    "2 Timothy": (18, 26, 17, 22),
    "Titus": (16, 15, 15),
    "Philemon":  (25,),
    
    # General Epistles and Prophecy
    "Hebrews": (14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40, 29, 25),
    "James": (27, 26, 18, 17, 20),
    "1 Peter": (25, 25, 22, 19, 14),
    "2 Peter": (21, 22, 18),
    "1 John": (10, 29, 24, 21, 21),
    "2 John": (13,),
    "3 John": (14,),
    "Jude": (25,),
    "Revelation": (20, 29, 22, 11, 14, 17, 17, 13, 21, 11, 19, 17, 18, 20, 8, 21, 18, 24, 21, 15, 27, 21)
}

def get_bible_verse():
    testament = random.choice([old_testament, new_testament])
    book = random.choice(list(testament.keys()))

    total_chapters = len(testament[book])
    chapter = random.randint(1, total_chapters)

    total_verses = testament[book][chapter - 1]
    verse = random.randint(1, total_verses)

    return book, chapter, verse

def get_reference(book, chapter, verse):

    url = f'https://bible-api.com/{book}{chapter}:{verse}?translation=kjv'
    
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = response.json()

        verse_text = data.get("text", "")
        print(f"{verse_text}")
    else:
        print(f"An error occured: {response.status_code}")

if __name__ == "__main__":
    book, chapter, verse = get_bible_verse()
    print("-"*70)
    print(f"Verse of the Day: {book} {chapter}:{verse}")
    print("-"*70)
    get_reference(book, chapter, verse)
    print("-"*70)
