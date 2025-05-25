import os 
from termcolor import colored 
import time

class QuizCreator:
    def __init__(self):
        self.quiz_file = input(colored("Enter the quiz file name (e.g., 'quiz_data.txt'): ", "blue")).strip()
        if not self.quiz_file.endswith(".txt"):
            self.quiz_file += ".txt"
        print(colored(f"Working with file: {os.path.abspath(self.quiz_file)}", "cyan"))
        self.main_file()
        self.create_quiz()

    def save_to_file(self, question_data):
        with open(self.quiz_file, "a", encoding="utf-8") as file:
            file.write("\n" + "-" * 50 + "\n")
            file.write("Question:\n" + question_data['question'] + "\n")
            for label, choice in question_data['choices'].items():
                file.write(f" {label}) {choice}\n")
            file.write("Answer:\n" + question_data['answer'] + "\n")
            file.write("-" * 50 + "\n")

    def create_quiz(self):
        print(colored("\nWelcome to my Python Quiz Creator! *ฅ^•ﻌ•^ฅ*\n", "yellow", attrs=["bold"]))
        time.sleep(1)

        print(colored("Let's get started! Add as many questions as you want ₍^. .^₎⟆", "green"))

        while True: 
            question = input(colored("Enter your question: ", "blue")).strip()
            choices = {}
            for option in ['a', 'b', 'c', 'd']:
                choice = input(colored(f" ⋆˚✿˖° Enter choice {option.upper()}: ", "cyan")).strip()
                choices[option] = choice

            correct = input(colored("Enter the correct answer (a, b, c, or d): ", "green")).strip().lower()

            if correct not in choices: 
                print(colored("Invalid answer (╥﹏╥). Must be one of: a, b, c, d.\n", "red"))
                continue

            question_data = {
                "question": question,
                "choices": choices,
                "answer": correct
            }
            self.save_to_file(question_data)
            print(colored("Question saved successfully! /ᐠ. .ᐟ\\ Ⳋ ✧\n", "yellow"))  

            again = input(colored("Add another question? (๑•᎑•๑) (type 'yes' to continue and 'no' to exit): ", "blue"))
            if again != 'yes':
                print(colored("\nCongratulations on creating your quiz!", "magenta", attrs=["bold"]))
                print(colored("Exiting... Goodbye! (∩˃ω˂∩)", "red", attrs=["bold"]))
                time.sleep(1)
                break
        
        print(colored(f"\nAll questions saved to '{self.quiz_file}'.", "green"))

    def main_file(self):
        if not os.path.exists(self.quiz_file):
            with open(self.quiz_file, "w") as file:
                file.write("=== Quiz Questions ===\n\n")

if __name__ == "__main__":
    creator = QuizCreator()
    creator.create_quiz()