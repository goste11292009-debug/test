from customtkinter import *
from PIL import Image

window = CTk()
window.geometry('400x400')
window.title('My first image window')

img = Image.open(r'C:\Users\23mar\OneDrive\Изображения\Снимки экрана\Знімок екрана 2025-10-25 170241.png')
img_ctk = CTkImage(light_image=img, size=(350, 200))

label = CTkLabel(window, text='', image=img_ctk)
label.pack(pady=10)

def rotate():
    image.rotate(90)
def bw():
    image.convert('1')
def

window.mainloop()