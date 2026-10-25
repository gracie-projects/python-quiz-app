
import json
import random
from pathlib import Path

HIGH_SCORE_FILE = Path(__file__).with_name("high_score.json")

QUESTIONS = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "define"},
        "answer": "B",
        "explanation": "The def keyword is used to define a function."
    },
    {
        "question": "Which data type stores True or False?",
        "options": {"A": "int", "B": "str", "C": "bool", "D": "list"},
        "answer": "C",
        "explanation": "bool is Python's Boolean data type."
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {"A": "//", "B": "#", "C": "/*", "D": "<!--"},
        "answer": "B",
        "explanation": "A single-line Python comment starts with #."
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": {"A": "add()", "B": "insert_end()", "C": "append()", "D": "push()"},
        "answer": "C",
        "explanation": "list.append(item) adds an item to the end."
    },
    {
        "question": "Which loop is commonly used to iterate over a list?",
        "options": {"A": "for", "B": "switch", "C": "repeat-until", "D": "foreach"},
        "answer": "A",
        "explanation": "A for loop can iterate through each list item."
    },
    {
        "question": "What does len('Python') return?",
        "options": {"A": "5", "B": "6", "C": "7", "D": "Python"},
        "answer": "B",
        "explanation": "Python has six characters."
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": {"A": "tuple", "B": "set", "C": "dictionary", "D": "string"},
        "answer": "C",
        "explanation": "A dictionary stores data as key-value pairs."
    },
    {
        "question": "Which keyword handles an exception?",
        "options": {"A": "catch", "B": "error", "C": "except", "D": "final"},
        "answer": "C",
        "explanation": "Python uses try and except to handle exceptions."
    },
    {
        "question": "Which operator checks equality?",
        "options": {"A": "=", "B": "==", "C": "!=", "D": ">="},
        "answer": "B",
        "explanation": "== compares two values for equality."
    },
    {
        "question": "Which module helps generate random selections?",
        "options": {"A": "math", "B": "json", "C": "random", "D": "pathlib"},
        "answer": "C",
        "explanation": "The random module provides functions for random selection."
    }
]


def load_high_score():
    """Read the saved high score, if the file exists and is valid."""
    try:
        data = json.loads(HIGH_SCORE_FILE.read_text(encoding="utf-8"))
        return max(0, int(data.get("high_score", 0)))
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        return 0


def save_high_score(score):
    """Save the highest score to a JSON file."""
    HIGH_SCORE_FILE.write_text(
        json.dumps({"high_score": score}, indent=4),
        encoding="utf-8"
    )


def get_answer():
    """Accept A, B, C, or D; keep asking until the input is valid."""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in {"A", "B", "C", "D"}:
            return answer
        print("Invalid input. Please enter A, B, C, or D.")


def play_quiz():
    score = 0
    questions = random.sample(QUESTIONS, len(QUESTIONS))

    print("\nWelcome to the Python Quiz App!")
    print(f"You will answer {len(questions)} questions.")
    print("Each correct answer earns 1 point.\n")

    for number, item in enumerate(questions, start=1):
        print(f"\nQuestion {number}/{len(questions)}")
        print(item["question"])

        for key, option in item["options"].items():
            print(f"  {key}. {option}")

        answer = get_answer()

        if answer == item["answer"]:
            score += 1
            print("Correct!")
        else:
            correct = item["answer"]
            print(f"Incorrect. Correct answer: {correct}. "
                  f"{item['options'][correct]}")

        print(f"Explanation: {item['explanation']}")

    percentage = (score / len(questions)) * 100
    previous_best = load_high_score()

    print("\n" + "=" * 35)
    print("QUIZ RESULTS")
    print(f"Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.1f}%")

    if score > previous_best:
        save_high_score(score)
        print("Congratulations! You achieved a new high score.")
    else:
        print(f"Your saved high score is: {previous_best}/{len(questions)}")

    print("=" * 35)


def main():
    while True:
        play_quiz()
        again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if again not in {"y", "yes"}:
            print("Thank you for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
