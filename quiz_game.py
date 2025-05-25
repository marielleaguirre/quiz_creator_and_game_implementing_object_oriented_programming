import os
import tkinter as tk
from tkinter import messagebox, filedialog

class QuizGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("✨ My Quiz Game! ✨")
        self.root.geometry("500x400")
        self.root.withdraw()
        self.current = {"index": -1, "score": 0, "total": 0, "data": [], "current_question": None}

    def load_questions(self, filename):
        if not os.path.exists(filename):
            print("Quiz file not found. (｡•́︿•̀｡)")
            return []

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip()

        raw_questions = content.split("-" * 50)
        questions = []

        for raw_content in raw_questions:
            lines = [line.strip() for line in raw_content.strip().splitlines()]
            if not lines or "Question:" not in lines[0]:
                continue

            try:
                question_text = lines[1]
                choices = {
                    'a': lines[2].split(")", 1)[1].strip(),
                    'b': lines[3].split(")", 1)[1].strip(),
                    'c': lines[4].split(")", 1)[1].strip(),
                    'd': lines[5].split(")", 1)[1].strip()
                }
                answer = lines[7].strip().lower()

                questions.append({
                    "questions": question_text,
                    "choices": choices,
                    "answer": answer
                })
            except (IndexError, ValueError):
                continue

        return questions
    
    def start(self):
        file_path = filedialog.askopenfilename(title="Select Quiz File", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            messagebox.showerror("No file selected", "You must select a quiz file to proceed")
            return

        questions = self.load_questions(file_path)
        if not questions:
            messagebox.showerror("No Questions Found", "The selected file does not contain valid quiz questions.")
            return

        self.current["data"] = questions
        self.current["total"] = len(questions)
        self.root.deiconify()
        self.setup_ui()
        self.load_next_question()
        self.root.mainloop()