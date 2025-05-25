import sys
import time
from termcolor import colored
from quiz_creator import QuizCreator 
from quiz_game import QuizGame

class MainMenu:
    def __init__(self):
        self.display_menu()

    def display_menu(self):
        while True:
            print(colored("\n✨ Welcome to My Quiz Program ✨", "cyan", attrs=["bold"]))
            print(colored("1. Create a New Quiz", "yellow"))
            print(colored("2. Take a Quiz", "green"))
            print(colored("3. Exit", "red"))

            choice = input(colored("\nPlease select an option (1-3): ", "blue")).strip()