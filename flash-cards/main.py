from tkinter import *
import pandas as pd
import random as r

new_word_dict = {}
words_to_learn_dict = {}

# --------- REMOVE KNOWN WORDS -------------

def is_known():
    words_to_learn_dict.remove(new_word_dict)
    new_card()
    data = pd.DataFrame(words_to_learn_dict)
    data.to_csv("data/Estonian_words_to_learn.csv", index=False)


# --------- NEW CARD -------------

def new_card():
    global new_word_dict, flip_timer
    w.after_cancel(flip_timer)
    new_word_dict = r.choice(words_to_learn_dict)
    new_word_Estonian = new_word_dict["Estonian"]
    canvas.itemconfig(card_background, image=front_card_img)
    canvas.itemconfig(language_text, text="Estonian", fill="black")
    canvas.itemconfig(word_text, text=new_word_Estonian, fill="black")
    flip_timer = w.after(3000, func=flip_card)

# --------- FLIP CARD -------------


def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=new_word_dict["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card_img)


# --------- DF -------------

try:
    new_data = pd.read_csv("data/Estonian_words_to_learn.csv")

except FileNotFoundError:
    original_data = pd.read_csv("data/estonian_500_list.csv")
    words_to_learn_dict = original_data.to_dict(orient="records")
else:
    words_to_learn_dict = new_data.to_dict(orient="records")

# --------- UI -------------

BACKGROUND_COLOR = "#B1DDC6"

w = Tk()
w.title("Flashy")
w.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = w.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

back_card_img = PhotoImage(file="images/card_back.png")
front_card_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_card_img)

language_text = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

tick_img = PhotoImage(file="images/right.png")
known_button = Button(image=tick_img, highlightthickness=0, command=is_known)
known_button.grid(column=0, row=1)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=new_card)
unknown_button.grid(column=1, row=1)

new_card()

w.mainloop()