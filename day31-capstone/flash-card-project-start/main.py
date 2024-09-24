import random
from tkinter import *
import pandas as pd


#----------------------------------file------------------------------------#
word = {}
to_translate = {}

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    to_translate = original_data.to_dict(orient='records')
else:
    to_translate = data.to_dict(orient='records')

def random_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_translate)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=word["French"], fill='black')
    canvas.itemconfig(canvas_img, image=card_front_img)
    window.after(3000, func=translator)

#----------------------------------Translator------------------------------------#

def translator():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")


def is_known():
    to_translate.remove(word)
    data2 = pd.DataFrame(to_translate)
    data2.to_csv('data/words_to_learn.csv', index=FALSE)
    random_word()
#----------------------------------UI------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=translator)


canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file='images/card_back.png')
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Helvetica", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Helvetica", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#images
wrong_image = PhotoImage(file="images/wrong.png", )
correct_image = PhotoImage(file="images/right.png")

#buttons
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_btn.grid(row=1, column=0)
correct_btn = Button(image=correct_image, highlightthickness=0, command=is_known)
correct_btn.grid(row=1, column=1)



random_word()





window.mainloop()
