import tkinter as tk

class QuizGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("✨ My Quiz Game! ✨")
        self.root.geometry("500x400")
        self.root.withdraw()
        self.current = {"index": -1, "score": 0, "total": 0, "data": [], "current_question": None}