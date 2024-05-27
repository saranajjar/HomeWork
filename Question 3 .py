import json


def load_questions_from_json(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions


def save_results_to_json(user_name, score):
    results = {user_name: score}
    with open('results.json', 'w') as file:
        json.dump(results, file)


def quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + ' ')
        if user_answer.lower() == answer.lower():
            score += 1
    return score


def main():
    file_path = "./questions.json"
    questions = load_questions_from_json(file_path)

    user_name = input("Enter your name: ")

    user_score = quiz(questions)

    print(f"Your score: {user_score}/{len(questions)}")

    save_results_to_json(user_name, user_score)


if __name__ == "__main__":
    main()