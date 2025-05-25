import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

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

    def setup_ui(self):
        self.root.configure(bg="#222")
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 13), padding=6, relief="flat", background="#444")

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"), wraplength=500, justify="center", fg="white", bg="#222")
        self.question_label.pack(pady=20)

        self.buttons = {}
        for key in ['a', 'b', 'c', 'd']:
            self.buttons[key] = tk.Button(self.root, text="", font=("Helvetica", 14), width=30, bg="#333", fg="white",
                                          activebackground="#222", activeforeground="blue",
                                          command=lambda k=key: self.check_answer(k))
            self.buttons[key].pack(pady=5)

        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14), fg="white", bg="#222")
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Next Question ⭢", font=("Helvetica", 12), bg="#007acc", fg="white", command=self.load_next_question)
        self.next_button.pack(pady=10)

    def load_next_question(self):
        if not self.current["data"]:
            return self.end_quiz()

        self.current["current_question"] = random.choice(self.current["data"])
        self.current["data"].remove(self.current["current_question"])

        self.question_label.config(text=self.current["current_question"]["questions"])
        for key in ['a', 'b', 'c', 'd']:
            choice = self.current["current_question"]["choices"][key]
            self.buttons[key].config(text=f"{key.upper()}) {choice}", state="normal")

        self.feedback_label.config(text="")
        self.next_button.config(state="disabled")

    def check_answer(self, selected):
        correct = self.current["current_question"]["answer"]
        if selected == correct:
            self.feedback_label.config(text="Correct! (≧□≦) ♡", fg="#4CAF50")
            self.current["score"] += 1
        else:
            correct_text = self.current["current_question"]["choices"][correct]
            self.feedback_label.config(text=f"Wrong! Correct answer is {correct.upper()}) {correct_text}", fg="crimson")

        for button in self.buttons.values():
            button.config(state="disabled")
        self.next_button.config(state="normal")

    def end_quiz(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        result = f" Quiz Finished! Your Score: {self.current['score']}/{self.current['total']}"
        result_label = tk.Label(self.root, text=result, font=("Helvetica", 18, "bold"), fg="#4CAF50", bg="#222")
        result_label.pack(pady=20)

        if self.current["score"] == self.current["total"]:
            message = "Perfect score! You're a quiz master! ✧*。٩(ˋ・‿・)ى✧*。"
        elif self.current["score"] >= self.current["total"] // 2:
            message = "Nice try! You did well! (੭˃ᴗ˂)੭"
        else:
            message = "Don't worry! Try again and do better next time! (๑•̀ᴗ•́)߼l"

        messagebox.showinfo("Quiz Result", message)

if __name__ == "__main__":
    game = QuizGame()
    game.start()