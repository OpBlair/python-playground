quiz_questions = [
    {
        "prompt": (
            "Which function is used to output text to the console in Python?"
        ),
        "options": ["A. echo", "B. print", "C. write", "D. display"],
        "answer": "B",
    },
    {
        "prompt": "What is the output of `print(2 ** 3)` in Python?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
        "answer": "C",
    },
    {
        "prompt": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B",
    },
    {
        "prompt": "Which of the following data types is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D",
    },
    {
        "prompt": "What is the correct file extension for Python files?",
        "options": ["A. .pt", "B. .pyt", "C. .py", "D. .python"],
        "answer": "C",
    },
    {
        "prompt": "Which symbol is used to write single-line comments in Python?",
        "options": ["A. #", "B. //", "C. /*", "D. <!--"],
        "answer": "A",
    },
]


def run_quiz(questions):
  score = 0
  total_questions = len(questions)

  for index, question in enumerate(questions, start=1):
    print(f"\n{index}. {question['prompt']}")
    for option in question["options"]:
      print(f"   {option}")

    # Input validation: keep asking until a valid choice is entered
    while True:
      user_input = input("Your answer (A/B/C/D): ").strip().upper()
      if user_input in ["A", "B", "C", "D"]:
        break
      print(":( Invalid choice. Please enter A, B, C, or D.")

    # Find the full text of the correct answer for better feedback
    correct_letter = question["answer"]
    correct_text = next(
        opt for opt in question["options"] if opt.startswith(correct_letter)
    )

    if user_input == correct_letter:
      print(":) Correct!")
      score += 1
    else:
      print(f"Incorrect. The correct answer was: {correct_text}")

    print("-" * 45)

  print("\nQuiz Over!")
  print(f"You got {score} out of {total_questions} correct.")
  percentage = (score / total_questions) * 100
  print(f"Your final score: {percentage:.0f}%")

  return score


if __name__ == "__main__":
  run_quiz(quiz_questions)
