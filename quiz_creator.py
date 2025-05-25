import os 
from termcolor import colored 
import time

class QuizCreator:
    def __init__(self):
        self.quiz_file = input(colored("Enter the quiz file name (e.g., 'quiz_data.txt'): ", "blue")).strip()
        self.main_file()

    def save_to_file(self):

    def create_quiz(self):
        question = input(colored("Enter your question: ", "blue")).strip()
        choices = {}
        for option in ['a', 'b', 'c', 'd']:
            choice = input(colored(f" ⋆˚✿˖° Enter choice {option.upper()}: ", "cyan")).strip()
            choices[option] = choice

        correct = input(colored("Enter the correct answer (a, b, c, or d): ", "green")).strip().lower()

        if correct not in choices: 
            print(colored("Invalid answer (╥﹏╥). Must be one of: a, b, c, d.\n", "red"))
            continue

    def main_file(self):
        if not os.path.exists(self.quiz_file):
            with open(self.quiz_file, "w") as f:
                f.write("=== Quiz Questions ===\n\n")

if __name__ == "__main__":
    creator = QuizCreator()
    creator.create_quiz()