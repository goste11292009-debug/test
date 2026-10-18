from customtkinter import *
def button_click(number):
   current_text = result_field.get()
   result_field.delete(0, "end")
   result_field.insert(0, current_text + str(number))
def do_math():
   result = eval(result_field.get())
   result_field.delete(0, 'end')
   result_field.insert(0, result)
window = CTk()
set_appearance_mode('dark')
window.geometry("400x500")
window.minsize(380,470)
window.title('Calculator')
result_field = CTkEntry(window, height=40)
result_field.pack(fill='x', pady=15, padx=15)
number_frame = CTkFrame(window)
number_frame.pack(pady=10)
numbers_btns = list()
for i in range(1, 10):
   row = (i - 1) // 3
   col = (i - 1) % 3
   btn = CTkButton(number_frame, text=f'{i}', width=80, height=80, command=lambda num=i: button_click(num))
   btn.grid(row=row, column=col, padx=5, pady=5)
   numbers_btns.append(btn)

btn_zero = CTkButton(number_frame, text='0', width=80, height=80)
btn_zero.grid(row=4, column=1, padx=5, pady=5)
numbers_btns.append(btn_zero)


btn_plus = CTkButton(number_frame, text='+', width=60, height=80, command=lambda num='+': button_click(num))
btn_plus.grid(row=2, column=4, padx=5, pady=5)


btn_result = CTkButton(number_frame, text='=', command=do_math, width=60, height=80)
btn_result.grid(row=4, column=4)


btn_point = CTkButton(number_frame, text='.', width=80, height=80, command=lambda num='.': button_click(num))
btn_point.grid(row=4, column=2)


btn_minus = CTkButton(number_frame, text='-', width=80, height=80, command=lambda num='-': button_click(num))
btn_minus.grid(row=4, column=0)


btn_mnoj = CTkButton(number_frame, text='*', width=60, height=80, command=lambda  num='*': button_click(num))
btn_mnoj.grid(row=1, column=4)


btn_div = CTkButton(number_frame, text='/', width=60, height=80, command=lambda  num='/': button_click(num))
btn_div.grid(row=0, column=4)


window.mainloop()