from pydoc import text

from customtkinter import *
from random import randint

def change_btn_pos():
    x_random = randint(0, win.winfo_width()-btn_no.winfo_width())
    y_random = randint(0, win.winfo_height()-btn_no.winfo_height())

def show_win():
    win2 = CTk()
    win2.geometry("200x100")
    win2.title("Choose")
    label_win = CTkLabel(win2, text="Good work choom!", font=("Arial", 14, "bold"))
    label_win.pack(pady=20)
    win2.mainloop()

win = CTk()
win.geometry("400x300")
win.title("Illusion of a choise")

label = CTkLabel(win, text="Logika imba?", font=("Arial", 14, "bold"))
label.pack(pady=40)

btn_no = CTkButton(win, text="No", command=change_btn_pos)
btn_no.place(x=50, y=200)

btn_yes = CTkButton(win, text="Yes", command=show_win)
btn_yes.place(x=200, y=200)

win.mainloop()