# Simple Quiz App

A lightweight, interactive command-line quiz application built in Python. Test your knowledge across any topic with instant feedback and a final score summary!

---

## Features

* **Interactive CLI Interface:** Runs directly in your terminal with clear, numbered prompts and multiple-choice options.
* **Instant Feedback:** Immediately lets you know if your answer is correct or reveals the right answer if you miss it.
* **Final Score Calculation:** Tallies your correct answers and displays your final score and percentage at the end.
* **Easily Customizable:** A modular dictionary structure allows you to swap out or add questions on any subject in seconds.

---

## Prerequisites

Make sure you have **Python 3.x** installed on your system. You can verify your installation by running this command in your terminal:

```bash
python --version
```
---
## Getting Started

1. Clone or download this script to your local machine (e.g., saved as quiz_app.py).
2.  Open your terminal or command prompt and navigate to the directory containing the file.
3.  Run the script using the following command:

``` bash
python filename.py
```
---
## How to Play

1. The application will present questions one by one along with multiple-choice options (A, B, C, D).
2. Type your chosen option letter (case-insensitive, e.g., A, b) and press Enter.
3. View your results for each question, followed by your overall score and percentage at the end.
---
## Customization

You can easily change the quiz topic or add new rounds by editing the quiz_questions list in the script. Each question follows a clean dictionary format:

``` python
{
    "prompt": "Your question here?",
    "options": ["A. Choice 1", "B. Choice 2", "C. Choice 3", "D. Choice 4"],
    "answer": "B"  # The correct option letter
}
```
---
## Future Improvements

The current version is intentionally simple, but there are several features that could be added in future versions:

1. **JSON-Based Question Bank :**
   Store questions in a .json file instead of directly inside the Python script.

2. **Question Randomization:**
    Randomize the order of questions each time the quiz starts.

3. **Answer Randomization:**
    Randomize the order of the multiple-choice options.

4. **Input Validation:**
    Prevent invalid inputs and ask the user to enter a valid option.

5. **Multiple Categories:**
    Allow users to choose categories such as Python, Geography, History, or Science.

6. **Difficulty Levels:**
    Add Easy, Medium, and Hard questions.

7. **High-Score System:**
    Save users' scores and display the highest score.

8. **Timer:**
    Add a time limit for answering each question.

9. **Quiz Restart:**
    Give users the option to play another round without restarting the program.

10. **Graphical User Interface:**
    Convert the command-line application into a desktop or web-based quiz application.

---
## License

This project is open-source and free to use for learning, modification, and sharing.
