from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_resul_label.config(text=f"{km}")


window = Tk()
window.title('Conversion Game')
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)
miles_input.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="Is equal to")
is_equal_label.grid(column=0,row=2)

km_resul_label = Label(text="0")
km_resul_label.grid(column=1,row=1)

km_label = Label(text="km")
km_label.grid(column=2,row=1)


cal_button = Button(text='Calculator', command=miles_to_km)
cal_button.grid(column=1,row=2)

window.mainloop()