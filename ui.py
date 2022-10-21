from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_board = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_board.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR, width=280,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.tick_button = Button()
        tick_image = PhotoImage(file="images/true.png")
        self.tick_button.config(image=tick_image, highlightthickness=0, borderwidth=0, command=self.tick_answer)
        self.tick_button.grid(row=2, column=0, pady=20)

        self.cross_button = Button()
        cross_image = PhotoImage(file="images/false.png")
        self.cross_button.config(image=cross_image, highlightthickness=0, borderwidth=0, command=self.cross_answer)
        self.cross_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_board.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def tick_answer(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def cross_answer(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
