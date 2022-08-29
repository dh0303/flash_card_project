from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(card_lang, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_lang, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(canvas_img, image=card_back_img)

def is_known():
    data_list.remove(current_card)
    data = pandas.DataFrame(data_list)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_back_img = PhotoImage(file='images/card_back.png')
card_lang = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font= ('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
yes_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_img, highlightthickness=0, command=is_known)
yes_button.grid(row=1, column=1)

no_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_img, highlightthickness=0, command=next_card)
no_button.grid(row=1, column=0)

# read from the CSV
try:
    df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('data/french_words.csv')

data_list = df.to_dict(orient='records')

print('中文')
next_card()

mainloop()