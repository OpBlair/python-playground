quiz_questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
        "answer": "B"
    },
    {
        "prompt": "What is the output of `print(2 ** 3)` in Python?",
        "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "prompt": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following data types is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "prompt": "What is the correct file extension for Python files?",
        "options": ["A. .pt", "B. .pyt", "C. .py", "D. .python"],
        "answer": "C"
    },
    {
        "prompt": "Which symbol is used to write single-line comments in Python?",
        "options": ["A. #", "B. //", "C. /*", "D. <!--"],
        "answer": "A"
    }
]

def run_quiz(quiz_questions):
    score = 0
    total_questions = len(quiz_questions)

    for index, question in enumerate(quiz_questions, start=1):
        print(f"\n{index}. {question['prompt']}")

        for option in question['options']:
            print(option)

        user_input = input("Enter your choice: ").strip().upper()

        if user_input == question['answer']:
            print("correct")
            score += 1
        else:
            print(f"The answer isn't correct, the correct answer is {question['answer']}")

        print("-" * 50)

    print("\nQuiz Over!")
    print(f"You got {score} out of {total_questions} correct.")
    percentage = (score / total_questions) * 100
    print(f"Your final score: {percentage:.0f}%")

    return score

if __name__ == "__main__":
    run_quiz(quiz_questions)