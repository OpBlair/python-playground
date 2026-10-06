import json

def load_questions(filename="questions.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error, the file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error, failed to parse json from {filename}")
        return []

def run_quiz(questions):
    if not questions:
        print("No questions available to run the quiz.") 
        return 0
       
    score = 0
    total_questions = len(questions)

    for index, question in enumerate(questions, start=1):
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
    quiz_questions = load_questions("questions.json")
    run_quiz(quiz_questions)
