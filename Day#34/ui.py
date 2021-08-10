THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(bg=THEME_COLOR, fg="white", text=f"Score: {self.quiz.score}")
        self.label.config(padx=10, pady=10, anchor="center", font=("Arial", 13, "normal"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct = PhotoImage(file="images/true.png")
        self.right = Button(image=correct, command=self.right_ans)
        self.right.grid(row=2, column=0, padx=20, pady=20)

        incorrect = PhotoImage(file="images/false.png")
        self.wrong = Button(image=incorrect, command=self.wrong_ans)
        self.wrong.grid(row=2, column=1, padx=20, pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())

    def right_ans(self):
        ans = "True"
        result = self.quiz.check_answer(ans)
        self.check_it(result)

    def wrong_ans(self):
        ans = "False"
        result = self.quiz.check_answer(ans)
        self.check_it(result)

    def check_it(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
            self.window.after(1000, self.change)
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.change)

    def change(self):
        self.next_question()
        self.canvas.config(bg="white")



