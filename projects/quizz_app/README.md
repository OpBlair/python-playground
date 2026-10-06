# Simple Quiz App

A lightweight, interactive command-line quiz application built in Python. Test your knowledge across any topic with instant feedback, a final score summary, and an external JSON-based question bank!

---

## Features

* **Interactive CLI Interface:** Runs directly in your terminal with clear, numbered prompts and multiple-choice options.
* **Instant Feedback:** Immediately lets you know if your answer is correct or reveals the right answer if you miss it.
* **Final Score Calculation:** Tallies your correct answers and displays your final score and percentage at the end.
* **JSON-Based Question Bank:** Questions are loaded dynamically from a separate `questions.json` file, making it easy to manage and update quiz content without modifying the source code.

---

## Prerequisites

Make sure you have **Python 3.x** installed on your system. You can verify your installation by running this command in your terminal:

```bash
python --version

```

## Project Files

Ensure you have both files in the same directory:

1. `main.py` (The main application script)
2. `questions.json` (The question bank)

## Getting Started

1. Download or clone both `main.py` and `questions.json` to your local machine into the same folder.
2. Open your terminal or command prompt and navigate to that directory.
3. Run the script using the following command:

```bash
python quiz_app.py

```

## How to Play

1. The application will load the questions from `questions.json` and present them one by one along with multiple-choice options (A, B, C, D).
2. Type your chosen option letter (case-insensitive, e.g., A, b) and press **Enter**.
3. View your results for each question, followed by your overall score and percentage at the end.

## Customization

You can easily change the quiz topic, add new questions, or edit existing ones by modifying the `questions.json` file. Each question follows a clean JSON structure:

```json
{
    "prompt": "What is the capital of France?",
    "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
    "answer": "B"
}

```

## Future Improvements

The current version includes an external question bank, but there are several features that could be added in future versions:

1. **Question Randomization**
Randomize the order of questions each time the quiz starts.
2. **Answer Randomization**
Randomize the order of the multiple-choice options for each question.
3. **Input Validation**
Prevent crashes or errors from invalid inputs and prompt the user to enter a valid option.
4. **Multiple Categories**
Allow users to choose categories such as Python, Geography, History, or Science.
5. **Difficulty Levels**
Add Easy, Medium, and Hard question tiers.
6. **High-Score System**
Save users' scores locally and display the highest score achieved.
7. **Timer**
Add a countdown timer for answering each question.
8. **Quiz Restart**
Give users the option to play another round or switch categories without restarting the program.
9. **Graphical User Interface**
Convert the command-line application into a desktop or web-based quiz application.

---

## License

This project is open-source and free to use for learning, modification, and sharing.
