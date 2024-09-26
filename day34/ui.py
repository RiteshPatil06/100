from tkinter import *
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        #canvas
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #scoreboard
        self.scoreboard_label = Label(
            text=f"Score: 0", fg='white',
            bg=THEME_COLOR, font=('Arial', 10, 'bold'))
        self.scoreboard_label.grid(row=0, column=1)

        #question
        self.question_text = self.canvas.create_text(
            150, 125, text="question",
            width=280,
            font=('Arial', 20, 'italic'))

        #buttons
        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2, column=0, pady= 10)

        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=1, pady= 10)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.scoreboard_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
